#!/bin/bash
"""
Azure Architecture Extraction Setup Script
Installs Azure CLI and sets up the extraction environment
"""

echo "🌟===============================================================🌟"
echo "        AZURE ARCHITECTURE EXTRACTOR SETUP"
echo "🌟===============================================================🌟"
echo ""

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Azure CLI is installed
echo "🔍 Checking Azure CLI installation..."
if command_exists az; then
    echo "✅ Azure CLI is already installed"
    az --version | head -1
else
    echo "❌ Azure CLI not found. Installing..."
    
    # Detect OS and install accordingly
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        echo "🐧 Detected Linux. Installing Azure CLI..."
        curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        echo "🍎 Detected macOS. Please install using Homebrew:"
        echo "   brew install azure-cli"
        echo "   Or download from: https://aka.ms/installazureclimacos"
        exit 1
    elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
        echo "🪟 Detected Windows. Please download from:"
        echo "   https://aka.ms/installazurecliwindows"
        exit 1
    else
        echo "❓ Unknown OS. Please install Azure CLI manually:"
        echo "   https://docs.microsoft.com/en-us/cli/azure/install-azure-cli"
        exit 1
    fi
fi

echo ""
echo "🔐 Checking Azure authentication..."
if az account show >/dev/null 2>&1; then
    echo "✅ Already authenticated to Azure"
    az account show --query "{name:name, subscriptionId:id}" -o table
else
    echo "❌ Not authenticated. Please login to Azure:"
    echo "   az login"
    echo ""
    read -p "Do you want to login now? (y/n): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        az login
    else
        echo "⚠️ Please run 'az login' before using the extraction tools"
    fi
fi

echo ""
echo "🐍 Checking Python environment..."
if command_exists python3; then
    echo "✅ Python 3 is available"
    python3 --version
else
    echo "❌ Python 3 not found. Please install Python 3.6 or later"
    exit 1
fi

echo ""
echo "📦 Setting up Python virtual environment..."
if [ ! -d "azure_extraction_env" ]; then
    python3 -m venv azure_extraction_env
    echo "✅ Virtual environment created"
else
    echo "✅ Virtual environment already exists"
fi

# Activate virtual environment and install dependencies
source azure_extraction_env/bin/activate
pip install --upgrade pip
pip install azure-cli azure-mgmt-resource azure-mgmt-compute azure-mgmt-network azure-mgmt-storage

echo ""
echo "🎯 Making scripts executable..."
chmod +x azure_architecture_extractor.py
chmod +x azure_dependency_analyzer.py

echo ""
echo "✅ Setup complete!"
echo ""
echo "🚀 Usage:"
echo "   1. Extract current architecture:"
echo "      python3 azure_architecture_extractor.py"
echo ""
echo "   2. Analyze dependencies and security:"
echo "      python3 azure_dependency_analyzer.py"
echo ""
echo "   3. View comprehensive menu:"
echo "      python3 azure_main_menu.py"
echo ""
echo "📁 Generated files will include:"
echo "   • azure_current_architecture.txt - Visual diagram of your resources"
echo "   • azure_cost_optimization_guide.txt - Cost optimization recommendations"
echo "   • azure_comprehensive_analysis.txt - Security and dependency analysis"
echo "   • azure_architecture_export_*.json - Complete resource data"
echo ""
echo "💡 Tips:"
echo "   • Run the extraction tools regularly to keep documentation updated"
echo "   • Review cost optimization recommendations monthly"
echo "   • Address security findings promptly"
echo "   • Use the JSON exports for automation and further analysis"
