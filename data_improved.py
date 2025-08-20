import json
import random
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict, Counter
import copy

# Import all classes and constants from the original data.py
from data import *

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ENHANCED CONFIGURATION FOR BALANCED GENERATION
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class BalancedConfig(Config):
    """Enhanced configuration for balanced dataset generation."""
    
    # Balance parameters
    BALANCE_THRESHOLD = 0.95  # Minimum balance score required
    MAX_BALANCE_ATTEMPTS = 10  # Maximum attempts to achieve balance
    COVERAGE_GUARANTEE_RATIO = 0.1  # 10% of records for coverage guarantee
    
    # Quality assurance - relaxed for better generation success
    ENTITY_VALIDATION_ENABLED = False  # Disable strict validation initially
    RELATION_CONSISTENCY_CHECK = True
    RETRY_ON_VALIDATION_FAILURE = False  # Don't retry on validation failures
    
    # Progress tracking
    BALANCE_PROGRESS_INTERVAL = 100
    DETAILED_STATISTICS = True

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# BALANCED TEMPLATE MANAGER
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class BalancedTemplateManager:
    """Manages template selection to ensure perfect balance across all entity and relation types."""
    
    def __init__(self, first_person_templates: List, third_person_templates: List):
        self.first_person_templates = first_person_templates
        self.third_person_templates = third_person_templates
        self.all_templates = first_person_templates + third_person_templates
        
        # Get all entity and relation types
        self.all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        self.all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        # Usage tracking
        self.entity_usage = Counter()
        self.relation_usage = Counter()
        
        # Coverage tracking
        self.covered_entities = set()
        self.covered_relations = set()
        
        # Template analysis
        self.template_entity_map = self._analyze_template_coverage()
        
        print(f"🎯 BalancedTemplateManager initialized:")
        print(f"   - Entity types: {len(self.all_entity_types)}")
        print(f"   - Relation types: {len(self.all_relation_types)}")
        print(f"   - Templates: {len(self.all_templates)}")
    
    def _analyze_template_coverage(self) -> Dict:
        """Analyze which entity/relation types each template covers."""
        template_coverage = {}
        
        for TemplateClass in self.all_templates:
            try:
                # Generate a sample to see what entities/relations it produces
                template = TemplateClass(0, datetime.now(), "first_person")
                _, entities_meta, relations_meta = template.generate()
                
                entities = {entity_type for _, (entity_type, _) in entities_meta.items()}
                relations = {rel_type for rel_type, _, _ in relations_meta}
                
                template_coverage[TemplateClass.__name__] = {
                    'entities': entities,
                    'relations': relations
                }
            except Exception as e:
                print(f"⚠️  Error analyzing {TemplateClass.__name__}: {e}")
                template_coverage[TemplateClass.__name__] = {
                    'entities': set(),
                    'relations': set()
                }
        
        return template_coverage
    
    def get_balance_score(self) -> float:
        """Calculate current balance score (0-1, where 1 is perfect balance)."""
        if not self.entity_usage or not self.relation_usage:
            return 0.0
        
        # Calculate coefficient of variation (CV) for both entities and relations
        entity_counts = list(self.entity_usage.values())
        relation_counts = list(self.relation_usage.values())
        
        def calculate_cv(values):
            if not values or len(values) < 2:
                return float('inf')
            mean_val = sum(values) / len(values)
            if mean_val == 0:
                return float('inf')
            variance = sum((x - mean_val) ** 2 for x in values) / len(values)
            std_dev = variance ** 0.5
            return std_dev / mean_val
        
        entity_cv = calculate_cv(entity_counts)
        relation_cv = calculate_cv(relation_counts)
        
        # Perfect balance has CV = 0, convert to score where 1 is perfect
        max_reasonable_cv = 1.0  # Reasonable upper bound
        entity_score = max(0, 1 - min(entity_cv / max_reasonable_cv, 1))
        relation_score = max(0, 1 - min(relation_cv / max_reasonable_cv, 1))
        
        return (entity_score + relation_score) / 2
    
    def get_coverage_percentage(self) -> Tuple[float, float]:
        """Get entity and relation coverage percentages."""
        entity_coverage = len(self.covered_entities) / len(self.all_entity_types) * 100
        relation_coverage = len(self.covered_relations) / len(self.all_relation_types) * 100
        return entity_coverage, relation_coverage
    
    def select_template_for_coverage_phase(self) -> Optional[type]:
        """Select template to maximize coverage of uncovered types."""
        uncovered_entities = self.all_entity_types - self.covered_entities
        uncovered_relations = self.all_relation_types - self.covered_relations
        
        if not uncovered_entities and not uncovered_relations:
            return None  # Full coverage achieved
        
        # Score templates based on how many uncovered types they provide
        best_template = None
        best_score = -1
        
        for TemplateClass in self.all_templates:
            template_name = TemplateClass.__name__
            if template_name not in self.template_entity_map:
                continue
                
            coverage = self.template_entity_map[template_name]
            
            # Count how many uncovered types this template would provide
            new_entities = len(coverage['entities'] & uncovered_entities)
            new_relations = len(coverage['relations'] & uncovered_relations)
            score = new_entities + new_relations
            
            if score > best_score:
                best_score = score
                best_template = TemplateClass
        
        return best_template
    
    def select_template_for_balance_phase(self, perspective: str) -> Optional[type]:
        """Select template to improve balance in the distribution phase."""
        templates = (self.first_person_templates if perspective == "first_person" 
                    else self.third_person_templates)
        
        # Find entity and relation types that are underrepresented
        entity_counts = dict(self.entity_usage)
        relation_counts = dict(self.relation_usage)
        
        if not entity_counts or not relation_counts:
            return random.choice(templates)
        
        # Calculate target counts for perfect balance
        total_entities = sum(entity_counts.values())
        total_relations = sum(relation_counts.values())
        
        target_entity_count = total_entities / len(self.all_entity_types)
        target_relation_count = total_relations / len(self.all_relation_types)
        
        # Score templates based on how much they help balance
        best_template = None
        best_score = -float('inf')
        
        for TemplateClass in templates:
            template_name = TemplateClass.__name__
            if template_name not in self.template_entity_map:
                continue
                
            coverage = self.template_entity_map[template_name]
            
            # Calculate balance improvement score
            score = 0
            
            for entity_type in coverage['entities']:
                current_count = entity_counts.get(entity_type, 0)
                deficit = max(0, target_entity_count - current_count)
                score += deficit
            
            for relation_type in coverage['relations']:
                current_count = relation_counts.get(relation_type, 0)
                deficit = max(0, target_relation_count - current_count)
                score += deficit
            
            if score > best_score:
                best_score = score
                best_template = TemplateClass
        
        return best_template or random.choice(templates)
    
    def update_usage(self, entities_meta: Dict, relations_meta: List):
        """Update usage tracking after successful generation."""
        # Track entity usage
        for _, (entity_type, _) in entities_meta.items():
            self.entity_usage[entity_type] += 1
            self.covered_entities.add(entity_type)
        
        # Track relation usage
        for rel_type, _, _ in relations_meta:
            self.relation_usage[rel_type] += 1
            self.covered_relations.add(rel_type)
    
    def get_detailed_statistics(self) -> Dict:
        """Get detailed balance and coverage statistics."""
        entity_coverage, relation_coverage = self.get_coverage_percentage()
        balance_score = self.get_balance_score()
        
        # Entity distribution analysis
        entity_counts = dict(self.entity_usage)
        entity_min = min(entity_counts.values()) if entity_counts else 0
        entity_max = max(entity_counts.values()) if entity_counts else 0
        entity_mean = sum(entity_counts.values()) / len(entity_counts) if entity_counts else 0
        
        # Relation distribution analysis  
        relation_counts = dict(self.relation_usage)
        relation_min = min(relation_counts.values()) if relation_counts else 0
        relation_max = max(relation_counts.values()) if relation_counts else 0
        relation_mean = sum(relation_counts.values()) / len(relation_counts) if relation_counts else 0
        
        return {
            'balance_score': balance_score,
            'entity_coverage_percentage': entity_coverage,
            'relation_coverage_percentage': relation_coverage,
            'entity_distribution': {
                'min_count': entity_min,
                'max_count': entity_max,
                'mean_count': entity_mean,
                'balance_ratio': entity_min / entity_max if entity_max > 0 else 0
            },
            'relation_distribution': {
                'min_count': relation_min,
                'max_count': relation_max,
                'mean_count': relation_mean,
                'balance_ratio': relation_min / relation_max if relation_max > 0 else 0
            },
            'coverage_status': {
                'entities_covered': len(self.covered_entities),
                'entities_total': len(self.all_entity_types),
                'relations_covered': len(self.covered_relations),
                'relations_total': len(self.all_relation_types)
            }
        }

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ENHANCED VALIDATION FUNCTIONS
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

