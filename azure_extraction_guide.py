#!/usr/bin/env python3
"""
Azure Architecture Extraction - Complete Usage Guide
Comprehensive guide for extracting and analyzing Azure architecture
"""

def show_main_menu():
    """Display the main extraction menu"""
    
    print("🌟" + "="*80 + "🌟")
    print("             AZURE ARCHITECTURE EXTRACTION TOOLKIT")
    print("🌟" + "="*80 + "🌟")
    print()
    print("🎯 Choose your extraction goal:")
    print()
    print("   1. 🏗️  Extract Complete Architecture")
    print("      └─ Get visual diagram of all your Azure resources")
    print()
    print("   2. 🔒 Security & Dependencies Analysis") 
    print("      └─ Analyze network topology and security configuration")
    print()
    print("   3. 💰 Cost Optimization Analysis")
    print("      └─ Get personalized cost optimization recommendations")
    print()
    print("   4. 📊 Export Resource Data (JSON)")
    print("      └─ Export complete resource inventory for automation")
    print()
    print("   5. 🔍 Interactive Resource Explorer")
    print("      └─ Browse and search your Azure resources")
    print()
    print("   6. 📚 View Azure Services Reference")
    print("      └─ Browse all available Azure services and patterns")
    print()
    print("   7. ⚙️  Setup & Prerequisites Check")
    print("      └─ Install Azure CLI and authenticate")
    print()
    print("   8. 📖 Help & Documentation")
    print("      └─ View detailed usage instructions")
    print()
    print("   0. 🚪 Exit")
    print()

def show_help_documentation():
    """Show detailed help and documentation"""
    
    help_text = """
📖 AZURE ARCHITECTURE EXTRACTION - DETAILED HELP

🎯 OVERVIEW
This toolkit helps you extract, analyze, and document your existing Azure infrastructure.
It provides automated discovery of resources, security analysis, cost optimization 
recommendations, and visual architecture diagrams.

🔧 PREREQUISITES
1. Azure CLI installed and configured
2. Azure account with appropriate permissions
3. Python 3.6 or later
4. Internet connection for Azure API calls

🔑 REQUIRED PERMISSIONS
Minimum required Azure permissions:
• Reader role on subscription or resource groups
• Network Contributor for detailed network analysis (optional)
• Security Reader for security assessments (optional)

📊 EXTRACTION CAPABILITIES

🏗️ ARCHITECTURE EXTRACTION
• Discovers all resources in your subscription
• Groups resources by type and resource group
• Creates visual text-based architecture diagrams
• Identifies resource relationships and dependencies

🔒 SECURITY ANALYSIS
• Maps network topology (VNets, subnets, NSGs)
• Identifies security misconfigurations
• Analyzes Network Security Group rules
• Provides security hardening recommendations

💰 COST OPTIMIZATION
• Identifies underutilized resources
• Suggests right-sizing opportunities
• Recommends Reserved Instance purchases
• Provides storage tier optimization advice

📁 OUTPUT FILES
The toolkit generates several files:

• azure_current_architecture.txt
  └─ Visual diagram of your entire Azure setup

• azure_cost_optimization_guide.txt
  └─ Personalized cost reduction recommendations

• azure_comprehensive_analysis.txt
  └─ Complete security and dependency analysis

• azure_architecture_export_[timestamp].json
  └─ Machine-readable complete resource inventory

🚀 GETTING STARTED

1. First Time Setup:
   ./setup_azure_extraction.sh

2. Authenticate to Azure:
   az login

3. Extract your architecture:
   python3 azure_architecture_extractor.py

4. Analyze security and dependencies:
   python3 azure_dependency_analyzer.py

🔍 DETAILED ANALYSIS FEATURES

📋 Resource Discovery
• Virtual Machines and their configurations
• Storage Accounts and blob containers
• Databases (SQL, Cosmos DB, MySQL, PostgreSQL)
• Networking components (VNets, subnets, NSGs, LBs)
• App Services and Function Apps
• Container services (AKS, Container Instances)
• Security services (Key Vault, Security Center)

🌐 Network Topology
• Virtual Network layouts and address spaces
• Subnet configurations and associated NSGs
• Load Balancer configurations and rules
• Public IP assignments and allocations
• VPN Gateway and ExpressRoute connections

🛡️ Security Assessment
• Network Security Group rule analysis
• Public IP exposure assessment
• Key Vault configuration review
• Azure AD integration verification
• Security Center findings summary

💡 USE CASES

🏢 Enterprise Architecture Documentation
• Maintain up-to-date architecture diagrams
• Compliance and audit documentation
• Change management and impact analysis
• Knowledge transfer and onboarding

🔄 Cloud Migration Projects
• Current state assessment and documentation
• Dependency mapping for migration planning
• Cost analysis for migration business case
• Target state architecture planning

💰 Cost Management
• Regular cost optimization reviews
• Budget planning and forecasting
• Resource utilization analysis
• Right-sizing recommendations

🔒 Security & Compliance
• Security posture assessments
• Compliance gap analysis
• Risk identification and mitigation
• Security monitoring and alerting setup

⚡ ADVANCED USAGE

🔗 Integration with Other Tools
The JSON exports can be integrated with:
• Infrastructure as Code tools (Terraform, ARM)
• Monitoring dashboards (Grafana, Power BI)
• ITSM tools (ServiceNow, Jira)
• Documentation platforms (Confluence, SharePoint)

🤖 Automation
• Schedule regular extractions with cron jobs
• Integrate with CI/CD pipelines
• Automate reporting and alerting
• Build custom analysis scripts

📈 Continuous Monitoring
• Set up monthly architecture reviews
• Track resource growth and changes
• Monitor cost trends and optimizations
• Maintain security compliance

🆘 TROUBLESHOOTING

❌ Common Issues:

1. "Azure CLI not found"
   Solution: Install Azure CLI using the setup script

2. "Not authenticated"
   Solution: Run 'az login' and follow the prompts

3. "Permission denied"
   Solution: Ensure you have Reader role on the subscription

4. "No resources found"
   Solution: Check if you're connected to the correct subscription

5. "Script fails with timeout"
   Solution: You may have a large number of resources; wait longer

📞 Getting Help:
• Check the README.md file for detailed instructions
• Review the generated log files for error details
• Ensure Azure CLI is properly configured
• Verify network connectivity to Azure APIs

🌟 BEST PRACTICES

📅 Regular Extractions
• Run monthly for up-to-date documentation
• Extract before major changes or deployments
• Include in disaster recovery planning
• Use for quarterly business reviews

🔄 Documentation Management
• Version control the generated files
• Share with relevant teams and stakeholders
• Use as input for architecture decision records
• Maintain alongside infrastructure code

💡 Optimization Workflow
1. Extract current architecture
2. Review cost optimization recommendations
3. Implement high-impact changes
4. Re-extract to validate improvements
5. Schedule regular reviews

🔒 Security Workflow
1. Run security analysis monthly
2. Address critical findings immediately
3. Implement recommended security controls
4. Document security improvements
5. Regular security posture reviews
"""
    
    print(help_text)

