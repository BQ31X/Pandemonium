#!/bin/bash
# Quick script to test agents before committing
# Usage: ./check_and_commit.sh "your commit message"

echo "🧪 Running agent tests before commit..."

# Run the test script
python test_agents.py

# Check if tests passed
if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Tests passed! Proceeding with commit..."
    
    # Add all changes and commit
    git add .
    
    if [ -n "$1" ]; then
        git commit -m "$1"
        echo "🎉 Committed with message: $1"
    else
        echo "ℹ️  No commit message provided. Staging files only."
        echo "   Run: git commit -m 'your message' to complete"
    fi
else
    echo ""
    echo "❌ Tests failed! Fix issues before committing."
    echo "   Check which agents are broken and fix them first."
    exit 1
fi 