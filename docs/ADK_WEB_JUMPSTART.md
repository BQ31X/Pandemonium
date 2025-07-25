# ADK Web Interface - Quick Start Guide

## What is ADK Web?
The ADK (Agent Development Kit) web interface is an interactive testing environment that lets you chat with our AI agents through a clean web UI. It's perfect for testing prompts, agent behavior, and game interactions.

## Getting Started (2 minutes)

### 1. Environment Setup
```bash
# Activate the conda environment
conda activate agentic-hackathon

# Navigate to project directory
cd /path/to/Pandemonium
```

### 2. Launch an Agent
```bash
# Test the Spymaster (our main agent)
ADK_AGENT=spymaster adk web

# Test the Operative
ADK_AGENT=operative adk web  

# Test the GameMaster
ADK_AGENT=gamemaster adk web

# Use custom port if needed
ADK_AGENT=spymaster adk web --port 8001
```

### 3. Open Your Browser
- Go to `http://localhost:8000` (or whatever port you used)
- You'll see a clean chat interface with your selected agent

## Quick Testing Examples

### Spymaster Agent
Try these inputs to test clue generation:
```
Give me a clue for: JUMP, LEAP, HOP
```
```
Target words: APPLE, ORANGE. Avoid: TREE, JUICE
```

### Operative Agent  
Test word guessing:
```
Clue: MOVEMENT 3. What words might this relate to?
```

### GameMaster Agent
Test game coordination:
```
Start a new game with 5 red words and 4 blue words
```

## Pro Tips

### Agent Switching
- **Stop current agent**: `Ctrl+C` in terminal
- **Switch agent**: Change `ADK_AGENT=newagent` and rerun
- **Multiple agents**: Use different ports (`--port 8001`, `--port 8002`)

### Development Workflow
1. **Test changes**: Launch agent → Test in browser → Stop (`Ctrl+C`)
2. **Edit prompts**: Modify agent files in `src/`
3. **Relaunch**: Run `adk web` command again
4. **Verify**: Check behavior in browser

### Debugging
- **Agent not found**: Check `src/__init__.py` registration
- **Import errors**: Run `python test_agents.py [agent_name]` first
- **Port busy**: Use `--port XXXX` with different number

## Current Agent Status
- ✅ **SpymasterAgent**: Generates clues for word groups
- ✅ **OperativeAgent**: Guesses words based on clues  
- ✅ **GameMasterAgent**: Basic game coordination
- 📝 **All agents**: Ready for prompt engineering & enhancement

## Need Help?
- Run automated tests: `python test_agents.py --help`
- Check agent status: `python test_agents.py --list`
- See development log: `docs/development-log/DEVELOPMENT_JOURNAL.md`

---
*Created for ODSC Hackathon - SpyGame Team* 