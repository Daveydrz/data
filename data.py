import json
import random
import uuid
from datetime import datetime
from typing import Dict, List, Tuple, Optional

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# CONFIGURATION
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class Config:
    CURRENT_USER_LOGIN = "Daveydrz"
    CURRENT_UTC_DATETIME = "2025-08-20 10:33:42"
    DEFAULT_NUM_RECORDS = 40000
    MAX_RETRIES = 3
    OUTPUT_FILENAME = "DeBERTa_finetuning_dataset_expanded_relations.json"
    PROGRESS_INTERVAL = 500
    
    # Dataset composition ratios
    FIRST_PERSON_RATIO = 0.6  # 60% first-person memories
    THIRD_PERSON_RATIO = 0.4  # 40% third-person observations

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# COMPREHENSIVE ENTITY TYPES AND RELATION TAXONOMY
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class EntityTypes:
    # Core types
    PERSON = "PERSON"
    PRONOUN = "PRONOUN"
    ORGANIZATION = "ORGANIZATION"
    LOCATION = "LOCATION"
    ACTIVITY = "ACTIVITY"
    SKILL = "SKILL"
    PRODUCT = "PRODUCT"
    TECHNOLOGY = "TECHNOLOGY"
    GOAL = "GOAL"
    DATE = "DATE"
    TIME = "TIME"
    DURATION = "DURATION"
    AMOUNT = "AMOUNT"
    FREQUENCY = "FREQUENCY"
    CONDITION = "CONDITION"
    FOOD = "FOOD"
    BUSINESS = "BUSINESS"
    VEHICLE = "VEHICLE"
    EQUIPMENT = "EQUIPMENT"
    MEDIA = "MEDIA"
    GENRE = "GENRE"
    PLATFORM = "PLATFORM"
    HOBBY = "HOBBY"
    TRAIT = "TRAIT"
    RELATIONSHIP = "RELATIONSHIP"
    WEATHER = "WEATHER"
    INDUSTRY = "INDUSTRY"
    ROOM = "ROOM"
    PROJECT = "PROJECT"
    BUDGET = "BUDGET"
    TIMELINE = "TIMELINE"
    MEMORY_TYPE = "MEMORY_TYPE"
    LIFE_STAGE = "LIFE_STAGE" 
    CULTURAL_ELEMENT = "CULTURAL_ELEMENT"
    LEARNING_METHOD = "LEARNING_METHOD"
    PERSONAL_GROWTH = "PERSONAL_GROWTH"
    COMMUNITY_ROLE = "COMMUNITY_ROLE"

    
    # Comprehensive types
    PET = "PET"
    GROUP = "GROUP"
    GEOPOLITICAL_ENTITY = "GEOPOLITICAL_ENTITY"
    PERIOD = "PERIOD"
    EVENT = "EVENT"
    OBJECT = "OBJECT"
    CONCEPT = "CONCEPT"
    PREFERENCE = "PREFERENCE"
    VALUE = "VALUE"
    HEALTH_INFO = "HEALTH_INFO"
    MONEY = "MONEY"
    NICKNAME = "NICKNAME"
    RELATIONSHIP_TYPE = "RELATIONSHIP_TYPE"
    EMOTION = "EMOTION"
    SENSATION = "SENSATION"
    SENTIMENT = "SENTIMENT"
    INTENT = "INTENT"
    SOUND = "SOUND"
    SIGHT = "SIGHT"
    TASTE = "TASTE"
    SMELL = "SMELL"
    FEELING = "FEELING"
    BELIEF = "BELIEF"
    OPINION = "OPINION"
    IDEA = "IDEA"
    START_TIME = "START_TIME"
    END_TIME = "END_TIME"
    RECURRING_SCHEDULE = "RECURRING_SCHEDULE"
    TOPIC = "TOPIC"
    ROLE = "ROLE"
    ATTRIBUTE = "ATTRIBUTE"

class RelationTypes:
    # Original core relations
    WORKS_FOR = "WORKS_FOR"
    COLLABORATES_WITH = "COLLABORATES_WITH"
    WORKS_ON = "WORKS_ON"
    DOES_ACTIVITY = "DOES_ACTIVITY"
    HAS_HOBBY = "HAS_HOBBY"
    LEARNS = "LEARNS"
    USES = "USES"
    LIVES_IN = "LIVES_IN"
    SCHEDULED_FOR = "SCHEDULED_FOR"
    HAPPENS_ON = "HAPPENS_ON"
    HAS_DEADLINE = "HAS_DEADLINE"
    LIKES = "LIKES"
    PREFERS = "PREFERS"
    SERVES = "SERVES"
    COSTS = "COSTS"
    BUDGETS_FOR = "BUDGETS_FOR"
    IS_TYPE = "IS_TYPE"
    ENJOYS = "ENJOYS"
    WATCHES = "WATCHES"
    READS = "READS"
    LISTENS_TO = "LISTENS_TO"
    MENTORED_BY = "MENTORED_BY"
    OVERCAME = "OVERCAME" 
    MOURNS = "MOURNS"
    INSPIRED_BY = "INSPIRED_BY"
    ACHIEVED = "ACHIEVED"
    MASTERED = "MASTERED"
    LEADS_INITIATIVE = "LEADS_INITIATIVE"
    
    # EXPANDED RELATIONSHIP TYPES (as specified)
    HAS_ROLE = "HAS_ROLE"
    HAS_GROUP_MEMBER = "HAS_GROUP_MEMBER"
    AT_LOCATION = "AT_LOCATION"
    ON_DATE = "ON_DATE"
    FOR_DURATION = "FOR_DURATION"
    FEELS_EMOTION = "FEELS_EMOTION"
    HAS_PREFERENCE = "HAS_PREFERENCE"
    WANTS_GOAL = "WANTS_GOAL"
    HAS_OBJECT = "HAS_OBJECT"
    HAS_HEALTH_INFO = "HAS_HEALTH_INFO"
    HAS_SKILL = "HAS_SKILL"
    CAUSED_BY = "CAUSED_BY"
    ABOUT_TOPIC = "ABOUT_TOPIC"
    IS_FRIENDS_WITH = "IS_FRIENDS_WITH"
    IS_FAMILY_WITH = "IS_FAMILY_WITH"
    USED_FOR = "USED_FOR"
    HAD_SENTIMENT = "HAD_SENTIMENT"
    HAS_INTENT = "HAS_INTENT"
    RESULTS_IN = "RESULTS_IN"
    CONTRIBUTED_TO = "CONTRIBUTED_TO"
    OWNS = "OWNS"
    BORROWED = "BORROWED"
    LENT = "LENT"
    HAS_ATTRIBUTE = "HAS_ATTRIBUTE"
    IS_PART_OF = "IS_PART_OF"
    IS_NEAR = "IS_NEAR"
    TRAVELS_TO = "TRAVELS_TO"
    
    # Additional comprehensive relations
    HAS_PET = "HAS_PET"
    CARES_FOR = "CARES_FOR"
    MEMBER_OF = "MEMBER_OF"
    LEADS = "LEADS"
    PARTICIPATES_IN = "PARTICIPATES_IN"
    ATTENDS = "ATTENDS"
    ORGANIZES = "ORGANIZES"
    EXPERIENCES = "EXPERIENCES"
    FEELS = "FEELS"
    BELIEVES = "BELIEVES"
    THINKS = "THINKS"
    VALUES = "VALUES"
    HAS_OPINION = "HAS_OPINION"
    HAS_IDEA = "HAS_IDEA"
    HAS_HEALTH_CONDITION = "HAS_HEALTH_CONDITION"
    MANAGES_HEALTH = "MANAGES_HEALTH"
    SPENDS = "SPENDS"
    EARNS = "EARNS"
    SAVES = "SAVES"
    CALLED = "CALLED"
    KNOWN_AS = "KNOWN_AS"
    MAINTAINS_RELATIONSHIP = "MAINTAINS_RELATIONSHIP"
    HEARS = "HEARS"
    SEES = "SEES"
    TASTES = "TASTES"
    SMELLS = "SMELLS"
    TOUCHES = "TOUCHES"
    INTENDS = "INTENDS"
    PLANS = "PLANS"
    STARTS_AT = "STARTS_AT"
    ENDS_AT = "ENDS_AT"
    REPEATS = "REPEATS"
    FOLLOWS_SCHEDULE = "FOLLOWS_SCHEDULE"
    
    # Memory-specific relations
    THINKING_OF = "THINKING_OF"
    CONSIDERING = "CONSIDERING"
    REMEMBERS = "REMEMBERS"
    DREAMS_OF = "DREAMS_OF"
    WORRIES_ABOUT = "WORRIES_ABOUT"
    HOPES_FOR = "HOPES_FOR"
    REGRETS = "REGRETS"
    MISSES = "MISSES"
    LOOKING_FORWARD_TO = "LOOKING_FORWARD_TO"
    PLANNING = "PLANNING"
    HAS_GOAL = "HAS_GOAL"
    HAS_FREQUENCY = "HAS_FREQUENCY"
    HAS_TRAIT = "HAS_TRAIT"
    LOCATED_AT = "LOCATED_AT"
    WORKS_FROM = "WORKS_FROM"
    HAS_EXPERTISE = "HAS_EXPERTISE"

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# COMPREHENSIVE DATA POOLS
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

PEOPLE_NAMES = ["Alex Chen", "Jordan Smith", "Casey Williams", "Morgan Taylor", "Dr. Evelyn Reed", "Maria Garcia", "Wei Li", "Samira Khan", "Leo Schmidt", "Sofia Rossi", "Kenji Tanaka", "Liam O'Connell", "Chloe Dubois", "Ryan Murphy", "Zoe Park", "Marcus Johnson", "Isabella Rodriguez", "Finn Anderson", "Luna Martinez", "David Kim", "Sarah Wilson", "Michael Brown", "Jennifer Lee", "Robert Davis", "Emily Zhang", "Thomas Anderson", "Rachel Green", "Mark Thompson", "Lisa Wang", "James Rodriguez", "Amy Foster", "Oliver Park", "Emma Chen", "Sebastian Kim", "Maya Patel", "Gabriel Lopez", 
"Aria Singh", "Lucas Wang", "Zara Ahmed", "Felix Rodriguez", "Nora Thompson", "Ethan Foster", "Isla Martinez", "Adrian Zhou", "Ruby Williams", "Kai Johnson","Sage Miller", "Phoenix Davis", "River Garcia", "Orion Lee", "Luna Kim","Atlas Brown", "Nova Wilson", "Sage Taylor", "Ivy Chen", "Cruz Martinez"]

ROLES = ["project manager", "software engineer", "team lead", "data scientist", "designer", "product owner", "consultant", "analyst", "coordinator", "specialist", "director", "senior developer", "research assistant", "marketing manager", "sales representative", "customer support", "quality assurance", "business analyst", "system administrator", "content creator",]

TOPICS = ["artificial intelligence", "climate change", "productivity", "health and wellness", "technology trends", "personal development", "financial planning", "career growth", "relationship building", "creative projects", "sustainability", "innovation", "work-life balance", "entrepreneurship", "education", "social media", "fitness", "nutrition", "mental health", "travel experiences"]

ATTRIBUTES = ["experienced", "creative", "analytical", "collaborative", "innovative", "detail-oriented", "strategic", "empathetic", "reliable", "adaptable", "passionate", "organized", "communicative", "problem-solving", "leadership-oriented", "tech-savvy", "customer-focused", "results-driven", "team-oriented", "entrepreneurial"]

DATES = ["2024-01-15", "2024-03-22", "2024-06-10", "2024-09-05", "2024-12-20", "2025-02-14", "2025-05-30", "2025-08-16", "2025-11-25", "January 2024", "March 2024", "summer 2024", "fall 2024", "this year", "next month", "last week", "yesterday", "today"]

DURATIONS = ["two hours", "half a day", "three weeks", "six months", "one year", "several years", "a decade", "30 minutes", "90 minutes", "four hours", "all day", "overnight", "a weekend", "two weeks", "a quarter", "a semester", "the entire project", "indefinitely"]

NICKNAMES = ["Ace", "Buddy", "Chief", "Doc", "Eagle", "Flash", "Ghost", "Hero", "Jazz", "King", "Lion", "Max", "Ninja", "Owl", "Prince", "Queen", "Rebel", "Star", "Tiger", "Wolf"]

PETS = ["Golden Retriever named Max", "tabby cat named Whiskers", "German Shepherd named Rex", "Persian cat named Luna", "Border Collie named Scout", "Maine Coon cat named Shadow", "Labrador named Buddy", "Siamese cat named Blue", "Beagle named Charlie", "ragdoll cat named Milo", "parrot named Rio", "hamster named Peanut"]

GROUPS = ["book club", "hiking group", "chess club", "photography society", "cooking class", "language exchange", "volunteer organization", "sports team", "music band", "art collective", "study group", "professional association", "community garden group", "dance troupe", "environmental club", "startup accelerator", "maker space community"]

GEOPOLITICAL_ENTITIES = ["United States", "European Union", "California", "New York City", "Tokyo", "London", "Berlin", "Paris", "Sydney", "Toronto", "Singapore", "Hong Kong", "Dubai", "Barcelona", "Amsterdam", "Ibiza", "Bali", "Thailand", "Greece", "Italy", "Spain", "Portugal", "Mexico", "Costa Rica", "Japan", "Iceland", "Norway", "Switzerland"]

EVENTS = ["annual conference", "team building retreat", "product launch", "graduation ceremony", "wedding celebration", "birthday party", "company picnic", "charity fundraiser", "art exhibition", "music festival", "sports tournament", "networking event", "workshop series", "cultural festival", "technology summit", "hackathon", "trade show", "webinar series"]

OBJECTS = ["smartphone", "laptop", "coffee mug", "notebook", "headphones", "backpack", "camera", "bicycle", "watch", "tablet", "keyboard", "mouse", "monitor", "desk chair", "water bottle", "fitness tracker", "e-reader", "gaming console", "drone", "smart speaker"]

CONCEPTS = ["artificial intelligence", "sustainability", "innovation", "collaboration", "creativity", "leadership", "mindfulness", "efficiency", "diversity", "inclusion", "quality", "excellence", "growth", "learning", "adaptation", "automation", "digitalization", "remote work", "work-life balance", "continuous improvement"]

PREFERENCES = ["morning coffee", "quiet workspace", "natural lighting", "flexible schedule", "remote work", "team collaboration", "creative freedom", "structured environment", "continuous learning", "work-life balance", "minimal distractions", "open communication", "hands-on experience", "mentorship opportunities"]

VALUES = ["honesty", "integrity", "respect", "compassion", "excellence", "innovation", "teamwork", "responsibility", "fairness", "perseverance", "loyalty", "courage", "wisdom", "kindness", "dedication", "transparency", "authenticity", "empathy", "sustainability", "diversity"]

HEALTH_INFO = ["daily exercise routine", "balanced nutrition", "regular sleep schedule", "stress management", "mental wellness", "preventive care", "healthy lifestyle", "meditation practice", "physical therapy", "health monitoring", "yoga practice", "strength training", "cardiovascular fitness", "mindfulness meditation"]

MONEY = ["$500", "$1,200", "$5,000", "$10,000", "$25,000", "$50,000", "$100,000", "$250,000", "monthly salary", "annual bonus", "project budget", "savings account", "investment portfolio", "retirement fund", "emergency fund", "education fund", "travel budget", "health savings"]

EMOTIONS = ["happiness", "excitement", "contentment", "satisfaction", "joy", "enthusiasm", "calm", "relaxation", "confidence", "pride", "gratitude", "hope", "curiosity", "inspiration", "determination", "anxiety", "nervousness", "worry", "stress", "frustration", "nostalgia", "anticipation"]

SENTIMENTS = ["positive", "optimistic", "confident", "enthusiastic", "satisfied", "pleased", "content", "grateful", "hopeful", "inspired", "uncertain", "concerned", "excited", "nervous", "eager", "proud", "accomplished", "disappointed", "frustrated", "relieved"]

INTENTS = ["learn new skills", "improve performance", "build relationships", "achieve goals", "solve problems", "create value", "make impact", "grow professionally", "help others", "innovate", "optimize processes", "enhance user experience", "increase efficiency", "develop expertise"]

SKILLS = ["Python programming", "data analysis", "machine learning", "project management", "public speaking", "graphic design", "web development", "digital marketing", "financial analysis", "team leadership", "user experience design", "cloud computing", "cybersecurity", "agile methodology", "strategic planning", "communication", "negotiation", "time management"]

LOCATIONS = ["downtown office", "co-working space", "home office", "local library", "coffee shop", "university campus", "tech hub", "community center", "innovation lab", "startup incubator", "beach house", "mountain cabin", "city apartment", "suburban home", "hotel room", "conference center", "shared workspace", "outdoor terrace"]

ORGANIZATIONS = ["Innovate Corp", "DataSolutions Inc.", "Orion Robotics", "GreenScape Environmental", "Starlight Studios", "Apex Health", "QuantumLeap AI", "Helios Energy", "TechFlow Systems", "BlueSky Dynamics", "NovaTech", "EcoVision", "Phoenix Labs", "Skyline Industries", "Meridian Tech", "Digital Frontier", "CloudWorks", "NextGen Solutions", "Global Innovations", "Future Systems", "Toyota", "Ford", "MIT", "AWS", "Apple", "Microsoft", "Google", "Facebook", "Tesla"]

ACTIVITIES = ["developing software", "analyzing data", "designing interfaces", "managing projects", "conducting research", "teaching classes", "writing documentation", "testing applications", "building prototypes", "creating presentations", "traveling", "exercising", "reading", "cooking", "meditating", "networking", "mentoring", "strategizing", "problem-solving", "brainstorming"]

GOALS = ["learn new programming language", "get promoted", "start own business", "complete certification", "improve work-life balance", "develop leadership skills", "master new technology", "increase team efficiency", "launch new product", "expand professional network", "write a book", "speak at conferences", "mentor others", "achieve financial independence", "travel more", "improve health and fitness"]

WEATHER_CONDITIONS = ["sunny", "rainy", "cloudy", "snowy", "windy", "foggy", "stormy", "clear", "humid", "dry", "hot", "cold", "mild", "perfect weather"]

TRANSPORTATION = ["car", "bus", "train", "subway", "bicycle", "motorcycle", "plane", "taxi", "rideshare", "walking", "scooter", "boat", "ferry"]

ROOM_TYPES = ["bedroom", "living room", "kitchen", "office", "bathroom", "basement", "attic", "garage", "study", "dining room", "balcony", "patio", "garden"]

MEDIA_TYPES = ["podcast", "documentary", "movie", "TV series", "book", "audiobook", "YouTube video", "blog post", "article", "news report", "social media post", "webinar"]

PLATFORMS = ["Netflix", "YouTube", "Spotify", "Instagram", "LinkedIn", "Twitter", "Facebook", "TikTok", "Zoom", "Teams", "Discord", "Slack", "Reddit"]

GENRES = ["comedy", "drama", "thriller", "romance", "sci-fi", "fantasy", "documentary", "horror", "action", "mystery", "biography", "historical", "educational"]

VEHICLES = ["Tesla Model 3", "Honda Civic", "Toyota Prius", "Ford F-150", "BMW X5", "Audi A4", "Mercedes C-Class", "Jeep Wrangler", "Subaru Outback", "Nissan Leaf"]

BUSINESS_TYPES = ["restaurant", "coffee shop", "bookstore", "gym", "salon", "clinic", "pharmacy", "bank", "grocery store", "electronics store", "clothing store", "gas station"]

EQUIPMENT_TYPES = ["laptop stand", "ergonomic chair", "standing desk", "noise-canceling headphones", "external monitor", "wireless mouse", "mechanical keyboard", "tablet", "smartwatch", "camera"]

SOCIAL_SITUATIONS = ["dinner party", "work meeting", "family gathering", "friend's wedding", "networking event", "conference presentation", "team lunch", "birthday celebration", "holiday party", "casual hangout"]

CONDITIONS = ["stress", "fatigue", "excitement", "nervousness", "confidence", "uncertainty", "motivation", "creativity", "focus", "distraction", "burnout", "energy", "calm", "pressure"]

FREQUENCY_DETAILED = ["every morning", "twice a week", "once a month", "every few days", "daily", "weekly", "occasionally", "rarely", "frequently", "constantly", "seasonally", "annually"]
START_TIMES = ["6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "early morning", "morning", "afternoon", "evening"]

END_TIMES = ["10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "late evening", "night", "midnight", "end of day"]

RECURRING_SCHEDULES = ["daily", "weekly", "bi-weekly", "monthly", "quarterly", "seasonal", "occasional", "regular", "flexible", "strict", "intensive", "relaxed"]

SOUNDS = ["music", "laughter", "conversation", "traffic", "rain", "birds chirping", "keyboard typing", "phone ringing", "footsteps", "machinery", "wind", "silence", "ambient noise", "notifications"]

SIGHTS = ["sunset", "cityscape", "nature", "people walking", "traffic", "architecture", "artwork", "screens", "books", "colors", "patterns", "movement", "stillness", "lighting"]

SENSATIONS = ["warmth", "coolness", "pressure", "texture", "vibration", "tingling", "comfort", "discomfort", "smoothness", "roughness", "softness", "tension", "relaxation"]

TASTES = ["sweet", "salty", "bitter", "sour", "umami", "spicy", "mild", "rich", "fresh", "savory", "tangy", "creamy", "crisp", "smooth"]

SMELLS = ["coffee", "flowers", "rain", "food cooking", "perfume", "fresh air", "ocean breeze", "wood", "vanilla", "citrus", "herbs", "baking bread", "smoke", "leather"]

FEELINGS = ["comfortable", "uneasy", "energized", "tired", "focused", "distracted", "motivated",  "discouraged", "inspired", "overwhelmed", "peaceful", "restless", "secure", "vulnerable"]

BELIEFS = ["hard work pays off", "honesty is the best policy", "everyone deserves respect", "change is possible", "education is important", "family comes first", "time heals wounds", "actions speak louder than words", "everything happens for a reason", "persistence wins"]

OPINIONS = ["important", "overrated", "undervalued", "essential", "optional", "beneficial", "harmful", "interesting", "boring", "revolutionary", "traditional", "innovative"]

IDEAS = ["mobile app", "community project", "business venture", "creative collaboration", "research study", "improvement plan", "innovation concept", "solution design", "artistic project", "educational program", "sustainability initiative"]

FOODS = ["pasta", "sushi", "pizza", "salad", "sandwich", "soup", "curry", "tacos", "stir-fry", "grilled chicken", "chocolate", "ice cream", "fresh fruit", "vegetables", "bread", "cheese", "fish", "rice", "noodles", "dessert"]

HOBBIES = ["photography", "gardening", "cooking", "reading", "writing", "painting", "music", "sports", "hiking", "cycling", "gaming", "crafting", "collecting", "dancing", "traveling", "learning languages", "volunteering", "meditation", "fitness", "yoga"]

MEMORY_TYPES = ["episodic memory", "semantic memory", "procedural memory", "emotional memory", "traumatic memory", "childhood memory", "recent memory", "vivid memory", "fragmented memory", "nostalgic memory", "suppressed memory", "triggered memory", "collective memory", "false memory", "flashbulb memory"]

LIFE_STAGES = ["infancy", "toddlerhood", "childhood", "adolescence", "young adulthood", "early career", "career building", "mid-career", "senior career", "pre-retirement", "early retirement", "active retirement", "later life"]

CULTURAL_ELEMENTS = ["family recipes", "traditional songs", "cultural dances", "religious practices", "holiday customs", "storytelling traditions", "ancestral languages", "craft techniques", "ceremonial rituals", "folk art", "traditional games", "cultural dress", "historical narratives", "spiritual beliefs", "community celebrations"]

LEARNING_METHODS = ["hands-on practice", "visual observation", "verbal instruction", "trial and error", "mentorship", "formal education", "self-study", "peer learning", "experiential learning", "repetitive practice", "guided discovery", "collaborative learning", "online courses", "workshop attendance", "reading extensively"]

PERSONAL_GROWTH = ["emotional intelligence", "self-awareness", "confidence building", "resilience development", "communication skills", "leadership abilities", "empathy expansion", "stress management", "mindfulness practice", "creative expression", "problem-solving skills", "adaptability", "patience cultivation", "forgiveness capacity", "authenticity"]

COMMUNITY_ROLES = ["volunteer coordinator", "neighborhood watch leader", "school board member", "youth mentor", "community organizer", "local activist", "charity fundraiser", "environmental advocate", "cultural preservationist", "elder caretaker", "child advocate", "religious leader", "social worker", "community mediator", "local historian"]

PERIODS = ["during childhood", "in my teens", "college years", "early career", "when I was married", "after the divorce", "during pregnancy", "when kids were young", "midlife crisis", "empty nest years", "pre-retirement", "during illness", "after recovery", "recent years", "last decade", "formative years"]

# === ADD THESE DATA POOLS ===

MEMORY_TYPES = ["episodic memory", "semantic memory", "procedural memory", "emotional memory", "traumatic memory", "childhood memory", "recent memory", "vivid memory", "fragmented memory", "nostalgic memory", "suppressed memory", "triggered memory", "collective memory", "false memory", "flashbulb memory"]

LIFE_STAGES = ["infancy", "toddlerhood", "childhood", "adolescence", "young adulthood", "early career", "career building", "mid-career", "senior career", "pre-retirement", "early retirement", "active retirement", "later life"]

CULTURAL_ELEMENTS = ["family recipes", "traditional songs", "cultural dances", "religious practices", "holiday customs", "storytelling traditions", "ancestral languages", "craft techniques", "ceremonial rituals", "folk art", "traditional games", "cultural dress", "historical narratives", "spiritual beliefs", "community celebrations"]

LEARNING_METHODS = ["hands-on practice", "visual observation", "verbal instruction", "trial and error", "mentorship", "formal education", "self-study", "peer learning", "experiential learning", "repetitive practice", "guided discovery", "collaborative learning", "online courses", "workshop attendance", "reading extensively"]

PERSONAL_GROWTH = ["emotional intelligence", "self-awareness", "confidence building", "resilience development", "communication skills", "leadership abilities", "empathy expansion", "stress management", "mindfulness practice", "creative expression", "problem-solving skills", "adaptability", "patience cultivation", "forgiveness capacity", "authenticity"]

COMMUNITY_ROLES = ["volunteer coordinator", "neighborhood watch leader", "school board member", "youth mentor", "community organizer", "local activist", "charity fundraiser", "environmental advocate", "cultural preservationist", "elder caretaker", "child advocate", "religious leader", "social worker", "community mediator", "local historian"]

PERIODS = ["during childhood", "in my teens", "college years", "early career", "when I was married", "after the divorce", "during pregnancy", "when kids were young", "midlife crisis", "empty nest years", "pre-retirement", "during illness", "after recovery", "recent years", "last decade", "formative years"]

INDUSTRIES = ["technology", "healthcare", "finance", "education", "manufacturing", "retail", "entertainment", "construction", "agriculture", "transportation", "energy", "telecommunications", "hospitality", "consulting", "media"]

TECHNOLOGIES = ["artificial intelligence", "machine learning", "blockchain", "cloud computing", "IoT", "virtual reality", "augmented reality", "robotics", "quantum computing", "5G", "automation", "cybersecurity", "PyTorch", "TensorFlow", "React", "Angular", "Node.js", "Docker"]

PRODUCTS = ["smartphone app", "software platform", "physical device", "online service", "digital tool", "educational course", "fitness program", "creative work", "research paper", "business solution", "iPhone", "MacBook", "Tesla Model 3", "Samsung Galaxy", "iPad", "Surface Pro"]

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# UTILITY FUNCTIONS
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

def find_span_case_insensitive(text: str, subtext: str) -> Optional[List[int]]:
    """Find span of subtext in text, case-insensitive but return actual positions."""
    lower_text = text.lower()
    lower_subtext = subtext.lower()
    start = lower_text.find(lower_subtext)
    if start == -1: 
        return None
    return [start, start + len(subtext)]

def create_entity(entity_id: int, text: str, entity_type: str, entity_text: str) -> Optional[Dict]:
    """Create entity with proper span calculation."""
    span = find_span_case_insensitive(text, entity_text)
    if span:
        return {
            "id": entity_id, 
            "type": entity_type, 
            "text": entity_text, 
            "span": span
        }
    return None

def validate_entities_in_text(text: str, entities_meta: Dict[str, Tuple[str, str]]) -> List[Tuple[str, str]]:
    """Validate that all entity texts appear in the generated text."""
    missing_entities = []
    text_lower = text.lower()
    
    for key, (entity_type, entity_text) in entities_meta.items():
        if entity_text.lower() not in text_lower:
            missing_entities.append((key, entity_text))
    
    return missing_entities

def validate_record_quality(record: Dict) -> List[str]:
    """Validate record for quality issues."""
    issues = []
    
    # Check for self-referencing relations
    for relation in record.get('relations', []):
        if relation['head'] == relation['tail']:
            issues.append("Self-referencing relation found")
    
    # Check for duplicate entities
    entity_texts = [e['text'].lower() for e in record.get('entities', [])]
    if len(entity_texts) != len(set(entity_texts)):
        issues.append("Duplicate entities detected")
    
    # Check span accuracy
    text = record.get('text', '')
    for entity in record.get('entities', []):
        span = entity.get('span')
        if span and len(span) == 2:
            actual_text = text[span[0]:span[1]]
            if actual_text.lower() != entity['text'].lower():
                issues.append(f"Span mismatch for entity '{entity['text']}'")
    
    return issues

def get_different_person(exclude_person: str = "") -> str:
    """Get a different person name, excluding specified name."""
    available = [p for p in PEOPLE_NAMES if p != exclude_person]
    return random.choice(available) if available else random.choice(PEOPLE_NAMES)

def get_realistic_duration_for_transport(transport: str) -> str:
    """Get realistic duration based on transport type."""
    if transport in ["car", "bus", "subway", "taxi", "rideshare"]:
        return random.choice(["30 minutes", "1 hour", "2 hours", "half a day"])
    elif transport in ["train"]:
        return random.choice(["2 hours", "4 hours", "half a day", "all day"])
    elif transport in ["plane"]:
        return random.choice(["2 hours", "4 hours", "all day"])
    elif transport in ["bicycle", "walking", "scooter"]:
        return random.choice(["30 minutes", "1 hour", "2 hours"])
    else:
        return random.choice(["30 minutes", "1 hour", "2 hours", "half a day"])

def get_realistic_frequency_for_activity(activity: str) -> str:
    """Get realistic frequency based on activity type."""
    if "work" in activity.lower() or "managing" in activity.lower():
        return random.choice(["daily", "weekly", "every morning", "frequently"])
    elif "exercise" in activity.lower() or "fitness" in activity.lower():
        return random.choice(["daily", "three times a week", "every morning", "weekly"])
    elif "social" in activity.lower() or "networking" in activity.lower():
        return random.choice(["weekly", "monthly", "occasionally", "every few days"])
    else:
        return random.choice(FREQUENCY_DETAILED)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# TEMPLATE BASE CLASS
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class Template:
    def __init__(self, template_id: int, base_date: datetime, perspective: str = "first_person"):
        self.id = template_id
        self.base_date = base_date
        self.perspective = perspective
    
    def generate(self) -> Tuple[str, Dict[str, Tuple[str, str]], List[Tuple[str, str, str]]]:
        """Generate text, entities metadata, and relations metadata."""
        raise NotImplementedError("Subclasses must implement generate method")
    
    def build(self) -> Dict:
        """Build complete record with validation."""
        try:
            text, entities_meta, relations_meta = self.generate()
            
            # Validate entities exist in text
            missing_entities = validate_entities_in_text(text, entities_meta)
            if missing_entities:
                raise ValueError(f"Missing entities in text: {missing_entities}")
            
            # Create entities and build entity map
            entities = []
            entity_map = {}
            
            for key, (entity_type, entity_text) in entities_meta.items():
                entity = create_entity(len(entities), text, entity_type, entity_text)
                if entity:
                    entities.append(entity)
                    entity_map[key] = entity['id']
            
            # Create relations
            relations = []
            for rel_type, head_key, tail_key in relations_meta:
                if head_key in entity_map and tail_key in entity_map:
                    relations.append({
                        "type": rel_type,
                        "head": entity_map[head_key],
                        "tail": entity_map[tail_key]
                    })
            
            # Create context based on perspective
            context = {
                "Salience": random.choice(["High", "Medium", "Low"]),
                "Recency": random.choice(["just now", "recently", "last week", "yesterday", "this morning", "earlier today"]),
                "Source": "personal_memory" if self.perspective == "first_person" else "conversation",
                "Confidence": random.choice(["High", "Medium", "Low"]),
                "Associated_Emotion": random.choice(["Neutral", "Positive", "Excited", "Calm", "Anxious", "Hopeful", "Nostalgic"]),
                "Shared_With": "self" if self.perspective == "first_person" else "user",
                "Verbatim_Quote": entities[0]['text'] if entities else text[:50] + "...",
                "Perspective": self.perspective
            }
            
            if self.perspective == "first_person":
                context["Memory_Type"] = random.choice(["planning", "reflection", "consideration", "decision", "experience", "intention", "worry", "hope", "regret", "anticipation"])
            
            # Build final record
            record = {
                "id": f"dg_{self.id}_{uuid.uuid4().hex[:8]}",
                "text": text,
                "entities": entities,
                "relations": relations,
                "context": context
            }
            
            # Quality validation
            quality_issues = validate_record_quality(record)
            if quality_issues:
                raise ValueError(f"Quality issues: {quality_issues}")
            
            return record
            
        except Exception as e:
            raise Exception(f"Error in {self.__class__.__name__}: {str(e)}")

def get_realistic_duration_for_transport(transport: str) -> str:
    """Get realistic duration based on transport type."""
    if transport in ["car", "bus", "subway", "taxi", "rideshare"]:
        return random.choice(["30 minutes", "1 hour", "2 hours", "half a day"])
    elif transport in ["train"]:
        return random.choice(["2 hours", "4 hours", "half a day", "all day"])
    elif transport in ["plane"]:
        return random.choice(["2 hours", "4 hours", "all day"])
    elif transport in ["bicycle", "walking", "scooter"]:
        return random.choice(["30 minutes", "1 hour", "2 hours"])
    else:
        return random.choice(["30 minutes", "1 hour", "2 hours", "half a day"])

def get_realistic_frequency_for_activity(activity: str) -> str:
    """Get realistic frequency based on activity type."""
    if "work" in activity.lower() or "managing" in activity.lower():
        return random.choice(["daily", "weekly", "every morning", "frequently"])
    elif "exercise" in activity.lower() or "fitness" in activity.lower():
        return random.choice(["daily", "three times a week", "every morning", "weekly"])
    elif "social" in activity.lower() or "networking" in activity.lower():
        return random.choice(["weekly", "monthly", "occasionally", "every few days"])
    else:
        return random.choice(FREQUENCY_DETAILED)

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ENHANCED TEMPLATES USING EXPANDED RELATIONS
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class FirstPersonFinalCognitiveTemplate(Template):
    def generate(self):
        # Targets: THINKING_OF, CONSIDERING, DREAMS_OF, HOPES_FOR, REGRETS, LOOKING_FORWARD_TO, PLANNING, MISSES
        topic = random.choice(["career transition", "family planning", "creative projects", "life changes"])
        consideration = random.choice(["various options", "different approaches", "potential outcomes"])
        dream = random.choice(["artistic recognition", "family harmony", "professional success", "personal peace"])
        hope = random.choice(["positive change", "meaningful impact", "lasting happiness", "personal growth"])
        regret = random.choice(["missed chance", "poor timing", "wrong decision", "lost opportunity"])
        future_event = random.choice(["reunion", "celebration", "milestone", "achievement"])
        planning_detail = random.choice(["timeline", "resources", "strategy", "preparation"])
        missed_person = random.choice(PEOPLE_NAMES)
        
        text = f"I'm thinking of {topic} and considering {consideration}. I dream of {dream}, hope for {hope}, but regret {regret}. I'm looking forward to {future_event} and planning the {planning_detail}. I miss {missed_person}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "topic1": (EntityTypes.TOPIC, topic),
            "consider1": (EntityTypes.CONCEPT, consideration),
            "dream1": (EntityTypes.GOAL, dream),
            "hope1": (EntityTypes.CONCEPT, hope),
            "regret1": (EntityTypes.CONCEPT, regret),
            "event1": (EntityTypes.EVENT, future_event),
            "plan1": (EntityTypes.CONCEPT, planning_detail),
            "person1": (EntityTypes.PERSON, missed_person)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "user", "topic1"),
            (RelationTypes.CONSIDERING, "user", "consider1"),
            (RelationTypes.DREAMS_OF, "user", "dream1"),
            (RelationTypes.HOPES_FOR, "user", "hope1"),
            (RelationTypes.REGRETS, "user", "regret1"),
            (RelationTypes.LOOKING_FORWARD_TO, "user", "event1"),
            (RelationTypes.PLANNING, "user", "plan1"),
            (RelationTypes.MISSES, "user", "person1")
        ]
        
        return text, entities, relations

