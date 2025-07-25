# SpyGame: Multi-Agent Word Guessing System

## Overview

SpyGame is a cooperative AI system that plays a guessing game (based on Codenames™), using three specialized agents working together to identify all "red" words on a game board in minimum turns. The system demonstrates advanced multi-agent coordination, natural language reasoning, and strategic game-playing using Google's ADK framework.

## System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Game Master   │◄──►│   Spymaster     │◄──►│   Operative     │
│                 │    │                 │    │                 │
│ • State Mgmt    │    │ • Clue Gen      │    │ • Word Guessing │
│ • Rule Enforce  │    │ • Risk Analysis │    │ • Clue Interp   │
│ • Turn Flow     │    │ • Strategy      │    │ • Confidence    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         └───────────────────────┼───────────────────────┘
                                 │
                    ┌─────────────────┐
                    │ Shared Session  │
                    │     State       │
                    │                 │
                    │ • Board Words   │
                    │ • Game Status   │
                    │ • Turn Counter  │
                    │ • Scores        │
                    └─────────────────┘
```

## Agent Responsibilities

### **Game Master Agent**
- **Role**: Central orchestrator and rule enforcer
- **Functions**: 
  - Manages canonical game state and board
  - Validates all clues and guesses
  - Implements IEEE competition scoring rules
  - Detects win/loss conditions
- **Tools Exposed**: `submit_clue()`, `submit_guess()`, `get_current_board_state()`

### **Spymaster Agent** 
- **Role**: Strategic clue generator
- **Functions**:
  - Analyzes full board (sees all word identities)
  - Generates single-word clues connecting multiple red words
  - Avoids dangerous words (assassin, blue, neutral)
  - Enforces strict clue constraints (not on board, single word, etc.)
- **AI Challenge**: Complex semantic reasoning and risk assessment

### **Operative Agent**
- **Role**: Intelligent word guesser
- **Functions**:
  - Interprets spymaster's clues semantically
  - Evaluates board words for clue relevance
  - Makes strategic guessing decisions (including N+1 logic)
  - Manages turn-ending and passing logic
- **AI Challenge**: Natural language understanding and confidence modeling

## Technology Stack

- **Agent Framework**: Google ADK (Agent Development Kit)
- **AI Models**: Gemini 2.0 Flash for natural language reasoning
- **Language**: Python 3.10
- **Communication**: ADK multi-agent patterns (Agent-as-Tool, Shared Session State, Workflow Agents)
- **Testing**: pytest with custom game simulation framework

## Game Flow

1. **Setup**: Game Master initializes 5x5 word board with hidden identities
2. **Spymaster Turn**: Analyzes board, generates clue (word + number)
3. **Operative Turn**: Interprets clue, makes up to N+1 guesses
4. **Validation**: Game Master processes guesses, updates state
5. **Repeat**: Continue until all red words found or game over

## Key Innovation

The system uses **sophisticated prompt engineering** to achieve human-level strategic reasoning in Codenames™, focusing on:
- Multi-word semantic clustering for clue generation
- Risk-aware decision making to avoid the assassin
- Dynamic confidence thresholds for optimal guessing

## Competition Alignment

Designed for IEEE CogTech Competition scoring:
- **Primary Metric**: Minimize turns to find all red words
- **Penalty System**: 25-point maximum for losses (assassin hit, all blue words revealed)
- **Optimization Target**: Consistent wins in fewer turns

## Technical Documentation

- **Complete Design**: See `SpyGameDesign.md` for full technical specification
- **Testing Guide**: See `TESTING_GUIDE.md` for development workflow
- **Implementation**: All agent code in `src/` directory

