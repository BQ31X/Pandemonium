#!/usr/bin/env python3
"""
Quick SpymasterAgent tester - generates word combinations for testing
Usage: python spymaster_tester.py [options]
"""

import random
import argparse
from shared_word_pool import get_words_by_category, ALL_WORDS

# Use shared word pool for consistent testing
WORD_CATEGORIES = get_words_by_category()
WORD_CATEGORIES['all'] = ALL_WORDS  # Add option to use entire pool

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

def main():
    parser = argparse.ArgumentParser(description='Generate word combinations for SpymasterAgent testing')
    parser.add_argument('--red', '--target', '-r', type=int, default=3, help='Number of RED target words (default: 3)')
    parser.add_argument('--blue', '--opponent', '-b', type=int, default=1, help='Number of BLUE opponent words (default: 1)')
    parser.add_argument('--neutral', '--civilian', '-n', type=int, default=1, help='Number of NEUTRAL civilian words (default: 1)')
    parser.add_argument('--assassin', '-a', type=int, default=1, help='Number of ASSASSIN words (default: 1)')
    parser.add_argument('--category', '-c', choices=list(WORD_CATEGORIES.keys()), help='Word category')
    parser.add_argument('--count', type=int, default=1, help='Number of prompts to generate')
    parser.add_argument('--list-categories', action='store_true', help='List available categories')
    
    # Preset scenarios
    parser.add_argument('--early-game', action='store_true', help='Early game scenario (9 red, 8 blue, 7 neutral, 1 assassin)')
    parser.add_argument('--mid-game', action='store_true', help='Mid game scenario (5 red, 4 blue, 3 neutral, 1 assassin)')
    parser.add_argument('--late-game', action='store_true', help='Late game scenario (2 red, 1 blue, 1 neutral, 1 assassin)')
    
    args = parser.parse_args()
    
    if args.list_categories:
        print("Available categories:")
        for cat, words in WORD_CATEGORIES.items():
            print(f"  {cat}: {', '.join(words[:5])}{'...' if len(words) > 5 else ''}")
        return
    
    # Handle preset scenarios
    if args.early_game:
        targets, blue, neutral, assassin = 9, 8, 7, 1
        print("EARLY GAME SCENARIO (25 words total)")
    elif args.mid_game:
        targets, blue, neutral, assassin = 5, 4, 3, 1
        print("MID GAME SCENARIO (13 words remaining)")
    elif args.late_game:
        targets, blue, neutral, assassin = 2, 1, 1, 1
        print("LATE GAME SCENARIO (5 words remaining)")
    else:
        targets, blue, neutral, assassin = args.red, args.blue, args.neutral, args.assassin
    
    if args.count > 1:
        print(f"Generating {args.count} test prompt(s):\n")
    
    for i in range(args.count):
        prompt = generate_test_prompt(targets, blue, neutral, assassin, args.category)
        if prompt:
            if args.count > 1:
                print(f"{i+1}. {prompt}")
            else:
                print(prompt)
        if args.count > 1:
            print()

if __name__ == "__main__":
    main() 