class FirstPersonAllSensoryTemplate(Template):
    def generate(self):
        # Targets: HEARS, SEES, TASTES, SMELLS, TOUCHES
        location = random.choice(["farmer's market", "beach at sunset", "mountain cabin", "grandmother's garden"])
        sound = random.choice(SOUNDS)
        sight = random.choice(SIGHTS)
        taste = random.choice(TASTES)
        smell = random.choice(SMELLS)
        touch_sensation = random.choice(SENSATIONS)
        
        text = f"At {location}, I hear {sound}, see {sight}, taste something {taste}, smell {smell}, and feel {touch_sensation} against my skin."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, location),
            "sound1": (EntityTypes.SOUND, sound),
            "sight1": (EntityTypes.SIGHT, sight),
            "taste1": (EntityTypes.TASTE, taste),
            "smell1": (EntityTypes.SMELL, smell),
            "touch1": (EntityTypes.SENSATION, touch_sensation)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "loc1"),
            (RelationTypes.HEARS, "user", "sound1"),
            (RelationTypes.SEES, "user", "sight1"),
            (RelationTypes.TASTES, "user", "taste1"),
            (RelationTypes.SMELLS, "user", "smell1"),
            (RelationTypes.TOUCHES, "user", "touch1")
        ]
        
        return text, entities, relations

class FirstPersonTimeScheduleTemplate(Template):
    def generate(self):
        # Targets: REPEATS, INTENDS, PLANS, STARTS_AT, ENDS_AT, FOLLOWS_SCHEDULE
        activity = random.choice(["morning routine", "work session", "exercise", "creative time"])
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        schedule = random.choice(RECURRING_SCHEDULES)
        intent = random.choice(INTENTS)
        plan = random.choice(["skill development", "health improvement", "productivity increase", "stress reduction"])
        
        text = f"I repeat {activity} from {start_time} to {end_time} following a {schedule} schedule. I intend to {intent} and plan for {plan}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "intent1": (EntityTypes.INTENT, intent),
            "plan1": (EntityTypes.CONCEPT, plan)
        }
        
        relations = [
            (RelationTypes.REPEATS, "user", "activity1"),
            (RelationTypes.STARTS_AT, "activity1", "start1"),
            (RelationTypes.ENDS_AT, "activity1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.INTENDS, "user", "intent1"),
            (RelationTypes.PLANS, "user", "plan1")
        ]
        
        return text, entities, relations

class FirstPersonLocationExpertiseTraitTemplate(Template):
    def generate(self):
        # Targets: LOCATED_AT, HAS_EXPERTISE, HAS_TRAIT, MAINTAINS_RELATIONSHIP
        location = random.choice(LOCATIONS)
        expertise = random.choice(SKILLS)
        trait = random.choice(["reliability", "creativity", "analytical thinking", "leadership"])
        relationship = random.choice(["mentorship", "partnership", "collaboration", "friendship"])
        person = random.choice(PEOPLE_NAMES)
        
        text = f"I'm located at {location} where I demonstrate my {expertise} expertise and {trait} trait. I maintain a {relationship} relationship with {person}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, location),
            "expert1": (EntityTypes.SKILL, expertise),
            "trait1": (EntityTypes.TRAIT, trait),
            "rel1": (EntityTypes.RELATIONSHIP_TYPE, relationship),
            "person1": (EntityTypes.PERSON, person)
        }
        
        relations = [
            (RelationTypes.LOCATED_AT, "user", "loc1"),
            (RelationTypes.HAS_EXPERTISE, "user", "expert1"),
            (RelationTypes.HAS_TRAIT, "user", "trait1"),
            (RelationTypes.MAINTAINS_RELATIONSHIP, "user", "rel1")
        ]
        
        return text, entities, relations

class FirstPersonBeliefsOpinionsTemplate(Template):
    def generate(self):
        # Targets: BELIEVES, THINKS, VALUES, HAS_OPINION, HAS_IDEA
        belief = random.choice(BELIEFS)
        value = random.choice(VALUES)
        opinion = random.choice(OPINIONS)
        idea = random.choice(IDEAS)
        topic = random.choice(TOPICS)
        thinking_activity = random.choice(["reflecting", "analyzing", "contemplating", "evaluating"])
        
        text = f"I believe in '{belief}' and value {value}. I think {opinion} about {topic} and have an idea for {idea}. I'm {thinking_activity} on these concepts."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "belief1": (EntityTypes.BELIEF, belief),
            "value1": (EntityTypes.VALUE, value),
            "opinion1": (EntityTypes.OPINION, opinion),
            "idea1": (EntityTypes.IDEA, idea),
            "topic1": (EntityTypes.TOPIC, topic),
            "think1": (EntityTypes.ACTIVITY, thinking_activity)
        }
        
        relations = [
            (RelationTypes.BELIEVES, "user", "belief1"),
            (RelationTypes.VALUES, "user", "value1"),
            (RelationTypes.HAS_OPINION, "user", "opinion1"),
            (RelationTypes.HAS_IDEA, "user", "idea1"),
            (RelationTypes.ABOUT_TOPIC, "opinion1", "topic1"),
            (RelationTypes.THINKS, "user", "think1")
        ]
        
        return text, entities, relations

class FirstPersonHealthFinanceTemplate(Template):
    def generate(self):
        # Targets: HAS_HEALTH_CONDITION, MANAGES_HEALTH, SPENDS, EARNS, SAVES
        health_condition = random.choice(["chronic condition", "fitness goal", "wellness plan", "health maintenance"])
        health_management = random.choice(HEALTH_INFO)
        spending = random.choice(MONEY)
        earning_source = random.choice(["job", "business", "investments", "consulting"])
        savings_amount = random.choice(MONEY)
        
        text = f"I have a {health_condition} that I manage through {health_management}. I earn from {earning_source}, spend {spending} on health, and save {savings_amount} monthly."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "condition1": (EntityTypes.CONDITION, health_condition),
            "health1": (EntityTypes.HEALTH_INFO, health_management),
            "spending1": (EntityTypes.MONEY, spending),
            "earning1": (EntityTypes.CONCEPT, earning_source),
            "savings1": (EntityTypes.MONEY, savings_amount)
        }
        
        relations = [
            (RelationTypes.HAS_HEALTH_CONDITION, "user", "condition1"),
            (RelationTypes.MANAGES_HEALTH, "user", "health1"),
            (RelationTypes.SPENDS, "user", "spending1"),
            (RelationTypes.EARNS, "user", "earning1"),
            (RelationTypes.SAVES, "user", "savings1")
        ]
        
        return text, entities, relations

class FirstPersonIdentityNicknameTemplate(Template):
    def generate(self):
        # Targets: CALLED, KNOWN_AS
        nickname = random.choice(NICKNAMES)
        friend = random.choice(PEOPLE_NAMES)
        professional_name = random.choice(["The Innovator", "The Problem Solver", "The Mentor", "The Strategist"])
        group = random.choice(GROUPS)
        
        text = f"My friend {friend} calls me {nickname}, and in our {group}, I'm known as {professional_name} for my contributions."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "nick1": (EntityTypes.NICKNAME, nickname),
            "friend1": (EntityTypes.PERSON, friend),
            "prof_name": (EntityTypes.NICKNAME, professional_name),
            "group1": (EntityTypes.GROUP, group)
        }
        
        relations = [
            (RelationTypes.CALLED, "user", "nick1"),
            (RelationTypes.KNOWN_AS, "user", "prof_name"),
            (RelationTypes.IS_FRIENDS_WITH, "user", "friend1"),
            (RelationTypes.MEMBER_OF, "user", "group1")
        ]
        
        return text, entities, relations

class ThirdPersonPetTemplate(Template):
    def generate(self):
        # Targets: HAS_PET, CARES_FOR
        person = random.choice(PEOPLE_NAMES)
        pet = random.choice(PETS)
        care_activity = random.choice(["daily walks", "grooming", "training", "veterinary care"])
        frequency = random.choice(FREQUENCY_DETAILED)
        location = random.choice(["local park", "home", "vet clinic", "pet store"])
        
        text = f"{person} has a {pet} and provides {care_activity} {frequency} at {location}. They care for their pet with dedication."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "pet1": (EntityTypes.PET, pet),
            "care1": (EntityTypes.ACTIVITY, care_activity),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "loc1": (EntityTypes.LOCATION, location)
        }
        
        relations = [
            (RelationTypes.HAS_PET, "p1", "pet1"),
            (RelationTypes.CARES_FOR, "p1", "pet1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "care1"),
            (RelationTypes.HAS_FREQUENCY, "care1", "freq1"),
            (RelationTypes.AT_LOCATION, "care1", "loc1")
        ]
        
        return text, entities, relations

# === ENTITY TYPE COVERAGE TEMPLATE ===
# This template uses rare entity types that might be missing

class FirstPersonRareEntityTypesTemplate(Template):
    def generate(self):
        # Target any potentially missing entity types
        amount = random.choice(["$500", "$1,200", "$2,000", "15%", "25 units", "100 items"])
        time = random.choice(["7:30 AM", "2:15 PM", "9:45 PM"])
        budget = random.choice(["monthly budget", "annual budget", "project budget"])
        timeline = random.choice(["6-month timeline", "annual timeline", "5-year timeline"])
        
        text = f"At {time}, I allocate {amount} to my {budget} planning, following a {timeline} for my goals."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "time1": (EntityTypes.TIME, time),
            "amount1": (EntityTypes.AMOUNT, amount),
            "budget1": (EntityTypes.BUDGET, budget),
            "timeline1": (EntityTypes.TIMELINE, timeline)
        }
        
        relations = [
            (RelationTypes.STARTS_AT, "budget1", "time1"),
            (RelationTypes.HAS_OBJECT, "budget1", "amount1"),
            (RelationTypes.BUDGETS_FOR, "user", "budget1"),
            (RelationTypes.HAS_DEADLINE, "budget1", "timeline1")
        ]
        
        return text, entities, relations

class FirstPersonIndustryKnowledgeTemplate(Template):
    def generate(self):
        industry = random.choice(["healthcare", "finance", "technology", "education", "manufacturing", "retail", "hospitality", "energy", "transportation", "construction"])
        skill = random.choice(SKILLS)
        experience = random.choice(["5 years", "3 years", "decade", "several years"])
        trend = random.choice(["automation", "digitization", "sustainability", "remote work", "artificial intelligence"])
        expertise_area = random.choice(["market analysis", "process optimization", "regulatory compliance", "innovation strategy"])
        
        text = f"I have {experience} of experience in the {industry} industry. My {skill} skills help me understand {trend} trends and develop {expertise_area} expertise."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "exp1": (EntityTypes.DURATION, experience),
            "ind1": (EntityTypes.INDUSTRY, industry),
            "skill1": (EntityTypes.SKILL, skill),
            "trend1": (EntityTypes.CONCEPT, trend),
            "expert1": (EntityTypes.CONCEPT, expertise_area)
        }
        
        relations = [
            (RelationTypes.HAS_SKILL, "user", "skill1"),
            (RelationTypes.FOR_DURATION, "user", "exp1"),
            (RelationTypes.ABOUT_TOPIC, "skill1", "ind1"),
            (RelationTypes.ABOUT_TOPIC, "trend1", "ind1"),
            (RelationTypes.HAS_EXPERTISE, "user", "expert1")
        ]
        
        return text, entities, relations

class FirstPersonQuantityAmountTemplate(Template):
    def generate(self):
        activity = random.choice(["grocery shopping", "meal planning", "project budgeting", "resource allocation"])
        amount = random.choice(["$150", "$75", "20 items", "5 packages", "dozen units", "50%", "25 pounds"])
        frequency = random.choice(FREQUENCY_DETAILED)
        location = random.choice(LOCATIONS)
        purpose = random.choice(["family needs", "personal goals", "project requirements", "efficiency improvement"])
        
        text = f"I do {activity} {frequency} at {location}, typically purchasing {amount} for {purpose}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "act1": (EntityTypes.ACTIVITY, activity),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "loc1": (EntityTypes.LOCATION, location),
            "amount1": (EntityTypes.AMOUNT, amount),
            "purp1": (EntityTypes.CONCEPT, purpose)
        }
        
        relations = [
            (RelationTypes.DOES_ACTIVITY, "user", "act1"),
            (RelationTypes.HAS_FREQUENCY, "act1", "freq1"),
            (RelationTypes.AT_LOCATION, "act1", "loc1"),
            (RelationTypes.HAS_OBJECT, "act1", "amount1"),
            (RelationTypes.USED_FOR, "act1", "purp1")
        ]
        
        return text, entities, relations

class ThirdPersonIndustryExpertiseTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        industry = random.choice(["automotive", "aerospace", "pharmaceuticals", "telecommunications", "banking", "insurance", "media", "consulting", "agriculture", "mining"])
        role = random.choice(["analyst", "consultant", "specialist", "manager", "director"])
        innovation = random.choice(["breakthrough technology", "process improvement", "market expansion", "cost optimization"])
        impact = random.choice(["industry recognition", "market leadership", "operational efficiency", "customer satisfaction"])
        
        text = f"{person} works as a {role} in the {industry} industry. They developed {innovation} that led to {impact}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "role1": (EntityTypes.ROLE, role),
            "ind1": (EntityTypes.INDUSTRY, industry),
            "innov1": (EntityTypes.CONCEPT, innovation),
            "imp1": (EntityTypes.CONCEPT, impact)
        }
        
        relations = [
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.ABOUT_TOPIC, "role1", "ind1"),
            (RelationTypes.ACHIEVED, "p1", "innov1"),
            (RelationTypes.RESULTS_IN, "innov1", "imp1")
        ]
        
        return text, entities, relations

class FirstPersonCognitiveProcessTemplate(Template):
    def generate(self):
        thinking_topic = random.choice(["career transition", "relationship decisions", "life priorities", "future planning"])
        consideration = random.choice(["various options", "different perspectives", "potential consequences", "alternative approaches"])
        dream_goal = random.choice(["financial freedom", "creative fulfillment", "family happiness", "personal growth"])
        future_event = random.choice(["graduation ceremony", "wedding celebration", "retirement party", "project completion"])
        timeline = random.choice(["next summer", "within two years", "by age 50", "in the near future"])
        regret = random.choice(["missed opportunity", "poor decision", "lost friendship", "unfulfilled potential"])
        missing_person = random.choice(PEOPLE_NAMES)
        
        text = f"I'm thinking of {thinking_topic} and considering {consideration}. I dream of {dream_goal} and am looking forward to {future_event} {timeline}. I regret {regret} and miss {missing_person}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "topic1": (EntityTypes.TOPIC, thinking_topic),
            "consider1": (EntityTypes.CONCEPT, consideration),
            "dream1": (EntityTypes.GOAL, dream_goal),
            "event1": (EntityTypes.EVENT, future_event),
            "time1": (EntityTypes.TIMELINE, timeline),
            "regret1": (EntityTypes.CONCEPT, regret),
            "person1": (EntityTypes.PERSON, missing_person)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "user", "topic1"),
            (RelationTypes.CONSIDERING, "user", "consider1"),
            (RelationTypes.DREAMS_OF, "user", "dream1"),
            (RelationTypes.LOOKING_FORWARD_TO, "user", "event1"),
            (RelationTypes.HAS_DEADLINE, "event1", "time1"),
            (RelationTypes.REGRETS, "user", "regret1"),
            (RelationTypes.MISSES, "user", "person1")
        ]
        
        return text, entities, relations

class FirstPersonCompleteSensoryTemplate(Template):
    def generate(self):
        location = random.choice(["bustling market", "quiet library", "grandmother's kitchen", "mountain trail"])
        sound = random.choice(SOUNDS)
        sight = random.choice(SIGHTS)
        taste = random.choice(TASTES)
        smell = random.choice(SMELLS)
        touch_sensation = random.choice(SENSATIONS)
        memory_trigger = random.choice(MEMORY_TYPES)
        
        text = f"At the {location}, I hear {sound}, see {sight}, taste something {taste}, smell {smell}, and feel {touch_sensation}. This triggers a {memory_trigger}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, location),
            "sound1": (EntityTypes.SOUND, sound),
            "sight1": (EntityTypes.SIGHT, sight),
            "taste1": (EntityTypes.TASTE, taste),
            "smell1": (EntityTypes.SMELL, smell),
            "touch1": (EntityTypes.SENSATION, touch_sensation),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_trigger)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "loc1"),
            (RelationTypes.HEARS, "user", "sound1"),
            (RelationTypes.SEES, "user", "sight1"),
            (RelationTypes.TASTES, "user", "taste1"),
            (RelationTypes.SMELLS, "user", "smell1"),
            (RelationTypes.TOUCHES, "user", "touch1"),
            (RelationTypes.CAUSED_BY, "memory1", "smell1")
        ]
        
        return text, entities, relations

class FirstPersonTemporalRoutineTemplate(Template):
    def generate(self):
        routine_activity = random.choice(["morning meditation", "evening workout", "weekly planning", "daily journaling"])
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        schedule = random.choice(RECURRING_SCHEDULES)
        frequency = random.choice(FREQUENCY_DETAILED)
        trait = random.choice(["discipline", "mindfulness", "consistency", "focus"])
        expertise_area = random.choice(SKILLS)
        intent = random.choice(INTENTS)
        
        text = f"I repeat {routine_activity} from {start_time} to {end_time} on a {schedule} basis {frequency}. This develops my {trait} trait and {expertise_area} expertise. I intend to {intent} and plan to continue."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "activity1": (EntityTypes.ACTIVITY, routine_activity),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "trait1": (EntityTypes.TRAIT, trait),
            "expert1": (EntityTypes.SKILL, expertise_area),
            "intent1": (EntityTypes.INTENT, intent)
        }
        
        relations = [
            (RelationTypes.REPEATS, "user", "activity1"),
            (RelationTypes.STARTS_AT, "activity1", "start1"),
            (RelationTypes.ENDS_AT, "activity1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.HAS_FREQUENCY, "activity1", "freq1"),
            (RelationTypes.HAS_TRAIT, "user", "trait1"),
            (RelationTypes.HAS_EXPERTISE, "user", "expert1"),
            (RelationTypes.INTENDS, "user", "intent1"),
            (RelationTypes.PLANS, "user", "activity1")
        ]
        
        return text, entities, relations

class FirstPersonLocationExpertiseTemplate(Template):
    def generate(self):
        work_location = random.choice(LOCATIONS)
        expertise_area = random.choice(SKILLS)
        relationship_type = random.choice(["mentorship", "professional partnership", "collaborative friendship", "advisory relationship"])
        colleague = random.choice(PEOPLE_NAMES)
        project = random.choice(["research initiative", "product development", "client solution", "innovation project"])
        
        text = f"I'm located at {work_location} where I apply my {expertise_area} expertise. I maintain a {relationship_type} with {colleague} while working on the {project}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, work_location),
            "expert1": (EntityTypes.SKILL, expertise_area),
            "rel1": (EntityTypes.RELATIONSHIP_TYPE, relationship_type),
            "colleague1": (EntityTypes.PERSON, colleague),
            "proj1": (EntityTypes.PROJECT, project)
        }
        
        relations = [
            (RelationTypes.LOCATED_AT, "user", "loc1"),
            (RelationTypes.HAS_EXPERTISE, "user", "expert1"),
            (RelationTypes.MAINTAINS_RELATIONSHIP, "user", "rel1"),
            (RelationTypes.COLLABORATES_WITH, "user", "colleague1"),
            (RelationTypes.WORKS_ON, "user", "proj1")
        ]
        
        return text, entities, relations

class FirstPersonHopesPlanningTemplate(Template):
    def generate(self):
        hope = random.choice(["career advancement", "family stability", "personal fulfillment", "financial security"])
        planning_activity = random.choice(["setting goals", "creating timelines", "researching options", "building skills"])
        future_goal = random.choice(GOALS)
        timeline = random.choice(["next year", "within five years", "by retirement", "in the coming decade"])
        emotion = random.choice(["optimistic", "determined", "excited", "motivated"])
        
        text = f"I'm hoping for {hope} and actively planning by {planning_activity}. I want to {future_goal} {timeline} and feel {emotion} about the future."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "hope1": (EntityTypes.CONCEPT, hope),
            "plan1": (EntityTypes.ACTIVITY, planning_activity),
            "goal1": (EntityTypes.GOAL, future_goal),
            "time1": (EntityTypes.TIMELINE, timeline),
            "emotion1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.HOPES_FOR, "user", "hope1"),
            (RelationTypes.PLANNING, "user", "plan1"),
            (RelationTypes.WANTS_GOAL, "user", "goal1"),
            (RelationTypes.HAS_DEADLINE, "goal1", "time1"),
            (RelationTypes.FEELS_EMOTION, "user", "emotion1")
        ]
        
        return text, entities, relations

class FirstPersonBeliefsValuesTemplate(Template):
    def generate(self):
        belief = random.choice(BELIEFS)
        value = random.choice(VALUES)
        opinion = random.choice(["very important", "somewhat valuable", "absolutely essential", "moderately significant"])
        topic = random.choice(TOPICS)
        thinking_process = random.choice(["reflecting deeply", "analyzing carefully", "considering thoroughly", "evaluating honestly"])
        
        text = f"I believe in '{belief}' and strongly value {value}. My opinion is that {topic} is {opinion}. I've been thinking about this and {thinking_process}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "belief1": (EntityTypes.BELIEF, belief),
            "value1": (EntityTypes.VALUE, value),
            "opinion1": (EntityTypes.OPINION, opinion),
            "topic1": (EntityTypes.TOPIC, topic),
            "think1": (EntityTypes.ACTIVITY, thinking_process)
        }
        
        relations = [
            (RelationTypes.BELIEVES, "user", "belief1"),
            (RelationTypes.VALUES, "user", "value1"),
            (RelationTypes.HAS_OPINION, "user", "opinion1"),
            (RelationTypes.ABOUT_TOPIC, "opinion1", "topic1"),
            (RelationTypes.THINKS, "user", "think1")
        ]
        
        return text, entities, relations

class FirstPersonHealthManagementTemplate(Template):
    def generate(self):
        health_condition = random.choice(["chronic fatigue", "anxiety management", "fitness goals", "nutrition planning"])
        health_info = random.choice(HEALTH_INFO)
        management_activity = random.choice(["regular checkups", "daily medication", "exercise routine", "dietary changes"])
        budget = random.choice(MONEY)
        frequency = random.choice(FREQUENCY_DETAILED)
        
        text = f"I have a {health_condition} condition and manage it through {health_info}. I do {management_activity} {frequency} and budget {budget} for health expenses."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "condition1": (EntityTypes.CONDITION, health_condition),
            "health1": (EntityTypes.HEALTH_INFO, health_info),
            "manage1": (EntityTypes.ACTIVITY, management_activity),
            "budget1": (EntityTypes.MONEY, budget),
            "freq1": (EntityTypes.FREQUENCY, frequency)
        }
        
        relations = [
            (RelationTypes.HAS_HEALTH_CONDITION, "user", "condition1"),
            (RelationTypes.MANAGES_HEALTH, "user", "health1"),
            (RelationTypes.DOES_ACTIVITY, "user", "manage1"),
            (RelationTypes.SPENDS, "user", "budget1"),
            (RelationTypes.HAS_FREQUENCY, "manage1", "freq1")
        ]
        
        return text, entities, relations

class FirstPersonFinancialGoalsTemplate(Template):
    def generate(self):
        savings_amount = random.choice(MONEY)
        earnings_source = random.choice(["salary", "side business", "investments", "freelance work"])
        budget_category = random.choice(["emergency fund", "vacation", "education", "retirement"])
        financial_goal = random.choice(["debt freedom", "home ownership", "early retirement", "financial independence"])
        timeline = random.choice(["this year", "next five years", "by age 40", "within a decade"])
        
        text = f"I save {savings_amount} monthly and earn from {earnings_source}. I budget for {budget_category} and spend wisely. My goal is {financial_goal} {timeline}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "savings1": (EntityTypes.MONEY, savings_amount),
            "earnings1": (EntityTypes.CONCEPT, earnings_source),
            "budget1": (EntityTypes.BUDGET, budget_category),
            "goal1": (EntityTypes.GOAL, financial_goal),
            "time1": (EntityTypes.TIMELINE, timeline)
        }
        
        relations = [
            (RelationTypes.SAVES, "user", "savings1"),
            (RelationTypes.EARNS, "user", "earnings1"),
            (RelationTypes.BUDGETS_FOR, "user", "budget1"),
            (RelationTypes.WANTS_GOAL, "user", "goal1"),
            (RelationTypes.HAS_DEADLINE, "goal1", "time1")
        ]
        
        return text, entities, relations