def run_extraction_workflow():
    """Run the complete extraction workflow"""
    import subprocess
    import os
    
    print("🚀 Starting complete Azure architecture extraction...")
    print("="*60)
    
    # Check if scripts exist
    scripts = [
        'azure_architecture_extractor.py',
        'azure_dependency_analyzer.py'
    ]
    
    for script in scripts:
        if not os.path.exists(script):
            print(f"❌ Script not found: {script}")
            return
    
    print("1. 🏗️  Extracting architecture...")
    try:
        result = subprocess.run(['python3', 'azure_architecture_extractor.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Architecture extraction completed")
        else:
            print(f"   ❌ Architecture extraction failed: {result.stderr}")
            return
    except Exception as e:
        print(f"   ❌ Error running architecture extractor: {e}")
        return
    
    print("\n2. 🔒 Analyzing dependencies and security...")
    try:
        result = subprocess.run(['python3', 'azure_dependency_analyzer.py'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("   ✅ Security analysis completed")
        else:
            print(f"   ❌ Security analysis failed: {result.stderr}")
    except Exception as e:
        print(f"   ❌ Error running dependency analyzer: {e}")
    
    print("\n🎉 Extraction workflow completed!")
    print("\n📁 Generated files:")
    print("   • azure_current_architecture.txt")
    print("   • azure_cost_optimization_guide.txt") 
    print("   • azure_comprehensive_analysis.txt")
    print("   • azure_architecture_export_*.json")

def main():
    """Main menu loop"""
    
    while True:
        show_main_menu()
        
        try:
            choice = input("🎯 Enter your choice (0-8): ").strip()
            
            if choice == "0":
                print("\n👋 Thank you for using Azure Architecture Extraction Toolkit!")
                break
                
            elif choice == "1":
                print("\n🏗️  Starting complete architecture extraction...")
                run_extraction_workflow()
                
            elif choice == "2":
                print("\n🔒 Starting security and dependencies analysis...")
                import subprocess
                subprocess.run(['python3', 'azure_dependency_analyzer.py'])
                
            elif choice == "3":
                print("\n💰 Starting cost optimization analysis...")
                import subprocess
                subprocess.run(['python3', 'azure_architecture_extractor.py'])
                print("💡 Review the azure_cost_optimization_guide.txt file for recommendations")
                
            elif choice == "4":
                print("\n📊 Exporting resource data to JSON...")
                import subprocess
                subprocess.run(['python3', 'azure_architecture_extractor.py'])
                print("💾 JSON export completed - check azure_architecture_export_*.json")
                
            elif choice == "5":
                print("\n🔍 Starting interactive resource explorer...")
                try:
                    import subprocess
                    subprocess.run(['python3', 'azure_main_menu.py'])
                except FileNotFoundError:
                    print("❌ Azure explorer not found. Please ensure all files are present.")
                
            elif choice == "6":
                print("\n📚 Opening Azure Services Reference...")
                try:
                    import subprocess
                    subprocess.run(['python3', 'azure_main_menu.py'])
                except FileNotFoundError:
                    print("❌ Azure services reference not found.")
                
            elif choice == "7":
                print("\n⚙️  Running setup and prerequisites check...")
                import subprocess
                subprocess.run(['./setup_azure_extraction.sh'])
                
            elif choice == "8":
                show_help_documentation()
                
            else:
                print("❌ Invalid choice. Please enter 0-8.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            
        if choice != "8":  # Don't pause after help
            input("\n📖 Press Enter to continue...")
            print("\n" + "="*100 + "\n")

if __name__ == "__main__":
    main()
