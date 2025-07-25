# SpyGame: Text-Based Interface Design

## Overview

SpyGame implements a clear, structured text-based interface that prioritizes system observability and multi-agent interaction visibility over visual complexity. This approach optimizes development time for core AI functionality while providing comprehensive game state tracking for evaluation and debugging.

## Example Game Session

### Initial Game Setup
```
--- SPYGAME: Cooperative AI ---

Initial Game Board:
🟥 RED WORDS:     ["Shark", "Whale", "Ocean", "Coral"]
🟦 BLUE WORDS:    ["Car", "Plane", "Train", "Bus"]
⚪ NEUTRAL WORDS: ["Tree", "Book", "Lamp", "Chair"]
💀 ASSASSIN:      ["Bomb"]

-- Unrevealed Words (Current Board State) --
Shark, Whale, Ocean, Coral, Car, Plane, Train, Bus, Tree, Book, Lamp, Chair, Bomb

--- Starting Turn 1 ---
```

### Game Loop Progression
```
--- Turn 1 ---
🎯 Spymaster (Clue Giver) provides clue: "Sea", 2

👀 Operative (Guesser) attempts guess: "Whale"
Game Master: "Whale" is RED. (Red words remaining: 3)

👀 Operative (Guesser) attempts guess: "Shark"
Game Master: "Shark" is RED. (Red words remaining: 2)

→ Guesses complete for clue "Sea", 2. Turn ends.

-- Board State After Turn 1 --
Revealed: Whale (RED), Shark (RED)
Unrevealed: Ocean, Coral, Car, Plane, Train, Bus, Tree, Book, Lamp, Chair, Bomb

--- Starting Turn 2 ---
🎯 Spymaster (Clue Giver) provides clue: "Travel", 1

👀 Operative (Guesser) attempts guess: "Bomb"
Game Master: "Bomb" is ASSASSIN. IMMEDIATE GAME OVER.
```

### Game Termination
```
*** GAME OVER ***
Result: ASSASSIN WORD FOUND! Team failed to find all red words.

Final Scores:
Red Words Found: 2 / 4
Blue Words Revealed: 0
Neutral Words Revealed: 0
Assassin Revealed: Yes

Total Turns Taken: 2
Final Score: 25 (Maximum penalty - IEEE scoring)
```

## Design Rationale

### **Clear Agent Roles**
Explicitly identifies which agent performs each action (🎯 Spymaster, 👀 Operative) making multi-agent interaction transparent for evaluation and debugging.

### **Game Master Authority**
All state changes and rule validations are explicitly attributed to the Game Master, emphasizing its role as the central arbiter and demonstrating proper multi-agent architecture.

### **Comprehensive State Tracking**
- **Current Board State**: Shows unrevealed words at critical decision points
- **Progress Indicators**: Real-time tracking of remaining words and game status  
- **Turn Structure**: Clear delineation of game phases and decision boundaries
- **Immediate Feedback**: Instant validation and consequence of each guess

### **Evaluation-Friendly Output**
- **Decision Traceability**: Complete game history for post-analysis
- **Performance Metrics**: All IEEE competition scoring data included
- **Error Conditions**: Clear indication of game termination reasons
- **Agent Reasoning Visibility**: Easy to follow multi-agent decision processes

## Technical Benefits

This interface design supports the competition submission by:

- **Maximizing Development Efficiency**: No time spent on UI frameworks during hackathon constraints
- **Enhancing System Observability**: Judges can easily trace agent interactions and validate AI reasoning
- **Providing Complete Logging**: Full game state history for performance analysis and debugging
- **Demonstrating Architecture**: Multi-agent coordination patterns clearly visible in output

The structured text format ensures that the sophisticated AI reasoning and multi-agent coordination remain the focus of evaluation, while providing all necessary information for comprehensive system assessment.