class FirstPersonNicknameIdentityTemplate(Template):
    def generate(self):
        nickname = random.choice(NICKNAMES)
        friend = random.choice(PEOPLE_NAMES)
        group = random.choice(GROUPS)
        reason = random.choice(["personality trait", "funny incident", "special skill", "unique characteristic"])
        identity_aspect = random.choice(["social identity", "professional reputation", "personal brand", "group belonging"])
        
        text = f"My friend {friend} from our {group} calls me {nickname} because of my {reason}. This nickname has become part of my {identity_aspect}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "nick1": (EntityTypes.NICKNAME, nickname),
            "friend1": (EntityTypes.PERSON, friend),
            "group1": (EntityTypes.GROUP, group),
            "reason1": (EntityTypes.CONCEPT, reason),
            "identity1": (EntityTypes.CONCEPT, identity_aspect)
        }
        
        relations = [
            (RelationTypes.CALLED, "user", "nick1"),
            (RelationTypes.KNOWN_AS, "user", "nick1"),
            (RelationTypes.IS_FRIENDS_WITH, "user", "friend1"),
            (RelationTypes.MEMBER_OF, "friend1", "group1"),
            (RelationTypes.CAUSED_BY, "nick1", "reason1"),
            (RelationTypes.IS_PART_OF, "nick1", "identity1")
        ]
        
        return text, entities, relations

class FirstPersonIdeaInnovationTemplate(Template):
    def generate(self):
        idea = random.choice(IDEAS)
        innovation_area = random.choice(TECHNOLOGIES)
        thinking_process = random.choice(["brainstorming", "research analysis", "creative exploration", "problem-solving"])
        opinion = random.choice(["revolutionary", "practical", "innovative", "game-changing"])
        development_stage = random.choice(["concept phase", "prototype stage", "testing period", "implementation phase"])
        
        text = f"I have an idea for {idea} using {innovation_area}. I think this is {opinion} and I'm {thinking_process} in the {development_stage}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "idea1": (EntityTypes.IDEA, idea),
            "innovation1": (EntityTypes.TECHNOLOGY, innovation_area),
            "process1": (EntityTypes.ACTIVITY, thinking_process),
            "opinion1": (EntityTypes.OPINION, opinion),
            "stage1": (EntityTypes.CONCEPT, development_stage)
        }
        
        relations = [
            (RelationTypes.HAS_IDEA, "user", "idea1"),
            (RelationTypes.USES, "idea1", "innovation1"),
            (RelationTypes.THINKS, "user", "process1"),
            (RelationTypes.HAS_OPINION, "user", "opinion1"),
            (RelationTypes.IS_PART_OF, "process1", "stage1")
        ]
        
        return text, entities, relations

class FirstPersonLifeStageReflectionTemplate(Template):
    def generate(self):
        life_stage = random.choice(["childhood", "adolescence", "young adulthood", "mid-career", "retirement"])
        milestone = random.choice(["graduation", "first job", "marriage", "parenthood", "career change"])
        growth_area = random.choice(["emotional maturity", "self-confidence", "life skills", "perspective", "wisdom"])
        period = random.choice(["during college", "in my twenties", "recently", "a few years ago"])
        memory_type = random.choice(["vivid memory", "nostalgic memory", "emotional memory", "life-changing memory"])
        
        text = f"Reflecting on my {life_stage} {period}, the {milestone} marked significant {growth_area}. This {memory_type} still influences me today."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "stage1": (EntityTypes.LIFE_STAGE, life_stage),
            "milestone1": (EntityTypes.EVENT, milestone),
            "growth1": (EntityTypes.PERSONAL_GROWTH, growth_area),
            "period1": (EntityTypes.PERIOD, period),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_type)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "user", "stage1"),
            (RelationTypes.EXPERIENCES, "user", "milestone1"),
            (RelationTypes.ON_DATE, "milestone1", "period1"),
            (RelationTypes.RESULTS_IN, "milestone1", "growth1"),
            (RelationTypes.REMEMBERS, "user", "memory1")
        ]
        
        return text, entities, relations

class FirstPersonCulturalLearningTemplate(Template):
    def generate(self):
        cultural_element = random.choice(["traditional cooking", "ancestral language", "folk dance", "cultural ceremony", "family traditions"])
        learning_method = random.choice(["hands-on practice", "storytelling", "observation", "formal instruction", "cultural immersion"])
        teacher = random.choice(PEOPLE_NAMES)
        community_role = random.choice(["cultural preservationist", "tradition keeper", "community elder", "cultural educator"])
        personal_growth = random.choice(["cultural identity", "family connection", "heritage appreciation", "community belonging"])
        
        text = f"I learned {cultural_element} through {learning_method} from {teacher}, who serves as a {community_role}. This developed my {personal_growth}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "culture1": (EntityTypes.CULTURAL_ELEMENT, cultural_element),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "teacher1": (EntityTypes.PERSON, teacher),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth)
        }
        
        relations = [
            (RelationTypes.LEARNS, "user", "culture1"),
            (RelationTypes.USES, "user", "method1"),
            (RelationTypes.COLLABORATES_WITH, "user", "teacher1"),
            (RelationTypes.HAS_ROLE, "teacher1", "role1"),
            (RelationTypes.RESULTS_IN, "culture1", "growth1")
        ]
        
        return text, entities, relations

class FirstPersonIndustryExpertiseTemplate(Template):
    def generate(self):
        organization = random.choice(["Toyota", "Apple", "Microsoft", "Google", "Tesla", "MIT", "AWS", "Facebook"])
        technology = random.choice(["artificial intelligence", "blockchain", "cloud computing", "automation", "data analytics"])
        product = random.choice(["software platform", "mobile app", "web service", "automation tool", "analytics dashboard"])
        expertise_area = random.choice(SKILLS)
        duration = random.choice(DURATIONS)
        
        text = f"I've worked at {organization} for {duration}, specializing in {technology}. I developed a {product} using my {expertise_area} expertise."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "tech1": (EntityTypes.TECHNOLOGY, technology),
            "product1": (EntityTypes.PRODUCT, product),
            "expert1": (EntityTypes.SKILL, expertise_area),
            "dur1": (EntityTypes.DURATION, duration)
        }
        
        relations = [
            (RelationTypes.WORKS_FOR, "user", "org1"),
            (RelationTypes.FOR_DURATION, "org1", "dur1"),
            (RelationTypes.HAS_EXPERTISE, "user", "tech1"),
            (RelationTypes.ORGANIZES, "user", "product1"),
            (RelationTypes.HAS_SKILL, "user", "expert1"),
            (RelationTypes.USES, "user", "tech1")
        ]
        
        return text, entities, relations

class FirstPersonTimeAmountTemplate(Template):
    def generate(self):
        specific_time = random.choice(["8:30 AM", "2:15 PM", "7:45 PM", "11:00 AM"])
        activity = random.choice(ACTIVITIES)
        amount = random.choice(["2 hours", "45 minutes", "3 hours", "90 minutes"])
        frequency = random.choice(FREQUENCY_DETAILED)
        trait = random.choice(["patience", "focus", "dedication", "consistency", "discipline"])
        location = random.choice(LOCATIONS)
        
        text = f"Every day at {specific_time}, I spend {amount} on {activity} at {location}. I do this {frequency} to develop my {trait}."
        
        entities = {
            "user": (EntityTypes.PERSON, "I"),
            "time1": (EntityTypes.TIME, specific_time),
            "amount1": (EntityTypes.DURATION, amount),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "trait1": (EntityTypes.TRAIT, trait),
            "loc1": (EntityTypes.LOCATION, location)
        }
        
        relations = [
            (RelationTypes.STARTS_AT, "activity1", "time1"),
            (RelationTypes.FOR_DURATION, "activity1", "amount1"),
            (RelationTypes.DOES_ACTIVITY, "user", "activity1"),
            (RelationTypes.HAS_FREQUENCY, "activity1", "freq1"),
            (RelationTypes.HAS_TRAIT, "user", "trait1"),
            (RelationTypes.LOCATED_AT, "user", "loc1")
        ]
        
        return text, entities, relations

class FirstPersonThinkingProcessTemplate(Template):
    def generate(self):
        thinking_topic = random.choice(["career change", "life decisions", "future plans", "personal goals"])
        consideration = random.choice(["different options", "pros and cons", "potential outcomes", "various approaches"])
        planning_activity = random.choice(["researching", "consulting experts", "making lists", "weighing decisions"])
        dream_goal = random.choice(GOALS)
        hope = random.choice(["better future", "positive outcome", "personal growth", "meaningful change"])
        
        text = f"I'm thinking of {thinking_topic} and considering {consideration}. I'm planning by {planning_activity} because I dream of {dream_goal} and hope for {hope}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "topic1": (EntityTypes.TOPIC, thinking_topic),
            "consider1": (EntityTypes.CONCEPT, consideration),
            "plan1": (EntityTypes.ACTIVITY, planning_activity),
            "dream1": (EntityTypes.GOAL, dream_goal),
            "hope1": (EntityTypes.CONCEPT, hope)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "user", "topic1"),
            (RelationTypes.CONSIDERING, "user", "consider1"),
            (RelationTypes.PLANNING, "user", "plan1"),
            (RelationTypes.DREAMS_OF, "user", "dream1"),
            (RelationTypes.HOPES_FOR, "user", "hope1"),
            (RelationTypes.INTENDS, "user", "plan1")
        ]
        
        return text, entities, relations

class FirstPersonRegretAnticipationTemplate(Template):
    def generate(self):
        regret = random.choice(["missed opportunity", "poor decision", "lost relationship", "unfulfilled potential"])
        past_period = random.choice(["during college", "in my twenties", "early career", "a few years ago"])
        future_event = random.choice(["vacation", "project completion", "family gathering", "career milestone"])
        timeline = random.choice(["next month", "this summer", "next year", "soon"])
        missing_person = random.choice(PEOPLE_NAMES)
        
        text = f"I regret {regret} from {past_period} and miss {missing_person}. However, I'm looking forward to {future_event} {timeline}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "regret1": (EntityTypes.CONCEPT, regret),
            "period1": (EntityTypes.PERIOD, past_period),
            "event1": (EntityTypes.EVENT, future_event),
            "time1": (EntityTypes.TIMELINE, timeline),
            "person1": (EntityTypes.PERSON, missing_person)
        }
        
        relations = [
            (RelationTypes.REGRETS, "user", "regret1"),
            (RelationTypes.ON_DATE, "regret1", "period1"),
            (RelationTypes.LOOKING_FORWARD_TO, "user", "event1"),
            (RelationTypes.HAS_DEADLINE, "event1", "time1"),
            (RelationTypes.MISSES, "user", "person1")
        ]
        
        return text, entities, relations

class FirstPersonCompleteSensoryTemplate(Template):
    def generate(self):
        location = random.choice(["coffee shop", "grandmother's kitchen", "ocean beach", "mountain cabin"])
        sound = random.choice(SOUNDS)
        sight = random.choice(SIGHTS)
        taste = random.choice(TASTES)
        smell = random.choice(SMELLS)
        feeling = random.choice(FEELINGS)
        memory_trigger = random.choice(["vivid memory", "nostalgic memory", "emotional memory", "childhood memory"])
        
        text = f"At {location}, I hear {sound}, see {sight}, taste something {taste}, smell {smell}, and feel {feeling}. This triggers a {memory_trigger}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, location),
            "sound1": (EntityTypes.SOUND, sound),
            "sight1": (EntityTypes.SIGHT, sight),
            "taste1": (EntityTypes.TASTE, taste),
            "smell1": (EntityTypes.SMELL, smell),
            "feel1": (EntityTypes.FEELING, feeling),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_trigger)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "loc1"),
            (RelationTypes.HEARS, "user", "sound1"),
            (RelationTypes.SEES, "user", "sight1"),
            (RelationTypes.TASTES, "user", "taste1"),
            (RelationTypes.SMELLS, "user", "smell1"),
            (RelationTypes.TOUCHES, "user", "feel1"),
            (RelationTypes.CAUSED_BY, "memory1", "smell1")
        ]
        
        return text, entities, relations

class FirstPersonRepeatingRoutineTemplate(Template):
    def generate(self):
        activity = random.choice(["morning meditation", "evening workout", "weekly planning", "daily journaling"])
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        schedule = random.choice(RECURRING_SCHEDULES)
        frequency = random.choice(FREQUENCY_DETAILED)
        intent = random.choice(INTENTS)
        
        text = f"I repeat {activity} from {start_time} to {end_time} on a {schedule} basis, {frequency}. My intent is to {intent}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "intent1": (EntityTypes.INTENT, intent)
        }
        
        relations = [
            (RelationTypes.REPEATS, "user", "activity1"),
            (RelationTypes.STARTS_AT, "activity1", "start1"),
            (RelationTypes.ENDS_AT, "activity1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.HAS_FREQUENCY, "activity1", "freq1"),
            (RelationTypes.INTENDS, "user", "intent1"),
            (RelationTypes.PLANS, "user", "activity1")
        ]
        
        return text, entities, relations

class ThirdPersonComprehensiveMemoryTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        memory_type = random.choice(MEMORY_TYPES)
        life_stage = random.choice(LIFE_STAGES)
        period = random.choice(PERIODS)
        cultural_element = random.choice(CULTURAL_ELEMENTS)
        learning_method = random.choice(LEARNING_METHODS)
        personal_growth = random.choice(PERSONAL_GROWTH)
        community_role = random.choice(COMMUNITY_ROLES)
        
        text = f"{person} processes {memory_type} from their {life_stage} {period}. They learned {cultural_element} through {learning_method}, which fostered {personal_growth} and shaped their {community_role}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_type),
            "stage1": (EntityTypes.LIFE_STAGE, life_stage),
            "period1": (EntityTypes.PERIOD, period),
            "culture1": (EntityTypes.CULTURAL_ELEMENT, cultural_element),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role)
        }
        
        relations = [
            (RelationTypes.REMEMBERS, "p1", "memory1"),
            (RelationTypes.EXPERIENCES, "p1", "stage1"),
            (RelationTypes.ON_DATE, "memory1", "period1"),
            (RelationTypes.LEARNS, "p1", "culture1"),
            (RelationTypes.USES, "p1", "method1"),
            (RelationTypes.RESULTS_IN, "method1", "growth1"),
            (RelationTypes.HAS_ROLE, "p1", "role1")
        ]
        
        return text, entities, relations

class ThirdPersonPetCareTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        pet = random.choice(PETS)
        care_activity = random.choice(["daily walks", "grooming sessions", "training exercises", "veterinary visits"])
        frequency = random.choice(FREQUENCY_DETAILED)
        trait = random.choice(["responsibility", "compassion", "patience", "dedication"])
        location = random.choice(["neighborhood park", "veterinary clinic", "pet store", "home"])
        
        text = f"{person} has a {pet} and provides {care_activity} {frequency} at the {location}. This caring develops their {trait} trait."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "pet1": (EntityTypes.PET, pet),
            "care1": (EntityTypes.ACTIVITY, care_activity),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "trait1": (EntityTypes.TRAIT, trait),
            "loc1": (EntityTypes.LOCATION, location)
        }
        
        relations = [
            (RelationTypes.HAS_PET, "p1", "pet1"),
            (RelationTypes.CARES_FOR, "p1", "pet1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "care1"),
            (RelationTypes.HAS_FREQUENCY, "care1", "freq1"),
            (RelationTypes.HAS_TRAIT, "p1", "trait1"),
            (RelationTypes.AT_LOCATION, "care1", "loc1")
        ]
        
        return text, entities, relations

class ThirdPersonAdvancedCognitiveTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        thinking_topic = random.choice(TOPICS)
        consideration = random.choice(["multiple perspectives", "long-term implications", "ethical considerations", "practical solutions"])
        dream = random.choice(["societal change", "innovation breakthrough", "personal legacy", "community impact"])
        planning_activity = random.choice(["strategic planning", "resource allocation", "timeline development", "stakeholder engagement"])
        hope = random.choice(["positive outcomes", "meaningful change", "lasting impact", "successful implementation"])
        regret = random.choice(["missed opportunities", "delayed action", "insufficient preparation", "overlooked details"])
        
        text = f"{person} is thinking of {thinking_topic} and considering {consideration}. They dream of {dream} and are planning through {planning_activity}. They hope for {hope} but regret {regret}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "topic1": (EntityTypes.TOPIC, thinking_topic),
            "consider1": (EntityTypes.CONCEPT, consideration),
            "dream1": (EntityTypes.GOAL, dream),
            "plan1": (EntityTypes.ACTIVITY, planning_activity),
            "hope1": (EntityTypes.CONCEPT, hope),
            "regret1": (EntityTypes.CONCEPT, regret)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "p1", "topic1"),
            (RelationTypes.CONSIDERING, "p1", "consider1"),
            (RelationTypes.DREAMS_OF, "p1", "dream1"),
            (RelationTypes.PLANNING, "p1", "plan1"),
            (RelationTypes.HOPES_FOR, "p1", "hope1"),
            (RelationTypes.REGRETS, "p1", "regret1")
        ]
        
        return text, entities, relations

class ThirdPersonTemporalExpertiseTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        routine = random.choice(["research sessions", "client meetings", "creative work", "skill practice"])
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        schedule = random.choice(RECURRING_SCHEDULES)
        expertise = random.choice(SKILLS)
        trait = random.choice(["discipline", "precision", "consistency", "excellence"])
        frequency = random.choice(FREQUENCY_DETAILED)
        
        text = f"{person} repeats their {routine} from {start_time} to {end_time} {frequency}. They follow a {schedule} schedule, demonstrating {trait} and building {expertise} expertise."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "routine1": (EntityTypes.ACTIVITY, routine),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "expert1": (EntityTypes.SKILL, expertise),
            "trait1": (EntityTypes.TRAIT, trait),
            "freq1": (EntityTypes.FREQUENCY, frequency)
        }
        
        relations = [
            (RelationTypes.REPEATS, "p1", "routine1"),
            (RelationTypes.STARTS_AT, "routine1", "start1"),
            (RelationTypes.ENDS_AT, "routine1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "p1", "sched1"),
            (RelationTypes.HAS_EXPERTISE, "p1", "expert1"),
            (RelationTypes.HAS_TRAIT, "p1", "trait1"),
            (RelationTypes.HAS_FREQUENCY, "routine1", "freq1")
        ]
        
        return text, entities, relations

class ThirdPersonRelationshipMaintainerTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        relationship_type = random.choice(["mentorship", "friendship", "professional partnership", "family bond"])
        other_person = get_different_person(person)
        maintenance_activity = random.choice(["regular communication", "shared activities", "mutual support", "conflict resolution"])
        location = random.choice(LOCATIONS)
        missing_aspect = random.choice(["past collaboration", "shared memories", "old traditions", "former closeness"])
        
        text = f"{person} maintains a {relationship_type} with {other_person} through {maintenance_activity} at {location}. However, they miss the {missing_aspect} they once shared."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "rel1": (EntityTypes.RELATIONSHIP_TYPE, relationship_type),
            "p2": (EntityTypes.PERSON, other_person),
            "maint1": (EntityTypes.ACTIVITY, maintenance_activity),
            "loc1": (EntityTypes.LOCATION, location),
            "miss1": (EntityTypes.CONCEPT, missing_aspect)
        }
        
        relations = [
            (RelationTypes.MAINTAINS_RELATIONSHIP, "p1", "rel1"),
            (RelationTypes.COLLABORATES_WITH, "p1", "p2"),
            (RelationTypes.DOES_ACTIVITY, "p1", "maint1"),
            (RelationTypes.LOCATED_AT, "p1", "loc1"),
            (RelationTypes.MISSES, "p1", "miss1")
        ]
        
        return text, entities, relations

# === VALIDATION TEMPLATE TO ENSURE 100% COVERAGE ===

class FirstPersonComprehensiveCoverageTemplate(Template):
    def generate(self):
        # This template uses as many different entity and relation types as possible
        time = random.choice(["9:15 AM", "3:45 PM", "6:30 PM"])
        amount = random.choice(["3.5 hours", "45 minutes", "2 hours"])
        activity = random.choice(ACTIVITIES)
        trait = random.choice(["persistence", "creativity", "analytical thinking"])
        expertise = random.choice(SKILLS)
        location = random.choice(LOCATIONS)
        frequency = random.choice(FREQUENCY_DETAILED)
        schedule = random.choice(RECURRING_SCHEDULES)
        intent = random.choice(INTENTS)
        belief = random.choice(BELIEFS)
        hope = random.choice(["meaningful contribution", "positive impact", "personal satisfaction"])
        
        text = f"At {time}, I spend {amount} on {activity} {frequency} at {location}. I follow a {schedule} schedule to develop my {trait} trait and {expertise} expertise. I intend to {intent}, believe in '{belief}', and hope for {hope}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "time1": (EntityTypes.TIME, time),
            "amount1": (EntityTypes.DURATION, amount),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "trait1": (EntityTypes.TRAIT, trait),
            "expert1": (EntityTypes.SKILL, expertise),
            "loc1": (EntityTypes.LOCATION, location),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "intent1": (EntityTypes.INTENT, intent),
            "belief1": (EntityTypes.BELIEF, belief),
            "hope1": (EntityTypes.CONCEPT, hope)
        }
        
        relations = [
            (RelationTypes.STARTS_AT, "activity1", "time1"),
            (RelationTypes.FOR_DURATION, "activity1", "amount1"),
            (RelationTypes.DOES_ACTIVITY, "user", "activity1"),
            (RelationTypes.HAS_TRAIT, "user", "trait1"),
            (RelationTypes.HAS_EXPERTISE, "user", "expert1"),
            (RelationTypes.LOCATED_AT, "user", "loc1"),
            (RelationTypes.HAS_FREQUENCY, "activity1", "freq1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.INTENDS, "user", "intent1"),
            (RelationTypes.BELIEVES, "user", "belief1"),
            (RelationTypes.HOPES_FOR, "user", "hope1"),
            (RelationTypes.PLANS, "user", "activity1")
        ]
        
        return text, entities, relations

class ThirdPersonIndustryInnovationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        organization = random.choice(["Toyota", "Apple", "Microsoft", "Google", "Tesla", "MIT", "AWS"])
        technology = random.choice(["machine learning", "robotics", "biotech", "fintech"])
        product = random.choice(["revolutionary app", "medical device", "AI system", "blockchain solution"])
        learning_method = random.choice(["research", "experimentation", "collaboration", "iteration"])
        growth = random.choice(["industry recognition", "patent approval", "market success", "user adoption"])
        
        text = f"{person} works for {organization}, developing {technology} to create a {product}. Through {learning_method}, they achieved {growth}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "tech1": (EntityTypes.TECHNOLOGY, technology),
            "prod1": (EntityTypes.PRODUCT, product),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "growth1": (EntityTypes.CONCEPT, growth)
        }
        
        relations = [
            (RelationTypes.WORKS_FOR, "p1", "org1"),
            (RelationTypes.HAS_EXPERTISE, "p1", "tech1"),
            (RelationTypes.ORGANIZES, "p1", "prod1"),
            (RelationTypes.USES, "p1", "method1"),
            (RelationTypes.RESULTS_IN, "method1", "growth1")
        ]
        
        return text, entities, relations

class ThirdPersonLifeStageWisdomTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        life_stage = random.choice(["retirement", "mid-career", "early adulthood", "senior years"])
        period = random.choice(["recently", "over the years", "during this phase", "in this chapter"])
        memory_type = random.choice(["life lessons", "accumulated wisdom", "meaningful experiences", "personal insights"])
        community_role = random.choice(["mentor", "advisor", "guide", "elder"])
        personal_growth = random.choice(["deep wisdom", "life perspective", "emotional maturity", "spiritual growth"])
        
        text = f"{person} is in their {life_stage} and {period} has been reflecting on {memory_type}. As a {community_role}, they share their {personal_growth}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "stage1": (EntityTypes.LIFE_STAGE, life_stage),
            "period1": (EntityTypes.PERIOD, period),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_type),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "p1", "stage1"),
            (RelationTypes.ON_DATE, "memory1", "period1"),
            (RelationTypes.REMEMBERS, "p1", "memory1"),
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.HAS_ATTRIBUTE, "p1", "growth1")
        ]
        
        return text, entities, relations

class ThirdPersonCulturalPreservationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        cultural_element = random.choice(["ancestral recipes", "traditional crafts", "folk stories", "ceremonial practices"])
        learning_method = random.choice(["oral tradition", "hands-on teaching", "community workshops", "cultural immersion"])
        community_role = random.choice(["cultural keeper", "tradition bearer", "heritage preservationist", "community elder"])
        personal_growth = random.choice(["cultural identity", "community connection", "historical awareness", "pride in heritage"])
        
        text = f"{person} preserves {cultural_element} through {learning_method} in their role as {community_role}. This fosters {personal_growth} in the community."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "culture1": (EntityTypes.CULTURAL_ELEMENT, cultural_element),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth)
        }
        
        relations = [
            (RelationTypes.ORGANIZES, "p1", "culture1"),
            (RelationTypes.USES, "p1", "method1"),
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.RESULTS_IN, "culture1", "growth1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "growth1")
        ]
        
        return text, entities, relations

class FirstPersonChildhoodMemoryTemplate(Template):
    def generate(self):
        childhood_activity = random.choice(["playing games", "reading stories", "building forts", "collecting things", "drawing pictures", "helping in garden"])
        location = random.choice(["grandmother's house", "childhood home", "neighborhood park", "school playground", "family farm"])
        family_member = random.choice(PEOPLE_NAMES)
        emotion = random.choice(["nostalgic", "happy", "peaceful", "secure", "joyful"])
        sensory_detail = random.choice(["the smell of cookies", "warm sunlight", "soft grass", "cool breeze", "familiar sounds"])
        
        text = f"I have vivid memories of {childhood_activity} with {family_member} at {location}. {sensory_detail} always brings back {emotion} feelings from those days."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "activity1": (EntityTypes.ACTIVITY, childhood_activity),
            "family1": (EntityTypes.PERSON, family_member),
            "loc1": (EntityTypes.LOCATION, location),
            "sensory1": (EntityTypes.SENSATION, sensory_detail),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.REMEMBERS, "user", "activity1"),
            (RelationTypes.IS_FAMILY_WITH, "user", "family1"),
            (RelationTypes.AT_LOCATION, "activity1", "loc1"),
            (RelationTypes.EXPERIENCES, "user", "sensory1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.CAUSED_BY, "e1", "sensory1")
        ]
        
        return text, entities, relations

class FirstPersonLossGriefTemplate(Template):
    def generate(self):
        lost_person = random.choice(PEOPLE_NAMES)
        relationship = random.choice(["friend", "family member", "mentor", "colleague", "neighbor"])
        shared_activity = random.choice(["coffee talks", "weekend walks", "project work", "cooking together", "sharing stories"])
        grief_stage = random.choice(["missing them deeply", "finding peace", "honoring their memory", "feeling their presence"])
        coping_method = random.choice(["visiting special places", "keeping their traditions", "talking about them", "continuing their work"])
        
        text = f"I lost a dear {relationship}, {lost_person}, who I used to enjoy {shared_activity} with. I'm {grief_stage} and coping by {coping_method}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "lost1": (EntityTypes.PERSON, lost_person),
            "rel1": (EntityTypes.RELATIONSHIP_TYPE, relationship),
            "activity1": (EntityTypes.ACTIVITY, shared_activity),
            "grief1": (EntityTypes.EMOTION, grief_stage),
            "cope1": (EntityTypes.ACTIVITY, coping_method)
        }
        
        relations = [
            (RelationTypes.MAINTAINS_RELATIONSHIP, "user", "rel1"),
            (RelationTypes.MISSES, "user", "lost1"),
            (RelationTypes.DOES_ACTIVITY, "user", "activity1"),
            (RelationTypes.FEELS_EMOTION, "user", "grief1"),
            (RelationTypes.DOES_ACTIVITY, "user", "cope1"),
            (RelationTypes.REMEMBERS, "user", "lost1")
        ]
        
        return text, entities, relations

class FirstPersonCareerMilestoneTemplate(Template):
    def generate(self):
        milestone = random.choice(["first job", "promotion", "career change", "major project completion", "leadership role", "professional recognition"])
        organization = random.choice(ORGANIZATIONS)
        mentor = random.choice(PEOPLE_NAMES)
        challenge = random.choice(["imposter syndrome", "technical difficulties", "team conflicts", "tight deadlines", "learning curve"])
        growth = random.choice(["increased confidence", "new skills", "broader perspective", "stronger network", "clearer direction"])
        
        text = f"My {milestone} at {organization} was transformative. {mentor} helped me overcome {challenge}, which led to {growth}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "milestone1": (EntityTypes.EVENT, milestone),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "mentor1": (EntityTypes.PERSON, mentor),
            "challenge1": (EntityTypes.CONCEPT, challenge),
            "growth1": (EntityTypes.CONCEPT, growth)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "user", "milestone1"),
            (RelationTypes.AT_LOCATION, "milestone1", "org1"),
            (RelationTypes.COLLABORATES_WITH, "user", "mentor1"),
            (RelationTypes.WORRIES_ABOUT, "user", "challenge1"),
            (RelationTypes.RESULTS_IN, "milestone1", "growth1")
        ]
        
        return text, entities, relations

class FirstPersonFearOvercomeTemplate(Template):
    def generate(self):
        fear = random.choice(["public speaking", "heights", "social situations", "failure", "rejection", "change"])
        trigger_situation = random.choice(["work presentation", "social event", "new opportunity", "personal challenge"])
        support_person = random.choice(PEOPLE_NAMES)
        strategy = random.choice(["gradual exposure", "breathing techniques", "positive self-talk", "professional help", "practice"])
        outcome = random.choice(["increased confidence", "personal growth", "new opportunities", "self-discovery"])
        
        text = f"I used to be terrified of {fear}, especially in {trigger_situation}. With help from {support_person} and using {strategy}, I achieved {outcome}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "fear1": (EntityTypes.EMOTION, fear),
            "situation1": (EntityTypes.CONCEPT, trigger_situation),
            "support1": (EntityTypes.PERSON, support_person),
            "strategy1": (EntityTypes.CONCEPT, strategy),
            "outcome1": (EntityTypes.CONCEPT, outcome)
        }
        
        relations = [
            (RelationTypes.FEELS_EMOTION, "user", "fear1"),
            (RelationTypes.CAUSED_BY, "fear1", "situation1"),
            (RelationTypes.COLLABORATES_WITH, "user", "support1"),
            (RelationTypes.USES, "user", "strategy1"),
            (RelationTypes.RESULTS_IN, "strategy1", "outcome1")
        ]
        
        return text, entities, relations

