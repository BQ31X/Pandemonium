# Agent Testing Guide

Quick guide for testing our agents during the hackathon. **Use these tools to avoid breaking shared code!**

## 🚀 Quick Start

### Test Everything (before commits)
```bash
python test_agents.py
```

### Test Individual Agent (while developing)
```bash
python test_agents.py spymaster
python test_agents.py operative  
python test_agents.py gamemaster
```

### Safe Commit (tests automatically)
```bash
./check_and_commit.sh "your commit message"
```

## 📋 Available Commands

| Command | What it does |
|---------|--------------|
| `python test_agents.py` | Test all agents |
| `python test_agents.py spymaster` | Test just spymaster |
| `python test_agents.py spymaster operative` | Test multiple agents |
| `python test_agents.py --list` | Show available agents |
| `./check_and_commit.sh "message"` | Test + commit if passed |

## 🛠️ Development Workflow

### 1. Before You Start Working
```bash
# Make sure everything works
python test_agents.py
```

### 2. While Developing
```bash
# Test just your agent frequently
python test_agents.py [your-agent-name]
```

### 3. Before Committing
```bash
# Option A: Test then commit manually
python test_agents.py
git add .
git commit -m "your message"

# Option B: Auto-test and commit
./check_and_commit.sh "your message"
```

## ⚡ Super Quick Tests

If you just want to check if an agent loads:
```bash
ADK_AGENT=spymaster python -c "from src import root_agent; print('✅ Works')"
```

## 🚨 If Tests Fail

1. **Don't commit broken code!**
2. Check which agent failed in the output
3. Fix the issue (usually missing imports or syntax errors)
4. Re-run tests
5. Only commit when all tests pass

## 🎯 Available Agents

- `telephone` - Original telephone game
- `day_trip` - Day planning agent  
- `spymaster` - Gives clues for word game
- `operative` - Guesses words from clues
- `gamemaster` - Orchestrates the game

## 💡 Tips

- **Run tests frequently** - catch issues early
- **Test your agent after every change** - use `python test_agents.py [agent-name]`
- **Use the auto-commit script** - it prevents broken commits
- **If unsure, test everything** - it only takes 5 seconds

---

*This testing setup ensures we maintain working code throughout the hackathon. When in doubt, test! 🧪* 