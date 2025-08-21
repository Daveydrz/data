#!/usr/bin/env python3
"""
Coverage Analysis Script for Entity Types
Identifies missing entity types and provides detailed analysis.
"""

import sys
from datetime import datetime
sys.path.append('.')
from data import *

def analyze_entity_coverage():
    """Analyze current entity type coverage and identify missing types."""
    print("🔍 DETAILED ENTITY COVERAGE ANALYSIS")
    print("=" * 60)
    
    # Get all entity types
    all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
    print(f"📊 Total Entity Types Defined: {len(all_entity_types)}")
    print(f"Entity Types: {sorted(all_entity_types)}")
    
    # Define template classes
    first_person_templates = [
        FirstPersonExpandedTravelTemplate,
        FirstPersonObjectOwnershipTemplate,
        FirstPersonHealthGoalTemplate,
        FirstPersonWorkRoleTemplate,
        FirstPersonWeatherMoodTemplate,
        FirstPersonTransportationMemoryTemplate,
        FirstPersonRoomPreferenceTemplate,
        FirstPersonMediaConsumptionTemplate,
        FirstPersonBusinessInteractionTemplate,
        FirstPersonEquipmentOwnershipTemplate,
        FirstPersonSocialAnxietyTemplate,
        FirstPersonSkillDevelopmentProgressTemplate,
        FirstPersonNicknameStoryTemplate,
        FirstPersonBorrowLendTemplate,
        FirstPersonFamilyTraditionTemplate,
        FirstPersonScheduleStressTemplate,
        FirstPersonValueConflictTemplate,
        FirstPersonSensoryOverloadTemplate,
        FirstPersonMoneyGoalTemplate,
        FirstPersonIdeaDevelopmentTemplate,
        FirstPersonBeliefChallengeTemplate,
        FirstPersonTasteMemoryTemplate,
        FirstPersonOpinionChangeTemplate,
        FirstPersonAttributeDevelopmentTemplate,
        FirstPersonChildhoodMemoryTemplate,
        FirstPersonLossGriefTemplate,
        FirstPersonCareerMilestoneTemplate,
        FirstPersonFearOvercomeTemplate,
        FirstPersonCreativeAchievementTemplate,
        FirstPersonHealthScareTemplate,
        FirstPersonFailureLessonTemplate,
        FirstPersonMentorshipMemoryTemplate,
        FirstPersonLifeStageReflectionTemplate,
        FirstPersonCulturalLearningTemplate,
        FirstPersonIndustryExpertiseTemplate,
        FirstPersonTimeAmountTemplate,
        FirstPersonThinkingProcessTemplate,
        FirstPersonRegretAnticipationTemplate,
        FirstPersonCompleteSensoryTemplate,
        FirstPersonRepeatingRoutineTemplate,
        FirstPersonComplexMemoryTemplate,
        FirstPersonMemoryRecallTemplate,
        FirstPersonCognitiveProcessTemplate,
        FirstPersonCompleteSensoryTemplate,
        FirstPersonTemporalRoutineTemplate,
        FirstPersonLocationExpertiseTemplate,
        FirstPersonHopesPlanningTemplate,
        FirstPersonBeliefsValuesTemplate,
        FirstPersonHealthManagementTemplate,
        FirstPersonFinancialGoalsTemplate,
        FirstPersonNicknameIdentityTemplate,
        FirstPersonIdeaInnovationTemplate,
        FirstPersonComprehensiveCoverageTemplate,
        FirstPersonRelationshipTemplate
    ]

    third_person_templates = [
        ThirdPersonGroupMembershipTemplate,
        ThirdPersonFamilyRelationshipTemplate,
        ThirdPersonCausationTemplate,
        ThirdPersonLocationProximityTemplate,
        ThirdPersonVehicleOwnershipTemplate,
        ThirdPersonMediaProductionTemplate,
        ThirdPersonWeatherImpactTemplate,
        ThirdPersonPlatformInfluenceTemplate,
        ThirdPersonRoomOrganizationTemplate,
        ThirdPersonGenrePreferenceTemplate,
        ThirdPersonBusinessOwnershipTemplate,
        ThirdPersonTransportationRoutineTemplate,
        ThirdPersonConditionManagementTemplate,
        ThirdPersonSentimentAnalysisTemplate,
        ThirdPersonIntentActionTemplate,
        ThirdPersonProximityNetworkTemplate,
        ThirdPersonAttributeRecognitionTemplate,
        ThirdPersonDateEventTemplate,
        ThirdPersonPartOfSystemTemplate,
        ThirdPersonWeatherAdaptationTemplate,
        ThirdPersonFriendshipBondTemplate,
        ThirdPersonEquipmentSharingTemplate,
        ThirdPersonTimeManagementTemplate,
        ThirdPersonBeliefInfluenceTemplate,
        ThirdPersonLifeTransitionTemplate,
        ThirdPersonCulturalExperienceTemplate,
        ThirdPersonGenerosityTemplate,
        ThirdPersonSkillMasteryTemplate,
        ThirdPersonCommunityLeadershipTemplate,
        ThirdPersonIndustryInnovationTemplate,
        ThirdPersonLifeStageWisdomTemplate,
        ThirdPersonCulturalPreservationTemplate,
        ThirdPersonComprehensiveMemoryTemplate,
        ThirdPersonPetCareTemplate,
        ThirdPersonAdvancedCognitiveTemplate,
        ThirdPersonTemporalExpertiseTemplate,
        ThirdPersonRelationshipMaintainerTemplate,
        ThirdPersonRelationshipTemplate
    ]
    
    # Test coverage by generating sample from each template
    covered_entities = set()
    template_entity_map = {}
    
    print(f"\n🧪 Testing {len(first_person_templates + third_person_templates)} templates...")
    
    for TemplateClass in first_person_templates + third_person_templates:
        try:
            template = TemplateClass(0, datetime.now(), "first_person")
            _, entities_meta, relations_meta = template.generate()
            
            template_entities = set()
            for _, (entity_type, _) in entities_meta.items():
                covered_entities.add(entity_type)
                template_entities.add(entity_type)
            
            template_entity_map[TemplateClass.__name__] = template_entities
                
        except Exception as e:
            print(f"⚠️  Error in {TemplateClass.__name__}: {e}")
    
    # Calculate coverage
    entity_coverage = (len(covered_entities) / len(all_entity_types)) * 100
    missing_entities = all_entity_types - covered_entities
    
    print(f"\n✅ COVERAGE RESULTS:")
    print(f"   - Entity coverage: {entity_coverage:.1f}% ({len(covered_entities)}/{len(all_entity_types)})")
    print(f"   - Covered entities: {sorted(covered_entities)}")
    
    if missing_entities:
        print(f"\n❌ MISSING ENTITY TYPES: {sorted(missing_entities)}")
        print(f"   - Count: {len(missing_entities)}")
        
        # Suggest what types of templates might cover these
        for entity in sorted(missing_entities):
            print(f"   - {entity}: Need template that uses EntityTypes.{entity}")
    else:
        print(f"\n🎉 PERFECT! All entity types are covered!")
    
    return len(missing_entities) == 0, missing_entities

def main():
    """Main function to run coverage analysis."""
    success, missing = analyze_entity_coverage()
    
    if success:
        print(f"\n🎯 SUCCESS: 100% entity coverage achieved!")
    else:
        print(f"\n🎯 TASK: Create templates to cover {len(missing)} missing entity type(s)")
        for entity in sorted(missing):
            print(f"   - Need template for EntityTypes.{entity}")

if __name__ == "__main__":
    main()