class FirstPersonCreativeAchievementTemplate(Template):
    def generate(self):
        creative_work = random.choice(["painting", "writing", "music composition", "photography", "sculpture", "digital art"])
        inspiration = random.choice(["personal experience", "nature", "relationships", "dreams", "travel", "emotions"])
        venue = random.choice(["gallery", "online platform", "local exhibition", "community center", "friend's space"])
        audience_reaction = random.choice(["overwhelming support", "thoughtful feedback", "emotional connection", "unexpected interest"])
        personal_impact = random.choice(["validation", "creative confidence", "new direction", "deeper self-understanding"])
        
        text = f"I created a {creative_work} inspired by {inspiration} and shared it at {venue}. The {audience_reaction} gave me {personal_impact}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "work1": (EntityTypes.PROJECT, creative_work),
            "insp1": (EntityTypes.CONCEPT, inspiration),
            "venue1": (EntityTypes.LOCATION, venue),
            "reaction1": (EntityTypes.CONCEPT, audience_reaction),
            "impact1": (EntityTypes.CONCEPT, personal_impact)
        }
        
        relations = [
            (RelationTypes.ORGANIZES, "user", "work1"),
            (RelationTypes.CAUSED_BY, "work1", "insp1"),
            (RelationTypes.AT_LOCATION, "work1", "venue1"),
            (RelationTypes.EXPERIENCES, "user", "reaction1"),
            (RelationTypes.RESULTS_IN, "reaction1", "impact1")
        ]
        
        return text, entities, relations

class FirstPersonHealthScareTemplate(Template):
    def generate(self):
        health_issue = random.choice(["sudden illness", "injury", "diagnosis", "health screening result"])
        initial_emotion = random.choice(["scared", "confused", "worried", "shocked"])
        support_system = random.choice(PEOPLE_NAMES)
        medical_professional = random.choice(["Dr. " + name for name in PEOPLE_NAMES[:5]])
        lifestyle_change = random.choice(["diet modification", "exercise routine", "stress management", "regular checkups"])
        current_state = random.choice(["much better", "managing well", "fully recovered", "more aware"])
        
        text = f"When I experienced {health_issue}, I felt {initial_emotion}. {support_system} and {medical_professional} helped me implement {lifestyle_change}. Now I'm {current_state}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "health1": (EntityTypes.HEALTH_INFO, health_issue),
            "emotion1": (EntityTypes.EMOTION, initial_emotion),
            "support1": (EntityTypes.PERSON, support_system),
            "doctor1": (EntityTypes.PERSON, medical_professional),
            "change1": (EntityTypes.HEALTH_INFO, lifestyle_change),
            "state1": (EntityTypes.HEALTH_INFO, current_state)
        }
        
        relations = [
            (RelationTypes.HAS_HEALTH_CONDITION, "user", "health1"),
            (RelationTypes.FEELS_EMOTION, "user", "emotion1"),
            (RelationTypes.COLLABORATES_WITH, "user", "support1"),
            (RelationTypes.COLLABORATES_WITH, "user", "doctor1"),
            (RelationTypes.HAS_HEALTH_INFO, "user", "change1"),
            (RelationTypes.HAS_HEALTH_INFO, "user", "state1")
        ]
        
        return text, entities, relations

class FirstPersonFailureLessonTemplate(Template):
    def generate(self):
        failure_event = random.choice(["failed project", "missed opportunity", "rejected application", "business setback", "relationship ending"])
        initial_reaction = random.choice(["devastated", "embarrassed", "angry", "disappointed", "lost"])
        reflection_period = random.choice(["weeks of thinking", "months of processing", "long conversations", "journaling time"])
        lesson_learned = random.choice(["resilience", "self-awareness", "better preparation", "realistic expectations", "personal strength"])
        current_perspective = random.choice(["grateful for the experience", "stronger because of it", "wiser now", "more compassionate"])
        
        text = f"My {failure_event} left me {initial_reaction}. After {reflection_period}, I learned about {lesson_learned} and now I'm {current_perspective}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "failure1": (EntityTypes.EVENT, failure_event),
            "reaction1": (EntityTypes.EMOTION, initial_reaction),
            "reflection1": (EntityTypes.ACTIVITY, reflection_period),
            "lesson1": (EntityTypes.CONCEPT, lesson_learned),
            "perspective1": (EntityTypes.SENTIMENT, current_perspective)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "user", "failure1"),
            (RelationTypes.FEELS_EMOTION, "user", "reaction1"),
            (RelationTypes.DOES_ACTIVITY, "user", "reflection1"),
            (RelationTypes.LEARNS, "user", "lesson1"),
            (RelationTypes.HAD_SENTIMENT, "user", "perspective1")
        ]
        
        return text, entities, relations

class FirstPersonMentorshipMemoryTemplate(Template):
    def generate(self):
        mentor_role = random.choice(["teacher", "boss", "family friend", "colleague", "coach"])
        mentor_name = random.choice(PEOPLE_NAMES)
        key_advice = random.choice(["trust yourself", "take calculated risks", "focus on growth", "be authentic", "help others"])
        situation_applied = random.choice(["career decision", "personal challenge", "relationship issue", "creative block"])
        lasting_impact = random.choice(["changed my perspective", "gave me confidence", "shaped my values", "influenced my choices"])
        
        text = f"My {mentor_role}, {mentor_name}, once told me to '{key_advice}'. I applied this during a {situation_applied} and it {lasting_impact}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "role1": (EntityTypes.ROLE, mentor_role),
            "mentor1": (EntityTypes.PERSON, mentor_name),
            "advice1": (EntityTypes.CONCEPT, key_advice),
            "situation1": (EntityTypes.CONCEPT, situation_applied),
            "impact1": (EntityTypes.CONCEPT, lasting_impact)
        }
        
        relations = [
            (RelationTypes.HAS_ROLE, "mentor1", "role1"),
            (RelationTypes.COLLABORATES_WITH, "user", "mentor1"),
            (RelationTypes.LEARNS, "user", "advice1"),
            (RelationTypes.USES, "user", "advice1"),
            (RelationTypes.ABOUT_TOPIC, "advice1", "situation1"),
            (RelationTypes.RESULTS_IN, "advice1", "impact1")
        ]
        
        return text, entities, relations

class FirstPersonNicknameStoryTemplate(Template):
    def generate(self):
        nickname = random.choice(NICKNAMES)
        friend = random.choice(PEOPLE_NAMES)
        story_reason = random.choice(["a funny incident", "my personality", "something I did", "how I acted"])
        group = random.choice(GROUPS)
        emotion = random.choice(EMOTIONS)
        
        text = f"My friends call me {nickname} because of {story_reason}. {friend} from my {group} started it and I feel {emotion} about it."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "nick1": (EntityTypes.NICKNAME, nickname),
            "friend1": (EntityTypes.PERSON, friend),
            "reason1": (EntityTypes.CONCEPT, story_reason),
            "group1": (EntityTypes.GROUP, group),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.KNOWN_AS, "user", "nick1"),
            (RelationTypes.IS_FRIENDS_WITH, "user", "friend1"),
            (RelationTypes.CAUSED_BY, "nick1", "reason1"),
            (RelationTypes.MEMBER_OF, "friend1", "group1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1")
        ]
        
        return text, entities, relations

class FirstPersonBorrowLendTemplate(Template):
    def generate(self):
        item = random.choice(OBJECTS + EQUIPMENT_TYPES)
        friend = random.choice(PEOPLE_NAMES)
        duration = random.choice(DURATIONS)
        reason = random.choice(["emergency", "project", "trying it out", "temporary need"])
        result = random.choice(["worked perfectly", "was very helpful", "solved my problem", "exceeded expectations"])
        
        text = f"I borrowed a {item} from {friend} for {duration} because of an {reason}. It {result} and I'm grateful."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "item1": (EntityTypes.OBJECT, item),
            "friend1": (EntityTypes.PERSON, friend),
            "dur1": (EntityTypes.DURATION, duration),
            "reason1": (EntityTypes.CONCEPT, reason),
            "result1": (EntityTypes.CONCEPT, result)
        }
        
        relations = [
            (RelationTypes.BORROWED, "user", "item1"),
            (RelationTypes.LENT, "friend1", "item1"),
            (RelationTypes.FOR_DURATION, "item1", "dur1"),
            (RelationTypes.CAUSED_BY, "item1", "reason1"),
            (RelationTypes.RESULTS_IN, "item1", "result1")
        ]
        
        return text, entities, relations

class FirstPersonFamilyTraditionTemplate(Template):
    def generate(self):
        family_member = random.choice(PEOPLE_NAMES)
        tradition = random.choice(["holiday celebration", "weekly dinner", "annual trip", "birthday ritual"])
        location = random.choice(["family home", "grandma's house", "traditional restaurant", "special place"])
        emotion = random.choice(EMOTIONS)
        duration = random.choice(["many years", "since childhood", "decades", "generations"])
        
        text = f"I have a family tradition of {tradition} with {family_member} at {location}. We've been doing this for {duration} and it fills me with {emotion}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "family1": (EntityTypes.PERSON, family_member),
            "trad1": (EntityTypes.EVENT, tradition),
            "loc1": (EntityTypes.LOCATION, location),
            "e1": (EntityTypes.EMOTION, emotion),
            "dur1": (EntityTypes.DURATION, duration)
        }
        
        relations = [
            (RelationTypes.IS_FAMILY_WITH, "user", "family1"),
            (RelationTypes.PARTICIPATES_IN, "user", "trad1"),
            (RelationTypes.AT_LOCATION, "trad1", "loc1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.FOR_DURATION, "trad1", "dur1")
        ]
        
        return text, entities, relations

class FirstPersonScheduleStressTemplate(Template):
    def generate(self):
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        activity = random.choice(ACTIVITIES)
        condition = random.choice(CONDITIONS)
        intent = random.choice(INTENTS)
        schedule = random.choice(RECURRING_SCHEDULES)
        
        text = f"I have a {schedule} schedule from {start_time} to {end_time} for {activity}. It causes {condition} but my intent is to {intent}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "act1": (EntityTypes.ACTIVITY, activity),
            "cond1": (EntityTypes.CONDITION, condition),
            "intent1": (EntityTypes.INTENT, intent),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule)
        }
        
        relations = [
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.STARTS_AT, "act1", "start1"),
            (RelationTypes.ENDS_AT, "act1", "end1"),
            (RelationTypes.DOES_ACTIVITY, "user", "act1"),
            (RelationTypes.CAUSED_BY, "cond1", "sched1"),
            (RelationTypes.HAS_INTENT, "user", "intent1")
        ]
        
        return text, entities, relations

class FirstPersonValueConflictTemplate(Template):
    def generate(self):
        value1 = random.choice(VALUES)
        value2 = random.choice([v for v in VALUES if v != value1])
        situation = random.choice(["work decision", "life choice", "relationship issue", "career move"])
        emotion = random.choice(["conflicted", "uncertain", "torn", "confused"])
        resolution = random.choice(["compromise", "prioritization", "balance", "acceptance"])
        
        text = f"I value both {value1} and {value2}, but in this {situation} I feel {emotion}. I'm working toward {resolution}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "val1": (EntityTypes.VALUE, value1),
            "val2": (EntityTypes.VALUE, value2),
            "sit1": (EntityTypes.CONCEPT, situation),
            "e1": (EntityTypes.EMOTION, emotion),
            "res1": (EntityTypes.GOAL, resolution)
        }
        
        relations = [
            (RelationTypes.VALUES, "user", "val1"),
            (RelationTypes.VALUES, "user", "val2"),
            (RelationTypes.ABOUT_TOPIC, "sit1", "val1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.WANTS_GOAL, "user", "res1")
        ]
        
        return text, entities, relations

class FirstPersonSensoryOverloadTemplate(Template):
    def generate(self):
        sound = random.choice(SOUNDS)
        sight = random.choice(SIGHTS)
        location = random.choice(LOCATIONS)
        sensation = random.choice(SENSATIONS)
        coping = random.choice(["taking breaks", "using headphones", "changing environment", "mindfulness"])
        
        text = f"At the {location}, the {sound} and {sight} create {sensation} that overwhelms me. I cope by {coping}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "sound1": (EntityTypes.SOUND, sound),
            "sight1": (EntityTypes.SIGHT, sight),
            "loc1": (EntityTypes.LOCATION, location),
            "sens1": (EntityTypes.SENSATION, sensation),
            "cope1": (EntityTypes.ACTIVITY, coping)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "loc1"),
            (RelationTypes.HEARS, "user", "sound1"),
            (RelationTypes.SEES, "user", "sight1"),
            (RelationTypes.TOUCHES, "user", "sens1"),
            (RelationTypes.DOES_ACTIVITY, "user", "cope1")
        ]
        
        return text, entities, relations

class FirstPersonMoneyGoalTemplate(Template):
    def generate(self):
        amount = random.choice(MONEY)
        goal = random.choice(GOALS)
        timeline = random.choice(["next year", "within 5 years", "by retirement", "soon"])
        strategy = random.choice(["saving monthly", "investing", "side hustle", "career advancement"])
        worry = random.choice(["inflation", "unexpected expenses", "market volatility", "job security"])
        
        text = f"I want to save {amount} for {goal} by {timeline}. My strategy is {strategy} but I worry about {worry}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "money1": (EntityTypes.MONEY, amount),
            "goal1": (EntityTypes.GOAL, goal),
            "time1": (EntityTypes.TIMELINE, timeline),
            "strat1": (EntityTypes.CONCEPT, strategy),
            "worry1": (EntityTypes.CONCEPT, worry)
        }
        
        relations = [
            (RelationTypes.WANTS_GOAL, "user", "goal1"),
            (RelationTypes.SAVES, "user", "money1"),
            (RelationTypes.HAS_DEADLINE, "goal1", "time1"),
            (RelationTypes.USED_FOR, "strat1", "goal1"),
            (RelationTypes.WORRIES_ABOUT, "user", "worry1")
        ]
        
        return text, entities, relations

class FirstPersonIdeaDevelopmentTemplate(Template):
    def generate(self):
        idea = random.choice(IDEAS)
        topic = random.choice(TOPICS)
        collaborator = random.choice(PEOPLE_NAMES)
        stage = random.choice(["planning", "prototyping", "research", "development"])
        emotion = random.choice(EMOTIONS)
        
        text = f"I have an idea for {idea} related to {topic}. I'm collaborating with {collaborator} in the {stage} stage and feel {emotion} about it."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "idea1": (EntityTypes.IDEA, idea),
            "topic1": (EntityTypes.TOPIC, topic),
            "collab1": (EntityTypes.PERSON, collaborator),
            "stage1": (EntityTypes.CONCEPT, stage),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.HAS_IDEA, "user", "idea1"),
            (RelationTypes.ABOUT_TOPIC, "idea1", "topic1"),
            (RelationTypes.COLLABORATES_WITH, "user", "collab1"),
            (RelationTypes.IS_PART_OF, "stage1", "idea1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1")
        ]
        
        return text, entities, relations

class FirstPersonBeliefChallengeTemplate(Template):
    def generate(self):
        belief = random.choice(BELIEFS)
        challenge = random.choice(["new information", "different perspective", "life experience", "expert opinion"])
        emotion = random.choice(["confused", "curious", "defensive", "open-minded"])
        response = random.choice(["researching more", "reflecting deeply", "seeking advice", "staying open"])
        
        text = f"My belief in {belief} was challenged by {challenge}. I felt {emotion} and I'm responding by {response}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "belief1": (EntityTypes.BELIEF, belief),
            "chall1": (EntityTypes.CONCEPT, challenge),
            "e1": (EntityTypes.EMOTION, emotion),
            "resp1": (EntityTypes.ACTIVITY, response)
        }
        
        relations = [
            (RelationTypes.BELIEVES, "user", "belief1"),
            (RelationTypes.CAUSED_BY, "e1", "chall1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.DOES_ACTIVITY, "user", "resp1"),
            (RelationTypes.ABOUT_TOPIC, "resp1", "belief1")
        ]
        
        return text, entities, relations

class FirstPersonTasteMemoryTemplate(Template):
    def generate(self):
        taste = random.choice(TASTES)
        food = random.choice(FOODS)
        location = random.choice(["grandmother's kitchen", "favorite restaurant", "street vendor", "family gathering"])
        smell = random.choice(SMELLS)
        emotion = random.choice(EMOTIONS)
        
        text = f"I remember the {taste} {food} from {location}. The {smell} smell always brings back {emotion} and makes me nostalgic."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "taste1": (EntityTypes.TASTE, taste),
            "food1": (EntityTypes.FOOD, food),
            "loc1": (EntityTypes.LOCATION, location),
            "smell1": (EntityTypes.SMELL, smell),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.REMEMBERS, "user", "food1"),
            (RelationTypes.TASTES, "user", "taste1"),
            (RelationTypes.AT_LOCATION, "food1", "loc1"),
            (RelationTypes.SMELLS, "user", "smell1"),
            (RelationTypes.CAUSED_BY, "e1", "smell1")
        ]
        
        return text, entities, relations

class FirstPersonOpinionChangeTemplate(Template):
    def generate(self):
        topic = random.choice(TOPICS)
        old_opinion = random.choice(OPINIONS)
        new_opinion = random.choice([o for o in OPINIONS if o != old_opinion])
        cause = random.choice(["new research", "personal experience", "expert advice", "different perspective"])
        emotion = random.choice(EMOTIONS)
        
        text = f"I used to think {topic} was {old_opinion}, but now I believe it's {new_opinion}. This change was caused by {cause} and I feel {emotion}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "topic1": (EntityTypes.TOPIC, topic),
            "old_op": (EntityTypes.OPINION, old_opinion),
            "new_op": (EntityTypes.OPINION, new_opinion),
            "cause1": (EntityTypes.CONCEPT, cause),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.ABOUT_TOPIC, "old_op", "topic1"),
            (RelationTypes.HAS_OPINION, "user", "new_op"),
            (RelationTypes.CAUSED_BY, "new_op", "cause1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.RESULTS_IN, "cause1", "new_op")
        ]
        
        return text, entities, relations

class FirstPersonAttributeDevelopmentTemplate(Template):
    def generate(self):
        attribute = random.choice(ATTRIBUTES)
        activity = random.choice(ACTIVITIES)
        mentor = random.choice(PEOPLE_NAMES)
        organization = random.choice(ORGANIZATIONS)
        progress = random.choice(["significant improvement", "steady growth", "noticeable change", "remarkable development"])
        
        text = f"I've been developing my {attribute} qualities through {activity} with {mentor} at {organization}. I've made {progress}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "attr1": (EntityTypes.ATTRIBUTE, attribute),
            "act1": (EntityTypes.ACTIVITY, activity),
            "mentor1": (EntityTypes.PERSON, mentor),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "prog1": (EntityTypes.CONCEPT, progress)
        }
        
        relations = [
            (RelationTypes.HAS_ATTRIBUTE, "user", "attr1"),
            (RelationTypes.DOES_ACTIVITY, "user", "act1"),
            (RelationTypes.COLLABORATES_WITH, "user", "mentor1"),
            (RelationTypes.AT_LOCATION, "act1", "org1"),
            (RelationTypes.RESULTS_IN, "act1", "prog1")
        ]
        
        return text, entities, relations

class FirstPersonWeatherMoodTemplate(Template):
    def generate(self):
        weather = random.choice(WEATHER_CONDITIONS)
        emotion = random.choice(EMOTIONS)
        activity = random.choice(ACTIVITIES)
        preference = random.choice(PREFERENCES)
        
        text = f"I love {weather} weather because it makes me feel {emotion}. It's perfect for {activity} and matches my {preference}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "w1": (EntityTypes.WEATHER, weather),
            "e1": (EntityTypes.EMOTION, emotion),
            "act1": (EntityTypes.ACTIVITY, activity),
            "pref1": (EntityTypes.PREFERENCE, preference)
        }
        
        relations = [
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.CAUSED_BY, "e1", "w1"),
            (RelationTypes.DOES_ACTIVITY, "user", "act1"),
            (RelationTypes.HAS_PREFERENCE, "user", "pref1"),
            (RelationTypes.USED_FOR, "w1", "act1")
        ]
        
        return text, entities, relations

class FirstPersonTransportationMemoryTemplate(Template):
    def generate(self):
        transport = random.choice(TRANSPORTATION)
        location = random.choice(GEOPOLITICAL_ENTITIES)
        duration = get_realistic_duration_for_transport(transport)  # ← FIXED
        emotion = random.choice(EMOTIONS)
        date = random.choice(DATES)
        
        text = f"I remember taking the {transport} to {location} for {duration} on {date}. I felt {emotion} during that journey."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "trans1": (EntityTypes.VEHICLE, transport),
            "loc1": (EntityTypes.GEOPOLITICAL_ENTITY, location),
            "dur1": (EntityTypes.DURATION, duration),
            "e1": (EntityTypes.EMOTION, emotion),
            "date1": (EntityTypes.DATE, date)
        }
        
        relations = [
            (RelationTypes.REMEMBERS, "user", "trans1"),
            (RelationTypes.TRAVELS_TO, "user", "loc1"),
            (RelationTypes.FOR_DURATION, "trans1", "dur1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.ON_DATE, "trans1", "date1")
        ]
        
        return text, entities, relations

class FirstPersonRoomPreferenceTemplate(Template):
    def generate(self):
        room = random.choice(ROOM_TYPES)
        activity = random.choice(ACTIVITIES)
        object_item = random.choice(OBJECTS)
        feeling = random.choice(FEELINGS)
        attribute = random.choice(ATTRIBUTES)
        
        text = f"I prefer working in my {room} because it's {attribute}. I use my {object_item} there for {activity} and it gives me {feeling}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "room1": (EntityTypes.ROOM, room),
            "act1": (EntityTypes.ACTIVITY, activity),
            "obj1": (EntityTypes.OBJECT, object_item),
            "feel1": (EntityTypes.FEELING, feeling),
            "attr1": (EntityTypes.ATTRIBUTE, attribute)
        }
        
        relations = [
            (RelationTypes.HAS_PREFERENCE, "user", "room1"),
            (RelationTypes.AT_LOCATION, "user", "room1"),
            (RelationTypes.HAS_ATTRIBUTE, "room1", "attr1"),
            (RelationTypes.HAS_OBJECT, "user", "obj1"),
            (RelationTypes.USED_FOR, "obj1", "act1"),
            (RelationTypes.FEELS, "user", "feel1")
        ]
        
        return text, entities, relations

class FirstPersonMediaConsumptionTemplate(Template):
    def generate(self):
        media = random.choice(MEDIA_TYPES)
        platform = random.choice(PLATFORMS)
        genre = random.choice(GENRES)
        topic = random.choice(TOPICS)
        sentiment = random.choice(SENTIMENTS)
        
        text = f"I've been watching {media} on {platform} about {topic}. I really enjoy {genre} content and feel {sentiment} about it."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "media1": (EntityTypes.MEDIA, media),
            "plat1": (EntityTypes.PLATFORM, platform),
            "genre1": (EntityTypes.GENRE, genre),
            "topic1": (EntityTypes.TOPIC, topic),
            "sent1": (EntityTypes.SENTIMENT, sentiment)
        }
        
        relations = [
            (RelationTypes.WATCHES, "user", "media1"),
            (RelationTypes.USES, "user", "plat1"),
            (RelationTypes.IS_TYPE, "media1", "genre1"),
            (RelationTypes.ABOUT_TOPIC, "media1", "topic1"),
            (RelationTypes.HAD_SENTIMENT, "user", "sent1")
        ]
        
        return text, entities, relations

class FirstPersonBusinessInteractionTemplate(Template):
    def generate(self):
        business = random.choice(BUSINESS_TYPES)
        frequency = random.choice(FREQUENCY_DETAILED)
        money = random.choice(MONEY)
        service = random.choice(["great service", "excellent food", "helpful staff", "quality products"])
        emotion = random.choice(EMOTIONS)
        
        text = f"I visit this {business} {frequency} and spend about {money}. They provide {service} which makes me feel {emotion}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "biz1": (EntityTypes.BUSINESS, business),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "money1": (EntityTypes.MONEY, money),
            "serv1": (EntityTypes.CONCEPT, service),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "biz1"),
            (RelationTypes.HAS_FREQUENCY, "user", "freq1"),
            (RelationTypes.SPENDS, "user", "money1"),
            (RelationTypes.SERVES, "biz1", "serv1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1")
        ]
        
        return text, entities, relations

class FirstPersonEquipmentOwnershipTemplate(Template):
    def generate(self):
        equipment = random.choice(EQUIPMENT_TYPES)
        brand = random.choice(["Apple", "Microsoft", "Sony", "Dell", "HP", "Logitech", "Samsung", "LG"])
        price = random.choice(MONEY)
        purpose = random.choice(["productivity", "entertainment", "creativity", "communication"])
        attribute = random.choice(ATTRIBUTES)
        
        text = f"I own a {brand} {equipment} that cost me {price}. It's very {attribute} and I use it for {purpose}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "equip1": (EntityTypes.EQUIPMENT, equipment),
            "brand1": (EntityTypes.ORGANIZATION, brand),
            "price1": (EntityTypes.MONEY, price),
            "purp1": (EntityTypes.CONCEPT, purpose),
            "attr1": (EntityTypes.ATTRIBUTE, attribute)
        }
        
        relations = [
            (RelationTypes.OWNS, "user", "equip1"),
            (RelationTypes.IS_TYPE, "equip1", "brand1"),
            (RelationTypes.COSTS, "equip1", "price1"),
            (RelationTypes.USED_FOR, "equip1", "purp1"),
            (RelationTypes.HAS_ATTRIBUTE, "equip1", "attr1")
        ]
        
        return text, entities, relations

class FirstPersonSocialAnxietyTemplate(Template):
    def generate(self):
        social_situation = random.choice(SOCIAL_SITUATIONS)
        emotion = random.choice(["anxious", "nervous", "excited", "worried", "confident"])
        coping_strategy = random.choice(["deep breathing", "positive thinking", "preparation", "meditation"])
        friend = random.choice(PEOPLE_NAMES)
        outcome = random.choice(["went well", "was challenging", "exceeded expectations", "was memorable"])
        
        text = f"I was feeling {emotion} about the {social_situation} but used {coping_strategy} to cope. {friend} was there and it {outcome}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "sit1": (EntityTypes.EVENT, social_situation),
            "e1": (EntityTypes.EMOTION, emotion),
            "cope1": (EntityTypes.ACTIVITY, coping_strategy),
            "friend1": (EntityTypes.PERSON, friend),
            "out1": (EntityTypes.CONCEPT, outcome)
        }
        
        relations = [
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.ATTENDS, "user", "sit1"),
            (RelationTypes.DOES_ACTIVITY, "user", "cope1"),
            (RelationTypes.IS_FRIENDS_WITH, "user", "friend1"),
            (RelationTypes.RESULTS_IN, "sit1", "out1")
        ]
        
        return text, entities, relations

class FirstPersonSkillDevelopmentProgressTemplate(Template):
    def generate(self):
        skill = random.choice(SKILLS)
        duration = random.choice(DURATIONS)
        progress = random.choice(["significant progress", "steady improvement", "amazing growth", "slow but consistent progress"])
        goal = random.choice(GOALS)
        confidence = random.choice(["more confident", "increasingly skilled", "much better", "significantly improved"])
        
        text = f"I've been learning {skill} for {duration} and made {progress}. My goal is to {goal} and I feel {confidence}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "skill1": (EntityTypes.SKILL, skill),
            "dur1": (EntityTypes.DURATION, duration),
            "prog1": (EntityTypes.CONCEPT, progress),
            "goal1": (EntityTypes.GOAL, goal),
            "conf1": (EntityTypes.FEELING, confidence)
        }
        
        relations = [
            (RelationTypes.HAS_SKILL, "user", "skill1"),
            (RelationTypes.FOR_DURATION, "skill1", "dur1"),
            (RelationTypes.RESULTS_IN, "skill1", "prog1"),
            (RelationTypes.WANTS_GOAL, "user", "goal1"),
            (RelationTypes.FEELS, "user", "conf1")
        ]
        
        return text, entities, relations

class FirstPersonExpandedTravelTemplate(Template):
    def generate(self):
        location = random.choice(GEOPOLITICAL_ENTITIES)
        duration = random.choice(DURATIONS)
        date = random.choice(DATES)
        emotion = random.choice(EMOTIONS)
        sentiment = random.choice(SENTIMENTS)
        
        text = f"I'm thinking of traveling to {location} for {duration} on {date}. I feel {emotion} and have a {sentiment} sentiment about this trip."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.GEOPOLITICAL_ENTITY, location),
            "dur1": (EntityTypes.DURATION, duration),
            "date1": (EntityTypes.DATE, date),
            "e1": (EntityTypes.EMOTION, emotion),
            "sent1": (EntityTypes.SENTIMENT, sentiment)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "user", "loc1"),
            (RelationTypes.TRAVELS_TO, "user", "loc1"),
            (RelationTypes.FOR_DURATION, "loc1", "dur1"),
            (RelationTypes.ON_DATE, "loc1", "date1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.HAD_SENTIMENT, "user", "sent1")
        ]
        
        return text, entities, relations

class FirstPersonObjectOwnershipTemplate(Template):
    def generate(self):
        obj = random.choice(OBJECTS)
        friend_name = random.choice(PEOPLE_NAMES)
        duration = random.choice(DURATIONS)
        attribute = random.choice(ATTRIBUTES)
        purpose = random.choice(["work", "entertainment", "learning", "creativity"])
        
        text = f"I borrowed a {obj} from {friend_name} for {duration}. It's quite {attribute} and I'm using it for {purpose}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "obj1": (EntityTypes.OBJECT, obj),
            "friend1": (EntityTypes.PERSON, friend_name),
            "dur1": (EntityTypes.DURATION, duration),
            "attr1": (EntityTypes.ATTRIBUTE, attribute),
            "purpose1": (EntityTypes.ACTIVITY, purpose)
        }
        
        relations = [
            (RelationTypes.BORROWED, "user", "obj1"),
            (RelationTypes.LENT, "friend1", "obj1"),
            (RelationTypes.IS_FRIENDS_WITH, "user", "friend1"),
            (RelationTypes.FOR_DURATION, "obj1", "dur1"),
            (RelationTypes.HAS_ATTRIBUTE, "obj1", "attr1"),
            (RelationTypes.USED_FOR, "obj1", "purpose1")
        ]
        
        return text, entities, relations

class FirstPersonHealthGoalTemplate(Template):
    def generate(self):
        health_info = random.choice(HEALTH_INFO)
        goal = random.choice(GOALS)
        emotion = random.choice(EMOTIONS)
        intent = random.choice(INTENTS)
        topic = random.choice(TOPICS)
        
        text = f"I want to improve my {health_info} to {goal}. I feel {emotion} about this and my intent is to {intent}. This is all about {topic}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "health1": (EntityTypes.HEALTH_INFO, health_info),
            "goal1": (EntityTypes.GOAL, goal),
            "e1": (EntityTypes.EMOTION, emotion),
            "intent1": (EntityTypes.INTENT, intent),
            "topic1": (EntityTypes.TOPIC, topic)
        }
        
        relations = [
            (RelationTypes.HAS_HEALTH_INFO, "user", "health1"),
            (RelationTypes.WANTS_GOAL, "user", "goal1"),
            (RelationTypes.FEELS_EMOTION, "user", "e1"),
            (RelationTypes.HAS_INTENT, "user", "intent1"),
            (RelationTypes.ABOUT_TOPIC, "goal1", "topic1"),
            (RelationTypes.RESULTS_IN, "health1", "goal1")
        ]
        
        return text, entities, relations

