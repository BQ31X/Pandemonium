# SpyGame: Technical Implementation Explanation

## 1. Multi-Agent Workflow

SpyGame implements a coordinated multi-agent system where three specialized agents collaborate to play a word-guessing game. The workflow follows a structured turn-based pattern:

### Core Game Loop:
1. **Game Master initializes** 5x5 word board with hidden identities (Red, Blue, Neutral, Assassin)
2. **Spymaster analyzes** full board state (sees all word identities)
3. **Spymaster generates** single-word clue + number using Gemini 2.0 Flash reasoning
4. **Operative interprets** clue and evaluates visible board words for relevance
5. **Operative makes guesses** (up to N+1) via semantic association
6. **Game Master validates** each guess, updates state, determines turn continuation
7. **Process repeats** until win condition (all red words found) or loss condition (Assassin hit or all Blue words hit)

### Agent Communication Pattern:
- **Tool-based interaction**: Agents call exposed functions rather than direct messaging
- **Shared state management**: Game Master maintains canonical truth
- **Workflow orchestration**: Clear turn-based progression with state transitions

## 2. Key Agent Modules

### **Game Master Agent** (`src/gamemaster.py`)
- **Role**: Central orchestrator, rule enforcer, state manager
- **Core Functions**:
  - `submit_clue(clue_word, number)`: Validates and logs Spymaster clues
  - `submit_guess(word)`: Processes Operative guesses, updates board state
  - `get_current_board_state(reveal_identities)`: Provides appropriate view to each agent
- **State Management**: Maintains shared session dictionary with board state, scores, turn tracking
- **Rule Enforcement**: IEEE competition scoring, constraint validation, win/loss detection

### **Spymaster Agent** (`src/spymaster.py`)
- **Role**: Strategic clue generator with full board knowledge
- **AI Challenge**: Multi-word semantic clustering while avoiding dangerous associations
- **Prompt Engineering Focus**: 
  - Analyze red/blue/neutral/assassin word distributions
  - Generate clues connecting multiple red words semantically
  - Apply strict constraints (not on board, single word, no direct forms)
  - Risk assessment to avoid assassin and opponent words
- **Output Format**: Structured `{"clue_word": str, "number": int}` responses

### **Operative Agent** (`src/operative.py`)
- **Role**: Clue interpreter and word guesser
- **AI Challenge**: Natural language understanding and confidence modeling
- **Reasoning Process**:
  - Semantic association between clue and visible board words
  - Risk assessment for each potential guess
  - Strategic N+1 guess logic (extra guess based on high confidence)
  - Pass/continue decision making
- **Decision Framework**: Balances maximizing correct guesses vs. minimizing dangerous mistakes

## 3. Technology Integration

### **Google ADK Framework**
- **Agent-as-Tool Pattern**: Game Master exposes callable functions to other agents
- **Shared Session State**: Centralized dictionary maintaining game truth
- **Workflow Agents**: Turn-based orchestration with clear state transitions

### **Gemini 2.0 Flash Integration**
- **Spymaster**: Complex semantic reasoning for clue generation
- **Operative**: Natural language understanding for clue interpretation
- **Prompt Design**: Structured prompts enforcing game rules and output formats
- **Error Handling**: Retry logic for malformed LLM responses

### **Tool Ecosystem**
- **Internal Tools**: Game Master functions (`submit_clue`, `submit_guess`, `get_current_board_state`)
- **ADK Tools**: Agent registration, communication, and state management
- **Testing Tools**: Custom simulation framework for end-to-end game evaluation

## 4. User Interface & System Output

### **Text-Based Interface Design**
SpyGame implements a structured text-based interface optimized for clarity and technical demonstration rather than visual appeal. This design choice prioritizes:

- **Development efficiency**: No time spent on UI frameworks during hackathon constraints
- **System observability**: Clear visibility into multi-agent decision processes
- **Judge evaluation**: Easy traceability of agent interactions and game progression

### **Interface Architecture**
```
🎯 Spymaster (Clue Giver) provides clue: "Sea", 2
👀 Operative (Guesser) attempts guess: "Whale"  
Game Master: "Whale" is RED. (Red words remaining: 3)
→ Guesses complete for clue "Sea", 2. Turn ends.
```

### **Key Interface Features**
- **Agent Role Identification**: Emoji and role labels clearly distinguish agent actions
- **Game Master Authority**: All state changes and validations explicitly attributed to Game Master
- **Progress Tracking**: Real-time updates on remaining words and game status
- **Turn Structure**: Clear delineation of game phases and decision points
- **Comprehensive Logging**: Complete game history for post-analysis and debugging

### **Output Formatting Strategy**
- **Initial Setup**: Full board composition with word categories revealed
- **Turn Progression**: Structured clue → guess → validation → state update cycle
- **State Visibility**: Current board state shown after significant changes
- **Game Termination**: Complete summary with performance metrics and termination reason

## 5. Observability & Testing

### **Testing Infrastructure**
- **Unit Tests**: Individual agent function validation
- **Integration Tests**: Multi-agent interaction scenarios
- **End-to-End Simulation**: Full game runs with performance metrics
- **CI/CD Pipeline**: Automated testing on every commit via GitHub Actions

### **Performance Metrics**
- **Primary**: Average turns to win (IEEE competition standard)
- **Secondary**: Win rate, assassin avoidance, clue effectiveness
- **Agent-Specific**: Spymaster clue quality, Operative guess accuracy

### **Debugging & Analysis**
- **Game Logs**: Structured output showing decision points and reasoning
- **State Tracking**: Complete game state history for post-game analysis
- **LLM Response Monitoring**: Prompt effectiveness and response quality tracking

## 6. Known Limitations & Evolution Areas

### **Current Implementation Constraints**
- **Vocabulary Scope**: Initially using curated word set for consistency
- **Deterministic Testing**: LLM non-determinism requires statistical validation approaches
- **Performance Optimization**: Initial focus on correctness over speed

### **Areas Likely to Evolve During Implementation**
- **Prompt Engineering**: Iterative refinement based on agent performance
- **N+1 Guess Logic**: May implement simpler version initially, enhance later
- **Risk Assessment**: Confidence thresholds and decision boundaries will be tuned
- **Memory Integration**: Potential addition of cross-game learning capabilities

### **Technical Debt Considerations**
- **LLM Call Optimization**: May need caching or response optimization for competition
- **Error Recovery**: Robust handling of edge cases in LLM responses
- **Scalability**: Current design optimized for single-game sessions

## 7. Implementation Strategy

Given hackathon constraints, development follows a phased approach:

**Phase 1 (Current)**: Core functionality with basic agent intelligence
**Phase 2**: Enhanced strategy and competition alignment  
**Phase 3**: Advanced AI reasoning and optimization

This document will be updated as implementation reveals practical challenges and solutions that differ from initial design assumptions.

---

*Last updated: Hackathon Day 1 - Subject to revision based on implementation discoveries*

