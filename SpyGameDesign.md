# **Codenames AI: Tech Design Document** {#codenames-ai:-tech-design-document}

[Codenames AI Design Document](#codenames-ai:-tech-design-document)

[1\. Project Overview](#1.-project-overview)

[1.1 Game Description](#1.1-game-description)

[1.2 Overall Objective](#1.2-overall-objective)

[1.3 Multi-Agent Architecture](#1.3-multi-agent-architecture)

[1.4 Communication Patterns](#1.4-communication-patterns)

[2\. Agent Design: Game Master Agent](#2.-agent-design:-game-master-agent)

[2.1 Name/Role & Persona](#2.1-name/role-&-persona)

[2.2 Inputs](#2.2-inputs)

[2.3 Outputs](#2.3-outputs)

[2.4 Actions/Behavior (Game Loop & Rule Enforcement)](#2.4-actions/behavior-\(game-loop-&-rule-enforcement\))

[2.5 Tools Exposed (for other Agents to use)](#2.5-tools-exposed-\(for-other-agents-to-use\))

[2.6 Internal Logic/Strategy (Core Functionality & Rule Enforcement)](#2.6-internal-logic/strategy-\(core-functionality-&-rule-enforcement\))

[2.7 Shared Session State (Managed by Game Master)](#2.7-shared-session-state-\(managed-by-game-master\))

[3\. Agent Design: Spymaster (Clue Giver) Agent](#3.-agent-design:-spymaster-\(clue-giver\)-agent)

[3.1 Name/Role & Persona](#3.1-name/role-&-persona)

[3.2 Inputs](#3.2-inputs)

[3.3 Outputs](#3.3-outputs)

[3.4 Actions/Behavior (Turn Flow)](#3.4-actions/behavior-\(turn-flow\))

[3.5 Tools](#3.5-tools)

[3.6 Internal Logic/Strategy (LLM Prompting Focus)](#3.6-internal-logic/strategy-\(llm-prompting-focus\))

[3.7 Constraints on Clue Word Generation](#3.7-constraints-on-clue-word-generation)

[4\. Agent Design: Operative (Guesser) Agent](#4.-agent-design:-operative-\(guesser\)-agent)

[4.1 Name/Role & Persona](#4.1-name/role-&-persona)

[4.2 Inputs](#4.2-inputs)

[4.3 Outputs](#4.3-outputs)

[4.4 Actions/Behavior (Turn Flow)](#4.4-actions/behavior-\(turn-flow\))

[4.5 Tools](#4.5-tools)

[4.6 Internal Logic/Strategy (LLM Prompting Focus)](#4.6-internal-logic/strategy-\(llm-prompting-focus\))

[4.7 Advanced Strategy Considerations (Optional if Time Permits)](#4.7-advanced-strategy-considerations-\(optional-if-time-permits\))

[5\. User Interface (Text-Based) Design](#5.-user-interface-\(text-based\)-design)

[5.1 Initial Game Setup Output](#5.1-initial-game-setup-output)

[5.2 Running Game Loop Output](#5.2-running-game-loop-output)

[5.3 Game End Output](#5.3-game-end-output)

[6\. Proposed Development Versions / Phases](#6.-proposed-development-versions-/-phases)

[6.1 Version 1: Core Functionality (Hackathon MVP)](#6.1-version-1:-core-functionality-\(hackathon-mvp\))

[6.2 Version 2: Enhanced Strategy & Competition Alignment (Basic IEEE Submission)](#6.2-version-2:-enhanced-strategy-&-competition-alignment-\(basic-ieee-submission\))

[6.3 Version 3: Advanced Intelligence & Research (Competitive IEEE Submission)](#6.3-version-3:-advanced-intelligence-&-research-\(competitive-ieee-submission\))

[7\. Technology Stack & Framework](#7.-technology-stack-&-framework)

[8\. Assumptions and Limitations](#8.-assumptions-and-limitations)

[9\. Testing Strategy](#9.-testing-strategy)

[9.1 Levels of Testing:](#9.1-levels-of-testing:)

[9.2 LLM-Specific Testing Considerations:](#9.2-llm-specific-testing-considerations:)

[9.3 Evaluation Metrics:](#9.3-evaluation-metrics:)

[Appendix 1](#appendix-1)

[Revised Key Data Structures and Terminology](#revised-key-data-structures-and-terminology)

[1\. Shared Session State Keys (Managed by Game Master)](#1.-shared-session-state-keys-\(managed-by-game-master\))

[2\. Tool Parameters & Return Values](#2.-tool-parameters-&-return-values)

[3\. Agent-Specific Actions/Outputs](#3.-agent-specific-actions/outputs)

## **1\. Project Overview** {#1.-project-overview}

### **1.1 Game Description** {#1.1-game-description}

This project aims to develop an AI system to play the cooperative word association game Codenames by Vlaada Chvatil. The game involves two teams (Red and Blue), each with a Spymaster and an Operative. This design focuses on a **single-team cooperative play** where the Red Team (Spymaster and Operative) attempts to identify all their team's words.

### **1.2 Overall Objective** {#1.2-overall-objective}

The primary objective for the Red Team is to identify all of its 'red' words on the game board in as **few turns as possible**. The game has strict rules regarding clue giving, guessing, and penalties for incorrect guesses.

### **1.3 Multi-Agent Architecture** {#1.3-multi-agent-architecture}

The system will be composed of three primary agents interacting with each other:

* **Game Master Agent:** The central arbiter and state manager of the game.  
* **Spymaster (Clue Giver) Agent:** Responsible for providing clues.  
* **Operative (Guesser) Agent:** Responsible for interpreting clues and making guesses.

### **1.4 Communication Patterns** {#1.4-communication-patterns}

The agents will communicate using a combination of established multi-agent patterns:

* **Agent-as-a-Tool:** The Game Master will expose specific functions (tools) that the Spymaster and Operative agents can call to submit actions (clues, guesses) or request information (board state).  
* **Shared Session State:** The Game Master will maintain a single, canonical shared session state (a dictionary or similar structure) that represents the "truth" of the current game board and overall game status. Other agents can query this state via Game Master tools.  
* **Workflow Agents:** The overall game progression dictates a clear workflow: Game Master sets up \-\> Spymaster acts \-\> Operative acts \-\> Game Master processes and transitions to next turn.

## **2\. Agent Design: Game Master Agent** {#2.-agent-design:-game-master-agent}

### **2.1 Name/Role & Persona** {#2.1-name/role-&-persona}

* **Name/Role:** Game Master Agent  
* **Persona:** The impartial, authoritative, and consistent arbiter of the Codenames game. It acts as a rule enforcer, state manager, and neutral facilitator. It holds the "truth" of the game board, processes all actions, applies rules, tracks scores, and determines game-ending conditions.

### **2.2 Inputs** {#2.2-inputs}

The Game Master Agent receives inputs primarily through tool calls from the Spymaster and Operative agents:

* **From Spymaster (via submit\_clue tool):**  
  * clue\_word (string): The clue provided by the Spymaster.  
  * number (integer): The count associated with the clue.  
* **From Operative (via submit\_guess tool):**  
  * word (string): The word chosen by the Operative as a guess.  
* **Initial Game Setup (at game start, potentially from a setup script/user input):**  
  * word\_list (list of strings): All words for the game board.  
  * word\_identities (dictionary/mapping): The true identity (RED, BLUE, NEUTRAL, ASSASSIN) for each word.  
  * first\_team (string): Which team goes first (e.g., "RED").

### **2.3 Outputs** {#2.3-outputs}

The Game Master Agent's outputs are primarily the results of actions and updates to the game state:

* **To Spymaster/Operative (as tool call responses):**  
  * Result of a guess (e.g., "RED", "BLUE", "NEUTRAL", "ASSASSIN").  
  * Confirmation of a valid clue submission.  
  * Updated game status (game\_over boolean, red\_words\_remaining).  
  * The current game board state (visible words, or full identities for Spymaster).  
* **To Interface:**  
  * Formatted game log output.  
  * Final game results and scores.

### **2.4 Actions/Behavior (Game Loop & Rule Enforcement)** {#2.4-actions/behavior-(game-loop-&-rule-enforcement)}

The Game Master Agent orchestrates the entire game:

* **Game Initialization:** Sets up the game board, initializes scores, tracks turns, and makes initial board state available.  
* **Turn Management:** Manages whose turn it is (Spymaster \-\> Operative \-\> Game Master processing \-\> next Spymaster turn).  
* **Clue Processing:** Receives and validates clue\_word and number from the Spymaster, logs the clue.  
* **Guess Processing:** Receives and validates word from the Operative, reveals its identity, updates Shared Session State, determines outcome, applies penalties, checks for game-ending conditions, and communicates results.  
* **Game State Updates:** Maintains the canonical Shared Session State of the game board, tracks scores.  
* **Game Termination:** Detects win/loss conditions and declares the game over.

### **2.5 Tools Exposed (for other Agents to use)** {#2.5-tools-exposed-(for-other-agents-to-use)}

The Game Master acts as a service provider, exposing the following tools:

* submit\_clue(clue\_word: str, number: int): Allows Spymaster to submit a clue.  
* submit\_guess(word: str): Allows Operative to submit a guess.  
* get\_current\_board\_state(reveal\_identities=False): Provides current board state (full identities if reveal\_identities=True for Spymaster).

### **2.6 Internal Logic/Strategy (Core Functionality & Rule Enforcement)** {#2.6-internal-logic/strategy-(core-functionality-&-rule-enforcement)}

The Game Master's internal logic is deterministic and rule-based:

* **Board State Management:** Accurate and secure tracking of word identities and revealed status.  
* **Rule Validation:** Rigorous checking of all submitted clues and guesses.  
* **Scoring & Progress Tracking:**  
  * Maintains current scores.  
  * **IEEE Scoring Rules (as per Cog2025 Codenames AI Competition):**  
    * **Objective:** Identify all red words in as **few turns as possible**.  
    * **Normal Game Completion:** If all red words are found, score is awarded **based on the number of turns taken** (lower turns \= better score).  
    * **Penalty/Loss Conditions (Maximum Score of 25 points):** If the Operative guesses **all blue words** or the **Assassin word**.  
* **Turn Progression:** Logical advancement of the game through phases.  
* **Win/Loss Condition Detection:** Precise detection of game-ending conditions.  
* **Error Handling:** Manages invalid inputs gracefully.

### **2.7 Shared Session State (Managed by Game Master)** {#2.7-shared-session-state-(managed-by-game-master)}

The Game Master is the authoritative source and manager of the central sessionstate dictionary:

* board\_words\_and\_identities: (e.g., \[{'word': 'SHARK', 'identity': 'RED', 'revealed': False}, ...\])  
* revealed\_words: (e.g., \['WHALE', 'TRAIN'\])  
* current\_turn\_number: (integer)  
* current\_player\_to\_act: (e.g., "SPYMASTER", "OPERATIVE")  
* current\_clue: (e.g., {'word': 'SEA', 'number': 2, 'given\_by': 'SPYMASTER'})  
* guesses\_made\_this\_clue: (integer)  
* red\_words\_found\_count: (integer)  
* blue\_words\_revealed\_count: (integer)  
* neutral\_words\_revealed\_count: (integer)  
* game\_status: (e.g., "in\_progress", "red\_team\_wins", "game\_over\_assassin")

---

## **3\. Agent Design: Spymaster (Clue Giver) Agent** {#3.-agent-design:-spymaster-(clue-giver)-agent}

### **3.1 Name/Role & Persona** {#3.1-name/role-&-persona}

* **Name/Role:** Spymaster (Clue Giver) Agent  
* **Persona:** The strategic, deductive, and clear communicator for the Red Team. It aims to provide the most effective single-word clue and number that connects as many 'red' words as possible, while carefully avoiding association with opponent's words or the assassin.

### **3.2 Inputs** {#3.2-inputs}

* **From Game Master (via get\_current\_board\_state tool):**  
  * full\_board\_state (dictionary/list): The true identity (Red, Blue, Neutral, Assassin) of *all* unrevealed words.  
  * red\_words\_remaining (integer): Count of unrevealed 'red' words.  
  * game\_status (string): Current status of the game.

### **3.3 Outputs** {#3.3-outputs}

* **Clue Action:**  
  * clue\_word (string): A single word (not on the board, adheres to constraints).  
  * number (integer): Count of words the clue relates to.

### **3.4 Actions/Behavior (Turn Flow)** {#3.4-actions/behavior-(turn-flow)}

* **Receive Board State:** Awaits full\_board\_state.  
* **Analyze Board:** Identifies all unrevealed words by identity.  
* **Generate Potential Clues:** Brainstorms clues that semantically connect 'red' words.  
* **Evaluate Clue Safety & Effectiveness:** Checks safety (avoiding blue, neutral, assassin) and effectiveness (strength of connection to red words).  
* **Select Best Clue:** Chooses clue\_word and number maximizing red words while minimizing risk.  
* **Submit Clue:** Calls submit\_clue tool on Game Master.  
* **Turn End:** Concludes turn after submitting clue.

### **3.5 Tools** {#3.5-tools}

* get\_current\_board\_state(reveal\_identities=True): From Game Master.  
* submit\_clue(clue\_word: str, number: int): To Game Master.

### **3.6 Internal Logic/Strategy (LLM Prompting Focus)** {#3.6-internal-logic/strategy-(llm-prompting-focus)}

* **Semantic Association & Clustering:** Ability to find common semantic themes.  
* **Negative Constraint Reasoning:** Crucially, avoiding connections to undesirable words.  
* **Ambiguity Detection:** Identifying if a clue could lead to wrong guesses.  
* **Risk Aversion:** Prioritizing safety over quantity, especially concerning the assassin.  
* **Game State Awareness:** Adjusting strategy based on remaining red words.  
* **Clue Generation:** Creativity in generating valid clues.

### **3.7 Constraints on Clue Word Generation** {#3.7-constraints-on-clue-word-generation}

The clue\_word must adhere to these rules:

1. **Not on the Board:** Must not be any word currently on the game board.  
2. **No Direct Word Forms/Roots:** Should not be a different grammatical form or share the exact same root as any word on the board (e.g., if "FISH" is on board, "FISHING" disallowed).  
3. **Single Word Only:** Must be a single, standalone word (no phrases, hyphenated words).  
4. **No Proper Nouns (General Rule):** Generally avoid specific names (people, cities), primarily common nouns, verbs, adjectives.  
5. **Semantic Connection Only:** Based on meaning, not phonetic similarity or spelling.  
6. **No Game Mechanic Words:** Must not be words related to game mechanics (e.g., "Assassin", "Red", "Blue").

---

## **4\. Agent Design: Operative (Guesser) Agent** {#4.-agent-design:-operative-(guesser)-agent}

### **4.1 Name/Role & Persona** {#4.1-name/role-&-persona}

* **Name/Role:** Operative (Guesser) Agent  
* **Persona:** A careful, logical, and risk-aware interpreter. It aims to maximize correct guesses based on the Spymaster's clue while minimizing the risk of hitting opponent's or assassin words.

### **4.2 Inputs** {#4.2-inputs}

* **From Spymaster (via Game Master or direct signal):**  
  * clue\_word (string)  
  * number (integer)  
* **From Game Master (via get\_current\_board\_state tool):**  
  * visible\_board (list of strings): Words currently visible (unrevealed).  
  * guesses\_made\_this\_turn (integer): Guesses already made in current turn.  
  * red\_words\_remaining (integer): Count of unrevealed red words.  
  * game\_status (string): Current game status.

### **4.3 Outputs** {#4.3-outputs}

* **Guess Action:**  
  * word\_to\_guess (string): A word from visible\_board.  
  * OR action: "pass": A signal to end its turn.

### **4.4 Actions/Behavior (Turn Flow)** {#4.4-actions/behavior-(turn-flow)}

* **Receive Clue:** Awaits clue\_word and number.  
* **Guessing Phase (up to N+1 guesses):**  
  * Analyzes clue vs. visible\_board.  
  * Identifies most relevant unrevealed word(s).  
  * Prioritizes high confidence, low risk words.  
  * Executes submit\_guess tool call.  
  * Receives and processes guess feedback.  
* **Strategic Passing:** Decides to pass based on guesses made, remaining guesses (within N+1 limit), confidence, and risk.  
* **Turn End:** Concludes when it passes, hits wrong word, or N+1 limit is reached.

### **4.5 Tools** {#4.5-tools}

* get\_current\_board\_state(): From Game Master.  
* submit\_guess(word: str): To Game Master.

### **4.6 Internal Logic/Strategy (LLM Prompting Focus)** {#4.6-internal-logic/strategy-(llm-prompting-focus)}

* **Clue Interpretation:** Understanding the semantic field of the clue.  
* **Word Association:** Matching board words to the clue's semantic field.  
* **Risk Assessment:** Evaluating likelihood of a word being 'red' vs. 'blue' or 'assassin'.  
* **Confidence Thresholds:** Implicit threshold for making a guess.  
* **Game State Awareness:** Considering remaining red words and guesses made.  
* **Passing Logic:** Decision process for when to pass.

### **4.7 Advanced Strategy Considerations (Optional if Time Permits)** {#4.7-advanced-strategy-considerations-(optional-if-time-permits)}

* **Strategic N+1 Guessing (Leveraging "Leftover Information"):** For later versions, the Operative could maintain memory of past clues and unrevealed words, re-evaluating them in subsequent turns for a highly strategic N+1 guess. This requires:  
  * Maintaining historical context of past clues.  
  * Dynamic re-evaluation of the board state based on cumulative information.  
  * Cross-clue inference.

---

## **5\. User Interface (Text-Based) Design** {#5.-user-interface-(text-based)-design}

The primary user interface will be a clear, informative text-based console output, managed by the Game Master.

### **5.1 Initial Game Setup Output** {#5.1-initial-game-setup-output}

* Displays the full initial game board (words only, identities hidden to Operative).  
* Indicates which team (Red) goes first.

### **5.2 Running Game Loop Output** {#5.2-running-game-loop-output}

* **Before Spymaster's turn:** Clearly indicates "Red Spymaster's Turn."  
* **After Spymaster gives clue:** Prints the clue, e.g., Spymaster clue: \[CLUE\_WORD\] \[NUMBER\].  
* **Before Operative's guess:** Indicates "Red Operative's Turn."  
* **After each Operative guess:**  
  * Prints the guess made: Operative guesses: \[GUESSED\_WORD\].  
  * Prints the result of the guess: Result: \[RED/BLUE/NEUTRAL/ASSASSIN\].  
  * If a non-red word is guessed, indicates turn change or game over.  
  * Updates and displays the current visible board (with revealed words marked appropriately).  
* **After turn ends:** Summarizes current scores/remaining words, indicates "End of Turn \[X\]".

### **5.3 Game End Output** {#5.3-game-end-output}

* Clearly states which team won (Red Team wins / Blue Team wins).  
* Displays the final score according to the IEEE rules.  
* Shows the final revealed state of the entire board.

---

## **6\. Proposed Development Versions / Phases** {#6.-proposed-development-versions-/-phases}

This phased approach allows for a Minimum Viable Product (MVP) for the hackathon, followed by progressive enhancements for a more competitive IEEE submission.

#### **6.1 Version 1: Core Functionality (Hackathon MVP)** {#6.1-version-1:-core-functionality-(hackathon-mvp)}

* **Goal:** Establish a complete, playable, albeit basic, single-team Codenames game.  
* **Game Master:** Basic state management, turn flow, rule enforcement (clue/guess validation), basic scoring (win/loss declaration), core win/loss detection.  
* **Spymaster Agent:** Generates any valid clue for at least one red word, adheres to basic constraints, prioritizes avoiding Assassin. No sophisticated ambiguity/quantity focus.  
* **Operative Agent:** Guesses based only on current clue, up to N words (no N+1), stops on non-red guess or N exhaustion.  
* **User Interface:** Simple running log, basic game end messages.

#### **6.2 Version 2: Enhanced Strategy & Competition Alignment (Basic IEEE Submission)** {#6.2-version-2:-enhanced-strategy-&-competition-alignment-(basic-ieee-submission)}

* **Goal:** Improve agent intelligence and fully align with the IEEE competition rules, including the scoring system.  
* **Game Master:** Fully implements IEEE scoring system (turns for wins, 25 points for losses). Robust error handling.  
* **Spymaster Agent:** Aims to connect multiple red words (2+) safely. Begins basic ambiguity detection (avoids obvious blue/neutral associations). Adheres to all refined clue constraints.  
* **Operative Agent:** Implements basic N+1 Guess Logic (makes one extra guess if highly confident about a word related to *current* clue). Basic risk assessment for N+1.  
* **User Interface:** More detailed turn logs, clear final score display.

#### **6.3 Version 3: Advanced Intelligence & Research (Competitive IEEE Submission)** {#6.3-version-3:-advanced-intelligence-&-research-(competitive-ieee-submission)}

* **Goal:** Push the boundaries of LLM agent intelligence, incorporating complex strategies and potentially novel AI concepts.  
* **Spymaster Agent:** Highly sophisticated ambiguity detection. Generates complex clues for multiple, less obvious connections.  
* **Operative Agent:** Advanced N+1 Guess Logic leveraging "Leftover Information" from previous clues. Dynamic risk assessment based on remaining word types.  
* **Shared Knowledge Base (Optional):** Explore agents leveraging a shared, curated set of semantic associations or strategic preferences.  
* **Evaluation & Analysis:** Implement robust logging for agent thought processes and develop tools for deeper analysis of game outcomes and strategy effectiveness.

---

## **7\. Technology Stack & Framework** {#7.-technology-stack-&-framework}

This project will leverage the following technologies for its implementation:

* **Agent Development Kit (ADK):** The foundational framework for orchestrating the multi-agent system, managing agent interactions, tool calls, and shared state.  
* **Large Language Models (LLMs):** Google Gemini 2.5 Flash will be the primary LLM, serving as the "brain" for the Spymaster and Operative agents' natural language understanding, semantic reasoning, and decision-making.  
* **Python:** The primary programming language for implementing all agents, the Game Master logic, and the overall game environment.  
* **Other Potential Libraries (As Needed):**  
  * pytest: For robust unit and integration testing.  
  * sentence-transformers: (Optional) For explicit word embedding generation and finer-grained semantic similarity calculations, potentially useful for Spymaster clue generation or Operative word evaluation beyond inherent LLM capabilities.  
  * nltk or spaCy: (Optional) For traditional NLP tasks like advanced tokenization, stemming/lemmatization, or Part-of-Speech tagging if specific linguistic rules are needed outside of LLM prompting.

---

## **8\. Assumptions and Limitations** {#8.-assumptions-and-limitations}

This section outlines key assumptions made during the design phase and known limitations, particularly relevant for the hackathon context versus potential future competition submissions.

1. **Agent Action Time Constraints & Looping Limits:**  
   * **Assumption:** Each agent will complete its turn and provide a valid action within a reasonable timeframe.  
   * **Limitation/Mitigation:** The Game Master Agent will enforce a maximum time limit for each agent's turn to prevent infinite loops or excessive computation. Internally, agents should incorporate maximum iteration limits for their reasoning processes.  
2. **Vocabulary List & Semantic Understanding:**  
   * **Hackathon Assumption:** For the hackathon MVP, the game will operate on a **pre-defined, curated list of words** (e.g., the original 395 Codenames words or a smaller, well-understood subset). This aims to minimize ambiguity and focus on debugging agent logic.  
   * **IEEE Competition Implication (Future Challenge):** The IEEE competition will use an *alternative, unknown, and potentially diverse word pool* (including slang, pop-culture terms). Adapting to such a dynamic and diverse vocabulary will be a key **future enhancement** (as part of Version 3), requiring more generalized LLM understanding rather than reliance on memorized associations.

---

## **9\. Testing Strategy** {#9.-testing-strategy}

Developing an effective testing strategy for an LLM-powered multi-agent system requires addressing both traditional software testing concerns and the unique challenges of non-deterministic AI.

### **9.1 Levels of Testing:** {#9.1-levels-of-testing:}

* **Unit Tests:** To verify the correctness of individual functions and components (e.g., Game Master's rule validation, tool functions, helper functions). pytest will be used.  
* **Integration Tests:** To verify that different agents and components interact correctly with each other and the Game Master, simulating single turn cycles and state transitions. pytest can be used.  
* **End-to-End / System Tests (Game Simulations):** To run full games from start to finish to evaluate overall system behavior and performance under various conditions, identifying robustness issues. Custom Python scripts will automate simulations and log results.

### **9.2 LLM-Specific Testing Considerations:** {#9.2-llm-specific-testing-considerations:}

* **Non-Determinism:** Acknowledging LLMs are probabilistic, testing will validate that prompts consistently elicit the *desired type* of reasoning and output format, rather than exact content.  
* **Retry Mechanisms:** Implementing and testing retry logic for LLM calls that fail or return malformed responses.

### **9.3 Evaluation Metrics:** {#9.3-evaluation-metrics:}

To quantitatively assess agent performance, the following metrics will be tracked during end-to-end game simulations:

* **Primary Competition Metric (IEEE-aligned):**  
  * **Average Turns to Win:** Mean number of turns to successfully find all red words (lower is better).  
  * **Win Rate:** Percentage of games won by the Red Team.  
* **Loss Condition Frequency:**  
  * **Assassin Hit Rate:** Frequency of hitting the assassin word (lower is better).  
  * **Blue Team Win Rate:** Frequency of Blue Team winning (e.g., due to Red Operative revealing all blue words).  
* **Agent-Specific Metrics (for analysis):**  
  * **Spymaster:** Average Clue Number, Clue Effectiveness (intended vs. guessed words).  
  * **Operative:** Guess Accuracy (correct red guesses vs. total), N+1 Guess Utilization/Success Rate.

# Appendix 1 {#appendix-1}

## Revised Key Data Structures and Terminology {#revised-key-data-structures-and-terminology}

This section consolidates the names of key variables, parameters, and data structures used throughout the design document to ensure consistency during implementation.

### 1\. Shared Session State Keys (Managed by Game Master) {#1.-shared-session-state-keys-(managed-by-game-master)}

These are the primary keys within the central `sessionstate` dictionary that represents the game's authoritative truth:

* `board_words_and_identities`: List of dictionaries, each describing a word on the board (`{'word': '...', 'identity': '...', 'revealed': False/True}`).  
* `revealed_words`: List of strings, words that have been guessed and revealed on the board.  
* `current_turn_number`: Integer, the current turn count of the game.  
* `current_player_to_act`: String, indicates whose turn it is (e.g., "SPYMASTER", "OPERATIVE").  
* `current_clue`: Dictionary, contains details of the clue most recently given by the Spymaster for the current turn.  
  * `word` (within `current_clue`): String, the clue word.  
  * `number` (within `current_clue`): Integer, the number given with the clue.  
  * `given_by` (within `current_clue`): String, the agent that gave the clue (e.g., "SPYMASTER").  
* `guesses_made_this_clue`: Integer, count of guesses made by the Operative for the *current* clue.  
* `red_words_found_count`: Integer, cumulative count of red words revealed by the Red Team.  
* `blue_words_revealed_count`: Integer, cumulative count of blue words revealed by either team.  
* `neutral_words_revealed_count`: Integer, cumulative count of neutral words revealed.  
* `game_status`: String, current state of the game (e.g., "in\_progress", "red\_team\_wins", "game\_over\_assassin", "blue\_team\_wins").

### 2\. Tool Parameters & Return Values {#2.-tool-parameters-&-return-values}

These are the inputs and outputs for the methods/functions that agents call on the Game Master:

* **`submit_clue` tool (Game Master input parameters):**  
  * `clue_word`: String, the word given as a clue by the Spymaster.  
  * `number`: Integer, the number given with the clue.  
* **`submit_clue` tool (Game Master output):**  
  * `success`: Boolean, `True` if the clue submission was valid and accepted.  
  * `message`: String, provides feedback on the submission (e.g., "Clue received," "Invalid clue: word on board").  
* **`submit_guess` tool (Game Master input parameter):**  
  * `word`: String, the word chosen by the Operative for a guess.  
* **`submit_guess` tool (Game Master output):**  
  * `guess_result`: String, the identity of the guessed word (e.g., "RED", "BLUE", "NEUTRAL", "ASSASSIN").  
  * `game_over`: Boolean, `True` if the game ended as a result of this guess.  
  * `red_words_remaining`: Integer, number of red words still unrevealed after the guess.  
  * `message`: String, provides feedback on the guess (e.g., "Correct\!", "Wrong\!").  
* **`get_current_board_state` tool (Game Master input parameter):**  
  * `reveal_identities`: Boolean, `True` if the caller (Spymaster) needs to see hidden word identities; `False` if only visible words are needed (for Operative).  
* **`get_current_board_state` tool (Game Master output structure):**  
  * `full_board_state`: List of dictionaries (`{'word': '...', 'identity': '...', 'revealed': False/True}`). **Only returned if `reveal_identities` was `True`.**  
  * `visible_board`: List of strings, words currently visible (unrevealed) on the board.  
  * `guesses_made_this_clue`: Integer, current count of guesses made for the active clue.  
  * `red_words_remaining`: Integer, count of unrevealed red words.  
  * `game_status`: String, current status of the game.

### 3\. Agent-Specific Actions/Outputs {#3.-agent-specific-actions/outputs}

These represent explicit actions or decision outcomes communicated by specific agents:

* `word_to_guess` (Operative): The specific string chosen by the Operative to be submitted as a guess.  
* `action: "pass"` (Operative): A conceptual signal indicating the Operative's decision to end its guessing turn. This would likely be implemented as a specific string value for an `operative_action` variable or as the return value of a method.

---

