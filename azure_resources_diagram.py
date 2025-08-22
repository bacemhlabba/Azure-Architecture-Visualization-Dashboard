#!/usr/bin/env python3
"""
Azure Resources Diagram Generator
Creates comprehensive diagrams showing all major Azure resources organized by categories.
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import *
from diagrams.azure.database import *
from diagrams.azure.analytics import *
from diagrams.azure.devops import *
from diagrams.azure.general import *
from diagrams.azure.identity import *
from diagrams.azure.integration import *
from diagrams.azure.iot import *
from diagrams.azure.migration import *
from diagrams.azure.ml import *
from diagrams.azure.mobile import *
from diagrams.azure.network import *
from diagrams.azure.security import *
from diagrams.azure.storage import *
from diagrams.azure.web import *
import os

def create_comprehensive_azure_diagram():
    """Create a comprehensive diagram of all Azure resources"""
    
    # Set output directory
    output_dir = "azure_diagrams"
    os.makedirs(output_dir, exist_ok=True)
    
    with Diagram("Azure Resources Overview", 
                 filename=f"{output_dir}/azure_resources_overview", 
                 show=False, 
                 direction="TB",
                 graph_attr={"size": "20,20!", "dpi": "300"}):
        
        # Compute Services
        with Cluster("Compute Services"):
            vm = VirtualMachines("Virtual Machines")
            vmss = VMScaleSet("VM Scale Sets")
            aks = KubernetesServices("AKS")
            container_instances = ContainerInstances("Container Instances")
            app_service = AppServices("App Service")
            functions = FunctionApps("Azure Functions")
            batch = Batch("Azure Batch")
            service_fabric = ServiceFabric("Service Fabric")
            
        # Storage Services  
        with Cluster("Storage Services"):
            blob_storage = BlobStorage("Blob Storage")
            disk_storage = DiskStorage("Disk Storage")
            file_storage = FileStorage("File Storage")
            queue_storage = QueueStorage("Queue Storage")
            table_storage = TableStorage("Table Storage")
            data_lake = DataLakeStorage("Data Lake Storage")
            
        # Database Services
        with Cluster("Database Services"):
            sql_database = SQLDatabases("SQL Database")
            cosmos_db = CosmosDb("Cosmos DB")
            mysql = DatabaseForMySQL("MySQL")
            postgresql = DatabaseForPostgreSQL("PostgreSQL")
            redis = RedisCache("Redis Cache")
            sql_managed = SQLManagedInstance("SQL Managed Instance")
            
        # Networking Services
        with Cluster("Networking Services"):
            vnet = VirtualNetworks("Virtual Network")
            load_balancer = LoadBalancers("Load Balancer")
            app_gateway = ApplicationGateway("Application Gateway")
            vpn_gateway = VPNGateway("VPN Gateway")
            express_route = ExpressRouteCircuits("ExpressRoute")
            traffic_manager = TrafficManagerProfiles("Traffic Manager")
            cdn = CDNProfiles("CDN")
            dns = DNSZones("DNS")
            firewall = Firewall("Azure Firewall")
            
        # Security & Identity
        with Cluster("Security & Identity"):
            active_directory = ActiveDirectory("Azure AD")
            key_vault = KeyVaults("Key Vault")
            security_center = SecurityCenter("Security Center")
            sentinel = Sentinel("Azure Sentinel")
            
        # AI & Machine Learning
        with Cluster("AI & Machine Learning"):
            cognitive_services = CognitiveServices("Cognitive Services")
            ml_service = MachineLearningService("ML Service")
            bot_services = BotServices("Bot Services")
            
        # Analytics & Big Data
        with Cluster("Analytics & Big Data"):
            synapse = SynapseAnalytics("Synapse Analytics")
            data_factory = DataFactory("Data Factory")
            databricks = Databricks("Databricks")
            hdinsight = HDInsight("HDInsight")
            stream_analytics = StreamAnalytics("Stream Analytics")
            
        # Integration Services
        with Cluster("Integration Services"):
            logic_apps = LogicApps("Logic Apps")
            service_bus = ServiceBus("Service Bus")
            event_grid = EventGrid("Event Grid")
            event_hubs = EventHubs("Event Hubs")
            api_management = APIManagement("API Management")
            
        # DevOps Services
        with Cluster("DevOps Services"):
            devops = DevopsOrganization("Azure DevOps")
            artifacts = Artifacts("Artifacts")
            pipelines = Pipelines("Pipelines")
            
        # IoT Services
        with Cluster("IoT Services"):
            iot_hub = IoTHub("IoT Hub")
            iot_central = IoTCentral("IoT Central")
            digital_twins = DigitalTwins("Digital Twins")
            
        # Management & Monitoring
        with Cluster("Management & Monitoring"):
            monitor = Monitor("Azure Monitor")
            log_analytics = LogAnalytics("Log Analytics")
            application_insights = ApplicationInsights("Application Insights")
            automation = Automation("Automation")
            resource_manager = ResourceGroups("Resource Manager")

def create_detailed_compute_diagram():
    """Create detailed diagram for compute services"""
    
    output_dir = "azure_diagrams"
    
    with Diagram("Azure Compute Services", 
                 filename=f"{output_dir}/azure_compute_detailed", 
                 show=False,
                 direction="LR"):
        
        with Cluster("Virtual Machines"):
            vm_windows = VirtualMachines("Windows VMs")
            vm_linux = VirtualMachines("Linux VMs")
            vm_spot = VirtualMachines("Spot VMs")
            
        with Cluster("Containers"):
            aks = KubernetesServices("AKS")
            aci = ContainerInstances("Container Instances")
            acr = ContainerRegistries("Container Registry")
            
        with Cluster("Serverless"):
            functions = FunctionApps("Functions")
            logic_apps = LogicApps("Logic Apps")
            
        with Cluster("Platform Services"):
            app_service = AppServices("App Service")
            static_web_apps = StaticWebApps("Static Web Apps")
            
        # Connections
        acr >> aks
        acr >> aci
        app_service >> functions

def create_detailed_storage_diagram():
    """Create detailed diagram for storage services"""
    
    output_dir = "azure_diagrams"
    
    with Diagram("Azure Storage Services", 
                 filename=f"{output_dir}/azure_storage_detailed", 
                 show=False,
                 direction="TB"):
        
        with Cluster("Storage Account Types"):
            general_purpose = BlobStorage("General Purpose v2")
            blob_storage = BlobStorage("Blob Storage")
            block_blob = BlobStorage("Block Blob Storage")
            file_storage = FileStorage("File Storage")
            
        with Cluster("Storage Tiers"):
            hot_tier = BlobStorage("Hot Tier")
            cool_tier = BlobStorage("Cool Tier")
            archive_tier = BlobStorage("Archive Tier")
            
        with Cluster("Data Services"):
            data_lake = DataLakeStorage("Data Lake Gen2")
            queue_storage = QueueStorage("Queue Storage")
            table_storage = TableStorage("Table Storage")

def create_network_diagram():
    """Create detailed network architecture diagram"""
    
    output_dir = "azure_diagrams"
    
    with Diagram("Azure Network Architecture", 
                 filename=f"{output_dir}/azure_network_detailed", 
                 show=False,
                 direction="TB"):
        
        with Cluster("Core Networking"):
            vnet = VirtualNetworks("Virtual Network")
            subnet = Subnets("Subnets")
            nsg = NetworkSecurityGroups("Network Security Groups")
            
        with Cluster("Load Balancing"):
            load_balancer = LoadBalancers("Load Balancer")
            app_gateway = ApplicationGateway("Application Gateway")
            traffic_manager = TrafficManagerProfiles("Traffic Manager")
            front_door = FrontDoors("Front Door")
            
        with Cluster("Connectivity"):
            vpn_gateway = VPNGateway("VPN Gateway")
            express_route = ExpressRouteCircuits("ExpressRoute")
            virtual_wan = VirtualWans("Virtual WAN")
            
        with Cluster("Security"):
            firewall = Firewall("Azure Firewall")
            ddos = DDOSProtectionPlans("DDoS Protection")
            
        with Cluster("DNS & CDN"):
            dns = DNSZones("DNS Zones")
            private_dns = PrivateDnsZones("Private DNS")
            cdn = CDNProfiles("CDN")
            
        # Network flow
        vnet >> subnet
        subnet >> nsg
        load_balancer >> vnet
        app_gateway >> vnet
        vpn_gateway >> vnet
        firewall >> vnet

def main():
    """Generate all Azure resource diagrams"""
    print("Generating Azure resource diagrams...")
    
    # Create output directory
    os.makedirs("azure_diagrams", exist_ok=True)
    
    # Generate diagrams
    create_comprehensive_azure_diagram()
    print("✓ Created comprehensive Azure resources overview")
    
    create_detailed_compute_diagram()
    print("✓ Created detailed compute services diagram")
    
    create_detailed_storage_diagram()
    print("✓ Created detailed storage services diagram")
    
    create_network_diagram()
    print("✓ Created detailed network architecture diagram")
    
    print("\nAll diagrams have been generated in the 'azure_diagrams' directory!")
    print("Files created:")
    print("- azure_resources_overview.png")
    print("- azure_compute_detailed.png")
    print("- azure_storage_detailed.png")
    print("- azure_network_detailed.png")

if __name__ == "__main__":
    main()