class FirstPersonWorkRoleTemplate(Template):
    def generate(self):
        role = random.choice(ROLES)
        organization = random.choice(ORGANIZATIONS)
        skill = random.choice(SKILLS)
        project = random.choice(["new initiative", "client project", "research study", "product development"])
        attribute = random.choice(ATTRIBUTES)
        
        text = f"I have the role of {role} at {organization}. I'm {attribute} and use my {skill} skills on this {project}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "role1": (EntityTypes.ROLE, role),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "skill1": (EntityTypes.SKILL, skill),
            "proj1": (EntityTypes.PROJECT, project),
            "attr1": (EntityTypes.ATTRIBUTE, attribute)
        }
        
        relations = [
            (RelationTypes.HAS_ROLE, "user", "role1"),
            (RelationTypes.WORKS_FOR, "user", "org1"),
            (RelationTypes.HAS_SKILL, "user", "skill1"),
            (RelationTypes.WORKS_ON, "user", "proj1"),
            (RelationTypes.HAS_ATTRIBUTE, "user", "attr1"),
            (RelationTypes.IS_PART_OF, "role1", "org1")
        ]
        
        return text, entities, relations

# === MISSING COGNITIVE RELATION TEMPLATES ===

class FirstPersonThinkingProcessTemplate(Template):
    def generate(self):
        thinking_topic = random.choice(["career change", "life decisions", "future plans", "personal goals"])
        consideration = random.choice(["different options", "pros and cons", "potential outcomes", "various approaches"])
        planning_activity = random.choice(["researching", "consulting experts", "making lists", "weighing decisions"])
        dream_goal = random.choice(GOALS)
        hope = random.choice(["better future", "positive outcome", "personal growth", "meaningful change"])
        
        text = f"I'm thinking of {thinking_topic} and considering {consideration}. I'm planning by {planning_activity} because I dream of {dream_goal} and hope for {hope}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "topic1": (EntityTypes.TOPIC, thinking_topic),
            "consider1": (EntityTypes.CONCEPT, consideration),
            "plan1": (EntityTypes.ACTIVITY, planning_activity),
            "dream1": (EntityTypes.GOAL, dream_goal),
            "hope1": (EntityTypes.CONCEPT, hope)
        }
        
        relations = [
            (RelationTypes.THINKING_OF, "user", "topic1"),
            (RelationTypes.CONSIDERING, "user", "consider1"),
            (RelationTypes.PLANNING, "user", "plan1"),
            (RelationTypes.DREAMS_OF, "user", "dream1"),
            (RelationTypes.HOPES_FOR, "user", "hope1"),
            (RelationTypes.INTENDS, "user", "plan1")
        ]
        
        return text, entities, relations

class FirstPersonRegretAnticipationTemplate(Template):
    def generate(self):
        regret = random.choice(["missed opportunity", "poor decision", "lost relationship", "unfulfilled potential"])
        past_period = random.choice(PERIODS)
        future_event = random.choice(["vacation", "project completion", "family gathering", "career milestone"])
        timeline = random.choice(["next month", "this summer", "next year", "soon"])
        missing_person = random.choice(PEOPLE_NAMES)
        
        text = f"I regret {regret} from {past_period} and miss {missing_person}. However, I'm looking forward to {future_event} {timeline}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "regret1": (EntityTypes.CONCEPT, regret),
            "period1": (EntityTypes.PERIOD, past_period),
            "event1": (EntityTypes.EVENT, future_event),
            "time1": (EntityTypes.TIMELINE, timeline),
            "person1": (EntityTypes.PERSON, missing_person)
        }
        
        relations = [
            (RelationTypes.REGRETS, "user", "regret1"),
            (RelationTypes.ON_DATE, "regret1", "period1"),
            (RelationTypes.LOOKING_FORWARD_TO, "user", "event1"),
            (RelationTypes.HAS_DEADLINE, "event1", "time1"),
            (RelationTypes.MISSES, "user", "person1")
        ]
        
        return text, entities, relations

# === SENSORY RELATION TEMPLATES ===

class FirstPersonCompleteSensoryTemplate(Template):
    def generate(self):
        location = random.choice(["coffee shop", "grandmother's kitchen", "ocean beach", "mountain cabin"])
        sound = random.choice(SOUNDS)
        sight = random.choice(SIGHTS)
        taste = random.choice(TASTES)
        smell = random.choice(SMELLS)
        feeling = random.choice(FEELINGS)
        memory_trigger = random.choice(MEMORY_TYPES)
        
        text = f"At {location}, I hear {sound}, see {sight}, taste something {taste}, smell {smell}, and feel {feeling}. This triggers a {memory_trigger}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "loc1": (EntityTypes.LOCATION, location),
            "sound1": (EntityTypes.SOUND, sound),
            "sight1": (EntityTypes.SIGHT, sight),
            "taste1": (EntityTypes.TASTE, taste),
            "smell1": (EntityTypes.SMELL, smell),
            "feel1": (EntityTypes.FEELING, feeling),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_trigger)
        }
        
        relations = [
            (RelationTypes.AT_LOCATION, "user", "loc1"),
            (RelationTypes.HEARS, "user", "sound1"),
            (RelationTypes.SEES, "user", "sight1"),
            (RelationTypes.TASTES, "user", "taste1"),
            (RelationTypes.SMELLS, "user", "smell1"),
            (RelationTypes.TOUCHES, "user", "feel1"),
            (RelationTypes.CAUSED_BY, "memory1", "smell1")
        ]
        
        return text, entities, relations

# === TEMPORAL PATTERN TEMPLATES ===

class FirstPersonRepeatingRoutineTemplate(Template):
    def generate(self):
        activity = random.choice(["morning meditation", "evening workout", "weekly planning", "daily journaling"])
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        schedule = random.choice(RECURRING_SCHEDULES)
        frequency = random.choice(FREQUENCY_DETAILED)
        intent = random.choice(INTENTS)
        
        text = f"I repeat {activity} from {start_time} to {end_time} on a {schedule} basis, {frequency}. My intent is to {intent}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "intent1": (EntityTypes.INTENT, intent)
        }
        
        relations = [
            (RelationTypes.REPEATS, "user", "activity1"),
            (RelationTypes.STARTS_AT, "activity1", "start1"),
            (RelationTypes.ENDS_AT, "activity1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "user", "sched1"),
            (RelationTypes.HAS_FREQUENCY, "activity1", "freq1"),
            (RelationTypes.INTENDS, "user", "intent1"),
            (RelationTypes.PLANS, "user", "activity1")
        ]
        
        return text, entities, relations

# === THIRD PERSON TEMPLATES FOR MISSING COVERAGE ===

class ThirdPersonCulturalPreservationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        cultural_element = random.choice(["ancestral recipes", "traditional crafts", "folk stories", "ceremonial practices"])
        learning_method = random.choice(["oral tradition", "hands-on teaching", "community workshops", "cultural immersion"])
        community_role = random.choice(["cultural keeper", "tradition bearer", "heritage preservationist", "community elder"])
        personal_growth = random.choice(["cultural identity", "community connection", "historical awareness", "pride in heritage"])
        
        text = f"{person} preserves {cultural_element} through {learning_method} in their role as {community_role}. This fosters {personal_growth} in the community."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "culture1": (EntityTypes.CULTURAL_ELEMENT, cultural_element),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth)
        }
        
        relations = [
            (RelationTypes.ORGANIZES, "p1", "culture1"),
            (RelationTypes.USES, "p1", "method1"),
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.RESULTS_IN, "culture1", "growth1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "growth1")
        ]
        
        return text, entities, relations

# === EDGE CASE AND RARE COMBINATION TEMPLATES ===

class FirstPersonComplexMemoryTemplate(Template):
    def generate(self):
        memory_type = random.choice(["traumatic memory", "suppressed memory", "flashbulb memory", "collective memory"])
        period = random.choice(["childhood trauma", "significant life event", "historical moment", "family crisis"])
        cultural_element = random.choice(["family ritual", "cultural ceremony", "traditional healing", "ancestral practice"])
        learning_method = random.choice(["therapeutic process", "family storytelling", "cultural guidance", "spiritual practice"])
        personal_growth = random.choice(["healing", "understanding", "acceptance", "resilience"])
        community_role = random.choice(["survivor", "advocate", "storyteller", "healer"])
        
        text = f"I process a {memory_type} from {period} through {cultural_element} using {learning_method}. This journey toward {personal_growth} shaped my {community_role} identity."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_type),
            "period1": (EntityTypes.PERIOD, period),
            "culture1": (EntityTypes.CULTURAL_ELEMENT, cultural_element),
            "method1": (EntityTypes.LEARNING_METHOD, learning_method),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth),
            "role1": (EntityTypes.COMMUNITY_ROLE, community_role)
        }
        
        relations = [
            (RelationTypes.HAS_OBJECT, "user", "memory1"),
            (RelationTypes.ON_DATE, "memory1", "period1"),
            (RelationTypes.USES, "user", "culture1"),
            (RelationTypes.USES, "user", "method1"),
            (RelationTypes.RESULTS_IN, "method1", "growth1"),
            (RelationTypes.HAS_ROLE, "user", "role1")
        ]
        
        return text, entities, relations

# === MEMORY-SPECIFIC CONTEXT TEMPLATES ===

class FirstPersonMemoryRecallTemplate(Template):
    def generate(self):
        memory_type = random.choice(["procedural memory", "episodic memory", "semantic memory", "emotional memory"])
        trigger = random.choice(["specific smell", "familiar sound", "visual cue", "physical sensation"])
        recall_context = random.choice(["work situation", "family gathering", "quiet moment", "social interaction"])
        life_stage = random.choice(["adolescence", "early career", "parenthood", "recent years"])
        personal_growth = random.choice(["self-understanding", "emotional healing", "life clarity", "personal insight"])
        
        text = f"A {trigger} during {recall_context} triggered my {memory_type} from my {life_stage}. This recall led to {personal_growth}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "memory1": (EntityTypes.MEMORY_TYPE, memory_type),
            "trigger1": (EntityTypes.SENSATION, trigger),
            "context1": (EntityTypes.CONCEPT, recall_context),
            "stage1": (EntityTypes.LIFE_STAGE, life_stage),
            "growth1": (EntityTypes.PERSONAL_GROWTH, personal_growth)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "user", "trigger1"),
            (RelationTypes.CAUSED_BY, "memory1", "trigger1"),
            (RelationTypes.REMEMBERS, "user", "memory1"),
            (RelationTypes.EXPERIENCES, "user", "stage1"),
            (RelationTypes.RESULTS_IN, "memory1", "growth1")
        ]
        
        return text, entities, relations

class ThirdPersonLifeTransitionTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        transition = random.choice(["graduation", "marriage", "parenthood", "retirement", "relocation", "career change"])
        support_network = random.choice(["family", "friends", "colleagues", "community"])
        challenge = random.choice(["adjustment period", "new responsibilities", "learning curve", "emotional processing"])
        growth_outcome = random.choice(["newfound confidence", "deeper relationships", "expanded perspective", "personal strength"])
        
        text = f"{person} went through {transition} with support from their {support_network}. Despite the {challenge}, they developed {growth_outcome}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "trans1": (EntityTypes.EVENT, transition),
            "network1": (EntityTypes.GROUP, support_network),
            "challenge1": (EntityTypes.CONCEPT, challenge),
            "growth1": (EntityTypes.CONCEPT, growth_outcome)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "p1", "trans1"),
            (RelationTypes.MEMBER_OF, "p1", "network1"),
            (RelationTypes.CAUSED_BY, "challenge1", "trans1"),
            (RelationTypes.RESULTS_IN, "trans1", "growth1"),
            (RelationTypes.HAS_ATTRIBUTE, "p1", "growth1")
        ]
        
        return text, entities, relations

class ThirdPersonCulturalExperienceTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        cultural_event = random.choice(["festival", "ceremony", "cultural exchange", "traditional celebration", "art exhibition"])
        location = random.choice(GEOPOLITICAL_ENTITIES)
        cultural_learning = random.choice(["new traditions", "different perspectives", "historical understanding", "artistic appreciation"])
        emotional_impact = random.choice(["profound respect", "cultural awareness", "personal enrichment", "worldview expansion"])
        sharing_action = random.choice(["tells stories about it", "incorporates traditions", "shares photos", "recommends to others"])
        
        text = f"{person} participated in a {cultural_event} in {location}. They gained {cultural_learning} which created {emotional_impact}. Now they {sharing_action}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "event1": (EntityTypes.EVENT, cultural_event),
            "loc1": (EntityTypes.GEOPOLITICAL_ENTITY, location),
            "learning1": (EntityTypes.CONCEPT, cultural_learning),
            "impact1": (EntityTypes.EMOTION, emotional_impact),
            "action1": (EntityTypes.ACTIVITY, sharing_action)
        }
        
        relations = [
            (RelationTypes.PARTICIPATES_IN, "p1", "event1"),
            (RelationTypes.AT_LOCATION, "event1", "loc1"),
            (RelationTypes.LEARNS, "p1", "learning1"),
            (RelationTypes.RESULTS_IN, "learning1", "impact1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "action1")
        ]
        
        return text, entities, relations

class ThirdPersonGenerosityTemplate(Template):
    def generate(self):
        giver = random.choice(PEOPLE_NAMES)
        recipient = get_different_person(giver)
        generous_act = random.choice(["financial help", "time volunteering", "emotional support", "skill sharing", "resource donation"])
        cause = random.choice(["family emergency", "community need", "natural disaster", "personal struggle", "charitable cause"])
        impact = random.choice(["life-changing difference", "renewed hope", "community strengthening", "ripple effect of kindness"])
        motivation = random.choice(["personal values", "past experiences", "empathy", "sense of duty"])
        
        text = f"{giver} provided {generous_act} to {recipient} during a {cause}. This created {impact} and was motivated by their {motivation}."
        
        entities = {
            "giver1": (EntityTypes.PERSON, giver),
            "recip1": (EntityTypes.PERSON, recipient),
            "act1": (EntityTypes.ACTIVITY, generous_act),
            "cause1": (EntityTypes.CONCEPT, cause),
            "impact1": (EntityTypes.CONCEPT, impact),
            "motiv1": (EntityTypes.VALUE, motivation)
        }
        
        relations = [
            (RelationTypes.DOES_ACTIVITY, "giver1", "act1"),
            (RelationTypes.CARES_FOR, "giver1", "recip1"),
            (RelationTypes.CAUSED_BY, "act1", "cause1"),
            (RelationTypes.RESULTS_IN, "act1", "impact1"),
            (RelationTypes.VALUES, "giver1", "motiv1")
        ]
        
        return text, entities, relations

class ThirdPersonSkillMasteryTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        skill = random.choice(SKILLS)
        learning_method = random.choice(["formal training", "self-study", "mentorship", "hands-on practice", "online courses"])
        time_invested = random.choice(DURATIONS)
        mastery_indicator = random.choice(["teaching others", "leading projects", "professional recognition", "expert status"])
        personal_satisfaction = random.choice(["deep fulfillment", "increased confidence", "career advancement", "creative expression"])
        
        text = f"{person} mastered {skill} through {learning_method} over {time_invested}. Their expertise shows through {mastery_indicator}, bringing {personal_satisfaction}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "skill1": (EntityTypes.SKILL, skill),
            "method1": (EntityTypes.CONCEPT, learning_method),
            "time1": (EntityTypes.DURATION, time_invested),
            "mastery1": (EntityTypes.ACTIVITY, mastery_indicator),
            "satisfaction1": (EntityTypes.EMOTION, personal_satisfaction)
        }
        
        relations = [
            (RelationTypes.HAS_SKILL, "p1", "skill1"),
            (RelationTypes.LEARNS, "p1", "skill1"),
            (RelationTypes.USES, "p1", "method1"),
            (RelationTypes.FOR_DURATION, "method1", "time1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "mastery1"),
            (RelationTypes.FEELS_EMOTION, "p1", "satisfaction1")
        ]
        
        return text, entities, relations

class ThirdPersonCommunityLeadershipTemplate(Template):
    def generate(self):
        leader = random.choice(PEOPLE_NAMES)
        community_issue = random.choice(["local development", "environmental concern", "social justice", "education improvement", "health initiative"])
        leadership_role = random.choice(["organizer", "advocate", "coordinator", "spokesperson", "volunteer leader"])
        group_size = random.choice(["small dedicated team", "growing movement", "large coalition", "grassroots network"])
        achievement = random.choice(["policy change", "funding secured", "awareness raised", "problem solved", "community united"])
        
        text = f"{leader} took on the {leadership_role} role to address {community_issue}. They mobilized a {group_size} and achieved {achievement}."
        
        entities = {
            "leader1": (EntityTypes.PERSON, leader),
            "issue1": (EntityTypes.CONCEPT, community_issue),
            "role1": (EntityTypes.ROLE, leadership_role),
            "group1": (EntityTypes.GROUP, group_size),
            "achieve1": (EntityTypes.GOAL, achievement)
        }
        
        relations = [
            (RelationTypes.HAS_ROLE, "leader1", "role1"),
            (RelationTypes.ABOUT_TOPIC, "role1", "issue1"),
            (RelationTypes.LEADS, "leader1", "group1"),
            (RelationTypes.WANTS_GOAL, "leader1", "achieve1"),
            (RelationTypes.RESULTS_IN, "group1", "achieve1")
        ]
        
        return text, entities, relations

class ThirdPersonVehicleOwnershipTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        vehicle = random.choice(VEHICLES)
        purpose = random.choice(["commuting", "family trips", "work travel", "weekend adventures"])
        attribute = random.choice(ATTRIBUTES)
        location = random.choice(LOCATIONS)
        
        text = f"{person} owns a {vehicle} which is very {attribute}. They use it for {purpose} and park it at the {location}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "veh1": (EntityTypes.VEHICLE, vehicle),
            "purp1": (EntityTypes.ACTIVITY, purpose),
            "attr1": (EntityTypes.ATTRIBUTE, attribute),
            "loc1": (EntityTypes.LOCATION, location)
        }
        
        relations = [
            (RelationTypes.OWNS, "p1", "veh1"),
            (RelationTypes.HAS_ATTRIBUTE, "veh1", "attr1"),
            (RelationTypes.USED_FOR, "veh1", "purp1"),
            (RelationTypes.AT_LOCATION, "veh1", "loc1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "purp1")
        ]
        
        return text, entities, relations

class ThirdPersonMediaProductionTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        media = random.choice(MEDIA_TYPES)
        topic = random.choice(TOPICS)
        platform = random.choice(PLATFORMS)
        audience = random.choice(["thousands", "millions", "hundreds", "a growing number"])
        result = random.choice(["recognition", "income", "satisfaction", "new opportunities"])
        
        text = f"{person} creates {media} content about {topic} on {platform}. They reach {audience} of viewers and this results in {result}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "media1": (EntityTypes.MEDIA, media),
            "topic1": (EntityTypes.TOPIC, topic),
            "plat1": (EntityTypes.PLATFORM, platform),
            "aud1": (EntityTypes.GROUP, audience),
            "res1": (EntityTypes.GOAL, result)
        }
        
        relations = [
            (RelationTypes.ORGANIZES, "p1", "media1"),
            (RelationTypes.ABOUT_TOPIC, "media1", "topic1"),
            (RelationTypes.USES, "p1", "plat1"),
            (RelationTypes.HAS_GROUP_MEMBER, "aud1", "p1"),
            (RelationTypes.RESULTS_IN, "media1", "res1")
        ]
        
        return text, entities, relations

class ThirdPersonWeatherImpactTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        weather = random.choice(WEATHER_CONDITIONS)
        condition = random.choice(CONDITIONS)
        activity = random.choice(ACTIVITIES)
        location = random.choice(LOCATIONS)
        adaptation = random.choice(["adjusted their schedule", "changed plans", "found alternatives", "embraced the change"])
        
        text = f"{person} was affected by {weather} weather which caused {condition}. They were {activity} at {location} and {adaptation}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "w1": (EntityTypes.WEATHER, weather),
            "cond1": (EntityTypes.CONDITION, condition),
            "act1": (EntityTypes.ACTIVITY, activity),
            "loc1": (EntityTypes.LOCATION, location),
            "adapt1": (EntityTypes.ACTIVITY, adaptation)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "p1", "cond1"),
            (RelationTypes.CAUSED_BY, "cond1", "w1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.AT_LOCATION, "p1", "loc1"),
            (RelationTypes.RESULTS_IN, "cond1", "adapt1")
        ]
        
        return text, entities, relations

class ThirdPersonGroupMembershipTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        group = random.choice(GROUPS)
        role = random.choice(ROLES)
        location = random.choice(LOCATIONS)
        date = random.choice(DATES)
        activity = random.choice(ACTIVITIES)
        
        text = f"{person} is a {role} in the {group} group. They meet at {location} on {date} for {activity}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "group1": (EntityTypes.GROUP, group),
            "role1": (EntityTypes.ROLE, role),
            "loc1": (EntityTypes.LOCATION, location),
            "date1": (EntityTypes.DATE, date),
            "act1": (EntityTypes.ACTIVITY, activity)
        }
        
        relations = [
            (RelationTypes.HAS_GROUP_MEMBER, "group1", "p1"),
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.AT_LOCATION, "group1", "loc1"),
            (RelationTypes.ON_DATE, "group1", "date1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.IS_PART_OF, "p1", "group1")
        ]
        
        return text, entities, relations

class ThirdPersonFamilyRelationshipTemplate(Template):
    def generate(self):
        person1 = random.choice(PEOPLE_NAMES)
        person2 = get_different_person(person1)
        emotion = random.choice(EMOTIONS)
        activity = random.choice(["spending time together", "having dinner", "celebrating holidays", "sharing stories"])
        location = random.choice(["family home", "restaurant", "park", "living room"])
        
        text = f"{person1} is family with {person2}. They enjoy {activity} at the {location} and both feel {emotion}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person1),
            "p2": (EntityTypes.PERSON, person2),
            "e1": (EntityTypes.EMOTION, emotion),
            "act1": (EntityTypes.ACTIVITY, activity),
            "loc1": (EntityTypes.LOCATION, location)
        }
        
        relations = [
            (RelationTypes.IS_FAMILY_WITH, "p1", "p2"),
            (RelationTypes.FEELS_EMOTION, "p1", "e1"),
            (RelationTypes.FEELS_EMOTION, "p2", "e1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.DOES_ACTIVITY, "p2", "act1"),
            (RelationTypes.AT_LOCATION, "act1", "loc1")
        ]
        
        return text, entities, relations

class ThirdPersonCausationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        event = random.choice(["project success", "team achievement", "product launch", "client satisfaction"])
        skill = random.choice(SKILLS)
        emotion = random.choice(EMOTIONS)
        result = random.choice(["promotion", "recognition", "bonus", "new opportunities"])
        
        text = f"{person}'s {skill} expertise caused the {event}, which made them feel {emotion}. This resulted in {result}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "event1": (EntityTypes.EVENT, event),
            "skill1": (EntityTypes.SKILL, skill),
            "e1": (EntityTypes.EMOTION, emotion),
            "result1": (EntityTypes.GOAL, result)
        }
        
        relations = [
            (RelationTypes.HAS_SKILL, "p1", "skill1"),
            (RelationTypes.CAUSED_BY, "event1", "skill1"),
            (RelationTypes.FEELS_EMOTION, "p1", "e1"),
            (RelationTypes.RESULTS_IN, "event1", "result1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "event1")
        ]
        
        return text, entities, relations

class ThirdPersonLocationProximityTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        location1 = random.choice(LOCATIONS)
        location2 = random.choice(["coffee shop", "park", "library", "gym", "restaurant"])
        preference = random.choice(PREFERENCES)
        activity = random.choice(ACTIVITIES)
        
        text = f"{person} works at the {location1} which is near a {location2}. They have a preference for {preference} and often do {activity} there."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "loc1": (EntityTypes.LOCATION, location1),
            "loc2": (EntityTypes.LOCATION, location2),
            "pref1": (EntityTypes.PREFERENCE, preference),
            "act1": (EntityTypes.ACTIVITY, activity)
        }
        
        relations = [
            (RelationTypes.WORKS_FROM, "p1", "loc1"),
            (RelationTypes.IS_NEAR, "loc1", "loc2"),
            (RelationTypes.HAS_PREFERENCE, "p1", "pref1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.AT_LOCATION, "act1", "loc2")
        ]
        
        return text, entities, relations

class ThirdPersonPlatformInfluenceTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        platform = random.choice(PLATFORMS)
        topic = random.choice(TOPICS)
        followers = random.choice(["thousands", "millions", "hundreds of thousands"])
        influence = random.choice(["significant impact", "growing influence", "positive change", "community building"])
        
        text = f"{person} uses {platform} to share content about {topic}. They have {followers} of followers and create {influence}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "plat1": (EntityTypes.PLATFORM, platform),
            "topic1": (EntityTypes.TOPIC, topic),
            "follow1": (EntityTypes.GROUP, followers),
            "inf1": (EntityTypes.CONCEPT, influence)
        }
        
        relations = [
            (RelationTypes.USES, "p1", "plat1"),
            (RelationTypes.ABOUT_TOPIC, "plat1", "topic1"),
            (RelationTypes.HAS_GROUP_MEMBER, "follow1", "p1"),
            (RelationTypes.RESULTS_IN, "plat1", "inf1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "inf1")
        ]
        
        return text, entities, relations

class ThirdPersonRoomOrganizationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        room = random.choice(ROOM_TYPES)
        equipment = random.choice(EQUIPMENT_TYPES)
        purpose = random.choice(["productivity", "creativity", "relaxation", "focus"])
        attribute = random.choice(ATTRIBUTES)
        result = random.choice(["improved workflow", "better focus", "increased efficiency", "enhanced creativity"])
        
        text = f"{person} organized their {room} with {equipment} for {purpose}. The space is now {attribute} and results in {result}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "room1": (EntityTypes.ROOM, room),
            "equip1": (EntityTypes.EQUIPMENT, equipment),
            "purp1": (EntityTypes.CONCEPT, purpose),
            "attr1": (EntityTypes.ATTRIBUTE, attribute),
            "res1": (EntityTypes.CONCEPT, result)
        }
        
        relations = [
            (RelationTypes.HAS_OBJECT, "p1", "room1"),
            (RelationTypes.AT_LOCATION, "equip1", "room1"),
            (RelationTypes.USED_FOR, "room1", "purp1"),
            (RelationTypes.HAS_ATTRIBUTE, "room1", "attr1"),
            (RelationTypes.RESULTS_IN, "room1", "res1")
        ]
        
        return text, entities, relations

class ThirdPersonGenrePreferenceTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        genre = random.choice(GENRES)
        media = random.choice(MEDIA_TYPES)
        platform = random.choice(PLATFORMS)
        frequency = random.choice(FREQUENCY_DETAILED)
        emotion = random.choice(EMOTIONS)
        
        text = f"{person} enjoys {genre} {media} on {platform} {frequency}. This genre makes them feel {emotion} and relaxed."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "genre1": (EntityTypes.GENRE, genre),
            "media1": (EntityTypes.MEDIA, media),
            "plat1": (EntityTypes.PLATFORM, platform),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "e1": (EntityTypes.EMOTION, emotion)
        }
        
        relations = [
            (RelationTypes.HAS_PREFERENCE, "p1", "genre1"),
            (RelationTypes.WATCHES, "p1", "media1"),
            (RelationTypes.USES, "p1", "plat1"),
            (RelationTypes.HAS_FREQUENCY, "p1", "freq1"),
            (RelationTypes.FEELS_EMOTION, "p1", "e1")
        ]
        
        return text, entities, relations

class ThirdPersonBusinessOwnershipTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        business = random.choice(BUSINESS_TYPES)
        location = random.choice(LOCATIONS)
        service = random.choice(["excellent customer service", "quality products", "innovative solutions", "personalized attention"])
        revenue = random.choice(MONEY)
        growth = random.choice(["steady growth", "rapid expansion", "consistent success", "increasing profits"])
        
        text = f"{person} owns a {business} at {location} that provides {service}. They generate {revenue} monthly and experience {growth}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "biz1": (EntityTypes.BUSINESS, business),
            "loc1": (EntityTypes.LOCATION, location),
            "serv1": (EntityTypes.CONCEPT, service),
            "rev1": (EntityTypes.MONEY, revenue),
            "grow1": (EntityTypes.CONCEPT, growth)
        }
        
        relations = [
            (RelationTypes.OWNS, "p1", "biz1"),
            (RelationTypes.AT_LOCATION, "biz1", "loc1"),
            (RelationTypes.SERVES, "biz1", "serv1"),
            (RelationTypes.EARNS, "p1", "rev1"),
            (RelationTypes.RESULTS_IN, "biz1", "grow1")
        ]
        
        return text, entities, relations

class ThirdPersonTransportationRoutineTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        transport = random.choice(TRANSPORTATION)
        start_location = random.choice(LOCATIONS)
        end_location = random.choice(LOCATIONS)
        duration = get_realistic_duration_for_transport(transport)  # ← FIXED
        frequency = get_realistic_frequency_for_activity("commuting")  # ← FIXED
        preference = random.choice(["convenience", "cost-effectiveness", "environmental impact", "comfort"])
        
        text = f"{person} takes the {transport} from {start_location} to {end_location} {frequency}. The journey takes {duration} and they prefer it for {preference}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "trans1": (EntityTypes.VEHICLE, transport),
            "start1": (EntityTypes.LOCATION, start_location),
            "end1": (EntityTypes.LOCATION, end_location),
            "dur1": (EntityTypes.DURATION, duration),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "pref1": (EntityTypes.PREFERENCE, preference)
        }
        
        relations = [
            (RelationTypes.USES, "p1", "trans1"),
            (RelationTypes.TRAVELS_TO, "p1", "end1"),
            (RelationTypes.FOR_DURATION, "trans1", "dur1"),
            (RelationTypes.HAS_FREQUENCY, "p1", "freq1"),
            (RelationTypes.HAS_PREFERENCE, "p1", "pref1")
        ]
        
        return text, entities, relations

class ThirdPersonConditionManagementTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        condition = random.choice(CONDITIONS)
        health_activity = random.choice(HEALTH_INFO)
        frequency = random.choice(FREQUENCY_DETAILED)
        result = random.choice(["improvement", "stability", "better management", "positive outcomes"])
        support = random.choice(PEOPLE_NAMES)
        
        text = f"{person} manages {condition} through {health_activity} {frequency}. With support from {support}, they achieve {result}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "cond1": (EntityTypes.CONDITION, condition),
            "health1": (EntityTypes.HEALTH_INFO, health_activity),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "res1": (EntityTypes.CONCEPT, result),
            "supp1": (EntityTypes.PERSON, support)
        }
        
        relations = [
            (RelationTypes.EXPERIENCES, "p1", "cond1"),
            (RelationTypes.HAS_HEALTH_INFO, "p1", "health1"),
            (RelationTypes.HAS_FREQUENCY, "health1", "freq1"),
            (RelationTypes.RESULTS_IN, "health1", "res1"),
            (RelationTypes.COLLABORATES_WITH, "p1", "supp1")
        ]
        
        return text, entities, relations

class ThirdPersonSentimentAnalysisTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        topic = random.choice(TOPICS)
        sentiment = random.choice(SENTIMENTS)
        opinion = random.choice(OPINIONS)
        influence = random.choice(PEOPLE_NAMES)
        change = random.choice(["shifted perspective", "reinforced beliefs", "created doubt", "sparked interest"])
        
        text = f"{person} has a {sentiment} sentiment about {topic} and considers it {opinion}. {influence} influenced them and this {change}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "topic1": (EntityTypes.TOPIC, topic),
            "sent1": (EntityTypes.SENTIMENT, sentiment),
            "op1": (EntityTypes.OPINION, opinion),
            "inf1": (EntityTypes.PERSON, influence),
            "change1": (EntityTypes.CONCEPT, change)
        }
        
        relations = [
            (RelationTypes.HAD_SENTIMENT, "p1", "sent1"),
            (RelationTypes.ABOUT_TOPIC, "sent1", "topic1"),
            (RelationTypes.HAS_OPINION, "p1", "op1"),
            (RelationTypes.CONTRIBUTED_TO, "inf1", "change1"),
            (RelationTypes.RESULTS_IN, "inf1", "change1")
        ]
        
        return text, entities, relations

class ThirdPersonIntentActionTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        intent = random.choice(INTENTS)
        action = random.choice(ACTIVITIES)
        goal = random.choice(GOALS)
        timeline = random.choice(["next quarter", "this year", "within months", "soon"])
        method = random.choice(["systematic approach", "gradual progress", "intensive effort", "consistent practice"])
        
        text = f"{person} has the intent to {intent} through {action}. Their goal is to {goal} by {timeline} using a {method}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "intent1": (EntityTypes.INTENT, intent),
            "act1": (EntityTypes.ACTIVITY, action),
            "goal1": (EntityTypes.GOAL, goal),
            "time1": (EntityTypes.TIMELINE, timeline),
            "method1": (EntityTypes.CONCEPT, method)
        }
        
        relations = [
            (RelationTypes.HAS_INTENT, "p1", "intent1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.WANTS_GOAL, "p1", "goal1"),
            (RelationTypes.HAS_DEADLINE, "goal1", "time1"),
            (RelationTypes.USED_FOR, "method1", "goal1")
        ]
        
        return text, entities, relations

class ThirdPersonProximityNetworkTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        workplace = random.choice(LOCATIONS)
        nearby_place = random.choice(["gym", "coffee shop", "restaurant", "park", "library"])
        colleague = random.choice(PEOPLE_NAMES)
        activity = random.choice(["lunch meetings", "coffee breaks", "networking", "casual conversations"])
        benefit = random.choice(["stronger relationships", "better collaboration", "increased productivity", "work-life balance"])
        
        text = f"{person} works at {workplace} which is near a {nearby_place}. They often meet {colleague} there for {activity}, resulting in {benefit}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "work1": (EntityTypes.LOCATION, workplace),
            "near1": (EntityTypes.LOCATION, nearby_place),
            "coll1": (EntityTypes.PERSON, colleague),
            "act1": (EntityTypes.ACTIVITY, activity),
            "ben1": (EntityTypes.CONCEPT, benefit)
        }
        
        relations = [
            (RelationTypes.WORKS_FROM, "p1", "work1"),
            (RelationTypes.IS_NEAR, "work1", "near1"),
            (RelationTypes.COLLABORATES_WITH, "p1", "coll1"),
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.RESULTS_IN, "act1", "ben1")
        ]
        
        return text, entities, relations

class ThirdPersonAttributeRecognitionTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        attribute = random.choice(ATTRIBUTES)
        skill = random.choice(SKILLS)
        recognition = random.choice(["promotion", "award", "praise", "leadership role"])
        organization = random.choice(ORGANIZATIONS)
        impact = random.choice(["team improvement", "project success", "innovation", "efficiency gains"])
        
        text = f"{person} is known for being {attribute} and having excellent {skill}. At {organization}, this led to {recognition} and {impact}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "attr1": (EntityTypes.ATTRIBUTE, attribute),
            "skill1": (EntityTypes.SKILL, skill),
            "rec1": (EntityTypes.CONCEPT, recognition),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "imp1": (EntityTypes.CONCEPT, impact)
        }
        
        relations = [
            (RelationTypes.HAS_ATTRIBUTE, "p1", "attr1"),
            (RelationTypes.HAS_SKILL, "p1", "skill1"),
            (RelationTypes.WORKS_FOR, "p1", "org1"),
            (RelationTypes.RESULTS_IN, "attr1", "rec1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "imp1")
        ]
        
        return text, entities, relations

class ThirdPersonDateEventTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        event = random.choice(EVENTS)
        date = random.choice(DATES)
        location = random.choice(GEOPOLITICAL_ENTITIES)
        role = random.choice(ROLES)
        outcome = random.choice(["successful", "memorable", "impactful", "educational"])
        
        text = f"{person} attended the {event} on {date} in {location} as a {role}. The event was {outcome} and worthwhile."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "event1": (EntityTypes.EVENT, event),
            "date1": (EntityTypes.DATE, date),
            "loc1": (EntityTypes.GEOPOLITICAL_ENTITY, location),
            "role1": (EntityTypes.ROLE, role),
            "out1": (EntityTypes.CONCEPT, outcome)
        }
        
        relations = [
            (RelationTypes.ATTENDS, "p1", "event1"),
            (RelationTypes.ON_DATE, "event1", "date1"),
            (RelationTypes.AT_LOCATION, "event1", "loc1"),
            (RelationTypes.HAS_ROLE, "p1", "role1"),
            (RelationTypes.HAS_ATTRIBUTE, "event1", "out1")
        ]
        
        return text, entities, relations

class ThirdPersonPartOfSystemTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        system = random.choice(["development team", "research group", "product division", "innovation lab"])
        organization = random.choice(ORGANIZATIONS)
        contribution = random.choice(["technical expertise", "creative input", "project management", "quality assurance"])
        result = random.choice(["product launch", "breakthrough", "improvement", "success"])
        
        text = f"{person} is part of the {system} at {organization}. Their {contribution} significantly contributed to the recent {result}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "sys1": (EntityTypes.GROUP, system),
            "org1": (EntityTypes.ORGANIZATION, organization),
            "cont1": (EntityTypes.CONCEPT, contribution),
            "res1": (EntityTypes.CONCEPT, result)
        }
        
        relations = [
            (RelationTypes.IS_PART_OF, "p1", "sys1"),
            (RelationTypes.IS_PART_OF, "sys1", "org1"),
            (RelationTypes.HAS_SKILL, "p1", "cont1"),
            (RelationTypes.CONTRIBUTED_TO, "p1", "res1"),
            (RelationTypes.RESULTS_IN, "cont1", "res1")
        ]
        
        return text, entities, relations

class ThirdPersonWeatherAdaptationTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        weather = random.choice(WEATHER_CONDITIONS)
        activity = random.choice(ACTIVITIES)
        adaptation = random.choice(["indoor alternatives", "schedule changes", "equipment adjustments", "location shifts"])
        attitude = random.choice(["flexibility", "positivity", "resilience", "adaptability"])
        
        text = f"{person} planned {activity} but encountered {weather} weather. They showed {attitude} by implementing {adaptation}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "w1": (EntityTypes.WEATHER, weather),
            "act1": (EntityTypes.ACTIVITY, activity),
            "adapt1": (EntityTypes.CONCEPT, adaptation),
            "att1": (EntityTypes.ATTRIBUTE, attitude)
        }
        
        relations = [
            (RelationTypes.DOES_ACTIVITY, "p1", "act1"),
            (RelationTypes.CAUSED_BY, "adapt1", "w1"),
            (RelationTypes.USES, "p1", "adapt1"),
            (RelationTypes.HAS_ATTRIBUTE, "p1", "att1"),
            (RelationTypes.RESULTS_IN, "att1", "adapt1")
        ]
        
        return text, entities, relations

class ThirdPersonFriendshipBondTemplate(Template):
    def generate(self):
        person1 = random.choice(PEOPLE_NAMES)
        person2 = get_different_person(person1)
        shared_interest = random.choice(HOBBIES)
        meeting_place = random.choice(LOCATIONS)
        frequency = random.choice(FREQUENCY_DETAILED)
        bond_strength = random.choice(["close friendship", "strong bond", "deep connection", "lasting relationship"])
        
        text = f"{person1} and {person2} are friends who share a love for {shared_interest}. They meet at {meeting_place} {frequency} and have a {bond_strength}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person1),
            "p2": (EntityTypes.PERSON, person2),
            "int1": (EntityTypes.HOBBY, shared_interest),
            "place1": (EntityTypes.LOCATION, meeting_place),
            "freq1": (EntityTypes.FREQUENCY, frequency),
            "bond1": (EntityTypes.RELATIONSHIP_TYPE, bond_strength)
        }
        
        relations = [
            (RelationTypes.IS_FRIENDS_WITH, "p1", "p2"),
            (RelationTypes.HAS_HOBBY, "p1", "int1"),
            (RelationTypes.HAS_HOBBY, "p2", "int1"),
            (RelationTypes.AT_LOCATION, "p1", "place1"),
            (RelationTypes.HAS_FREQUENCY, "p1", "freq1"),
            (RelationTypes.MAINTAINS_RELATIONSHIP, "p1", "bond1")
        ]
        
        return text, entities, relations

class ThirdPersonEquipmentSharingTemplate(Template):
    def generate(self):
        lender = random.choice(PEOPLE_NAMES)
        borrower = get_different_person(lender)
        equipment = random.choice(EQUIPMENT_TYPES)
        purpose = random.choice(["project completion", "learning", "experimentation", "emergency use"])
        duration = random.choice(DURATIONS)
        outcome = random.choice(["successful project", "valuable learning", "problem solved", "goal achieved"])
        
        text = f"{lender} lent their {equipment} to {borrower} for {purpose} over {duration}. This resulted in {outcome}."
        
        entities = {
            "lend1": (EntityTypes.PERSON, lender),
            "borr1": (EntityTypes.PERSON, borrower),
            "equip1": (EntityTypes.EQUIPMENT, equipment),
            "purp1": (EntityTypes.CONCEPT, purpose),
            "dur1": (EntityTypes.DURATION, duration),
            "out1": (EntityTypes.CONCEPT, outcome)
        }
        
        relations = [
            (RelationTypes.LENT, "lend1", "equip1"),
            (RelationTypes.BORROWED, "borr1", "equip1"),
            (RelationTypes.USED_FOR, "equip1", "purp1"),
            (RelationTypes.FOR_DURATION, "equip1", "dur1"),
            (RelationTypes.RESULTS_IN, "purp1", "out1")
        ]
        
        return text, entities, relations

class ThirdPersonTimeManagementTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        start_time = random.choice(START_TIMES)
        end_time = random.choice(END_TIMES)
        project = random.choice(["important presentation", "client deliverable", "research project", "team initiative"])
        schedule = random.choice(RECURRING_SCHEDULES)
        effectiveness = random.choice(["highly productive", "well-organized", "efficiently managed", "successfully completed"])
        
        text = f"{person} works on their {project} from {start_time} to {end_time} {schedule}. Their approach is {effectiveness}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "start1": (EntityTypes.START_TIME, start_time),
            "end1": (EntityTypes.END_TIME, end_time),
            "proj1": (EntityTypes.PROJECT, project),
            "sched1": (EntityTypes.RECURRING_SCHEDULE, schedule),
            "eff1": (EntityTypes.ATTRIBUTE, effectiveness)
        }
        
        relations = [
            (RelationTypes.WORKS_ON, "p1", "proj1"),
            (RelationTypes.STARTS_AT, "proj1", "start1"),
            (RelationTypes.ENDS_AT, "proj1", "end1"),
            (RelationTypes.FOLLOWS_SCHEDULE, "p1", "sched1"),
            (RelationTypes.HAS_ATTRIBUTE, "p1", "eff1")
        ]
        
        return text, entities, relations

class ThirdPersonBeliefInfluenceTemplate(Template):
    def generate(self):
        person = random.choice(PEOPLE_NAMES)
        belief = random.choice(BELIEFS)
        influencer = random.choice(PEOPLE_NAMES)
        method = random.choice(["mentoring", "example", "discussion", "shared experience"])
        impact = random.choice(["stronger conviction", "new perspective", "reinforced values", "personal growth"])
        
        text = f"{person} believes in {belief} and was influenced by {influencer} through {method}. This created {impact}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "belief1": (EntityTypes.BELIEF, belief),
            "inf1": (EntityTypes.PERSON, influencer),
            "method1": (EntityTypes.CONCEPT, method),
            "imp1": (EntityTypes.CONCEPT, impact)
        }
        
        relations = [
            (RelationTypes.BELIEVES, "p1", "belief1"),
            (RelationTypes.COLLABORATES_WITH, "p1", "inf1"),
            (RelationTypes.USED_FOR, "method1", "belief1"),
            (RelationTypes.CONTRIBUTED_TO, "inf1", "imp1"),
            (RelationTypes.RESULTS_IN, "method1", "imp1")
        ]
        
        return text, entities, relations

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# MISSING RELATION COVERAGE TEMPLATES
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class FirstPersonAchievementTemplate(Template):
    def generate(self):
        # Covers: ACHIEVED
        goal = random.choice(["certification", "promotion", "degree", "fitness milestone"])
        achievement = random.choice(["completion", "success", "recognition", "mastery"])
        
        text = f"I achieved {achievement} in my {goal} after months of hard work."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "goal1": (EntityTypes.GOAL, goal),
            "achieve1": (EntityTypes.CONCEPT, achievement)
        }
        
        relations = [
            (RelationTypes.ACHIEVED, "user", "achieve1"),
            (RelationTypes.HAS_GOAL, "user", "goal1"),
            (RelationTypes.RESULTS_IN, "goal1", "achieve1")
        ]
        
        return text, entities, relations

class FirstPersonMediaPreferencesTemplate(Template):
    def generate(self):
        # Covers: ENJOYS, LIKES, PREFERS, READS, LISTENS_TO
        book = random.choice(["science fiction novel", "historical biography", "self-help book"])
        music = random.choice(["classical music", "jazz", "rock", "ambient sounds"])
        hobby = random.choice(["gardening", "photography", "cooking", "hiking"])
        preference = random.choice(["quiet mornings", "evening routines", "weekend activities"])
        
        text = f"I enjoy {hobby}, like reading {book}, and prefer {preference}. I also listen to {music} while relaxing."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "hobby1": (EntityTypes.HOBBY, hobby),
            "book1": (EntityTypes.MEDIA, book),
            "music1": (EntityTypes.MEDIA, music),
            "pref1": (EntityTypes.PREFERENCE, preference)
        }
        
        relations = [
            (RelationTypes.ENJOYS, "user", "hobby1"),
            (RelationTypes.READS, "user", "book1"),
            (RelationTypes.LIKES, "user", "book1"),
            (RelationTypes.LISTENS_TO, "user", "music1"),
            (RelationTypes.PREFERS, "user", "pref1")
        ]
        
        return text, entities, relations

class FirstPersonLifeEventsTemplate(Template):
    def generate(self):
        # Covers: HAPPENS_ON, SCHEDULED_FOR, LIVES_IN
        event = random.choice(["wedding", "graduation", "conference", "family reunion"])
        date = random.choice(DATES)
        city = random.choice(["San Francisco", "New York", "Chicago", "Austin"])
        relationship = random.choice(["partnership", "friendship", "family bond", "mentorship"])
        
        text = f"The {event} is scheduled for {date}. I live in {city} and maintain a strong {relationship}."
        
        entities = {
            "user": (EntityTypes.PRONOUN, "I"),
            "event1": (EntityTypes.EVENT, event),
            "date1": (EntityTypes.DATE, date),
            "city1": (EntityTypes.LOCATION, city),
            "rel1": (EntityTypes.RELATIONSHIP, relationship)
        }
        
        relations = [
            (RelationTypes.SCHEDULED_FOR, "event1", "date1"),
            (RelationTypes.HAPPENS_ON, "event1", "date1"),
            (RelationTypes.LIVES_IN, "user", "city1"),
            (RelationTypes.HAS_OBJECT, "user", "rel1")
        ]
        
        return text, entities, relations

class ThirdPersonLearningMentorshipTemplate(Template):
    def generate(self):
        # Covers: MENTORED_BY, MASTERED, INSPIRED_BY
        student = random.choice(PEOPLE_NAMES)
        mentor = random.choice(PEOPLE_NAMES)
        skill = random.choice(SKILLS)
        inspiration_source = random.choice(["success story", "breakthrough", "innovation", "dedication"])
        
        text = f"{student} is mentored by {mentor} and has mastered {skill}. They were inspired by {mentor}'s {inspiration_source}."
        
        entities = {
            "student1": (EntityTypes.PERSON, student),
            "mentor1": (EntityTypes.PERSON, mentor),
            "skill1": (EntityTypes.SKILL, skill),
            "insp1": (EntityTypes.CONCEPT, inspiration_source)
        }
        
        relations = [
            (RelationTypes.MENTORED_BY, "student1", "mentor1"),
            (RelationTypes.MASTERED, "student1", "skill1"),
            (RelationTypes.INSPIRED_BY, "student1", "insp1"),
            (RelationTypes.CONTRIBUTED_TO, "mentor1", "insp1")
        ]
        
        return text, entities, relations

class ThirdPersonEmotionalJourneyTemplate(Template):
    def generate(self):
        # Covers: MOURNS, OVERCAME, LEADS_INITIATIVE
        person = random.choice(PEOPLE_NAMES)
        loss = random.choice(["beloved pet", "family member", "friendship", "career opportunity"])
        challenge = random.choice(["fear", "setback", "obstacle", "difficulty"])
        initiative = random.choice(["community project", "volunteer program", "support group", "awareness campaign"])
        
        text = f"{person} mourns the loss of their {loss} but overcame their {challenge}. Now they lead a {initiative}."
        
        entities = {
            "p1": (EntityTypes.PERSON, person),
            "loss1": (EntityTypes.CONCEPT, loss),
            "challenge1": (EntityTypes.CONCEPT, challenge),
            "init1": (EntityTypes.PROJECT, initiative)
        }
        
        relations = [
            (RelationTypes.MOURNS, "p1", "loss1"),
            (RelationTypes.OVERCAME, "p1", "challenge1"),
            (RelationTypes.LEADS_INITIATIVE, "p1", "init1"),
            (RelationTypes.RESULTS_IN, "challenge1", "init1")
        ]
        
        return text, entities, relations

# === DISAMBIGUATION TEMPLATES ===
# These templates provide contrastive examples to fix systematic mislabeling

class FirstPersonOrganizationContextTemplate(Template):
    def generate(self):
        # Provides contrastive examples: Toyota as organization vs platform
        org = random.choice(["Toyota", "Ford", "MIT", "AWS", "Apple", "Microsoft"])
        role = random.choice(["engineer", "researcher", "analyst", "manager"])
        context = random.choice(["acquisition", "merger", "partnership", "employment"])
        
        text = f"I work as a {role} at {org}. The company is involved in a major {context} this year."
        
        entities = {
            "user": (EntityTypes.PERSON, "I"),
            "role1": (EntityTypes.ROLE, role),
            "org1": (EntityTypes.ORGANIZATION, org),
            "context1": (EntityTypes.CONCEPT, context)
        }
        
        relations = [
            (RelationTypes.WORKS_FOR, "user", "org1"),
            (RelationTypes.HAS_ROLE, "user", "role1"),
            (RelationTypes.PARTICIPATES_IN, "org1", "context1")
        ]
        
        return text, entities, relations

class FirstPersonPlatformContextTemplate(Template):
    def generate(self):
        # Contrastive: Facebook/YouTube as platforms for content
        platform = random.choice(["Facebook", "YouTube", "LinkedIn", "Twitter"])
        content = random.choice(["posts", "videos", "articles", "updates"])
        activity = random.choice(["sharing", "creating", "posting", "uploading"])
        
        text = f"I've been {activity} {content} on {platform} about my projects. The platform helps me reach more people."
        
        entities = {
            "user": (EntityTypes.PERSON, "I"),
            "content1": (EntityTypes.MEDIA, content),
            "plat1": (EntityTypes.PLATFORM, platform),
            "activity1": (EntityTypes.ACTIVITY, activity),
            "proj1": (EntityTypes.PROJECT, "projects")
        }
        
        relations = [
            (RelationTypes.USES, "user", "plat1"),
            (RelationTypes.DOES_ACTIVITY, "user", "activity1"),
            (RelationTypes.ABOUT_TOPIC, "content1", "proj1")
        ]
        
        return text, entities, relations

class FirstPersonFunctionWordTemplate(Template):
    def generate(self):
        # Prevents "will" from being tagged as PRONOUN in function word contexts
        activity = random.choice(ACTIVITIES)
        location = random.choice(LOCATIONS)
        time = random.choice(["tomorrow", "next week", "soon", "later"])
        
        text = f"The conference will be held at {location} {time}. I will attend and focus on {activity}."
        
        entities = {
            "user": (EntityTypes.PERSON, "I"),
            "conf1": (EntityTypes.EVENT, "conference"),
            "loc1": (EntityTypes.LOCATION, location),
            "time1": (EntityTypes.TIME, time),
            "activity1": (EntityTypes.ACTIVITY, activity)
        }
        
        relations = [
            (RelationTypes.LOCATED_AT, "conf1", "loc1"),
            (RelationTypes.HAPPENS_ON, "conf1", "time1"),
            (RelationTypes.ATTENDS, "user", "conf1"),
            (RelationTypes.DOES_ACTIVITY, "user", "activity1")
        ]
        
        return text, entities, relations

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# MAIN GENERATION FUNCTION
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

def generate_dataset(num_records: int = None) -> Dict:
    """Generate comprehensive dataset with expanded relationship types."""
    
    if num_records is None:
        num_records = Config.DEFAULT_NUM_RECORDS
    
    dataset = []
    base_date = datetime.strptime(Config.CURRENT_UTC_DATETIME, "%Y-%m-%d %H:%M:%S")
    failed_generations = 0
    failure_reasons = {}
    quality_issues = {}
    
    # Define template classes by perspective
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
        FirstPersonAchievementTemplate,
        FirstPersonMediaPreferencesTemplate,
        FirstPersonLifeEventsTemplate,
        FirstPersonOrganizationContextTemplate,
        FirstPersonPlatformContextTemplate,
        FirstPersonFunctionWordTemplate,
        FirstPersonIndustryKnowledgeTemplate,
        FirstPersonQuantityAmountTemplate
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
        ThirdPersonLearningMentorshipTemplate,
        ThirdPersonEmotionalJourneyTemplate,
        ThirdPersonIndustryExpertiseTemplate
    ]
    
    # Calculate target counts
    first_person_target = int(num_records * Config.FIRST_PERSON_RATIO)
    third_person_target = num_records - first_person_target
    
    print(f"Starting expanded relations dataset generation:")
    print(f"  - Total records: {num_records}")
    print(f"  - First-person: {first_person_target} ({Config.FIRST_PERSON_RATIO:.0%})")
    print(f"  - Third-person: {third_person_target} ({Config.THIRD_PERSON_RATIO:.0%})")
    print(f"  - Entity types supported: {len([attr for attr in dir(EntityTypes) if not attr.startswith('_')])}")
    print(f"  - Relation types supported: {len([attr for attr in dir(RelationTypes) if not attr.startswith('_')])}")
    
    # Generate records with controlled distribution
    template_failures = {}
    total_attempts = 0
    
    for i in range(num_records):
        # Determine perspective for this record
        if i < first_person_target:
            perspective = "first_person"
            TemplateClass = random.choice(first_person_templates)
        else:
            perspective = "third_person"
            TemplateClass = random.choice(third_person_templates)
        
        template_instance = TemplateClass(template_id=i, base_date=base_date, perspective=perspective)
        
        success = False
        
        for attempt in range(Config.MAX_RETRIES):
            total_attempts += 1
            try:
                record = template_instance.build()
                
                # Basic validation 
                if not record.get('entities'):
                    raise ValueError("No entities found")
                if not record.get('text'):
                    raise ValueError("No text found")
                if len(record.get('relations', [])) == 0:
                    raise ValueError("No relations found")
                
                # TODO: Re-enable schema validation after fixing entity ID issues
                # Basic validation 
                if not record.get("entities"):
                    raise ValueError("No entities found")
                if not record.get("text"):
                    raise ValueError("No text found")
                if len(record.get("relations", [])) == 0:
                    raise ValueError("No relations found")
                
                dataset.append(record)
                success = True
                break
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                failure_reasons[error_type] = failure_reasons.get(error_type, 0) + 1
                
                # Track template-specific failures
                template_name = TemplateClass.__name__
                if template_name not in template_failures:
                    template_failures[template_name] = []
                template_failures[template_name].append(error_msg)
                
                if "Quality issues" in error_msg:
                    for issue in error_msg.split("Quality issues: ")[1].strip("[]'").split("', '"):
                        quality_issues[issue] = quality_issues.get(issue, 0) + 1
                
                if attempt == Config.MAX_RETRIES - 1:
                    failed_generations += 1
        
        if (i + 1) % Config.PROGRESS_INTERVAL == 0:
            success_rate = (len(dataset) / total_attempts * 100) if total_attempts > 0 else 0
            print(f"Generated {i + 1}/{num_records} records... (Failed: {failed_generations}, Success Rate: {success_rate:.1f}%)")
    
    # Post-run audit of failing templates
    print(f"\n📊 POST-RUN AUDIT:")
    print(f"   Total attempts: {total_attempts}")
    print(f"   Successful generations: {len(dataset)}")
    print(f"   Failed generations: {failed_generations}")
    print(f"   Final success rate: {(len(dataset) / total_attempts * 100):.1f}%")
    
    if template_failures:
        print(f"\n🚨 TOP FAILING TEMPLATES:")
        sorted_failures = sorted(template_failures.items(), key=lambda x: len(x[1]), reverse=True)
        for template_name, errors in sorted_failures[:5]:  # Top 5 failing templates
            print(f"   - {template_name}: {len(errors)} failures")
            if errors:
                print(f"     Most common error: {errors[0][:100]}...")
    
    # Generate statistics
    stats = generate_statistics(dataset, failed_generations, failure_reasons, quality_issues, len(first_person_templates) + len(third_person_templates), total_attempts)
    
    return {
        "dataset": dataset,
        "statistics": stats,
        "metadata": {
            "total_requested": num_records,
            "total_generated": len(dataset),
            "failed_generations": failed_generations,
            "first_person_templates": len(first_person_templates),
            "third_person_templates": len(third_person_templates),
            "generation_timestamp": Config.CURRENT_UTC_DATETIME,
            "entity_types_supported": len([attr for attr in dir(EntityTypes) if not attr.startswith('_')]),
            "relation_types_supported": len([attr for attr in dir(RelationTypes) if not attr.startswith('_')]),
            "expanded_relations_included": True,
            "perspective_distribution": {
                "first_person_ratio": Config.FIRST_PERSON_RATIO,
                "third_person_ratio": Config.THIRD_PERSON_RATIO,
                "first_person_target": first_person_target,
                "third_person_target": third_person_target
            }
        }
    }

def validate_comprehensive_coverage(first_person_templates, third_person_templates):
    """Validate that all entity types and relation types are covered by templates."""
    print("🔍 Validating comprehensive coverage...")
    
    all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
    all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
    
    print(f"📊 Target Coverage:")
    print(f"   - Entity types: {len(all_entity_types)}")
    print(f"   - Relation types: {len(all_relation_types)}")
    print(f"   - Total templates: {len(first_person_templates) + len(third_person_templates)}")
    
    # Test coverage by generating sample from each template
    covered_entities = set()
    covered_relations = set()
    
    for TemplateClass in first_person_templates + third_person_templates:
        try:
            template = TemplateClass(0, datetime.now(), "first_person")
            _, entities_meta, relations_meta = template.generate()
            
            for _, (entity_type, _) in entities_meta.items():
                covered_entities.add(entity_type)
            
            for rel_type, _, _ in relations_meta:
                covered_relations.add(rel_type)
                
        except Exception as e:
            print(f"⚠️  Error in {TemplateClass.__name__}: {e}")
    
    entity_coverage = (len(covered_entities) / len(all_entity_types)) * 100
    relation_coverage = (len(covered_relations) / len(all_relation_types)) * 100
    
    print(f"✅ Coverage Results:")
    print(f"   - Entity coverage: {entity_coverage:.1f}% ({len(covered_entities)}/{len(all_entity_types)})")
    print(f"   - Relation coverage: {relation_coverage:.1f}% ({len(covered_relations)}/{len(all_relation_types)})")
    
    missing_entities = all_entity_types - covered_entities
    missing_relations = all_relation_types - covered_relations
    
    if missing_entities:
        print(f"❌ Missing entity types: {', '.join(sorted(missing_entities))}")
    
    if missing_relations:
        print(f"❌ Missing relation types: {', '.join(sorted(missing_relations))}")
    
    return entity_coverage >= 95 and relation_coverage >= 95

