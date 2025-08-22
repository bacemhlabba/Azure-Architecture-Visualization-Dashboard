#!/usr/bin/env python3
"""
Azure Resources Diagram Generator (Simplified Version)
Creates comprehensive diagrams showing major Azure resources organized by categories.
"""

from diagrams import Diagram, Cluster, Edge
import os

def create_simplified_azure_diagram():
    """Create a simplified diagram of major Azure resources using text and basic shapes"""
    
    # Set output directory
    output_dir = "azure_diagrams"
    os.makedirs(output_dir, exist_ok=True)
    
    # First, let's try to import what's actually available
    try:
        from diagrams.azure.compute import VM, AKS, AppServices, FunctionApps, ContainerInstances
        from diagrams.azure.storage import BlobStorage, FileStorage, QueueStorage, TableStorage
        from diagrams.azure.database import SQLDatabases, CosmosDb
        from diagrams.azure.network import VirtualNetworks, LoadBalancers, ApplicationGateway
        from diagrams.azure.security import KeyVaults
        from diagrams.azure.analytics import DataFactory
        from diagrams.azure.integration import ServiceBus, LogicApps
        from diagrams.azure.web import StaticWebApps
        
        with Diagram("Azure Resources Overview", 
                     filename=f"{output_dir}/azure_resources_overview", 
                     show=False, 
                     direction="TB",
                     graph_attr={"size": "16,12!", "dpi": "200"}):
            
            # Compute Services
            with Cluster("Compute Services"):
                vm = VM("Virtual Machines")
                aks = AKS("Azure Kubernetes Service")
                app_service = AppServices("App Service")
                functions = FunctionApps("Azure Functions")
                containers = ContainerInstances("Container Instances")
                
            # Storage Services  
            with Cluster("Storage Services"):
                blob_storage = BlobStorage("Blob Storage")
                file_storage = FileStorage("File Storage")
                queue_storage = QueueStorage("Queue Storage")
                table_storage = TableStorage("Table Storage")
                
            # Database Services
            with Cluster("Database Services"):
                sql_database = SQLDatabases("SQL Database")
                cosmos_db = CosmosDb("Cosmos DB")
                
            # Networking Services
            with Cluster("Networking Services"):
                vnet = VirtualNetworks("Virtual Network")
                load_balancer = LoadBalancers("Load Balancer")
                app_gateway = ApplicationGateway("Application Gateway")
                
            # Security Services
            with Cluster("Security & Identity"):
                key_vault = KeyVaults("Key Vault")
                
            # Integration & Analytics
            with Cluster("Integration & Analytics"):
                data_factory = DataFactory("Data Factory")
                service_bus = ServiceBus("Service Bus")
                logic_apps = LogicApps("Logic Apps")
                
            # Web Services
            with Cluster("Web Services"):
                static_web = StaticWebApps("Static Web Apps")
                
            # Add some connections to show relationships
            app_service >> sql_database
            aks >> vnet
            functions >> blob_storage
            logic_apps >> service_bus
                
        print("✓ Created Azure resources overview diagram")
        
    except ImportError as e:
        print(f"Import error: {e}")
        print("Creating text-based diagram instead...")
        create_text_based_diagram(output_dir)

