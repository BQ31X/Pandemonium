# Word Pool & Testing Infrastructure Guide

## Overview
This guide covers our shared vocabulary and testing tools designed for consistent Spymaster and Operative agent development. All tools use the same 250-word pool to ensure coordinated testing between team members.

## 🎯 Shared Word Pool (`shared_word_pool.py`)

### Competition-Ready Vocabulary (250 words)
Our word pool is designed to match the IEEE competition requirements, including non-standard terms:

| **Category** | **Count** | **Examples** | **Purpose** |
|--------------|-----------|--------------|-------------|
| **Standard** | 120 words | SHARK, HAMMER, BEACH, JUMP | Classic Codenames-style words |
| **Pop Culture** | 70 words | BATMAN, HOGWARTS, NETFLIX, MARIO | Movies, TV, games, fictional places |
| **Modern Slang** | 30 words | VIRAL, MEME, FLEX, GHOST | Internet culture, gaming terms |
| **Technical** | 30 words | AI, BLOCKCHAIN, QUANTUM, ALGORITHM | Tech/science concepts |

### Key Features
- **Diverse coverage**: Handles unexpected competition vocabulary
- **Easy importing**: `from shared_word_pool import WORD_POOL, get_random_words`
- **Category access**: Generate focused test sets by theme
- **Team consistency**: Both Spymaster and Operative developers use identical vocabulary

### Usage Examples
```python
# Get 25 random words for board simulation
from shared_word_pool import get_random_words
board_words = get_random_words(25)

# Get words by category for focused testing  
from shared_word_pool import get_words_by_category
categories = get_words_by_category()
pop_culture_words = categories['pop_culture']
```

## ⚙️ Enhanced Testing Tool (`spymaster_tester.py`)

### Purpose
Generate realistic word combinations with proper risk assessment for systematic agent testing. Replaces manual word selection with automated, competition-aware scenarios.

### Command Line Interface

#### **Basic Usage**
```bash
# Default scenario (3 red, 1 blue, 1 neutral, 1 assassin)
python spymaster_tester.py

# Custom word counts
python spymaster_tester.py --red 2 --blue 2 --neutral 1 --assassin 1
```

#### **Flexible Argument Names**
All arguments support multiple names for team convenience:

| **Concept** | **All Valid Options** |
|-------------|----------------------|
| RED words (targets) | `--red`, `--target`, `-r` |
| BLUE words (opponent) | `--blue`, `--opponent`, `-b` |
| NEUTRAL words (civilians) | `--neutral`, `--civilian`, `-n` |
| ASSASSIN words | `--assassin`, `-a` |

#### **Game State Scenarios**
```bash
# Early game (full 25-word board)
python spymaster_tester.py --early-game

# Mid game (13 words remaining)  
python spymaster_tester.py --mid-game

# Late game (5 words remaining, high pressure)
python spymaster_tester.py --late-game
```

#### **Category Filtering**
```bash
# Test only pop culture words
python spymaster_tester.py --category pop_culture --red 3

# Test technical terms
python spymaster_tester.py --category technical --red 2 --blue 1

# Available categories: standard, pop_culture, slang, technical, all
python spymaster_tester.py --list-categories
```

#### **Multiple Prompts**
```bash
# Generate 5 different test scenarios
python spymaster_tester.py --count 5 --red 2 --blue 1
```

#### **Operative Testing Format**
Generate scenarios specifically designed for operative agent testing:
```bash
# Basic operative test
python spymaster_tester.py --operative

# Short alias (recommended)
python spymaster_tester.py -o --red 2 --blue 2

# High-pressure operative scenario
python spymaster_tester.py -o --late-game
```

### Output Format

#### **Standard Format (Spymaster Testing)**
```
Target words (red): BATMAN, JOKER. Opponent words (blue): HERO. Civilian words (neutral): CAPE. ASSASSIN: GOTHAM
```

#### **Operative Format (with `--operative` or `-o`)**
```
=== FOR EVALUATION (Human Tester) ===
Target words (red): BATMAN, JOKER. Opponent words (blue): HERO. Civilian words (neutral): CAPE. ASSASSIN: GOTHAM

=== FOR OPERATIVE AGENT (Copy-Paste Ready) ===
Board words: HERO, BATMAN, CAPE, JOKER, GOTHAM
Clue: VILLAIN 2
```

**Design rationale:**
- **UPPERCASE words**: The actual game data (most important)
- **lowercase indicators**: Helpful context without visual clutter
- **ASSASSIN emphasis**: Highlights the critical risk word
- **Dual output**: Evaluation context + clean agent input for operative testing

### Typical Workflows

#### **For Spymaster Development:**
1. Generate test scenario: `python spymaster_tester.py --red 3 --blue 2`
2. Copy prompt to ADK web interface (`ADK_AGENT=spymaster adk web`)
3. Test spymaster response quality
4. Iterate prompts based on performance

#### **For Operative Development:**
1. Generate operative test scenarios: `python spymaster_tester.py --operative --red 3 --blue 2`
2. Use **"FOR OPERATIVE AGENT"** section for clean agent input (no category spoilers)
3. Use **"FOR EVALUATION"** section to judge if agent picked correctly
4. Test high-pressure scenarios: `python spymaster_tester.py -o --late-game`
5. Coordinate with Spymaster developer using same word pool and scenarios

#### **For Integration Testing:**
1. Generate full board: `python spymaster_tester.py --early-game`
2. Test complete Spymaster → Operative workflow
3. Verify risk assessment across game states

## 🎲 Quick Reference

### **Most Useful Commands**
```bash
# Default balanced test
python spymaster_tester.py

# High-pressure endgame
python spymaster_tester.py --late-game

# Pop culture challenge  
python spymaster_tester.py --category pop_culture --red 3 --blue 2

# Multiple test cases
python spymaster_tester.py --count 10 --red 2 --blue 1

# Custom risk scenario
python spymaster_tester.py --target 4 --opponent 3 --civilian 2
```

### **Help & Discovery**
```bash
# See all options
python spymaster_tester.py --help

# List word categories
python spymaster_tester.py --list-categories

# Check word pool directly
python shared_word_pool.py
```

## 🤝 Team Coordination Benefits

### **Consistent Vocabulary**
- Both Spymaster and Operative developers test with identical 250-word pool
- No vocabulary mismatches between agent development
- Competition-realistic word diversity (pop culture, slang, technical terms)

### **Systematic Testing**
- Reproducible test scenarios for performance comparison
- Risk-aware testing (opponent vs civilian vs assassin words)
- Game state awareness (early vs late game pressure)

### **Efficient Iteration**
- No manual word selection - automated generation
- Quick copy-paste testing workflow
- Category filtering for focused development

### **Competition Readiness**
- Unknown vocabulary simulation
- Mixed word type challenges (HOGWARTS + ALGORITHM + FLEX)
- Risk assessment training for different word types

---

*Created for ODSC Hackathon - SpyGame Team*  
*Use these tools for coordinated Spymaster and Operative agent development* 