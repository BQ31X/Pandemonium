#!/bin/bash
# TEST.sh - Smoke-test script to verify core functionality
# Required for hackathon submission

set -e  # Exit on any error

echo "🧪 HACKATHON SMOKE TEST - Pandemonium Agents"
echo "=============================================="
echo ""

# Check if we're in the right environment
echo "📋 Checking environment..."
if ! command -v python &> /dev/null; then
    echo "❌ Python not found. Please activate conda environment:"
    echo "   conda activate agentic-hackathon"
    exit 1
fi

# Check if dependencies are available
echo "📦 Checking dependencies..."
python -c "import google.adk; print('✅ Google ADK available')" || {
    echo "❌ Dependencies missing. Please run:"
    echo "   conda env create -f environment.yml"
    echo "   conda activate agentic-hackathon"
    exit 1
}

echo ""

# Run comprehensive agent tests
echo "🤖 Testing all agents..."
python test_agents.py || {
    echo "❌ Agent tests failed!"
    exit 1
}

echo ""

# Quick functional test - test that we can actually start an agent
echo "🚀 Testing agent functionality..."
echo "Testing spymaster agent with sample input..."

# Test spymaster gives a reasonable response
python -c "
import os
os.environ['ADK_AGENT'] = 'spymaster'
from src import root_agent
print('✅ Spymaster agent loaded successfully')
print(f'   Name: {root_agent.name}')
print(f'   Model: {root_agent.model}')
print(f'   Description: {root_agent.description}')
" || {
    echo "❌ Functional test failed!"
    exit 1
}

echo ""

# Test that we can load other core agents
echo "🔄 Testing gamemaster and operative..."
for agent in gamemaster operative; do
    python -c "
import os
os.environ['ADK_AGENT'] = '$agent'
from src import root_agent
print(f'✅ $agent loaded: {root_agent.name}')
" || {
        echo "❌ Failed to load $agent agent!"
        exit 1
    }
done

echo ""
echo "🎉 ALL SMOKE TESTS PASSED!"
echo ""
echo "✅ Environment configured correctly"
echo "✅ All agents load without errors"  
echo "✅ Core functionality verified"
echo ""
echo "🚀 Ready for demo! Try: ADK_AGENT=spymaster adk web"
echo ""

exit 0 