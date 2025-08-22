#!/usr/bin/env python3
"""
Azure Resources Setup and Usage Guide
"""

def display_menu():
    """Display the main menu with available options"""
    
    print("🌟" + "="*80 + "🌟")
    print("        AZURE RESOURCES DIAGRAM GENERATOR - COMPLETE SUITE")
    print("🌟" + "="*80 + "🌟")
    print()
    print("📁 Generated Files:")
    print("   ├── 📊 azure_diagrams/azure_resources_comprehensive_guide.txt")
    print("   ├── 📋 azure_diagrams/azure_service_selection_matrix.txt") 
    print("   ├── 🎨 azure_diagrams/azure_ascii_diagram.txt")
    print("   ├── 📚 azure_services_catalog.json")
    print("   └── 📖 README.md")
    print()
    print("🚀 Available Tools:")
    print("   1. 📖 View Comprehensive Azure Guide")
    print("   2. 🎨 View ASCII Diagram")
    print("   3. 📋 View Service Selection Matrix")
    print("   4. 🔍 Interactive Azure Explorer")
    print("   5. 📊 Export Services Catalog (JSON)")
    print("   6. 💡 Show Quick Tips")
    print("   7. 🏗️  Show Architecture Examples")
    print("   8. 💰 Show Cost Optimization Tips")
    print("   9. 🔧 Generate Additional Diagrams")
    print("   0. 🚪 Exit")
    print()

def show_quick_tips():
    """Display quick tips for Azure usage"""
    
    tips = """
💡 AZURE QUICK TIPS & BEST PRACTICES

🏷️  NAMING CONVENTIONS:
   - Use consistent naming: rg-prod-eastus-001
   - Include environment: dev, test, prod
   - Include location: eastus, westeurope
   - Include purpose: web, db, storage

🔒 SECURITY BEST PRACTICES:
   - Always use Azure AD for authentication
   - Store secrets in Key Vault
   - Enable MFA for all accounts
   - Use Network Security Groups
   - Regular security reviews with Security Center

💰 COST OPTIMIZATION:
   - Use Reserved Instances for predictable workloads (up to 72% savings)
   - Implement auto-scaling to match demand
   - Use Azure Spot VMs for fault-tolerant workloads (up to 90% savings)
   - Regular resource right-sizing
   - Set up cost alerts and budgets

📊 MONITORING & PERFORMANCE:
   - Enable Application Insights for all applications
   - Set up Azure Monitor dashboards
   - Use Log Analytics for centralized logging
   - Configure alerts for critical metrics
   - Regular performance reviews

🏗️  ARCHITECTURE PRINCIPLES:
   - Design for failure (availability zones)
   - Use managed services when possible
   - Implement proper backup strategies
   - Plan for disaster recovery
   - Use Infrastructure as Code (ARM, Terraform)
"""
    
    print(tips)

def show_architecture_examples():
    """Display common architecture patterns"""
    
    architectures = """
🏗️  COMMON AZURE ARCHITECTURES

📱 BASIC WEB APPLICATION:
   Internet → Azure Front Door → App Service → Azure SQL Database
                                    ↓
                              Azure Blob Storage (for static content)
   
   Cost: ~$100-500/month
   Use cases: Small to medium websites, APIs

🐳 MICROSERVICES ARCHITECTURE:
   Internet → API Management → Azure Kubernetes Service (AKS)
                                        ↓
                              Azure Service Bus ← → Cosmos DB
                                        ↓              ↓
                                Redis Cache        Event Grid
   
   Cost: ~$500-2000/month
   Use cases: Large applications, high scalability needs

⚡ SERVERLESS ARCHITECTURE:
   Event Grid → Azure Functions → Cosmos DB
        ↓              ↓              ↓
   Logic Apps → Storage Queue → Table Storage
   
   Cost: Pay-per-execution (very low for sporadic usage)
   Use cases: Event-driven apps, batch processing

📊 BIG DATA ANALYTICS:
   IoT Devices → Event Hubs → Stream Analytics → Data Lake Storage Gen2
                                     ↓                    ↓
                              Cosmos DB           Synapse Analytics
                                     ↓                    ↓
                            Machine Learning       Power BI Dashboard
   
   Cost: ~$1000-5000/month
   Use cases: Real-time analytics, IoT data processing

🎮 GAMING BACKEND:
   Game Clients → Traffic Manager → App Service (multiple regions)
                                          ↓
                     Redis Cache ← → Cosmos DB (globally distributed)
                                          ↓
                               Azure Functions (game logic)
   
   Cost: ~$300-1500/month
   Use cases: Mobile games, multiplayer games

🔒 ENTERPRISE SECURITY:
   On-premises → ExpressRoute → Azure Virtual Network
                                        ↓
                    Azure AD ← → Key Vault ← → Security Center
                        ↓              ↓              ↓
                 Conditional      Secrets &     Threat Detection
                   Access       Certificates
   
   Cost: ~$200-1000/month
   Use cases: Enterprise applications, compliance requirements
"""
    
    print(architectures)

