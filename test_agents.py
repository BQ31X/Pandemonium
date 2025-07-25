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
    """Run all agent tests."""
    print("🧪 Testing all agents...\n")
    
    passed = 0
    failed = 0
    
    for agent in AGENTS:
        if test_agent(agent):
            passed += 1
        else:
            failed += 1
    
    print(f"\n📊 Results: {passed} passed, {failed} failed")
    
    if failed == 0:
        print("🎉 All agents working! Safe to commit.")
        return 0
    else:
        print("⚠️  Some agents broken. Fix before committing.")
        return 1

if __name__ == "__main__":
    exit(main()) 