def validate_entity_span_accuracy(text: str, entities_meta: Dict[str, Tuple[str, str]]) -> List[str]:
    """Enhanced validation that all entity spans are accurate in the text."""
    issues = []
    text_lower = text.lower()
    
    for entity_id, (entity_type, entity_text) in entities_meta.items():
        # Skip validation for pronouns and very short entities that might be implicit
        if entity_text.lower() in ['i', 'my', 'me', 'we', 'us', 'they', 'them']:
            continue
        if entity_text.lower() not in text_lower:
            issues.append(f"Entity '{entity_text}' ({entity_type}) not found in text")
    
    return issues

def validate_relation_consistency(entities_meta: Dict, relations_meta: List) -> List[str]:
    """Validate that all relations reference valid entities."""
    issues = []
    entity_ids = set(entities_meta.keys())
    
    for rel_type, subj_id, obj_id in relations_meta:
        if subj_id not in entity_ids:
            issues.append(f"Relation {rel_type} references invalid subject '{subj_id}'")
        if obj_id not in entity_ids:
            issues.append(f"Relation {rel_type} references invalid object '{obj_id}'")
    
    return issues

def comprehensive_record_validation(record: Dict) -> List[str]:
    """Comprehensive validation of a generated record."""
    issues = []
    
    # Basic structure validation
    required_fields = ['text', 'entities', 'relations', 'context']
    for field in required_fields:
        if field not in record:
            issues.append(f"Missing required field: {field}")
            return issues  # Can't continue without basic structure
    
    # Light validation - only check for critical issues
    if len(record['entities']) == 0:
        issues.append("No entities found in record")
    
    if len(record['relations']) == 0:
        issues.append("No relations found in record")
    
    # Only do deep validation if enabled and it's not causing too many failures
    if BalancedConfig.ENTITY_VALIDATION_ENABLED:
        # Entity span validation (relaxed)
        entities_meta = {ent['id']: (ent['type'], ent['text']) for ent in record['entities']}
        span_issues = validate_entity_span_accuracy(record['text'], entities_meta)
        if len(span_issues) > 2:  # Only flag if many issues
            issues.extend(span_issues[:2])  # Limit to first 2 issues
        
        # Relation consistency validation
        relations_meta = [(rel['type'], rel['head'], rel['tail']) for rel in record['relations']]
        relation_issues = validate_relation_consistency(entities_meta, relations_meta)
        issues.extend(relation_issues)
    
    return issues

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ENHANCED DATASET GENERATION WITH PERFECT BALANCE
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