def create_text_based_diagram(output_dir):
    """Create a text-based representation when graphical diagrams fail"""
    
    diagram_text = """
# Azure Resources Comprehensive Overview

## 🖥️ COMPUTE SERVICES
┌─────────────────────────────────────┐
│  Virtual Machines (VMs)             │  ← On-demand computing resources
│  VM Scale Sets                      │  ← Auto-scaling VM groups  
│  Azure Kubernetes Service (AKS)     │  ← Managed Kubernetes
│  Container Instances                │  ← Serverless containers
│  App Service                        │  ← PaaS web apps and APIs
│  Azure Functions                    │  ← Serverless compute
│  Azure Batch                        │  ← Large-scale parallel workloads
│  Service Fabric                     │  ← Microservices platform
│  Azure Container Registry          │  ← Container image registry
└─────────────────────────────────────┘

## 💾 STORAGE SERVICES  
┌─────────────────────────────────────┐
│  Blob Storage                       │  ← Object storage (files, images, videos)
│  File Storage                       │  ← Managed file shares (SMB/NFS)
│  Queue Storage                      │  ← Message queuing service
│  Table Storage                      │  ← NoSQL key-value store
│  Disk Storage                       │  ← High-performance VM disks
│  Data Lake Storage Gen2            │  ← Big data analytics storage
│  Azure NetApp Files                │  ← Enterprise-grade file storage
└─────────────────────────────────────┘

## 🗄️ DATABASE SERVICES
┌─────────────────────────────────────┐
│  Azure SQL Database                 │  ← Managed relational database
│  Azure SQL Managed Instance        │  ← SQL Server in the cloud
│  Cosmos DB                          │  ← Multi-model NoSQL database
│  Azure Database for MySQL          │  ← Managed MySQL
│  Azure Database for PostgreSQL     │  ← Managed PostgreSQL  
│  Redis Cache                        │  ← In-memory caching
│  Azure Synapse Analytics           │  ← Enterprise data warehouse
│  Azure Database Migration Service  │  ← Database migration tool
└─────────────────────────────────────┘

## 🌐 NETWORKING SERVICES
┌─────────────────────────────────────┐
│  Virtual Network (VNet)             │  ← Isolated network environments
│  Subnets                            │  ← Network segmentation
│  Network Security Groups           │  ← Firewall rules
│  Load Balancer                      │  ← Layer 4 load balancing
│  Application Gateway                │  ← Layer 7 load balancing + WAF
│  Traffic Manager                    │  ← DNS-based traffic routing
│  Azure Front Door                   │  ← Global load balancer + CDN
│  VPN Gateway                        │  ← Site-to-site connectivity
│  ExpressRoute                       │  ← Private connectivity to Azure
│  Azure Firewall                     │  ← Managed network security
│  CDN                                │  ← Content delivery network
│  DNS Zones                          │  ← Domain name system
│  Private DNS                        │  ← Internal name resolution
└─────────────────────────────────────┘

## 🔐 SECURITY & IDENTITY
┌─────────────────────────────────────┐
│  Azure Active Directory (AAD)       │  ← Identity and access management
│  Azure AD B2C                       │  ← Customer identity management
│  Key Vault                          │  ← Secrets and certificate management
│  Security Center                    │  ← Security posture management
│  Azure Sentinel                     │  ← Security information and event management
│  Azure Information Protection       │  ← Data classification and protection
│  Azure Privileged Identity Mgmt     │  ← Just-in-time privileged access
│  Azure Multi-Factor Authentication  │  ← Additional security layer
└─────────────────────────────────────┘

## 🤖 AI & MACHINE LEARNING
┌─────────────────────────────────────┐
│  Azure Machine Learning             │  ← End-to-end ML lifecycle
│  Cognitive Services                 │  ← Pre-built AI capabilities
│  ├── Computer Vision                │  ← Image and video analysis
│  ├── Speech Services                │  ← Speech to text, text to speech
│  ├── Language Understanding         │  ← Natural language processing
│  ├── Decision Services              │  ← Anomaly detection, content moderation
│  Bot Framework                      │  ← Conversational AI platform
│  Azure Databricks                   │  ← Apache Spark analytics platform
│  Azure Cognitive Search             │  ← AI-powered search service
└─────────────────────────────────────┘

## 📊 ANALYTICS & BIG DATA
┌─────────────────────────────────────┐
│  Azure Synapse Analytics            │  ← Enterprise data warehouse
│  Azure Data Factory                 │  ← Data integration and ETL
│  Azure Databricks                   │  ← Apache Spark analytics
│  HDInsight                          │  ← Managed Hadoop, Spark, Kafka
│  Stream Analytics                   │  ← Real-time stream processing
│  Azure Analysis Services            │  ← Enterprise BI semantic model
│  Power BI Embedded                  │  ← Embedded analytics
│  Data Lake Analytics                │  ← On-demand analytics job service
│  Azure Purview                      │  ← Data governance and discovery
└─────────────────────────────────────┘

## 🔗 INTEGRATION SERVICES
┌─────────────────────────────────────┐
│  Logic Apps                         │  ← Workflow automation
│  Service Bus                        │  ← Enterprise messaging
│  Event Grid                         │  ← Event routing service
│  Event Hubs                         │  ← Big data streaming platform
│  API Management                     │  ← API gateway and management
│  Azure Relay                        │  ← Hybrid connectivity
│  BizTalk Services                   │  ← Enterprise integration
└─────────────────────────────────────┘

## 🚀 DEVOPS & DEVELOPMENT
┌─────────────────────────────────────┐
│  Azure DevOps                       │  ← Complete DevOps toolchain
│  ├── Azure Repos                    │  ← Git repositories
│  ├── Azure Pipelines                │  ← CI/CD pipelines
│  ├── Azure Boards                   │  ← Work item tracking
│  ├── Azure Test Plans               │  ← Manual and exploratory testing
│  ├── Azure Artifacts                │  ← Package management
│  GitHub Actions                     │  ← CI/CD workflows
│  Azure Container Registry          │  ← Container image registry
│  Azure Resource Manager            │  ← Infrastructure as code
└─────────────────────────────────────┘

## 🌍 IOT SERVICES
┌─────────────────────────────────────┐
│  IoT Hub                            │  ← Device-to-cloud communication
│  IoT Central                        │  ← IoT application platform
│  Azure Sphere                       │  ← Secured MCU platform
│  IoT Edge                           │  ← Edge computing for IoT
│  Digital Twins                      │  ← IoT spatial intelligence
│  Time Series Insights               │  ← IoT data analytics
│  Maps                               │  ← Location-based services
└─────────────────────────────────────┘

## 📱 MOBILE SERVICES
┌─────────────────────────────────────┐
│  Mobile Apps                        │  ← Mobile backend services
│  Notification Hubs                  │  ← Push notifications
│  Visual Studio App Center           │  ← Mobile DevOps
│  Xamarin                            │  ← Cross-platform mobile development
└─────────────────────────────────────┘

## 📈 MANAGEMENT & MONITORING
┌─────────────────────────────────────┐
│  Azure Monitor                      │  ← Comprehensive monitoring solution
│  ├── Application Insights           │  ← Application performance monitoring
│  ├── Log Analytics                  │  ← Log data analysis
│  ├── Metrics                        │  ← Performance metrics
│  ├── Alerts                         │  ← Proactive notifications
│  Azure Automation                   │  ← Process automation
│  Azure Policy                       │  ← Governance and compliance
│  Azure Resource Manager             │  ← Resource lifecycle management
│  Cost Management                    │  ← Cost analysis and optimization
│  Azure Advisor                      │  ← Best practices recommendations
│  Azure Service Health               │  ← Service status and health
└─────────────────────────────────────┘

## 🌊 MIGRATION SERVICES
┌─────────────────────────────────────┐
│  Azure Migrate                      │  ← Migration assessment and tools
│  Azure Site Recovery                │  ← Disaster recovery and migration
│  Database Migration Service         │  ← Database migration
│  Azure Import/Export               │  ← Offline data transfer
│  Data Box                          │  ← Physical data transfer appliance
└─────────────────────────────────────┘

## ⚡ COMMON ARCHITECTURE PATTERNS

### 1. Three-Tier Web Application
Internet → Azure Front Door → Application Gateway → App Service → Azure SQL Database
                            ↓
                        Blob Storage (static content)

### 2. Microservices on Kubernetes
Internet → Application Gateway → AKS Cluster → Cosmos DB
                                    ↓           ↓
                            Service Bus → Redis Cache

### 3. Serverless Architecture  
Event Grid → Azure Functions → Cosmos DB
    ↓              ↓
Logic Apps → Table Storage

### 4. Big Data Analytics Pipeline
Event Hubs → Stream Analytics → Data Lake Storage Gen2 → Synapse Analytics → Power BI
                                       ↓
                               Azure Machine Learning

### 5. IoT Solution
IoT Devices → IoT Hub → Stream Analytics → Cosmos DB
                 ↓            ↓
            IoT Edge → Time Series Insights

## 🏷️ SERVICE TIERS & PRICING MODELS

### Compute Pricing
- Pay-as-you-go: Hourly billing
- Reserved Instances: 1-3 year commitments (up to 72% savings)
- Spot Instances: Unused capacity (up to 90% savings)
- Hybrid Benefit: Use existing licenses

### Storage Tiers
- Hot: Frequently accessed data
- Cool: Infrequently accessed (30+ days)
- Archive: Rarely accessed (180+ days)

### Database Tiers
- Basic: Development and testing
- Standard: Production workloads
- Premium: High-performance requirements
- Hyperscale: Large databases (up to 100TB)

## 🔧 BEST PRACTICES

### 1. Resource Organization
- Use Resource Groups for logical grouping
- Implement consistent naming conventions
- Apply comprehensive tagging strategy
- Use Management Groups for enterprise governance

### 2. Security Best Practices
- Enable Azure Security Center
- Use Azure AD for all authentication
- Store secrets in Key Vault
- Implement network security groups
- Enable audit logging

### 3. Cost Optimization
- Use Azure Advisor recommendations
- Implement auto-scaling where possible
- Right-size resources regularly
- Use reserved instances for predictable workloads
- Monitor costs with budgets and alerts

### 4. High Availability & Disaster Recovery
- Deploy across multiple availability zones
- Use geo-redundant storage
- Implement Azure Site Recovery
- Regular backup and restore testing
- Design for failure scenarios

### 5. Performance Optimization
- Use CDN for global content delivery
- Implement caching strategies
- Optimize database queries
- Use Application Insights for monitoring
- Right-size compute resources
"""
    
    # Write to file
    with open(f"{output_dir}/azure_resources_comprehensive_guide.txt", "w") as f:
        f.write(diagram_text)
    
    print("✓ Created comprehensive text-based Azure resources guide")