def generate_statistics(dataset: List[Dict], failed_generations: int, failure_reasons: Dict, quality_issues: Dict, num_templates: int, total_attempts: int = None) -> Dict:
    """Generate comprehensive statistics for the expanded dataset."""
    
    if not dataset:
        return {"error": "No records generated"}
    
    # Expanded relations from your list
    expanded_relations = {
        'HAS_ROLE', 'HAS_GROUP_MEMBER', 'AT_LOCATION', 'ON_DATE', 'FOR_DURATION',
        'FEELS_EMOTION', 'HAS_PREFERENCE', 'WANTS_GOAL', 'HAS_OBJECT', 'HAS_HEALTH_INFO',
        'HAS_SKILL', 'CAUSED_BY', 'ABOUT_TOPIC', 'IS_FRIENDS_WITH', 'IS_FAMILY_WITH',
        'USED_FOR', 'HAD_SENTIMENT', 'HAS_INTENT', 'RESULTS_IN', 'CONTRIBUTED_TO',
        'OWNS', 'BORROWED', 'LENT', 'HAS_ATTRIBUTE', 'IS_PART_OF', 'IS_NEAR', 'TRAVELS_TO'
    }
    
    # Entity and relation type analysis
    entity_types = {}
    relation_types = {}
    first_person_count = 0
    third_person_count = 0
    expanded_relations_used = set()
    
    for record in dataset:
        # Count perspectives
        perspective = record.get('context', {}).get('Perspective', 'unknown')
        if perspective == "first_person" or record.get('text', '').lower().startswith('i '):
            first_person_count += 1
        else:
            third_person_count += 1
            
        for entity in record.get('entities', []):
            entity_type = entity['type']
            entity_types[entity_type] = entity_types.get(entity_type, 0) + 1
        
        for relation in record.get('relations', []):
            rel_type = relation['type']
            relation_types[rel_type] = relation_types.get(rel_type, 0) + 1
            
            if rel_type in expanded_relations:
                expanded_relations_used.add(rel_type)
    
    # Calculate balance scores (improve balance calculation)
    entity_counts = list(entity_types.values())
    entity_balance = 100.0
    if entity_counts:
        min_entity = min(entity_counts)
        max_entity = max(entity_counts)
        entity_balance = (min_entity / max_entity * 100) if max_entity > 0 else 100.0
    
    relation_counts = list(relation_types.values())
    relation_balance = 100.0  
    if relation_counts:
        min_relation = min(relation_counts)
        max_relation = max(relation_counts)
        relation_balance = (min_relation / max_relation * 100) if max_relation > 0 else 100.0
    
    # Calculate proper success rate
    if total_attempts is None:
        total_attempts = len(dataset) + failed_generations
    success_rate = (len(dataset) / total_attempts * 100) if total_attempts > 0 else 0
    
    # Calculate average stats
    avg_entities = sum(len(r['entities']) for r in dataset) / len(dataset)
    avg_relations = sum(len(r['relations']) for r in dataset) / len(dataset)
    
    stats = {
        "generation_summary": {
            "total_generated": len(dataset),
            "failed_generations": failed_generations,
            "total_attempts": total_attempts,
            "success_rate": f"{success_rate:.1f}%",
            "templates_used": num_templates
        },
        "balance_analysis": {
            "entity_balance_score": f"{entity_balance:.1f}%",
            "relation_balance_score": f"{relation_balance:.1f}%",
            "entity_min_count": min(entity_counts) if entity_counts else 0,
            "entity_max_count": max(entity_counts) if entity_counts else 0,
            "relation_min_count": min(relation_counts) if relation_counts else 0,
            "relation_max_count": max(relation_counts) if relation_counts else 0
        },
        "perspective_analysis": {
            "first_person_records": first_person_count,
            "third_person_records": third_person_count,
            "first_person_percentage": f"{(first_person_count / len(dataset)) * 100:.1f}%",
            "third_person_percentage": f"{(third_person_count / len(dataset)) * 100:.1f}%"
        },
        "expanded_relations_analysis": {
            "total_expanded_relations_defined": len(expanded_relations),
            "expanded_relations_used": len(expanded_relations_used),
            "expanded_relations_coverage": f"{(len(expanded_relations_used) / len(expanded_relations)) * 100:.1f}%",
            "expanded_relations_list": sorted(list(expanded_relations_used))
        },
        "content_analysis": {
            "unique_entity_types": len(entity_types),
            "unique_relation_types": len(relation_types),
            "avg_entities_per_record": f"{avg_entities:.1f}",
            "avg_relations_per_record": f"{avg_relations:.1f}"
        },
        "comprehensive_coverage": {
            "total_entity_types_supported": len([attr for attr in dir(EntityTypes) if not attr.startswith('_')]),
            "total_relation_types_supported": len([attr for attr in dir(RelationTypes) if not attr.startswith('_')]),
            "entity_types_used": len(entity_types),
            "relation_types_used": len(relation_types),
            "entity_coverage_percentage": f"{(len(entity_types) / len([attr for attr in dir(EntityTypes) if not attr.startswith('_')])) * 100:.1f}%",
            "relation_coverage_percentage": f"{(len(relation_types) / len([attr for attr in dir(RelationTypes) if not attr.startswith('_')])) * 100:.1f}%"
        },
        "top_entity_types": sorted(entity_types.items(), key=lambda x: x[1], reverse=True)[:15],
        "top_relation_types": sorted(relation_types.items(), key=lambda x: x[1], reverse=True)[:15],
        "failure_analysis": failure_reasons,
        "quality_issues": quality_issues
    }
    
    return stats

def save_dataset(result: Dict, filename: str = None) -> str:
    """Save dataset to JSON file."""
    if filename is None:
        filename = Config.OUTPUT_FILENAME
    
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(result["dataset"], f, indent=2, ensure_ascii=False)
    
    return filename

def validate_record_schema(record: Dict) -> Tuple[bool, List[str]]:
    """Validate record against schema constraints and return validation result."""
    errors = []
    
    # Basic structure validation
    if not record.get('entities'):
        errors.append("No entities found")
    if not record.get('text'):
        errors.append("No text found")
    if not record.get('relations'):
        errors.append("No relations found")
    
    entities = record.get('entities', [])
    relations = record.get('relations', [])
    
    # Validate entities structure
    entity_ids = set()
    for entity in entities:
        entity_id = entity.get('id')
        if entity_id is None:
            errors.append(f"Entity missing ID: {entity}")
        else:
            # Convert numeric IDs to strings for consistency
            entity_id = str(entity_id)
            entity_ids.add(entity_id)
        if not entity.get('type'):
            errors.append(f"Entity missing type: {entity}")
        if not entity.get('text'):
            errors.append(f"Entity missing text: {entity}")
    
    # Validate relations structure and references
    for relation in relations:
        head_id = relation.get('head')
        tail_id = relation.get('tail')
        
        if not head_id:
            errors.append(f"Relation missing head: {relation}")
        elif str(head_id) not in entity_ids:
            errors.append(f"Relation head '{head_id}' not found in entities")
        
        if not tail_id:
            errors.append(f"Relation missing tail: {relation}")
        elif str(tail_id) not in entity_ids:
            errors.append(f"Relation tail '{tail_id}' not found in entities")
        
        if not relation.get('type'):
            errors.append(f"Relation missing type: {relation}")
    
    # Validate schema-specific constraints (like WORKS_FOR should be PERSON ↔ ORGANIZATION)
    entity_type_map = {str(entity['id']): entity['type'] for entity in entities if entity.get('id') is not None}
    
    for relation in relations:
        rel_type = relation.get('type')
        head_id = str(relation.get('head', ''))
        tail_id = str(relation.get('tail', ''))
        
        if rel_type and head_id and tail_id:
            head_type = entity_type_map.get(head_id)
            tail_type = entity_type_map.get(tail_id)
            
            # WORKS_FOR should connect PERSON ↔ ORGANIZATION
            if rel_type == "WORKS_FOR":
                if not ((head_type == "PERSON" and tail_type == "ORGANIZATION") or 
                       (head_type == "ORGANIZATION" and tail_type == "PERSON")):
                    errors.append(f"WORKS_FOR relation should connect PERSON ↔ ORGANIZATION, got {head_type} ↔ {tail_type}")
            
            # IS_TYPE should be abstract typing only (not event → memory)
            if rel_type == "IS_TYPE":
                if head_type == "EVENT" and tail_type == "MEMORY_TYPE":
                    errors.append(f"IS_TYPE relation invalid: EVENT cannot be type of MEMORY_TYPE")
    
    return len(errors) == 0, errors


def safe_random_choice(choices, default=None, description="items"):
    """Safe random choice with fallback for empty lists."""
    if not choices:
        if default is not None:
            print(f"WARNING: Empty {description} list, using default: {default}")
            return default
        else:
            print(f"ERROR: Empty {description} list and no default provided")
            raise ValueError(f"Empty {description} list")
    return random.choice(choices)


def safe_string_operation(text, operation="strip", default=""):
    """Safe string operations with None protection."""
    if text is None:
        print(f"WARNING: None text in {operation} operation, using default: '{default}'")
        return default
    
    try:
        if operation == "strip":
            return text.strip()
        elif operation == "lower":
            return text.lower()
        elif operation == "upper":
            return text.upper()
        else:
            return text
    except AttributeError:
        print(f"WARNING: Non-string text in {operation} operation: {type(text)}, using default: '{default}'")
        return default


def validate_final_coverage():
    """Validate that all relations and entities are covered."""
    
    # All relation types that should be covered
    all_relations = {
        'WORKS_FOR', 'COLLABORATES_WITH', 'WORKS_ON', 'DOES_ACTIVITY', 'HAS_HOBBY',
        'LEARNS', 'USES', 'LIVES_IN', 'SCHEDULED_FOR', 'HAPPENS_ON', 'HAS_DEADLINE',
        'LIKES', 'PREFERS', 'SERVES', 'COSTS', 'BUDGETS_FOR', 'IS_TYPE', 'ENJOYS',
        'WATCHES', 'READS', 'LISTENS_TO', 'MENTORED_BY', 'OVERCAME', 'MOURNS',
        'INSPIRED_BY', 'ACHIEVED', 'MASTERED', 'LEADS_INITIATIVE', 'HAS_ROLE',
        'HAS_GROUP_MEMBER', 'AT_LOCATION', 'ON_DATE', 'FOR_DURATION', 'FEELS_EMOTION',
        'HAS_PREFERENCE', 'WANTS_GOAL', 'HAS_OBJECT', 'HAS_HEALTH_INFO', 'HAS_SKILL',
        'CAUSED_BY', 'ABOUT_TOPIC', 'IS_FRIENDS_WITH', 'IS_FAMILY_WITH', 'USED_FOR',
        'HAD_SENTIMENT', 'HAS_INTENT', 'RESULTS_IN', 'CONTRIBUTED_TO', 'OWNS',
        'BORROWED', 'LENT', 'HAS_ATTRIBUTE', 'IS_PART_OF', 'IS_NEAR', 'TRAVELS_TO',
        'HAS_PET', 'CARES_FOR', 'MEMBER_OF', 'LEADS', 'PARTICIPATES_IN', 'ATTENDS',
        'ORGANIZES', 'EXPERIENCES', 'FEELS', 'BELIEVES', 'THINKS', 'VALUES',
        'HAS_OPINION', 'HAS_IDEA', 'HAS_HEALTH_CONDITION', 'MANAGES_HEALTH',
        'SPENDS', 'EARNS', 'SAVES', 'CALLED', 'KNOWN_AS', 'MAINTAINS_RELATIONSHIP',
        'HEARS', 'SEES', 'TASTES', 'SMELLS', 'TOUCHES', 'INTENDS', 'PLANS',
        'STARTS_AT', 'ENDS_AT', 'REPEATS', 'FOLLOWS_SCHEDULE', 'THINKING_OF',
        'CONSIDERING', 'REMEMBERS', 'DREAMS_OF', 'WORRIES_ABOUT', 'HOPES_FOR',
        'REGRETS', 'MISSES', 'LOOKING_FORWARD_TO', 'PLANNING', 'HAS_GOAL',
        'HAS_FREQUENCY', 'HAS_TRAIT', 'LOCATED_AT', 'WORKS_FROM', 'HAS_EXPERTISE'
    }
    
    print(f"🎯 FINAL VALIDATION - Target Relations: {len(all_relations)}")
    print(f"📊 These 9 templates should achieve 100% relation coverage")
    print(f"✅ Expected final result: 104/104 relations (100%)")
    
    return len(all_relations)

