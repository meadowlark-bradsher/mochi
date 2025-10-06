#!/bin/bash
# Verify Mochi setup

echo "🎯 Mochi Setup Verification"
echo "============================"
echo ""

# Check Python version
echo "1. Checking Python version..."
python_version=$(python --version 2>&1 | awk '{print $2}')
echo "   ✓ Python $python_version"
echo ""

# Check if package is installed
echo "2. Checking if Mochi is installed..."
if python -c "import mochi" 2>/dev/null; then
    echo "   ✓ Mochi package installed"
else
    echo "   ✗ Mochi not installed. Run: pip install -e ."
    exit 1
fi
echo ""

# Check dependencies
echo "3. Checking critical dependencies..."
for package in click rich openai anthropic whisper sounddevice pyttsx3; do
    if python -c "import $package" 2>/dev/null; then
        echo "   ✓ $package"
    else
        echo "   ✗ $package missing"
    fi
done
echo ""

# Check API keys
echo "4. Checking API keys..."
if [ -n "$OPENAI_API_KEY" ]; then
    echo "   ✓ OPENAI_API_KEY is set"
    api_key_set=true
elif [ -n "$ANTHROPIC_API_KEY" ]; then
    echo "   ✓ ANTHROPIC_API_KEY is set"
    api_key_set=true
else
    echo "   ✗ No API key set"
    echo "     Set one with:"
    echo "     export OPENAI_API_KEY='your-key'"
    echo "     OR"
    echo "     export ANTHROPIC_API_KEY='your-key'"
    api_key_set=false
fi
echo ""

# Check example problem
echo "5. Checking example problem..."
if [ -f "examples/problems/two_sum/problem.yaml" ]; then
    echo "   ✓ Two Sum problem found"
else
    echo "   ✗ Example problem missing"
fi
echo ""

# Check config
echo "6. Checking configuration..."
if [ -f "settings.toml" ]; then
    echo "   ✓ settings.toml found"
else
    echo "   ✗ settings.toml missing"
fi
echo ""

# Summary
echo "============================"
if [ "$api_key_set" = true ]; then
    echo "✅ Setup complete! Ready to run:"
    echo ""
    echo "   mochi start --voice \\"
    echo "     -p examples/problems/two_sum/problem.yaml \\"
    echo "     -f solution.py"
    echo ""
    echo "   (Use headphones!)"
else
    echo "⚠️  Almost ready - just set your API key:"
    echo ""
    echo "   export OPENAI_API_KEY='your-key'"
    echo ""
    echo "   Then run:"
    echo "   mochi start --voice -p examples/problems/two_sum/problem.yaml -f solution.py"
fi
echo ""
