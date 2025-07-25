#!/usr/bin/env python3
"""
Quick test script to verify all agents are working.
Run this before commits or when teammates make changes.
"""

import os
import subprocess
import sys

# List of all agents that should work
AGENTS = ['telephone', 'day_trip', 'spymaster', 'operative', 'gamemaster']

def test_agent(agent_name):
    """Test if an agent can be loaded without errors."""
    try:
        # Set environment and try to import
        env = os.environ.copy()
        env['ADK_AGENT'] = agent_name
        
        result = subprocess.run([
            sys.executable, '-c', 
            'from src import root_agent; print(f"✅ {root_agent.name}")'
        ], env=env, capture_output=True, text=True, timeout=10)
        
        if result.returncode == 0:
            print(f"✅ {agent_name}: {result.stdout.strip()}")
            return True
        else:
            print(f"❌ {agent_name}: ERROR - {result.stderr.strip()}")
            return False
            
    except subprocess.TimeoutExpired:
        print(f"❌ {agent_name}: TIMEOUT")
        return False
    except Exception as e:
        print(f"❌ {agent_name}: EXCEPTION - {e}")
        return False

def main():
    """Run agent tests."""
    import argparse
    
    parser = argparse.ArgumentParser(description='Test agents')
    parser.add_argument('agents', nargs='*', help='Specific agents to test (default: all)')
    parser.add_argument('--list', action='store_true', help='List available agents')
    args = parser.parse_args()
    
    if args.list:
        print("Available agents:")
        for agent in AGENTS:
            print(f"  • {agent}")
        return 0
    
    # Determine which agents to test
    if args.agents:
        agents_to_test = []
        for agent in args.agents:
            if agent in AGENTS:
                agents_to_test.append(agent)
            else:
                print(f"❌ Unknown agent: {agent}")
                print(f"Available agents: {', '.join(AGENTS)}")
                return 1
    else:
        agents_to_test = AGENTS
    
    # Run tests
    if len(agents_to_test) == 1:
        print(f"🧪 Testing {agents_to_test[0]} agent...\n")
    else:
        print(f"🧪 Testing {len(agents_to_test)} agents...\n")
    
    passed = 0
    failed = 0
    
    for agent in agents_to_test:
        if test_agent(agent):
            passed += 1
        else:
            failed += 1
    
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        if len(agents_to_test) == 1:
            print(f"🎉 {agents_to_test[0]} working!")
        else:
            print("🎉 All tested agents working! Safe to commit.")
        return 0
    else:
        print("⚠️  Some agents broken. Fix before committing.")
        return 1

if __name__ == "__main__":
    exit(main()) 