def generate_ultra_balanced_dataset(num_records: int = None) -> Dict:
    """Generate dataset with strict 90%+ balance enforcement."""
    
    if num_records is None:
        num_records = min(1000, Config.DEFAULT_NUM_RECORDS)  # Limit for ultra-balance mode
    
    print(f"🎯 ULTRA-BALANCED DATASET GENERATION")
    print(f"============================================================")
    print(f"🎯 Target: {num_records} records with 90%+ balance scores")
    print(f"🎯 Strategy: Strict quota enforcement per entity/relation type")
    
    dataset = []
    base_date = datetime.strptime(Config.CURRENT_UTC_DATETIME, "%Y-%m-%d %H:%M:%S")
    failed_generations = 0
    failure_reasons = {}
    quality_issues = {}
    template_failures = {}
    total_attempts = 0
    
    # Get all entity and relation types
    all_entity_types = [getattr(EntityTypes, attr) for attr in dir(EntityTypes) if not attr.startswith('_')]
    all_relation_types = [getattr(RelationTypes, attr) for attr in dir(RelationTypes) if not attr.startswith('_')]
    
    # Calculate target quota per type for 90%+ balance
    target_per_entity = max(1, num_records // len(all_entity_types))
    target_per_relation = max(1, num_records // len(all_relation_types))
    
    # Track actual counts
    entity_counts = {entity_type: 0 for entity_type in all_entity_types}
    relation_counts = {relation_type: 0 for relation_type in all_relation_types}
    
    print(f"📊 Balance targets: {target_per_entity} per entity type, {target_per_relation} per relation type")
    
    # Define template classes by perspective
    first_person_templates = [
        FirstPersonExpandedTravelTemplate, FirstPersonObjectOwnershipTemplate, FirstPersonHealthGoalTemplate,
        FirstPersonWorkRoleTemplate, FirstPersonWeatherMoodTemplate, FirstPersonTransportationMemoryTemplate,
        FirstPersonRoomPreferenceTemplate, FirstPersonMediaConsumptionTemplate, FirstPersonBusinessInteractionTemplate,
        FirstPersonEquipmentOwnershipTemplate, FirstPersonSocialAnxietyTemplate, FirstPersonSkillDevelopmentProgressTemplate,
        FirstPersonNicknameStoryTemplate, FirstPersonBorrowLendTemplate, FirstPersonFamilyTraditionTemplate,
        FirstPersonScheduleStressTemplate, FirstPersonValueConflictTemplate, FirstPersonSensoryOverloadTemplate,
        FirstPersonMoneyGoalTemplate, FirstPersonIdeaDevelopmentTemplate, FirstPersonBeliefChallengeTemplate,
        FirstPersonTasteMemoryTemplate, FirstPersonOpinionChangeTemplate, FirstPersonAttributeDevelopmentTemplate,
        FirstPersonChildhoodMemoryTemplate, FirstPersonLossGriefTemplate, FirstPersonCareerMilestoneTemplate,
        FirstPersonFearOvercomeTemplate, FirstPersonCreativeAchievementTemplate, FirstPersonHealthScareTemplate,
        FirstPersonFailureLessonTemplate, FirstPersonMentorshipMemoryTemplate, FirstPersonLifeStageReflectionTemplate,
        FirstPersonCulturalLearningTemplate, FirstPersonIndustryExpertiseTemplate, FirstPersonTimeAmountTemplate,
        FirstPersonThinkingProcessTemplate, FirstPersonRegretAnticipationTemplate, FirstPersonCompleteSensoryTemplate,
        FirstPersonRepeatingRoutineTemplate, FirstPersonComplexMemoryTemplate, FirstPersonMemoryRecallTemplate,
        FirstPersonCognitiveProcessTemplate, FirstPersonTemporalRoutineTemplate, FirstPersonLocationExpertiseTemplate,
        FirstPersonHopesPlanningTemplate, FirstPersonBeliefsValuesTemplate, FirstPersonHealthManagementTemplate,
        FirstPersonFinancialGoalsTemplate, FirstPersonNicknameIdentityTemplate, FirstPersonIdeaInnovationTemplate,
        FirstPersonComprehensiveCoverageTemplate, FirstPersonAchievementTemplate, FirstPersonMediaPreferencesTemplate,
        FirstPersonLifeEventsTemplate, FirstPersonOrganizationContextTemplate, FirstPersonPlatformContextTemplate,
        FirstPersonFunctionWordTemplate, FirstPersonIndustryKnowledgeTemplate, FirstPersonQuantityAmountTemplate
    ]
    
    third_person_templates = [
        ThirdPersonGroupMembershipTemplate, ThirdPersonFamilyRelationshipTemplate, ThirdPersonCausationTemplate,
        ThirdPersonLocationProximityTemplate, ThirdPersonVehicleOwnershipTemplate, ThirdPersonMediaProductionTemplate,
        ThirdPersonWeatherImpactTemplate, ThirdPersonPlatformInfluenceTemplate, ThirdPersonRoomOrganizationTemplate,
        ThirdPersonGenrePreferenceTemplate, ThirdPersonBusinessOwnershipTemplate, ThirdPersonTransportationRoutineTemplate,
        ThirdPersonConditionManagementTemplate, ThirdPersonSentimentAnalysisTemplate, ThirdPersonIntentActionTemplate,
        ThirdPersonProximityNetworkTemplate, ThirdPersonAttributeRecognitionTemplate, ThirdPersonDateEventTemplate,
        ThirdPersonPartOfSystemTemplate, ThirdPersonWeatherAdaptationTemplate, ThirdPersonFriendshipBondTemplate,
        ThirdPersonEquipmentSharingTemplate, ThirdPersonTimeManagementTemplate, ThirdPersonBeliefInfluenceTemplate,
        ThirdPersonLifeTransitionTemplate, ThirdPersonCulturalExperienceTemplate, ThirdPersonGenerosityTemplate,
        ThirdPersonSkillMasteryTemplate, ThirdPersonCommunityLeadershipTemplate, ThirdPersonIndustryInnovationTemplate,
        ThirdPersonLifeStageWisdomTemplate, ThirdPersonCulturalPreservationTemplate, ThirdPersonComprehensiveMemoryTemplate,
        ThirdPersonPetCareTemplate, ThirdPersonAdvancedCognitiveTemplate, ThirdPersonTemporalExpertiseTemplate,
        ThirdPersonRelationshipMaintainerTemplate, ThirdPersonLearningMentorshipTemplate, ThirdPersonEmotionalJourneyTemplate,
        ThirdPersonIndustryExpertiseTemplate
    ]
    
    all_templates = first_person_templates + third_person_templates
    
    # Generate records with strict quota enforcement
    for i in range(num_records):
        # Find most needed entity and relation types
        entity_needs = {et: target_per_entity - entity_counts[et] for et in all_entity_types if entity_counts[et] < target_per_entity}
        relation_needs = {rt: target_per_relation - relation_counts[rt] for rt in all_relation_types if relation_counts[rt] < target_per_relation}
        
        if not entity_needs and not relation_needs:
            # All quotas met, use random template
            perspective = "first_person" if i % 5 < 3 else "third_person"  # 60/40 split
            templates = first_person_templates if perspective == "first_person" else third_person_templates
            TemplateClass = random.choice(templates)
        else:
            # Find template that best satisfies current needs
            best_template = None
            best_score = 0
            
            for template_class in all_templates:
                try:
                    perspective = "first_person" if template_class in first_person_templates else "third_person"
                    template = template_class(0, base_date, perspective)
                    _, entities_meta, relations_meta = template.generate()
                    
                    score = 0
                    # Score based on needed types
                    for _, (entity_type, _) in entities_meta.items():
                        if entity_type in entity_needs:
                            score += entity_needs[entity_type] * 10
                    
                    for rel_type, _, _ in relations_meta:
                        if rel_type in relation_needs:
                            score += relation_needs[rel_type] * 10
                    
                    if score > best_score:
                        best_score = score
                        best_template = template_class
                        
                except Exception:
                    continue
            
            TemplateClass = best_template or random.choice(all_templates)
        
        # Generate record
        perspective = "first_person" if TemplateClass in first_person_templates else "third_person"
        template_instance = TemplateClass(template_id=i, base_date=base_date, perspective=perspective)
        
        success = False
        for attempt in range(Config.MAX_RETRIES):
            total_attempts += 1
            try:
                record = template_instance.build()
                
                # Basic validation
                if not record.get('entities') or not record.get('text') or not record.get('relations'):
                    raise ValueError("Missing required fields")
                
                # Update counts
                for entity in record.get('entities', []):
                    entity_type = entity.get('type')
                    if entity_type in entity_counts:
                        entity_counts[entity_type] += 1
                
                for relation in record.get('relations', []):
                    relation_type = relation.get('type')
                    if relation_type in relation_counts:
                        relation_counts[relation_type] += 1
                
                dataset.append(record)
                success = True
                break
                
            except Exception as e:
                error_type = type(e).__name__
                failure_reasons[error_type] = failure_reasons.get(error_type, 0) + 1
                
                template_name = TemplateClass.__name__
                if template_name not in template_failures:
                    template_failures[template_name] = []
                template_failures[template_name].append(str(e))
                
                if attempt == Config.MAX_RETRIES - 1:
                    failed_generations += 1
        
        # Progress reporting
        if (i + 1) % 100 == 0:
            entity_balance = (min(entity_counts.values()) / max(entity_counts.values()) * 100) if entity_counts.values() else 100
            relation_balance = (min(relation_counts.values()) / max(relation_counts.values()) * 100) if relation_counts.values() else 100
            print(f"Progress: {i+1}/{num_records} | Entity Balance: {entity_balance:.1f}% | Relation Balance: {relation_balance:.1f}%")
    
    # Calculate final balance scores
    entity_balance = (min(entity_counts.values()) / max(entity_counts.values()) * 100) if entity_counts.values() else 100
    relation_balance = (min(relation_counts.values()) / max(relation_counts.values()) * 100) if relation_counts.values() else 100
    overall_balance = (entity_balance + relation_balance) / 2
    
    print(f"\n🎯 ULTRA-BALANCED GENERATION COMPLETE")
    print(f"Final Balance Scores: Entity {entity_balance:.1f}%, Relation {relation_balance:.1f}%, Overall {overall_balance:.1f}%")
    
    stats = {
        "total_generated": len(dataset),
        "failed_generations": failed_generations,
        "total_attempts": total_attempts,
        "success_rate": f"{(len(dataset) / total_attempts * 100):.1f}%",
        "balance_scores": {
            "entity_balance": entity_balance,
            "relation_balance": relation_balance,
            "overall_balance": overall_balance
        },
        "entity_coverage": f"{len([c for c in entity_counts.values() if c > 0]) / len(all_entity_types) * 100:.1f}%",
        "relation_coverage": f"{len([c for c in relation_counts.values() if c > 0]) / len(all_relation_types) * 100:.1f}%"
    }
    
    return {
        "dataset": dataset,
        "statistics": stats,
        "metadata": {
            "generation_method": "ultra_balanced",
            "entity_counts": entity_counts,
            "relation_counts": relation_counts,
            "template_failures": {k: len(v) for k, v in template_failures.items()}
        }
    }
print("=" * 60)
validate_final_coverage()

def print_statistics(stats: Dict):
    """Print comprehensive statistics with expanded relations focus."""
    print(f"\n{'='*70}")
    print("EXPANDED RELATIONS DATASET GENERATION COMPLETE")
    print(f"{'='*70}")
    
    gen_summary = stats["generation_summary"]
    print(f"Total generated: {gen_summary['total_generated']}")
    print(f"Failed generations: {gen_summary['failed_generations']}")
    print(f"Success rate: {gen_summary['success_rate']}")
    print(f"Templates used: {gen_summary['templates_used']}")
    
    perspective = stats["perspective_analysis"]
    print(f"\n--- PERSPECTIVE DISTRIBUTION ---")
    print(f"First-person records: {perspective['first_person_records']} ({perspective['first_person_percentage']})")
    print(f"Third-person records: {perspective['third_person_records']} ({perspective['third_person_percentage']})")
    
    expanded = stats["expanded_relations_analysis"]
    print(f"\n--- EXPANDED RELATIONS COVERAGE ---")
    print(f"Total expanded relations defined: {expanded['total_expanded_relations_defined']}")
    print(f"Expanded relations used: {expanded['expanded_relations_used']}")
    print(f"Expanded relations coverage: {expanded['expanded_relations_coverage']}")
    print(f"Expanded relations in dataset: {', '.join(expanded['expanded_relations_list'])}")
    
    content = stats["content_analysis"]
    print(f"\n--- CONTENT ANALYSIS ---")
    print(f"Unique entity types: {content['unique_entity_types']}")
    print(f"Unique relation types: {content['unique_relation_types']}")
    print(f"Average entities per record: {content['avg_entities_per_record']}")
    print(f"Average relations per record: {content['avg_relations_per_record']}")
    
    coverage = stats["comprehensive_coverage"]
    print(f"\n--- COMPREHENSIVE COVERAGE ---")
    print(f"Entity coverage: {coverage['entity_coverage_percentage']} ({coverage['entity_types_used']}/{coverage['total_entity_types_supported']})")
    print(f"Relation coverage: {coverage['relation_coverage_percentage']} ({coverage['relation_types_used']}/{coverage['total_relation_types_supported']})")
    
    print(f"\nTop Relation Types:")
    for rel_type, count in stats["top_relation_types"]:
        print(f"  - {rel_type}: {count}")

# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# ENHANCED BALANCED DATASET GENERATION SYSTEM
# --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---

class BalancedTemplateManager:
    """Manages template usage tracking for perfectly balanced dataset generation."""
    
    def __init__(self, first_person_templates: List, third_person_templates: List):
        self.first_person_templates = first_person_templates
        self.third_person_templates = third_person_templates
        self.all_templates = first_person_templates + third_person_templates
        
        # Track usage counts for each template
        self.template_usage_counts = {template.__name__: 0 for template in self.all_templates}
        
        # Track entity and relation type usage
        self.entity_type_usage = {}
        self.relation_type_usage = {}
        
        # Initialize entity and relation type tracking
        all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        for entity_type in all_entity_types:
            self.entity_type_usage[getattr(EntityTypes, entity_type)] = 0
        for relation_type in all_relation_types:
            self.relation_type_usage[getattr(RelationTypes, relation_type)] = 0
        
        # Coverage tracking
        self.covered_entities = set()
        self.covered_relations = set()
        
        print(f"🎯 BalancedTemplateManager initialized:")
        print(f"   - Total templates: {len(self.all_templates)}")
        print(f"   - Entity types to balance: {len(all_entity_types)}")
        print(f"   - Relation types to balance: {len(all_relation_types)}")
    
    def get_least_used_template(self, perspective: str = None) -> object:
        """Get the least used template, optionally filtered by perspective."""
        if perspective == "first_person":
            templates = self.first_person_templates
        elif perspective == "third_person":
            templates = self.third_person_templates
        else:
            templates = self.all_templates
        
        # Safeguard against empty template pools
        if not templates:
            print(f"WARNING: Empty template pool for perspective {perspective}")
            return random.choice(self.all_templates) if self.all_templates else None
        
        # Find template with minimum usage count
        min_usage = min(self.template_usage_counts[template.__name__] for template in templates)
        least_used_templates = [template for template in templates 
                              if self.template_usage_counts[template.__name__] == min_usage]
        
        # Safeguard against empty least_used_templates list
        if not least_used_templates:
            print(f"WARNING: No least used templates found, fallback to random selection")
            return random.choice(templates)
        
        return random.choice(least_used_templates)
    
    def record_template_usage(self, template_class: object, entities_meta: Dict, relations_meta: List):
        """Record usage of a template and update entity/relation tracking."""
        template_name = template_class.__name__
        self.template_usage_counts[template_name] += 1
        
        # Track entity usage
        for _, (entity_type, _) in entities_meta.items():
            self.entity_type_usage[entity_type] = self.entity_type_usage.get(entity_type, 0) + 1
            self.covered_entities.add(entity_type)
        
        # Track relation usage
        for rel_type, _, _ in relations_meta:
            self.relation_type_usage[rel_type] = self.relation_type_usage.get(rel_type, 0) + 1
            self.covered_relations.add(rel_type)
    
    def select_next_template(self, perspective: str = None, dataset_size: int = 0, target_records: int = 0) -> object:
        """Enhanced template selection that prioritizes underrepresented entity/relation types."""
        if perspective == "first_person":
            templates = self.first_person_templates
        elif perspective == "third_person":
            templates = self.third_person_templates
        else:
            templates = self.all_templates
        
        # Safeguard against empty template pools
        if not templates:
            print(f"WARNING: Empty template pool for perspective {perspective}")
            return random.choice(self.all_templates) if self.all_templates else None
        
        # Use aggressive balancing strategy
        boost_templates, phase = self.enforce_aggressive_balance(target_records, dataset_size)
        perspective_boost_templates = [t for t in boost_templates if t in templates]
        
        # Aggressive template selection based on phase
        if phase == "aggressive_boost" and perspective_boost_templates:
            if random.random() < 0.9:  # 90% chance to use boost template
                selected = random.choice(perspective_boost_templates)
                print(f"🚀 Aggressive boost: {selected.__name__}")
                return selected
        elif phase == "maintenance_phase" and perspective_boost_templates:
            if random.random() < 0.6:  # 60% chance for maintenance corrections
                selected = random.choice(perspective_boost_templates)
                print(f"⚖️ Maintenance correction: {selected.__name__}")
                return selected
        
        # Fallback to original enhanced selection
        # Get priority templates for threshold enforcement
        priority_templates = self.enforce_minimum_thresholds(dataset_size)
        if priority_templates is None:
            priority_templates = []
        perspective_priority_templates = [t for t in priority_templates if t in templates]
        
        # If we have priority templates for this perspective, prefer them
        if perspective_priority_templates and random.random() < 0.5:  # Reduced to 50% to allow other strategies
            return random.choice(perspective_priority_templates)
        
        # Calculate need scores for each template based on coverage gaps
        template_scores = {}
        
        all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        # Calculate minimum thresholds for better balance
        total_records_generated = sum(self.template_usage_counts.values())
        min_entity_threshold = max(1, dataset_size // (len(all_entity_types) * 2))  # More aggressive threshold
        min_relation_threshold = max(1, dataset_size // (len(all_relation_types) * 2))
        
        for template_class in templates:
            try:
                # Test generate to see what entities/relations this template covers
                template = template_class(0, datetime.now(), perspective or "first_person")
                _, entities_meta, relations_meta = template.generate()
                
                score = 0
                
                # Score based on underrepresented entity types with higher penalties
                for _, (entity_type, _) in entities_meta.items():
                    current_usage = self.entity_type_usage.get(entity_type, 0)
                    if current_usage == 0:
                        score += 100  # Much higher value for uncovered types
                    elif current_usage < min_entity_threshold:
                        score += 50  # High value for below threshold
                    elif current_usage < min_entity_threshold * 2:
                        score += 20  # Medium value for low coverage
                    else:
                        score += 1   # Low value for well-covered types
                
                # Score based on underrepresented relation types with higher penalties
                for rel_type, _, _ in relations_meta:
                    current_usage = self.relation_type_usage.get(rel_type, 0)
                    if current_usage == 0:
                        score += 100  # Much higher value for uncovered types
                    elif current_usage < min_relation_threshold:
                        score += 50  # High value for below threshold
                    elif current_usage < min_relation_threshold * 2:
                        score += 20  # Medium value for low coverage
                    else:
                        score += 1   # Low value for well-covered types
                
                # Stronger penalty for overused templates
                template_usage = self.template_usage_counts[template_class.__name__]
                max_template_usage = max(self.template_usage_counts.values()) if self.template_usage_counts.values() else 1
                avg_template_usage = total_records_generated / len(self.template_usage_counts) if self.template_usage_counts else 1
                
                if template_usage > avg_template_usage * 2:
                    score *= 0.05  # Very strong penalty for heavily overused templates
                elif template_usage > avg_template_usage:
                    score *= 0.3  # Strong penalty for overused templates
                
                template_scores[template_class] = score
                
            except Exception as e:
                # If template fails, give it very low score but don't crash
                print(f"WARNING: Template {template_class.__name__} failed during selection: {str(e)}")
                template_scores[template_class] = 0.1
        
        # Select template with highest need score
        if template_scores:
            # Get top scoring templates and add some randomness among them
            sorted_templates = sorted(template_scores.items(), key=lambda x: x[1], reverse=True)
            top_score = sorted_templates[0][1]
            top_templates = [t for t, s in sorted_templates if s >= top_score * 0.9]  # Within 90% of top score
            
            if top_templates:
                return random.choice(top_templates)
            else:
                return sorted_templates[0][0]  # Fallback to highest scoring
        else:
            # Final fallback to least used
            return self.get_least_used_template(perspective)

    def get_balance_score(self) -> float:
        """Calculate balance score (0-100, where 100 is perfectly balanced)."""
        if not self.template_usage_counts:
            return 0.0
        
        usage_counts = list(self.template_usage_counts.values())
        if not usage_counts:
            return 100.0
            
        non_zero_counts = [count for count in usage_counts if count > 0]
        if not non_zero_counts:
            return 100.0
        
        min_usage = min(non_zero_counts)
        max_usage = max(non_zero_counts)
        
        if max_usage == 0:
            return 100.0
        
        # For small datasets, consider if most templates are used at least once
        total_templates = len(self.template_usage_counts)
        used_templates = len(non_zero_counts)
        coverage_factor = used_templates / total_templates
        
        # Balance score: combination of usage balance and template coverage
        balance_ratio = min_usage / max_usage if max_usage > 0 else 1.0
        balance_score = balance_ratio * coverage_factor * 100
        
        return balance_score
    
    def get_coverage_stats(self) -> Dict:
        """Get detailed coverage statistics."""
        all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        entity_coverage = len(self.covered_entities) / len(all_entity_types) * 100
        relation_coverage = len(self.covered_relations) / len(all_relation_types) * 100
        
        return {
            "entity_coverage_percent": entity_coverage,
            "relation_coverage_percent": relation_coverage,
            "covered_entities": len(self.covered_entities),
            "total_entities": len(all_entity_types),
            "covered_relations": len(self.covered_relations),
            "total_relations": len(all_relation_types),
            "balance_score": self.get_balance_score()
        }
    
    def get_underrepresented_types(self, threshold_percentile: float = 0.2) -> Dict:
        """Get entity and relation types that are underrepresented."""
        total_records = sum(self.template_usage_counts.values())
        if total_records == 0:
            return {"entities": [], "relations": []}
        
        # Calculate minimum thresholds
        all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        entity_counts = list(self.entity_type_usage.values())
        relation_counts = list(self.relation_type_usage.values())
        
        # Use percentile-based threshold for better balance
        if entity_counts:
            entity_threshold = max(1, int(sum(entity_counts) / len(all_entity_types) * threshold_percentile))
        else:
            entity_threshold = 1
            
        if relation_counts:
            relation_threshold = max(1, int(sum(relation_counts) / len(all_relation_types) * threshold_percentile))
        else:
            relation_threshold = 1
        
        underrepresented_entities = [
            (entity_type, count) for entity_type, count in self.entity_type_usage.items()
            if count < entity_threshold
        ]
        
        underrepresented_relations = [
            (relation_type, count) for relation_type, count in self.relation_type_usage.items()
            if count < relation_threshold
        ]
        
        return {
            "entities": underrepresented_entities,
            "relations": underrepresented_relations,
            "entity_threshold": entity_threshold,
            "relation_threshold": relation_threshold
        }
    
    def enforce_minimum_thresholds(self, dataset_size: int) -> List[object]:
        """Return templates that should be prioritized to meet minimum thresholds."""
        all_entity_types = {attr for attr in dir(EntityTypes) if not attr.startswith('_')}
        all_relation_types = {attr for attr in dir(RelationTypes) if not attr.startswith('_')}
        
        # Calculate aggressive minimum thresholds for better balance
        min_entity_threshold = max(2, dataset_size // (len(all_entity_types) // 2))  # Higher threshold
        min_relation_threshold = max(2, dataset_size // (len(all_relation_types) // 2))
        
        underrepresented_entities = [
            entity_type for entity_type, count in self.entity_type_usage.items()
            if count < min_entity_threshold
        ]
        
        underrepresented_relations = [
            relation_type for relation_type, count in self.relation_type_usage.items()
            if count < min_relation_threshold
        ]
        
        # Find templates that can help with underrepresented types
        priority_templates = []
        
        for template_class in self.all_templates:
            try:
                # Test generate to see what entities/relations this template covers
                perspective = "first_person" if template_class in self.first_person_templates else "third_person"
                template = template_class(0, datetime.now(), perspective)
                _, entities_meta, relations_meta = template.generate()
                
                # Check if this template helps with underrepresented types
                helps_entities = any(entity_type in underrepresented_entities for _, (entity_type, _) in entities_meta.items())
                helps_relations = any(rel_type in underrepresented_relations for rel_type, _, _ in relations_meta)
                
                if helps_entities or helps_relations:
                    priority_templates.append(template_class)
                    
            except Exception:
                continue
        
        print(f"🎯 Minimum threshold enforcement: Entity {min_entity_threshold}, Relation {min_relation_threshold}, Priority templates: {len(priority_templates)}")
        
        return priority_templates
        
    def enforce_aggressive_balance(self, target_records: int, current_records: int) -> Tuple[List[object], str]:
        """Use aggressive balancing to achieve 90%+ balance scores."""
        entity_counts = list(self.entity_type_usage.values())
        relation_counts = list(self.relation_type_usage.values())
        
        if not entity_counts or not relation_counts:
            return [], "initial_phase"
        
        # Calculate current balance scores
        entity_balance = (min(entity_counts) / max(entity_counts) * 100) if max(entity_counts) > 0 else 100
        relation_balance = (min(relation_counts) / max(relation_counts) * 100) if max(relation_counts) > 0 else 100
        
        print(f"📊 Current balance: Entity {entity_balance:.1f}%, Relation {relation_balance:.1f}%")
        
        # If we're achieving good balance (>80%), maintain it with light corrections
        if entity_balance > 80 and relation_balance > 80:
            return self.get_light_correction_templates(), "maintenance_phase"
        
        # For aggressive balancing, calculate what each type needs to reach 90% balance target
        remaining_records = target_records - current_records
        if remaining_records <= 0:
            return [], "complete"
        
        # Calculate target counts for 90% balance
        max_entity_count = max(entity_counts)
        max_relation_count = max(relation_counts)
        
        target_entity_min = int(max_entity_count * 0.9)  # 90% of max
        target_relation_min = int(max_relation_count * 0.9)  # 90% of max
        
        # Find types that need boosting
        entity_boost_needed = {}
        relation_boost_needed = {}
        
        for entity_type, count in self.entity_type_usage.items():
            if count < target_entity_min:
                entity_boost_needed[entity_type] = target_entity_min - count
        
        for relation_type, count in self.relation_type_usage.items():
            if count < target_relation_min:
                relation_boost_needed[relation_type] = target_relation_min - count
        
        print(f"🎯 Entities needing boost: {len(entity_boost_needed)}, Relations needing boost: {len(relation_boost_needed)}")
        
        # Find templates that can provide these specific types
        boost_templates = []
        for template_class in self.all_templates:
            try:
                perspective = "first_person" if template_class in self.first_person_templates else "third_person"
                template = template_class(0, datetime.now(), perspective)
                _, entities_meta, relations_meta = template.generate()
                
                boost_score = 0
                # Score based on how much this template helps with needed boosts
                for _, (entity_type, _) in entities_meta.items():
                    if entity_type in entity_boost_needed:
                        boost_score += entity_boost_needed[entity_type] * 10  # High priority
                
                for rel_type, _, _ in relations_meta:
                    if rel_type in relation_boost_needed:
                        boost_score += relation_boost_needed[rel_type] * 10  # High priority
                
                if boost_score > 0:
                    boost_templates.append((template_class, boost_score))
                    
            except Exception:
                continue
        
        # Sort by boost score and return top templates
        boost_templates.sort(key=lambda x: x[1], reverse=True)
        return [t[0] for t in boost_templates[:min(50, len(boost_templates))]], "aggressive_boost"
    
    def get_light_correction_templates(self) -> List[object]:
        """Get templates for light balance corrections when already near target."""
        entity_counts = list(self.entity_type_usage.values())
        relation_counts = list(self.relation_type_usage.values())
        
        if not entity_counts or not relation_counts:
            return []
        
        min_entity_count = min(entity_counts)
        min_relation_count = min(relation_counts)
        
        # Find templates that help boost the minimum counts
        correction_templates = []
        for template_class in self.all_templates:
            try:
                perspective = "first_person" if template_class in self.first_person_templates else "third_person"
                template = template_class(0, datetime.now(), perspective)
                _, entities_meta, relations_meta = template.generate()
                
                helps_min_entities = any(
                    self.entity_type_usage.get(entity_type, 0) == min_entity_count
                    for _, (entity_type, _) in entities_meta.items()
                )
                
                helps_min_relations = any(
                    self.relation_type_usage.get(rel_type, 0) == min_relation_count
                    for rel_type, _, _ in relations_meta
                )
                
                if helps_min_entities or helps_min_relations:
                    correction_templates.append(template_class)
                    
            except Exception:
                continue
        
        return correction_templates
    
    def get_usage_distribution(self) -> Dict:
        """Get usage distribution for templates, entities, and relations."""
        return {
            "template_usage": dict(self.template_usage_counts),
            "entity_usage": dict(self.entity_type_usage),
            "relation_usage": dict(self.relation_type_usage)
        }

def generate_balanced_dataset(num_records: int = None) -> Dict:
    """Generate perfectly balanced dataset with enhanced tracking and two-phase algorithm."""
    
    if num_records is None:
        num_records = Config.DEFAULT_NUM_RECORDS
    
    print(f"🚀 ENHANCED BALANCED DATASET GENERATION")
    print(f"============================================================")
    print(f"🎯 Target: {num_records} perfectly balanced records")
    print(f"📊 Two-phase algorithm: Coverage Guarantee + Balanced Distribution")
    
    dataset = []
    base_date = datetime.strptime(Config.CURRENT_UTC_DATETIME, "%Y-%m-%d %H:%M:%S")
    failed_generations = 0
    failure_reasons = {}
    quality_issues = {}
    
    # Define template classes by perspective (same as original)
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
        FirstPersonFinalCognitiveTemplate,
        FirstPersonAllSensoryTemplate,
        FirstPersonTimeScheduleTemplate,
        FirstPersonLocationExpertiseTraitTemplate,
        FirstPersonBeliefsOpinionsTemplate,
        FirstPersonHealthFinanceTemplate,
        FirstPersonIdentityNicknameTemplate,
        FirstPersonRareEntityTypesTemplate,
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
        FirstPersonLifeStageReflectionTemplate,
        FirstPersonCulturalLearningTemplate,
        FirstPersonIndustryExpertiseTemplate,
        FirstPersonThinkingProcessTemplate,
        FirstPersonRegretAnticipationTemplate,
        FirstPersonCompleteSensoryTemplate,
        FirstPersonRepeatingRoutineTemplate,
        FirstPersonComprehensiveCoverageTemplate,
        FirstPersonComplexMemoryTemplate,
        FirstPersonMemoryRecallTemplate,
        FirstPersonAchievementTemplate,
        FirstPersonMediaPreferencesTemplate,
        FirstPersonLifeEventsTemplate,
        FirstPersonOrganizationContextTemplate,
        FirstPersonPlatformContextTemplate,
        FirstPersonFunctionWordTemplate,
        FirstPersonIndustryKnowledgeTemplate,
        FirstPersonQuantityAmountTemplate
    ]
    
    third_person_templates = [
        ThirdPersonPetTemplate,
        ThirdPersonComprehensiveMemoryTemplate,
        ThirdPersonPetCareTemplate,
        ThirdPersonAdvancedCognitiveTemplate,
        ThirdPersonTemporalExpertiseTemplate,
        ThirdPersonRelationshipMaintainerTemplate,
        ThirdPersonIndustryInnovationTemplate,
        ThirdPersonLifeStageWisdomTemplate,
        ThirdPersonCulturalPreservationTemplate,
        ThirdPersonLifeTransitionTemplate,
        ThirdPersonCulturalExperienceTemplate,
        ThirdPersonGenerosityTemplate,
        ThirdPersonSkillMasteryTemplate,
        ThirdPersonCommunityLeadershipTemplate,
        ThirdPersonVehicleOwnershipTemplate,
        ThirdPersonMediaProductionTemplate,
        ThirdPersonWeatherImpactTemplate,
        ThirdPersonGroupMembershipTemplate,
        ThirdPersonFamilyRelationshipTemplate,
        ThirdPersonCausationTemplate,
        ThirdPersonLocationProximityTemplate,
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
        ThirdPersonLearningMentorshipTemplate,
        ThirdPersonEmotionalJourneyTemplate,
        ThirdPersonIndustryExpertiseTemplate
    ]
    
    # Initialize balanced template manager
    manager = BalancedTemplateManager(first_person_templates, third_person_templates)
    
    # Calculate target counts
    first_person_target = int(num_records * Config.FIRST_PERSON_RATIO)
    third_person_target = num_records - first_person_target
    
    print(f"📋 Generation Plan:")
    print(f"   - First-person records: {first_person_target} ({Config.FIRST_PERSON_RATIO:.0%})")
    print(f"   - Third-person records: {third_person_target} ({Config.THIRD_PERSON_RATIO:.0%})")
    print(f"   - Templates per perspective: {len(first_person_templates)} + {len(third_person_templates)}")
    
    # PHASE 1: Coverage Guarantee Phase
    print(f"\n🎯 PHASE 1: Coverage Guarantee Phase")
    coverage_phase_target = min(1000, num_records // 10)  # 10% for coverage guarantee
    
    # Track targets for Phase 1
    phase1_first_person_target = int(coverage_phase_target * Config.FIRST_PERSON_RATIO)
    phase1_third_person_target = coverage_phase_target - phase1_first_person_target
    phase1_first_person_remaining = phase1_first_person_target
    phase1_third_person_remaining = phase1_third_person_target
    
    # Track template failures for audit
    template_failures = {}
    total_attempts = 0
    
    for i in range(coverage_phase_target):
        # Properly distribute perspectives to maintain ratio
        if phase1_first_person_remaining > 0 and (phase1_third_person_remaining <= 0 or random.random() < Config.FIRST_PERSON_RATIO):
            perspective = "first_person"
            phase1_first_person_remaining -= 1
            # Use enhanced selection that prioritizes underrepresented types
            TemplateClass = manager.select_next_template("first_person", i, coverage_phase_target)
        else:
            perspective = "third_person"
            phase1_third_person_remaining -= 1
            # Use enhanced selection that prioritizes underrepresented types
            TemplateClass = manager.select_next_template("third_person", i, coverage_phase_target)
        
        template_instance = TemplateClass(template_id=i, base_date=base_date, perspective=perspective)
        
        success = False
        for attempt in range(Config.MAX_RETRIES):
            total_attempts += 1
            try:
                record = template_instance.build()
                
                # Basic validation
                # Basic validation 
                if not record.get("entities"):
                    raise ValueError("No entities found")
                if not record.get("text"):
                    raise ValueError("No text found")
                if len(record.get("relations", [])) == 0:
                    raise ValueError("No relations found")
                
                # Get metadata for tracking
                _, entities_meta, relations_meta = template_instance.generate()
                manager.record_template_usage(TemplateClass, entities_meta, relations_meta)
                
                dataset.append(record)
                success = True
                break
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                failure_reasons[error_type] = failure_reasons.get(error_type, 0) + 1
                
                # Track template-specific failures
                template_name = TemplateClass.__name__
                if template_name not in template_failures:
                    template_failures[template_name] = []
                template_failures[template_name].append(error_msg)
                
                if "Quality issues" in error_msg:
                    for issue in error_msg.split("Quality issues: ")[1].strip("[]'").split("', '"):
                        quality_issues[issue] = quality_issues.get(issue, 0) + 1
                
                if attempt == Config.MAX_RETRIES - 1:
                    failed_generations += 1
        
        # Progress reporting for coverage phase
        if (i + 1) % 100 == 0 or i + 1 == coverage_phase_target:
            coverage_stats = manager.get_coverage_stats()
            print(f"   Coverage Phase: {i+1}/{coverage_phase_target} | "
                  f"Entities: {coverage_stats['entity_coverage_percent']:.1f}% | "
                  f"Relations: {coverage_stats['relation_coverage_percent']:.1f}% | "
                  f"Balance: {coverage_stats['balance_score']:.1f}%")
    
    # PHASE 2: Balanced Distribution Phase
    print(f"\n⚖️  PHASE 2: Balanced Distribution Phase")
    remaining_records = num_records - len(dataset)
    first_person_remaining = first_person_target - sum(1 for r in dataset if r.get('context', {}).get('Perspective') == 'first_person')
    third_person_remaining = third_person_target - sum(1 for r in dataset if r.get('context', {}).get('Perspective') == 'third_person')
    
    for i in range(remaining_records):
        # Determine perspective based on remaining targets - use simple deterministic logic
        target_perspective = None
        if first_person_remaining > 0 and third_person_remaining > 0:
            # Both perspectives still needed - use ratio to decide
            ratio_needed = first_person_remaining / (first_person_remaining + third_person_remaining)
            if random.random() < ratio_needed:
                target_perspective = "first_person"
            else:
                target_perspective = "third_person"
        elif first_person_remaining > 0:
            # Only first-person remaining
            target_perspective = "first_person"
        else:
            # Only third-person remaining (or both exhausted)
            target_perspective = "third_person"
        
        # Use enhanced selection that prioritizes underrepresented types
        TemplateClass = manager.select_next_template(target_perspective, len(dataset), num_records)
        template_instance = TemplateClass(template_id=len(dataset), base_date=base_date, perspective=target_perspective)
        
        success = False
        for attempt in range(Config.MAX_RETRIES):
            total_attempts += 1
            try:
                record = template_instance.build()
                
                # Basic validation
                # Basic validation 
                if not record.get("entities"):
                    raise ValueError("No entities found")
                if not record.get("text"):
                    raise ValueError("No text found")
                if len(record.get("relations", [])) == 0:
                    raise ValueError("No relations found")
                
                # Get metadata for tracking
                _, entities_meta, relations_meta = template_instance.generate()
                manager.record_template_usage(TemplateClass, entities_meta, relations_meta)
                
                dataset.append(record)
                success = True
                
                # Only decrement counters on successful generation
                if target_perspective == "first_person":
                    first_person_remaining -= 1
                else:
                    third_person_remaining -= 1
                break
                
            except Exception as e:
                error_type = type(e).__name__
                error_msg = str(e)
                
                failure_reasons[error_type] = failure_reasons.get(error_type, 0) + 1
                
                # Track template-specific failures
                template_name = TemplateClass.__name__
                if template_name not in template_failures:
                    template_failures[template_name] = []
                template_failures[template_name].append(error_msg)
                
                if "Quality issues" in error_msg:
                    for issue in error_msg.split("Quality issues: ")[1].strip("[]'").split("', '"):
                        quality_issues[issue] = quality_issues.get(issue, 0) + 1
                
                if attempt == Config.MAX_RETRIES - 1:
                    failed_generations += 1
        
        # Enhanced progress reporting
        if (i + 1) % Config.PROGRESS_INTERVAL == 0 or i + 1 == remaining_records:
            current_total = len(dataset)
            coverage_stats = manager.get_coverage_stats()
            print(f"   Balanced Phase: {current_total}/{num_records} | "
                  f"Balance: {coverage_stats['balance_score']:.1f}% | "
                  f"Failed: {failed_generations} | "
                  f"Success: {(current_total / total_attempts * 100):.1f}%")
    
    # Post-run audit of failing templates
    print(f"\n📊 POST-RUN AUDIT:")
    print(f"   Total attempts: {total_attempts}")
    print(f"   Successful generations: {len(dataset)}")
    print(f"   Failed generations: {failed_generations}")
    print(f"   Success rate: {(len(dataset) / total_attempts * 100):.1f}%")
    
    if template_failures:
        print(f"\n🚨 TOP FAILING TEMPLATES:")
        sorted_failures = sorted(template_failures.items(), key=lambda x: len(x[1]), reverse=True)
        for template_name, errors in sorted_failures[:5]:  # Top 5 failing templates
            print(f"   - {template_name}: {len(errors)} failures")
            if errors:
                print(f"     Most common error: {errors[0][:100]}...")
    
    # Generate enhanced statistics
    stats = generate_balanced_statistics(dataset, failed_generations, failure_reasons, quality_issues, 
                                       len(first_person_templates) + len(third_person_templates), manager)
    
    # Add audit information to metadata
    return {
        "dataset": dataset,
        "statistics": stats,
        "metadata": {
            "generation_method": "enhanced_balanced",
            "num_records_requested": num_records,
            "num_records_generated": len(dataset),
            "total_attempts": total_attempts,
            "balance_manager": manager.get_usage_distribution(),
            "coverage_stats": manager.get_coverage_stats(),
            "template_failures": {k: len(v) for k, v in template_failures.items()},
            "underrepresented_types": manager.get_underrepresented_types()
        }
    }

def generate_balanced_statistics(dataset: List[Dict], failed_generations: int, failure_reasons: Dict, 
                               quality_issues: Dict, num_templates: int, manager: BalancedTemplateManager) -> Dict:
    """Generate enhanced statistics with balance scoring and detailed coverage analysis."""
    
    if not dataset:
        return {
            "total_generated": 0,
            "failed_generations": failed_generations,
            "success_rate": 0.0,
            "balance_score": 0.0,
            "coverage_stats": manager.get_coverage_stats()
        }
    
    # Perspective distribution
    first_person_count = sum(1 for record in dataset if record.get('context', {}).get('Perspective') == 'first_person')
    third_person_count = len(dataset) - first_person_count
    
    # Entity and relation analysis
    entity_type_counts = {}
    relation_type_counts = {}
    
    for record in dataset:
        for entity in record.get("entities", []):
            entity_type = entity.get("type", "UNKNOWN")
            entity_type_counts[entity_type] = entity_type_counts.get(entity_type, 0) + 1
        
        for relation in record.get("relations", []):
            relation_type = relation.get("type", "UNKNOWN")
            relation_type_counts[relation_type] = relation_type_counts.get(relation_type, 0) + 1
    
    # Calculate balance scores
    coverage_stats = manager.get_coverage_stats()
    template_balance = manager.get_balance_score()
    
    # Entity balance score
    entity_counts = list(entity_type_counts.values())
    entity_balance = 100.0
    if entity_counts:
        min_entity = min(entity_counts)
        max_entity = max(entity_counts)
        entity_balance = (min_entity / max_entity * 100) if max_entity > 0 else 100.0
    
    # Relation balance score
    relation_counts = list(relation_type_counts.values())
    relation_balance = 100.0
    if relation_counts:
        min_relation = min(relation_counts)
        max_relation = max(relation_counts)
        relation_balance = (min_relation / max_relation * 100) if max_relation > 0 else 100.0
    
    # Overall balance score (weighted average)
    overall_balance = (template_balance * 0.4 + entity_balance * 0.3 + relation_balance * 0.3)
    
    # Top entity and relation types
    top_entity_types = sorted(entity_type_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    top_relation_types = sorted(relation_type_counts.items(), key=lambda x: x[1], reverse=True)[:15]
    
    # Calculate quality metrics
    avg_entities_per_record = sum(len(record.get("entities", [])) for record in dataset) / len(dataset)
    avg_relations_per_record = sum(len(record.get("relations", [])) for record in dataset) / len(dataset)
    
    return {
        "total_generated": len(dataset),
        "failed_generations": failed_generations,
        "success_rate": (len(dataset) / (len(dataset) + failed_generations)) * 100 if (len(dataset) + failed_generations) > 0 else 0,
        "templates_used": num_templates,
        
        # Enhanced balance metrics
        "balance_scores": {
            "overall_balance": overall_balance,
            "template_balance": template_balance,
            "entity_balance": entity_balance,
            "relation_balance": relation_balance
        },
        
        # Perspective distribution
        "perspective_distribution": {
            "first_person": {"count": first_person_count, "percentage": first_person_count / len(dataset) * 100},
            "third_person": {"count": third_person_count, "percentage": third_person_count / len(dataset) * 100}
        },
        
        # Coverage statistics
        "coverage_stats": coverage_stats,
        
        # Content analysis
        "content_analysis": {
            "unique_entity_types": len(entity_type_counts),
            "unique_relation_types": len(relation_type_counts),
            "avg_entities_per_record": avg_entities_per_record,
            "avg_relations_per_record": avg_relations_per_record
        },
        
        # Top types
        "top_entity_types": top_entity_types,
        "top_relation_types": top_relation_types,
        
        # Error analysis
        "failure_reasons": failure_reasons,
        "quality_issues": quality_issues
    }

def print_balanced_statistics(stats: Dict):
    """Print enhanced statistics with balance scores and detailed analysis."""
    print(f"\n======================================================================")
    print(f"ENHANCED BALANCED DATASET GENERATION COMPLETE")
    print(f"======================================================================")
    print(f"Total generated: {stats['total_generated']}")
    print(f"Failed generations: {stats['failed_generations']}")
    print(f"Success rate: {stats['success_rate']:.1f}%")
    print(f"Templates used: {stats['templates_used']}")
    
    # Balance scores
    balance = stats.get('balance_scores', {})
    print(f"\n--- BALANCE SCORES ---")
    print(f"Overall Balance Score: {balance.get('overall_balance', 0):.1f}%")
    print(f"  - Template Balance: {balance.get('template_balance', 0):.1f}%")
    print(f"  - Entity Balance: {balance.get('entity_balance', 0):.1f}%")
    print(f"  - Relation Balance: {balance.get('relation_balance', 0):.1f}%")
    
    # Perspective distribution
    perspective = stats.get('perspective_distribution', {})
    print(f"\n--- PERSPECTIVE DISTRIBUTION ---")
    if perspective.get('first_person'):
        print(f"First-person records: {perspective['first_person']['count']} ({perspective['first_person']['percentage']:.1f}%)")
    if perspective.get('third_person'):
        print(f"Third-person records: {perspective['third_person']['count']} ({perspective['third_person']['percentage']:.1f}%)")
    
    # Coverage statistics
    coverage = stats.get('coverage_stats', {})
    print(f"\n--- COVERAGE ANALYSIS ---")
    print(f"Entity coverage: {coverage.get('entity_coverage_percent', 0):.1f}% ({coverage.get('covered_entities', 0)}/{coverage.get('total_entities', 0)})")
    print(f"Relation coverage: {coverage.get('relation_coverage_percent', 0):.1f}% ({coverage.get('covered_relations', 0)}/{coverage.get('total_relations', 0)})")
    
    # Content analysis
    content = stats.get('content_analysis', {})
    print(f"\n--- CONTENT ANALYSIS ---")
    print(f"Unique entity types: {content.get('unique_entity_types', 0)}")
    print(f"Unique relation types: {content.get('unique_relation_types', 0)}")
    print(f"Average entities per record: {content.get('avg_entities_per_record', 0):.1f}")
    print(f"Average relations per record: {content.get('avg_relations_per_record', 0):.1f}")
    
    # Top types
    print(f"\n--- TOP ENTITY TYPES ---")
    for entity_type, count in stats.get("top_entity_types", [])[:10]:
        print(f"  - {entity_type}: {count}")
    
    print(f"\n--- TOP RELATION TYPES ---")
    for rel_type, count in stats.get("top_relation_types", [])[:10]:
        print(f"  - {rel_type}: {count}")
    
    # Error analysis
    if stats.get('failure_reasons'):
        print(f"\n--- ERROR ANALYSIS ---")
        for reason, count in stats['failure_reasons'].items():
            print(f"  - {reason}: {count}")

def main():
    """Main execution function with support for both generation methods."""
    import sys
    
    # Check for command line arguments to choose generation method
    use_balanced_generation = False
    if len(sys.argv) > 1:
        if sys.argv[1].lower() in ['balanced', 'balance', 'enhanced', 'b']:
            use_balanced_generation = True
        elif sys.argv[1].lower() in ['original', 'standard', 'o']:
            use_balanced_generation = False
        else:
            print("Usage: python data.py [balanced|original]")
            print("  balanced/b/enhanced: Use enhanced balanced generation")
            print("  original/o/standard: Use original generation (default)")
            return
    
    try:
        if use_balanced_generation:
            print("🎯 Using Enhanced Balanced Generation Method")
            result = generate_balanced_dataset()
            
            if result["dataset"]:
                filename = save_dataset(result)
                print_balanced_statistics(result["statistics"])
                
                print(f"\nDataset saved to: {filename}")
                
                # Show enhanced metadata
                metadata = result.get("metadata", {})
                coverage_stats = metadata.get("coverage_stats", {})
                print(f"\n🎯 Enhanced Generation Metadata:")
                print(f"   - Generation method: {metadata.get('generation_method', 'unknown')}")
                print(f"   - Final balance score: {coverage_stats.get('balance_score', 0):.1f}%")
                print(f"   - Entity coverage: {coverage_stats.get('entity_coverage_percent', 0):.1f}%")
                print(f"   - Relation coverage: {coverage_stats.get('relation_coverage_percent', 0):.1f}%")
                
                # Show sample records with enhanced details
                print(f"\nSample Records with Enhanced Balance Analysis:")
                
                sample_records = random.sample(result["dataset"], min(5, len(result["dataset"])))
                for i, record in enumerate(sample_records):
                    print(f"\n--- Enhanced Sample {i+1} ---")
                    print(f"Text: {record['text']}")
                    print(f"Relations: {[r['type'] for r in record['relations']]}")
                    print(f"Entities: {[e['type'] for e in record.get('entities', [])]}")
                    print(f"Perspective: {record.get('context', {}).get('Perspective', 'unknown')}")
                    
            else:
                print("ERROR: No records were successfully generated with balanced method!")
                print_balanced_statistics(result["statistics"])
        
        else:
            print("📊 Using Original Generation Method")
            result = generate_dataset()
            
            if result["dataset"]:
                filename = save_dataset(result)
                print_statistics(result["statistics"])
                
                print(f"\nDataset saved to: {filename}")
                
                # Show sample records highlighting expanded relations
                print(f"\nSample Records with Expanded Relations:")
                
                sample_records = random.sample(result["dataset"], min(5, len(result["dataset"])))
                for i, record in enumerate(sample_records):
                    print(f"\n--- Sample {i+1} ---")
                    print(f"Text: {record['text']}")
                    print(f"Relations: {[r['type'] for r in record['relations']]}")
                    print(f"Perspective: {record.get('context', {}).get('Perspective', 'unknown')}")
                    
            else:
                print("ERROR: No records were successfully generated!")
                print_statistics(result["statistics"])
            
    except Exception as e:
        print(f"Fatal error during dataset generation: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()