def show_cost_optimization():
    """Display cost optimization strategies"""
    
    cost_tips = """
💰 AZURE COST OPTIMIZATION STRATEGIES

🎯 COMPUTE OPTIMIZATION:
   • Reserved Instances: 1-3 year commitments save up to 72%
   • Azure Spot VMs: Use spare capacity for up to 90% savings
   • Auto-scaling: Scale resources based on demand
   • Right-sizing: Regular review and adjust VM sizes
   • B-series VMs: For variable workloads with CPU bursting

💾 STORAGE OPTIMIZATION:
   • Lifecycle Management: Auto-move data to cooler tiers
   • Hot Tier: Frequently accessed data
   • Cool Tier: Infrequently accessed (30+ days) - 50% cheaper
   • Archive Tier: Rarely accessed (180+ days) - 80% cheaper
   • Data Deduplication: Reduce redundant data

🗄️  DATABASE OPTIMIZATION:
   • Azure SQL Database: Use appropriate service tier
   • Serverless: Auto-pause for development databases
   • Read Replicas: Offload read operations
   • Elastic Pools: Share resources across databases
   • Reserved Capacity: For predictable workloads

🌐 NETWORKING OPTIMIZATION:
   • CDN: Reduce bandwidth costs and improve performance
   • ExpressRoute: For large data transfers vs. VPN
   • Traffic Manager: Route to least expensive regions
   • Private Endpoints: Reduce data transfer costs

📊 MONITORING & GOVERNANCE:
   • Azure Cost Management: Set budgets and alerts
   • Azure Advisor: Get personalized recommendations
   • Resource Tags: Track costs by project/department
   • Azure Policy: Enforce cost controls
   • Regular Reviews: Monthly cost analysis

💡 PRO TIPS:
   • Use Azure Pricing Calculator for estimates
   • Take advantage of Azure Credits (Visual Studio, MSDN)
   • Consider Azure Dev/Test pricing for non-production
   • Use Azure Migrate for cost-effective cloud migration planning
   • Implement Infrastructure as Code for consistent deployments

📈 COST ESTIMATION EXAMPLES:
   Small Business:     $100-500/month
   Medium Enterprise:  $1,000-5,000/month  
   Large Enterprise:   $10,000-50,000/month
   Global Enterprise:  $100,000+/month
"""
    
    print(cost_tips)

def main():
    """Main interactive menu"""
    
    while True:
        display_menu()
        
        try:
            choice = input("🎯 Enter your choice (0-9): ").strip()
            
            if choice == "0":
                print("\n👋 Thank you for using Azure Resources Diagram Generator!")
                print("📚 Don't forget to check the generated files in the azure_diagrams/ directory")
                break
                
            elif choice == "1":
                print("\n📖 Opening Comprehensive Azure Guide...")
                try:
                    with open("azure_diagrams/azure_resources_comprehensive_guide.txt", "r") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("❌ Guide file not found. Please run: python azure_diagram_simplified.py")
                    
            elif choice == "2":
                print("\n🎨 Opening ASCII Diagram...")
                try:
                    with open("azure_diagrams/azure_ascii_diagram.txt", "r") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("❌ ASCII diagram not found. Please run: python create_ascii_diagram.py")
                    
            elif choice == "3":
                print("\n📋 Opening Service Selection Matrix...")
                try:
                    with open("azure_diagrams/azure_service_selection_matrix.txt", "r") as f:
                        print(f.read())
                except FileNotFoundError:
                    print("❌ Matrix file not found. Please run: python azure_diagram_simplified.py")
                    
            elif choice == "4":
                print("\n🔍 Starting Interactive Azure Explorer...")
                try:
                    import subprocess
                    subprocess.run(["python", "azure_explorer.py"])
                except Exception as e:
                    print(f"❌ Error starting explorer: {e}")
                    
            elif choice == "5":
                print("\n📊 Exporting Services Catalog...")
                try:
                    from azure_explorer import AzureResourceExplorer
                    explorer = AzureResourceExplorer()
                    explorer.export_to_json()
                except Exception as e:
                    print(f"❌ Error exporting catalog: {e}")
                    
            elif choice == "6":
                show_quick_tips()
                
            elif choice == "7":
                show_architecture_examples()
                
            elif choice == "8":
                show_cost_optimization()
                
            elif choice == "9":
                print("\n🔧 Generating Additional Diagrams...")
                try:
                    import subprocess
                    subprocess.run(["python", "azure_diagram_simplified.py"])
                    subprocess.run(["python", "create_ascii_diagram.py"])
                    print("✅ Additional diagrams generated!")
                except Exception as e:
                    print(f"❌ Error generating diagrams: {e}")
                    
            else:
                print("❌ Invalid choice. Please enter 0-9.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
            
        input("\n📖 Press Enter to continue...")
        print("\n" + "="*100 + "\n")

if __name__ == "__main__":
    main()
