#!/usr/bin/env python3
"""
Quick SpymasterAgent tester - generates word combinations for testing
Usage: python spymaster_tester.py [options]
"""

import random
#import argparse
from .shared_word_pool import get_words_by_category, ALL_WORDS

# Use shared word pool for consistent testing
WORD_CATEGORIES = get_words_by_category()
WORD_CATEGORIES['all'] = ALL_WORDS  # Add option to use entire pool

def generate_json_prompt(red_count=3, blue_count=1, neutral_count=1, assassin_count=1, category=None):
    """Generate a test prompt with target words and different types of avoid words."""

    if category:
        if category not in WORD_CATEGORIES:
            print(f"Unknown category: {category}")
            print(f"Available: {', '.join(WORD_CATEGORIES.keys())}")
            return None
        word_pool = WORD_CATEGORIES[category].copy()
    else:
        # Mix from all categories
        word_pool = []
        for words in WORD_CATEGORIES.values():
            word_pool.extend(words)

    total_words = red_count + blue_count + neutral_count + assassin_count

    # Select random words
    if len(word_pool) < total_words:
        print(f"Not enough words in pool for {total_words} total words")
        return None

    selected = random.sample(word_pool, total_words)

    # Assign word types
    targets = selected[:red_count]
    blue_words = selected[red_count:red_count + blue_count]
    neutral_words = selected[red_count + blue_count:red_count + blue_count + neutral_count]
    assassin_words = selected[red_count + blue_count + neutral_count:total_words]

    json_board = targets + blue_words + neutral_words + assassin_words
    json_board_mapping = {"red_words": targets, "blue_words": blue_words, "civilian_words": neutral_words,
                          "assassin_word": assassin_words, "board_words": json_board}
    # Build prompt with risk levels
    # Build prompt with risk levels
    prompt_parts = f"board_words:{json_board}\nboard_words_mapping:{json_board_mapping}"


    return prompt_parts

def generate_test_prompt(red_count=3, blue_count=1, neutral_count=1, assassin_count=1, category=None):
    """Generate a test prompt with target words and different types of avoid words."""

    if category:
        if category not in WORD_CATEGORIES:
            print(f"Unknown category: {category}")
            print(f"Available: {', '.join(WORD_CATEGORIES.keys())}")
            return None
        word_pool = WORD_CATEGORIES[category].copy()
    else:
        # Mix from all categories
        word_pool = []
        for words in WORD_CATEGORIES.values():
            word_pool.extend(words)

    total_words = red_count + blue_count + neutral_count + assassin_count

    # Select random words
    if len(word_pool) < total_words:
        print(f"Not enough words in pool for {total_words} total words")
        return None

    selected = random.sample(word_pool, total_words)

    # Assign word types
    targets = selected[:red_count]
    blue_words = selected[red_count:red_count + blue_count]
    neutral_words = selected[red_count + blue_count:red_count + blue_count + neutral_count]
    assassin_words = selected[red_count + blue_count + neutral_count:total_words]

    # Build prompt with risk levels
    prompt_parts = [f"Target words (red): {', '.join(targets)}"]

    if blue_words:
        prompt_parts.append(f"Opponent words (blue): {', '.join(blue_words)}")
    if neutral_words:
        prompt_parts.append(f"Civilian words (neutral): {', '.join(neutral_words)}")
    if assassin_words:
        prompt_parts.append(f"ASSASSIN: {', '.join(assassin_words)}")

    return ". ".join(prompt_parts)



def generate_sample_clue(targets):
    """Generate a simple sample clue for target words (basic implementation)"""
    import random
    
    # Simple clue generation - in real game, spymaster would do this
    sample_clues = {
        # Animals
        frozenset(['SHARK', 'WHALE', 'FISH']): ('OCEAN', 3),
        frozenset(['CAT', 'DOG', 'BIRD']): ('PET', 3),
        frozenset(['LION', 'TIGER', 'BEAR']): ('WILD', 3),
        
        # Pop culture  
        frozenset(['BATMAN', 'SUPERMAN', 'SPIDERMAN']): ('HERO', 3),
        frozenset(['JOKER', 'VADER', 'VOLDEMORT']): ('VILLAIN', 3),
        frozenset(['HOGWARTS', 'JEDI', 'MATRIX']): ('FANTASY', 3),
        
        # Actions
        frozenset(['JUMP', 'LEAP', 'HOP']): ('MOVEMENT', 3),
        frozenset(['RUN', 'WALK', 'CLIMB']): ('EXERCISE', 3),
        
        # Objects
        frozenset(['PHONE', 'LAPTOP', 'SCREEN']): ('TECHNOLOGY', 3),
        frozenset(['HAMMER', 'KNIFE', 'SWORD']): ('TOOL', 3),
    }
    
    # Try to find a matching clue pattern
    target_set = frozenset(targets)
    for pattern, (clue, num) in sample_clues.items():
        if pattern.issubset(target_set):
            return clue, min(num, len(targets))
    
    # Fallback: generic clues
    fallback_clues = ['CONNECT', 'RELATED', 'TOGETHER', 'SIMILAR', 'GROUP']
    return random.choice(fallback_clues), len(targets)

