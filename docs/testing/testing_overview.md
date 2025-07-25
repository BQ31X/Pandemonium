# Testing Overview - SpyGame Development

## 🎯 Purpose
This directory contains all testing tools and documentation for coordinated SpyGame development. Choose the right testing approach for your current task.

## 📁 Testing Categories

### 📋 [Design Philosophy](./testing_design_philosophy.md) - "Why we built it this way"
**Strategic decisions about LLM vs deterministic approaches**
- Where we use LLM (agents being tested) vs deterministic methods (testing infrastructure)
- Benefits: reproducible evaluation, clean separation of concerns, competition readiness
- Rationale for judges and team coordination

**When to read:** Understanding our testing methodology, judge submissions, competition alignment

### 🔧 [Agent Testing](./agent_testing.md) - "Does my code work?"
**For ensuring your agents load and function correctly**
- Unit tests for agent imports and basic functionality
- CI pipeline integration  
- Pre-commit testing to prevent broken code
- Quick agent validation

**When to use:** Before committing code, after making agent changes, debugging import errors

### 🎲 [Prompt Testing](./prompt_testing.md) - "How good are my agent responses?"  
**For testing agent intelligence and prompt engineering**
- 250-word shared vocabulary pool
- Spymaster clue generation testing
- Operative guessing scenario testing
- Risk-aware word combinations
- Game state simulation (early/mid/late game)

**When to use:** Improving agent prompts, testing clue quality, coordinating vocabulary between teammates

### 🚀 Integration Testing *(Coming Soon)*
**For testing multi-agent workflows**
- GameMaster orchestration testing
- Spymaster → Operative communication flows
- End-to-end game simulation
- Performance benchmarking

**When to use:** Verifying complete system functionality, demo preparation

### 📊 Performance Testing *(Coming Soon)*
**For competition readiness**
- Automated game runs with scoring
- Response time analysis  
- Strategy effectiveness measurement
- IEEE competition simulation

**When to use:** Final optimization, competition preparation

## 🚀 Quick Start

### Just Starting Development?
1. **Check everything works**: Follow [Agent Testing Guide](./agent_testing.md)
2. **Test your prompts**: Use [Prompt Testing Guide](./prompt_testing.md) 
3. **Coordinate with team**: Share vocabulary and test results

### Working on Prompts?
→ **[Prompt Testing Guide](./prompt_testing.md)** - Word generation, scenario testing

### Committing Code?  
→ **[Agent Testing Guide](./agent_testing.md)** - Unit tests, CI validation

### Preparing for Demo/Competition?
→ **Integration & Performance Testing** *(guides coming soon)*

## 🛠️ Available Tools

| **Tool** | **Purpose** | **Location** | **Guide** |
|----------|-------------|--------------|-----------|
| **Design Philosophy** | LLM vs deterministic approach rationale | [Design Philosophy](./testing_design_philosophy.md) | For judges & methodology |
| `test_agents.py` | Agent import/function testing | Root directory | [Agent Testing](./agent_testing.md) |
| `shared_word_pool.py` | 250-word competition vocabulary | Root directory | [Prompt Testing](./prompt_testing.md) |
| `spymaster_tester.py` | Scenario generation for prompts & operative testing | Root directory | [Prompt Testing](./prompt_testing.md) |
| `check_and_commit.sh` | Automated test-then-commit | Root directory | [Agent Testing](./agent_testing.md) |
| CI Pipeline | Automated testing on push | `.github/workflows/` | [Agent Testing](./agent_testing.md) |

## 🤝 Team Coordination

### **For Team Member 1 (GameMaster/Backend):**
- Primary: [Agent Testing](./agent_testing.md) for solid infrastructure
- Secondary: Integration testing setup *(coming soon)*

### **For Team Member 2 (Operative/UI):**  
- Primary: [Prompt Testing](./prompt_testing.md) for clue interpretation
- Use shared vocabulary from `shared_word_pool.py`
- Coordinate scenarios with Spymaster developer

### **For Team Member 3 (Spymaster/Strategy):**
- Primary: [Prompt Testing](./prompt_testing.md) for clue generation  
- Focus on `spymaster_tester.py` tool for systematic prompt iteration
- Share test scenarios with Operative developer

## 📋 Development Workflow

```bash
# 1. Ensure code works (always)
python test_agents.py

# 2a. Test/improve Spymaster prompts (iterative)  
python spymaster_tester.py --late-game
# → Copy to ADK web interface for testing

# 2b. Test/improve Operative prompts (iterative)
python spymaster_tester.py -o --red 3 --blue 2
# → Copy "FOR OPERATIVE AGENT" section to ADK web interface

# 3. Commit safely
./check_and_commit.sh "your changes"

# 4. Coordinate with team
# → Share vocabulary, test scenarios, results
```

## 🆘 Getting Help

- **"My agent won't load"** → [Agent Testing Guide](./agent_testing.md)
- **"How do I test clue quality?"** → [Prompt Testing Guide](./prompt_testing.md)  
- **"Need word combinations"** → `python spymaster_tester.py --help`
- **"Tests failing?"** → Check the specific testing guide for troubleshooting

---

*Keep this overview updated as we add new testing tools and capabilities!*  
*When in doubt, test early and test often! 🧪* 