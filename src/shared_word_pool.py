#!/usr/bin/env python3
"""
Shared Word Pool for SpyGame - Competition-Ready Vocabulary
250 words covering standard terms, pop culture, slang, proper nouns
Use this for consistent testing between Spymaster and Operative agents
"""

# Standard Codenames-style words (120 words)
STANDARD_WORDS = [
    # Animals
    "SHARK", "WOLF", "BEAR", "EAGLE", "TIGER", "SNAKE", "WHALE", "SPIDER", "LION", "DUCK",
    "HORSE", "CAT", "DOG", "BIRD", "FISH", "MOUSE", "RABBIT", "ELEPHANT", "MONKEY", "FOX",
    
    # Objects/Tools
    "HAMMER", "KNIFE", "BOOK", "PHONE", "CHAIR", "TABLE", "LAMP", "CLOCK", "MIRROR", "BOTTLE",
    "KEY", "LOCK", "SWORD", "SHIELD", "CAMERA", "SCREEN", "BATTERY", "ENGINE", "WHEEL", "ROPE",
    
    # Places
    "BEACH", "FOREST", "MOUNTAIN", "CITY", "SCHOOL", "HOSPITAL", "BANK", "AIRPORT", "BRIDGE", "TOWER",
    "CASTLE", "CHURCH", "MUSEUM", "HOTEL", "RESTAURANT", "LIBRARY", "PARK", "STADIUM", "THEATER", "FACTORY",
    
    # Actions/Verbs
    "JUMP", "RUN", "SWIM", "FLY", "CLIMB", "DIVE", "SLIDE", "DANCE", "SING", "WRITE",
    "READ", "COOK", "DRIVE", "WALK", "SLEEP", "DREAM", "LAUGH", "CRY", "FIGHT", "LOVE",
    
    # Colors/Attributes
    "RED", "BLUE", "GREEN", "YELLOW", "BLACK", "WHITE", "PURPLE", "ORANGE", "PINK", "BROWN",
    "HOT", "COLD", "FAST", "SLOW", "BIG", "SMALL", "LOUD", "QUIET", "BRIGHT", "DARK",
    
    # Food
    "APPLE", "ORANGE", "BANANA", "BREAD", "CHEESE", "PIZZA", "CAKE", "SOUP", "RICE", "MEAT",
    "COFFEE", "TEA", "WATER", "MILK", "SUGAR", "SALT", "PEPPER", "HONEY", "BUTTER", "EGG"
]

# Pop Culture & Entertainment (70 words)
POP_CULTURE_WORDS = [
    # Movies/TV
    "BATMAN", "SUPERMAN", "SPIDERMAN", "JOKER", "VADER", "YODA", "HULK", "THOR", "GANDALF", "HOBBIT",
    "MATRIX", "TERMINATOR", "ALIEN", "PREDATOR", "ZOMBIE", "VAMPIRE", "WIZARD", "DRAGON", "NINJA", "PIRATE",
    "JEDI", "SITH", "ROBOT", "CYBORG", "MUTANT", "CLONE", "AVATAR", "TITAN", "MONSTER", "BEAST",
    
    # Gaming
    "MARIO", "SONIC", "POKEMON", "ZELDA", "MINECRAFT", "FORTNITE", "XBOX", "NINTENDO", "PLAYSTATION", "ARCADE",
    
    # Pop References
    "HOGWARTS", "TARDIS", "LIGHTSABER", "KRYPTONITE", "VIBRANIUM", "MJOLNIR", "STARK", "WAYNE", "PARKER", "KENT",
    "NETFLIX", "YOUTUBE", "INSTAGRAM", "TIKTOK", "SPOTIFY", "TESLA", "APPLE", "GOOGLE", "AMAZON", "DISNEY",
    
    # Fictional Places/Things
    "GOTHAM", "METROPOLIS", "WAKANDA", "ASGARD", "NARNIA", "PANDORA", "ATLANTIS", "UTOPIA", "OLYMPUS", "VALHALLA"
]

# Modern Slang & Internet Culture (30 words)
SLANG_WORDS = [
    "VIRAL", "MEME", "TROLL", "SPAM", "HACK", "GLITCH", "NOOB", "EPIC", "FAIL", "WIN",
    "GHOST", "STAN", "FLEX", "SIMP", "SALTY", "TOXIC", "CRINGE", "BASIC", "SAVAGE", "MOOD",
    "VIBE", "YEET", "FOMO", "GOAT", "FIRE", "SLAY", "WOKE", "BOOMER", "KAREN", "CHAD"
]

# Technical & Abstract (30 words)
TECHNICAL_WORDS = [
    "CODE", "DATA", "CLOUD", "SERVER", "NETWORK", "WIFI", "BLOCKCHAIN", "CRYPTO", "AI", "ALGORITHM",
    "PIXEL", "DIGITAL", "VIRTUAL", "QUANTUM", "LASER", "RADAR", "SATELLITE", "SOLAR", "NUCLEAR", "ELECTRIC",
    "LOGIC", "THEORY", "CONCEPT", "PATTERN", "SYSTEM", "METHOD", "PROCESS", "FUNCTION", "VARIABLE", "PROTOCOL"
]

# Combine all word lists
ALL_WORDS = STANDARD_WORDS + POP_CULTURE_WORDS + SLANG_WORDS + TECHNICAL_WORDS

# Verify count
assert len(ALL_WORDS) == 250, f"Expected 250 words, got {len(ALL_WORDS)}"

# Export for easy importing
WORD_POOL = ALL_WORDS

def get_random_words(count=25, categories=None):
    """Get random words for board generation"""
    import random
    
    if categories:
        word_source = []
        if 'standard' in categories:
            word_source.extend(STANDARD_WORDS)
        if 'pop_culture' in categories:
            word_source.extend(POP_CULTURE_WORDS)
        if 'slang' in categories:
            word_source.extend(SLANG_WORDS)
        if 'technical' in categories:
            word_source.extend(TECHNICAL_WORDS)
    else:
        word_source = ALL_WORDS
    
    return random.sample(word_source, min(count, len(word_source)))

def get_words_by_category():
    """Return words organized by category"""
    return {
        'standard': STANDARD_WORDS,
        'pop_culture': POP_CULTURE_WORDS,
        'slang': SLANG_WORDS,
        'technical': TECHNICAL_WORDS
    }

if __name__ == "__main__":
    print(f"Total words: {len(ALL_WORDS)}")
    print(f"Standard: {len(STANDARD_WORDS)}")
    print(f"Pop Culture: {len(POP_CULTURE_WORDS)}")
    print(f"Slang: {len(SLANG_WORDS)}")
    print(f"Technical: {len(TECHNICAL_WORDS)}")
    
    # Sample board
    print(f"\nSample 25-word board:")
    sample = get_random_words(25)
    for i, word in enumerate(sample, 1):
        print(f"{i:2d}. {word}") 