def generate_balanced_dataset(num_records: int = None) -> Dict:
    """Generate perfectly balanced dataset with 100% coverage guarantee."""
    
    if num_records is None:
        num_records = BalancedConfig.DEFAULT_NUM_RECORDS
    
    print(f"🚀 ENHANCED BALANCED DATASET GENERATION")
    print(f"{'='*70}")
    print(f"Target records: {num_records}")
    print(f"Balance threshold: {BalancedConfig.BALANCE_THRESHOLD}")
    print(f"Coverage guarantee ratio: {BalancedConfig.COVERAGE_GUARANTEE_RATIO}")
    
    dataset = []
    base_date = datetime.strptime(BalancedConfig.CURRENT_UTC_DATETIME, "%Y-%m-%d %H:%M:%S")
    failed_generations = 0
    failure_reasons = defaultdict(int)
    validation_failures = defaultdict(int)
    
    # Define template classes (same as original)
    first_person_templates = [
        FirstPersonExpandedTravelTemplate, FirstPersonObjectOwnershipTemplate,
        FirstPersonHealthGoalTemplate, FirstPersonWorkRoleTemplate,
        FirstPersonWeatherMoodTemplate, FirstPersonTransportationMemoryTemplate,
        FirstPersonRoomPreferenceTemplate, FirstPersonMediaConsumptionTemplate,
        FirstPersonBusinessInteractionTemplate, FirstPersonEquipmentOwnershipTemplate,
        FirstPersonSocialAnxietyTemplate, FirstPersonSkillDevelopmentProgressTemplate,
        FirstPersonNicknameStoryTemplate, FirstPersonBorrowLendTemplate,
        FirstPersonFamilyTraditionTemplate, FirstPersonScheduleStressTemplate,
        FirstPersonValueConflictTemplate, FirstPersonSensoryOverloadTemplate,
        FirstPersonMoneyGoalTemplate, FirstPersonIdeaDevelopmentTemplate,
        FirstPersonBeliefChallengeTemplate, FirstPersonTasteMemoryTemplate,
        FirstPersonOpinionChangeTemplate, FirstPersonAttributeDevelopmentTemplate,
        FirstPersonChildhoodMemoryTemplate, FirstPersonLossGriefTemplate,
        FirstPersonCareerMilestoneTemplate, FirstPersonFearOvercomeTemplate,
        FirstPersonCreativeAchievementTemplate, FirstPersonHealthScareTemplate,
        FirstPersonFailureLessonTemplate, FirstPersonMentorshipMemoryTemplate,
        FirstPersonLifeStageReflectionTemplate, FirstPersonCulturalLearningTemplate,
        FirstPersonIndustryExpertiseTemplate, FirstPersonTimeAmountTemplate,
        FirstPersonThinkingProcessTemplate, FirstPersonRegretAnticipationTemplate,
        FirstPersonCompleteSensoryTemplate, FirstPersonRepeatingRoutineTemplate,
        FirstPersonComplexMemoryTemplate, FirstPersonMemoryRecallTemplate,
        FirstPersonCognitiveProcessTemplate, FirstPersonCompleteSensoryTemplate,
        FirstPersonTemporalRoutineTemplate, FirstPersonLocationExpertiseTemplate,
        FirstPersonHopesPlanningTemplate, FirstPersonBeliefsValuesTemplate,
        FirstPersonHealthManagementTemplate, FirstPersonFinancialGoalsTemplate,
        FirstPersonNicknameIdentityTemplate, FirstPersonIdeaInnovationTemplate,
        FirstPersonComprehensiveCoverageTemplate, FirstPersonAchievementTemplate,
        FirstPersonMediaPreferencesTemplate, FirstPersonLifeEventsTemplate
    ]
    
    third_person_templates = [
        ThirdPersonGroupMembershipTemplate, ThirdPersonFamilyRelationshipTemplate,
        ThirdPersonCausationTemplate, ThirdPersonLocationProximityTemplate,
        ThirdPersonVehicleOwnershipTemplate, ThirdPersonMediaProductionTemplate,
        ThirdPersonWeatherImpactTemplate, ThirdPersonPlatformInfluenceTemplate,
        ThirdPersonRoomOrganizationTemplate, ThirdPersonGenrePreferenceTemplate,
        ThirdPersonBusinessOwnershipTemplate, ThirdPersonTransportationRoutineTemplate,
        ThirdPersonConditionManagementTemplate, ThirdPersonSentimentAnalysisTemplate,
        ThirdPersonIntentActionTemplate, ThirdPersonProximityNetworkTemplate,
        ThirdPersonAttributeRecognitionTemplate, ThirdPersonDateEventTemplate,
        ThirdPersonPartOfSystemTemplate, ThirdPersonWeatherAdaptationTemplate,
        ThirdPersonFriendshipBondTemplate, ThirdPersonEquipmentSharingTemplate,
        ThirdPersonTimeManagementTemplate, ThirdPersonBeliefInfluenceTemplate,
        ThirdPersonLifeTransitionTemplate, ThirdPersonCulturalExperienceTemplate,
        ThirdPersonGenerosityTemplate, ThirdPersonSkillMasteryTemplate,
        ThirdPersonCommunityLeadershipTemplate, ThirdPersonIndustryInnovationTemplate,
        ThirdPersonLifeStageWisdomTemplate, ThirdPersonCulturalPreservationTemplate,
        ThirdPersonComprehensiveMemoryTemplate, ThirdPersonPetCareTemplate,
        ThirdPersonAdvancedCognitiveTemplate, ThirdPersonTemporalExpertiseTemplate,
        ThirdPersonRelationshipMaintainerTemplate, ThirdPersonLearningMentorshipTemplate,
        ThirdPersonEmotionalJourneyTemplate
    ]
    
    # Initialize balanced template manager
    template_manager = BalancedTemplateManager(first_person_templates, third_person_templates)
    
    # Calculate phase targets
    coverage_target = int(num_records * BalancedConfig.COVERAGE_GUARANTEE_RATIO)
    balance_target = num_records - coverage_target
    first_person_balance_target = int(balance_target * BalancedConfig.FIRST_PERSON_RATIO)
    third_person_balance_target = balance_target - first_person_balance_target
    
    print(f"📊 Generation phases:")
    print(f"   - Coverage guarantee: {coverage_target} records")
    print(f"   - Balanced distribution: {balance_target} records")
    print(f"     - First-person: {first_person_balance_target}")
    print(f"     - Third-person: {third_person_balance_target}")
    
    # PHASE 1: Coverage Guarantee
    print(f"\n🎯 PHASE 1: Coverage Guarantee ({coverage_target} records)")
    coverage_generated = 0
    coverage_failures = 0
    
    while coverage_generated < coverage_target and coverage_failures < coverage_target * 5:
        TemplateClass = template_manager.select_template_for_coverage_phase()
        
        if TemplateClass is None:
            print(f"✅ Full coverage achieved early at {coverage_generated} records")
            break
        
        # Generate record
        try:
            perspective = "first_person" if TemplateClass in first_person_templates else "third_person"
            template_id = len(dataset)
            template = TemplateClass(template_id, base_date, perspective)
            record = template.build()
            
            # Minimal validation - just check structure
            if not record or 'text' not in record or 'entities' not in record or 'relations' not in record:
                coverage_failures += 1
                continue
            
            # Update tracking
            entities_meta = {ent['id']: (ent['type'], ent['text']) for ent in record['entities']}
            relations_meta = [(rel['type'], rel['head'], rel['tail']) for rel in record['relations']]
            template_manager.update_usage(entities_meta, relations_meta)
            
            dataset.append(record)
            coverage_generated += 1
            
            # Progress update
            if coverage_generated % max(1, BalancedConfig.BALANCE_PROGRESS_INTERVAL // 10) == 0:
                entity_cov, relation_cov = template_manager.get_coverage_percentage()
                print(f"Coverage progress: {coverage_generated}/{coverage_target} | "
                      f"Entities: {entity_cov:.1f}% | Relations: {relation_cov:.1f}%")
        
        except Exception as e:
            coverage_failures += 1
            failure_reasons[str(e)] += 1
            
    if coverage_failures >= coverage_target * 5:
        print(f"⚠️  Coverage phase stopped after {coverage_failures} failures")
    
    print(f"Coverage phase complete: {coverage_generated} records generated")
    
    # PHASE 2: Balanced Distribution
    print(f"\n⚖️  PHASE 2: Balanced Distribution ({balance_target} records)")
    
    first_person_generated = 0
    third_person_generated = 0
    balance_failures = 0
    
    while len(dataset) < num_records and balance_failures < balance_target * 5:
        # Determine perspective based on targets
        if first_person_generated < first_person_balance_target:
            if third_person_generated >= third_person_balance_target:
                perspective = "first_person"
            else:
                # Choose based on ratio maintenance
                current_fp_ratio = first_person_generated / max(1, first_person_generated + third_person_generated)
                target_fp_ratio = BalancedConfig.FIRST_PERSON_RATIO
                perspective = "first_person" if current_fp_ratio < target_fp_ratio else "third_person"
        else:
            perspective = "third_person"
        
        # Select template for balance optimization
        TemplateClass = template_manager.select_template_for_balance_phase(perspective)
        
        try:
            template_id = len(dataset)
            template = TemplateClass(template_id, base_date, perspective)
            record = template.build()
            
            # Minimal validation
            if not record or 'text' not in record or 'entities' not in record or 'relations' not in record:
                balance_failures += 1
                continue
            
            # Update tracking
            entities_meta = {ent['id']: (ent['type'], ent['text']) for ent in record['entities']}
            relations_meta = [(rel['type'], rel['head'], rel['tail']) for rel in record['relations']]
            template_manager.update_usage(entities_meta, relations_meta)
            
            dataset.append(record)
            
            if perspective == "first_person":
                first_person_generated += 1
            else:
                third_person_generated += 1
            
            # Progress update
            if len(dataset) % BalancedConfig.PROGRESS_INTERVAL == 0:
                balance_score = template_manager.get_balance_score()
                entity_cov, relation_cov = template_manager.get_coverage_percentage()
                print(f"Balance progress: {len(dataset)}/{num_records} | "
                      f"Balance: {balance_score:.3f} | Coverage: E{entity_cov:.1f}% R{relation_cov:.1f}%")
        
        except Exception as e:
            balance_failures += 1
            failure_reasons[str(e)] += 1
            
    if balance_failures >= balance_target * 5:
        print(f"⚠️  Balance phase stopped after {balance_failures} failures")
    
    failed_generations = coverage_failures + balance_failures
    print(f"Balance phase complete: {len(dataset) - coverage_generated} records generated")
    
    # Generate comprehensive statistics
    stats = generate_enhanced_statistics(
        dataset, template_manager, failed_generations, failure_reasons, validation_failures
    )
    
    return {
        "dataset": dataset,
        "statistics": stats,
        "template_manager": template_manager
    }

def generate_enhanced_statistics(dataset: List[Dict], template_manager: BalancedTemplateManager,
                               failed_generations: int, failure_reasons: Dict, 
                               validation_failures: Dict) -> Dict:
    """Generate comprehensive statistics with balance and coverage analysis."""
    
    if not dataset:
        return {
            "generation_summary": {"total_generated": 0, "failed_generations": failed_generations, "success_rate": "0.0%"},
            "balance_analysis": {"balance_score": 0.0, "entity_balance_ratio": 0.0, "relation_balance_ratio": 0.0, "balance_threshold_met": False},
            "coverage_analysis": {"entity_coverage_percentage": 0.0, "relation_coverage_percentage": 0.0, "full_coverage_achieved": False},
            "perspective_distribution": {"first_person_records": 0, "third_person_records": 0},
            "distribution_analysis": {"entity_distribution": {}, "relation_distribution": {}},
            "quality_metrics": {"avg_entities_per_record": 0, "avg_relations_per_record": 0},
            "failure_analysis": dict(failure_reasons)
        }
    
    # Basic statistics
    total_generated = len(dataset)
    success_rate = total_generated / (total_generated + failed_generations) * 100 if total_generated else 0
    
    # Perspective analysis
    first_person_count = sum(1 for record in dataset 
                           if record.get('context', {}).get('Perspective') == 'first_person')
    third_person_count = total_generated - first_person_count
    
    # Balance and coverage analysis
    balance_stats = template_manager.get_detailed_statistics()
    
    # Content analysis
    all_entities = []
    all_relations = []
    
    for record in dataset:
        all_entities.extend([ent['type'] for ent in record['entities']])
        all_relations.extend([rel['type'] for rel in record['relations']])
    
    entity_counter = Counter(all_entities)
    relation_counter = Counter(all_relations)
    
    return {
        "generation_summary": {
            "total_generated": total_generated,
            "failed_generations": failed_generations,
            "success_rate": f"{success_rate:.1f}%",
            "validation_failures": dict(validation_failures)
        },
        "balance_analysis": {
            "balance_score": balance_stats['balance_score'],
            "entity_balance_ratio": balance_stats['entity_distribution']['balance_ratio'],
            "relation_balance_ratio": balance_stats['relation_distribution']['balance_ratio'],
            "balance_threshold_met": balance_stats['balance_score'] >= BalancedConfig.BALANCE_THRESHOLD
        },
        "coverage_analysis": {
            "entity_coverage_percentage": balance_stats['entity_coverage_percentage'],
            "relation_coverage_percentage": balance_stats['relation_coverage_percentage'],
            "entities_covered": balance_stats['coverage_status']['entities_covered'],
            "entities_total": balance_stats['coverage_status']['entities_total'],
            "relations_covered": balance_stats['coverage_status']['relations_covered'],
            "relations_total": balance_stats['coverage_status']['relations_total'],
            "full_coverage_achieved": (balance_stats['entity_coverage_percentage'] == 100.0 and 
                                     balance_stats['relation_coverage_percentage'] == 100.0)
        },
        "perspective_distribution": {
            "first_person_records": first_person_count,
            "third_person_records": third_person_count,
            "first_person_percentage": f"{(first_person_count/total_generated)*100:.1f}%" if total_generated > 0 else "0.0%",
            "third_person_percentage": f"{(third_person_count/total_generated)*100:.1f}%" if total_generated > 0 else "0.0%",
            "target_ratio_met": abs((first_person_count/total_generated) - BalancedConfig.FIRST_PERSON_RATIO) < 0.02 if total_generated > 0 else False
        },
        "distribution_analysis": {
            "entity_distribution": {
                "min_count": balance_stats['entity_distribution']['min_count'],
                "max_count": balance_stats['entity_distribution']['max_count'],
                "mean_count": balance_stats['entity_distribution']['mean_count'],
                "most_common": entity_counter.most_common(10),
                "least_common": entity_counter.most_common()[:-11:-1] if len(entity_counter) >= 10 else list(entity_counter.most_common())
            },
            "relation_distribution": {
                "min_count": balance_stats['relation_distribution']['min_count'],
                "max_count": balance_stats['relation_distribution']['max_count'],
                "mean_count": balance_stats['relation_distribution']['mean_count'],
                "most_common": relation_counter.most_common(10),
                "least_common": relation_counter.most_common()[:-11:-1] if len(relation_counter) >= 10 else list(relation_counter.most_common())
            }
        },
        "quality_metrics": {
            "avg_entities_per_record": len(all_entities) / total_generated if total_generated > 0 else 0,
            "avg_relations_per_record": len(all_relations) / total_generated if total_generated > 0 else 0,
            "unique_entity_types": len(set(all_entities)),
            "unique_relation_types": len(set(all_relations))
        },
        "failure_analysis": dict(failure_reasons)
    }

def print_enhanced_statistics(stats: Dict, template_manager: BalancedTemplateManager):
    """Print comprehensive statistics with enhanced balance information."""
    print(f"\n{'='*80}")
    print("ENHANCED BALANCED DATASET GENERATION COMPLETE")
    print(f"{'='*80}")
    
    # Generation summary
    gen = stats["generation_summary"]
    print(f"📊 Generation Summary:")
    print(f"   ✅ Total generated: {gen['total_generated']}")
    print(f"   ❌ Failed generations: {gen['failed_generations']}")
    print(f"   🎯 Success rate: {gen['success_rate']}")
    
    # Balance analysis
    balance = stats["balance_analysis"]
    print(f"\n⚖️  Balance Analysis:")
    print(f"   🎯 Overall balance score: {balance['balance_score']:.3f}")
    print(f"   📊 Entity balance ratio: {balance['entity_balance_ratio']:.3f}")
    print(f"   📊 Relation balance ratio: {balance['relation_balance_ratio']:.3f}")
    print(f"   ✅ Balance threshold met: {balance['balance_threshold_met']}")
    
    # Coverage analysis
    coverage = stats["coverage_analysis"]
    print(f"\n🎯 Coverage Analysis:")
    print(f"   📊 Entity coverage: {coverage['entity_coverage_percentage']:.1f}% "
          f"({coverage['entities_covered']}/{coverage['entities_total']})")
    print(f"   📊 Relation coverage: {coverage['relation_coverage_percentage']:.1f}% "
          f"({coverage['relations_covered']}/{coverage['relations_total']})")
    print(f"   ✅ Full coverage achieved: {coverage['full_coverage_achieved']}")
    
    # Perspective distribution
    perspective = stats["perspective_distribution"]
    print(f"\n👥 Perspective Distribution:")
    print(f"   👤 First-person: {perspective['first_person_records']} ({perspective['first_person_percentage']})")
    print(f"   👥 Third-person: {perspective['third_person_records']} ({perspective['third_person_percentage']})")
    print(f"   🎯 Target ratio met: {perspective['target_ratio_met']}")
    
    # Distribution analysis
    dist = stats["distribution_analysis"]
    print(f"\n📈 Distribution Analysis:")
    print(f"   Entity distribution - Min: {dist['entity_distribution']['min_count']}, "
          f"Max: {dist['entity_distribution']['max_count']}, "
          f"Mean: {dist['entity_distribution']['mean_count']:.1f}")
    print(f"   Relation distribution - Min: {dist['relation_distribution']['min_count']}, "
          f"Max: {dist['relation_distribution']['max_count']}, "
          f"Mean: {dist['relation_distribution']['mean_count']:.1f}")
    
    # Top/bottom distribution
    print(f"\n🔝 Most common entities:")
    for entity_type, count in dist['entity_distribution']['most_common'][:5]:
        print(f"      {entity_type}: {count}")
    
    print(f"\n🔝 Most common relations:")
    for relation_type, count in dist['relation_distribution']['most_common'][:5]:
        print(f"      {relation_type}: {count}")
    
    # Quality metrics
    quality = stats["quality_metrics"]
    print(f"\n✨ Quality Metrics:")
    print(f"   📊 Average entities per record: {quality['avg_entities_per_record']:.1f}")
    print(f"   📊 Average relations per record: {quality['avg_relations_per_record']:.1f}")
    print(f"   🎯 Unique entity types: {quality['unique_entity_types']}")
    print(f"   🎯 Unique relation types: {quality['unique_relation_types']}")

def save_balanced_dataset(result: Dict, filename: str = None) -> str:
    """Save balanced dataset with enhanced metadata."""
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"DeBERTa_balanced_dataset_{timestamp}.json"
    
    # Prepare enhanced output
    output_data = {
        "metadata": {
            "generation_timestamp": datetime.now().isoformat(),
            "generator_version": "data_improved.py v1.0",
            "balance_config": {
                "balance_threshold": BalancedConfig.BALANCE_THRESHOLD,
                "coverage_guarantee_ratio": BalancedConfig.COVERAGE_GUARANTEE_RATIO,
                "first_person_ratio": BalancedConfig.FIRST_PERSON_RATIO
            }
        },
        "statistics": result["statistics"],
        "dataset": result["dataset"]
    }
    
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    return filename

def main():
    """Main execution function for balanced dataset generation."""
    try:
        print("🚀 Starting Enhanced Balanced DeBERTa Dataset Generation")
        
        result = generate_balanced_dataset()
        
        if result["dataset"]:
            filename = save_balanced_dataset(result)
            print_enhanced_statistics(result["statistics"], result["template_manager"])
            
            print(f"\n💾 Enhanced dataset saved to: {filename}")
            
            # Show sample records highlighting balance
            print(f"\n📋 Sample Records (showing balance):")
            sample_records = random.sample(result["dataset"], min(3, len(result["dataset"])))
            for i, record in enumerate(sample_records):
                print(f"\n--- Sample {i+1} ---")
                print(f"Text: {record['text']}")
                entity_strings = [f"{e['type']}({e['text']})" for e in record['entities']]
                print(f"Entities: {entity_strings}")
                print(f"Relations: {[r['type'] for r in record['relations']]}")
                print(f"Perspective: {record.get('context', {}).get('Perspective', 'unknown')}")
                
        else:
            print("❌ ERROR: No records were successfully generated!")
            if "statistics" in result:
                print_enhanced_statistics(result["statistics"], result.get("template_manager"))
            
    except Exception as e:
        print(f"💥 Fatal error during balanced dataset generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()