def create_service_matrix():
    """Create a service selection matrix"""
    
    output_dir = "azure_diagrams"
    
    matrix_content = """
# Azure Service Selection Matrix

## Choose the Right Service for Your Needs

### COMPUTE SERVICES SELECTION
┌─────────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ Requirement         │ Virtual Machine │ App Service     │ Azure Functions │
├─────────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ Full OS Control     │ ✅ YES          │ ❌ NO           │ ❌ NO           │
│ Custom Software     │ ✅ YES          │ ⚠️ LIMITED      │ ⚠️ LIMITED      │
│ Auto-scaling        │ ⚠️ MANUAL       │ ✅ YES          │ ✅ YES          │
│ Pay per execution   │ ❌ NO           │ ❌ NO           │ ✅ YES          │
│ Maintenance         │ 🔧 HIGH         │ 🔧 LOW          │ 🔧 NONE         │
│ Best for            │ Legacy apps     │ Web apps        │ Event-driven    │
└─────────────────────┴─────────────────┴─────────────────┴─────────────────┘

### DATABASE SERVICES SELECTION
┌─────────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ Requirement         │ SQL Database    │ Cosmos DB       │ MySQL/PostgreSQL│
├─────────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ ACID Transactions   │ ✅ YES          │ ⚠️ LIMITED      │ ✅ YES          │
│ Global Distribution │ ⚠️ LIMITED      │ ✅ YES          │ ❌ NO           │
│ Multiple APIs       │ ❌ SQL ONLY     │ ✅ YES          │ ❌ SQL ONLY     │
│ Auto-scaling        │ ✅ YES          │ ✅ YES          │ ⚠️ LIMITED      │
│ Open Source         │ ❌ NO           │ ❌ NO           │ ✅ YES          │
│ Best for            │ .NET apps       │ Global apps     │ LAMP stack      │
└─────────────────────┴─────────────────┴─────────────────┴─────────────────┘

### STORAGE SERVICES SELECTION
┌─────────────────────┬─────────────────┬─────────────────┬─────────────────┐
│ Use Case            │ Blob Storage    │ File Storage    │ Data Lake Gen2  │
├─────────────────────┼─────────────────┼─────────────────┼─────────────────┤
│ Unstructured data   │ ✅ BEST         │ ❌ NO           │ ✅ YES          │
│ File shares         │ ❌ NO           │ ✅ BEST         │ ❌ NO           │
│ Big data analytics  │ ⚠️ LIMITED      │ ❌ NO           │ ✅ BEST         │
│ Web content         │ ✅ YES          │ ❌ NO           │ ❌ NO           │
│ Backup & archive    │ ✅ YES          │ ✅ YES          │ ✅ YES          │
│ Hierarchical NS     │ ❌ NO           │ ✅ YES          │ ✅ YES          │
└─────────────────────┴─────────────────┴─────────────────┴─────────────────┘

## Cost Estimation Guidelines

### VM Sizing Guide
- B-series: Burstable (dev/test) - $8-50/month
- D-series: General purpose - $30-500/month  
- F-series: Compute optimized - $50-800/month
- M-series: Memory optimized - $200-5000/month

### Storage Pricing (per GB/month)
- Blob Hot: $0.018
- Blob Cool: $0.010  
- Blob Archive: $0.002
- Premium SSD: $0.15
- Standard HDD: $0.045

### Database Pricing Examples
- SQL Database Basic: $5/month
- SQL Database Standard S2: $30/month
- Cosmos DB (1000 RU/s): $60/month
- MySQL Basic: $25/month
"""
    
    with open(f"{output_dir}/azure_service_selection_matrix.txt", "w") as f:
        f.write(matrix_content)
    
    print("✓ Created Azure service selection matrix")

def main():
    """Generate all Azure resource documentation and diagrams"""
    print("🌟 Generating Azure Resources Documentation...")
    print("=" * 50)
    
    # Create output directory
    os.makedirs("azure_diagrams", exist_ok=True)
    
    # Try to create graphical diagram, fallback to text
    create_simplified_azure_diagram()
    
    # Create additional documentation
    create_service_matrix()
    
    print("\n📁 Files created in 'azure_diagrams' directory:")
    print("- azure_resources_overview.png (if successful)")
    print("- azure_resources_comprehensive_guide.txt")
    print("- azure_service_selection_matrix.txt")
    
    print("\n✨ Azure resources documentation generation complete!")
    print("\n💡 Pro tip: Also run 'python azure_explorer.py' for interactive exploration!")

if __name__ == "__main__":
    main()