def format_for_operative(standard_prompt, targets, blue_words, neutral_words, assassin_words):
    """Format test data for operative testing with evaluation context and clean agent input"""
    
    # Generate sample clue
    clue_word, clue_number = generate_sample_clue(targets)
    
    # All words in random order (like real game board)
    all_words = targets + blue_words + neutral_words + assassin_words
    random.shuffle(all_words)
    
    result = []
    result.append("=== FOR EVALUATION (Human Tester) ===")
    result.append(standard_prompt)
    result.append("")
    result.append("=== FOR OPERATIVE AGENT (Copy-Paste Ready) ===")
    result.append(f"Board words: {', '.join(all_words)}")
    result.append(f"Clue: {clue_word} {clue_number}")
    
    return "\n".join(result)


def main():
    import random
    #parser = argparse.ArgumentParser(description='Generate word combinations for SpymasterAgent testing')
    #parser.add_argument('--red', '--target', '-r', type=int, default=3, help='Number of RED target words (default: 3)')
    #parser.add_argument('--blue', '--opponent', '-b', type=int, default=1, help='Number of BLUE opponent words (default: 1)')
    #parser.add_argument('--neutral', '--civilian', '-n', type=int, default=1, help='Number of NEUTRAL civilian words (default: 1)')
    #parser.add_argument('--assassin', '-a', type=int, default=1, help='Number of ASSASSIN words (default: 1)')
    #parser.add_argument('--category', '-c', choices=list(WORD_CATEGORIES.keys()), help='Word category')
    #parser.add_argument('--count', type=int, default=1, help='Number of prompts to generate')
    #parser.add_argument('--list-categories', action='store_true', help='List available categories')
    
    # Preset scenarios
    #parser.add_argument('--early-game', action='store_true', help='Early game scenario (9 red, 8 blue, 7 neutral, 1 assassin)')
    #parser.add_argument('--mid-game', action='store_true', help='Mid game scenario (5 red, 4 blue, 3 neutral, 1 assassin)')
    #parser.add_argument('--late-game', action='store_true', help='Late game scenario (2 red, 1 blue, 1 neutral, 1 assassin)')
    #parser.add_argument('--operative-format', '--operative', '-o', action='store_true', help='Generate format for operative testing (includes sample clue and clean board)')
    
    #args = parser.parse_args()
    
    #if args.list_categories:
    #    print("Available categories:")
    #    for cat, words in WORD_CATEGORIES.items():
    #        print(f"  {cat}: {', '.join(words[:5])}{'...' if len(words) > 5 else ''}")
    #    return
    
    # Handle preset scenarios
    #if args.early_game:
    targets, blue, neutral, assassin = 4, 3, 2, 1
    #    print("EARLY GAME SCENARIO (25 words total)")
    #elif args.mid_game:
    #    targets, blue, neutral, assassin = 5, 4, 3, 1
    #    print("MID GAME SCENARIO (13 words remaining)")
    #elif args.late_game:
    #    targets, blue, neutral, assassin = 2, 1, 1, 1
    #    print("LATE GAME SCENARIO (5 words remaining)")
    #else:
    #targets, blue, neutral, assassin = args.red, args.blue, args.neutral, args.assassin
    
    #if args.count > 1:
    #    print(f"Generating {args.count} test prompt(s):\n")
    
    for i in range(1):
        # Generate word lists first  
        #if args.category:
        #    if args.category not in WORD_CATEGORIES:
        #        print(f"Unknown category: {args.category}")
        #        print(f"Available: {', '.join(WORD_CATEGORIES.keys())}")
        #        continue
        #    word_pool = WORD_CATEGORIES[args.category].copy()
        #else:
        #    word_pool = []
        #    for words in WORD_CATEGORIES.values():
        #        word_pool.extend(words)

        word_pool = []
        for words in WORD_CATEGORIES.values():
               word_pool.extend(words)

        total_words = targets + blue + neutral + assassin
        if len(word_pool) < total_words:
            print(f"Not enough words in pool for {total_words} total words")
            continue
            
        selected = random.sample(word_pool, total_words)
        target_words = selected[:targets]
        blue_words = selected[targets:targets + blue]
        neutral_words = selected[targets + blue:targets + blue + neutral]
        assassin_words = selected[targets + blue + neutral:total_words]
        
        # Generate standard prompt
        prompt_parts = [f"Target words (red): {', '.join(target_words)}"]
        if blue_words:
            prompt_parts.append(f"Opponent words (blue): {', '.join(blue_words)}")
        if neutral_words:
            prompt_parts.append(f"Civilian words (neutral): {', '.join(neutral_words)}")
        if assassin_words:
            prompt_parts.append(f"ASSASSIN: {', '.join(assassin_words)}")

        json_board = target_words + blue_words + neutral_words + assassin_words
        json_board_mapping = {"red_words": target_words, "blue_words": blue_words, "civilian_words": neutral_words,
                              "assassin_word": assassin_words, "board_words": json_board}
        # Build prompt with risk levels
        prompt_parts = f"{json_board_mapping}"

        standard_prompt = prompt_parts
        
        # Output based on format
        #if args.operative_format:
        #    operative_output = format_for_operative(standard_prompt, target_words, blue_words, neutral_words, assassin_words)
        #    if args.count > 1:
        #        print(f"{i+1}.")
        #        print(operative_output)
        #    else:
        #        print(operative_output)
        #else:
        #    if args.count > 1:
        #        print(f"{i+1}. {standard_prompt}")
        #    else:
        print(standard_prompt)
        
        #if args.count > 1:
        #    print()
    return standard_prompt

if __name__ == "__main__":
    main() 