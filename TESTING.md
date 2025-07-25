# Testing Documentation

All testing guides and tools have been organized in the **`docs/testing/`** directory.

## 📖 **Start Here:** [Testing Overview](docs/testing/testing_overview.md)

The overview will guide you to the right testing approach for your current task:

- **🔧 Agent Testing** - Does my code work? (unit tests, CI, imports)
- **🎲 Prompt Testing** - How good are my agent responses? (word scenarios, prompt engineering)  
- **🚀 Integration Testing** *(coming soon)* - Multi-agent workflows
- **📊 Performance Testing** *(coming soon)* - Competition readiness

## ⚡ Quick Commands

```bash
# Test agents work
python test_agents.py

# Generate word scenarios  
python spymaster_tester.py --help

# Safe commit
./check_and_commit.sh "your message"
```

---
**Full documentation:** [`docs/testing/testing_overview.md`](docs/testing/testing_overview.md) 