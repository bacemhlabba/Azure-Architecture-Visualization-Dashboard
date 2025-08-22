#!/usr/bin/env python3
"""
Interactive Azure Resources Explorer
Allows users to explore Azure services by category and generate custom diagrams.
"""

import json
from typing import Dict, List, Any

class AzureResourceExplorer:
    """Interactive explorer for Azure resources"""
    
    def __init__(self):
        self.azure_services = self._load_azure_services()
    
    def _load_azure_services(self) -> Dict[str, Any]:
        """Load comprehensive Azure services catalog"""
        return {
            "compute": {
                "name": "Compute Services",
                "description": "Services for running applications and workloads",
                "services": {
                    "virtual_machines": {
                        "name": "Virtual Machines",
                        "description": "Scalable, on-demand computing resources",
                        "use_cases": ["Web servers", "Application servers", "Database servers", "Development environments"],
                        "pricing_models": ["Pay-as-you-go", "Reserved instances", "Spot instances"],
                        "sizes": ["B-series (Burstable)", "D-series (General purpose)", "F-series (Compute optimized)", "M-series (Memory optimized)"]
                    },
                    "app_service": {
                        "name": "App Service",
                        "description": "Fully managed platform for building web apps and APIs",
                        "use_cases": ["Web applications", "REST APIs", "Mobile backends", "Static websites"],
                        "supported_languages": ["C#", "Java", "Node.js", "Python", "PHP", "Ruby"],
                        "features": ["Auto-scaling", "Custom domains", "SSL certificates", "Deployment slots"]
                    },
                    "azure_functions": {
                        "name": "Azure Functions",
                        "description": "Event-driven serverless compute platform",
                        "use_cases": ["Event processing", "Data transformation", "API backends", "Scheduled tasks"],
                        "triggers": ["HTTP", "Timer", "Blob storage", "Queue", "Event Hub", "Service Bus"],
                        "pricing": "Pay per execution"
                    },
                    "kubernetes_service": {
                        "name": "Azure Kubernetes Service (AKS)",
                        "description": "Managed Kubernetes container orchestration",
                        "use_cases": ["Microservices", "Container orchestration", "CI/CD", "Machine learning workloads"],
                        "features": ["Auto-scaling", "Azure AD integration", "GPU support", "Virtual nodes"]
                    },
                    "container_instances": {
                        "name": "Container Instances",
                        "description": "Run containers without managing servers",
                        "use_cases": ["Batch processing", "Development/testing", "Event-driven applications"],
                        "features": ["Per-second billing", "Custom sizes", "Persistent storage", "Virtual network integration"]
                    }
                }
            },
            "storage": {
                "name": "Storage Services",
                "description": "Secure, scalable, and durable storage solutions",
                "services": {
                    "blob_storage": {
                        "name": "Blob Storage",
                        "description": "Object storage for unstructured data",
                        "use_cases": ["Data backup", "Content distribution", "Data archiving", "Big data analytics"],
                        "tiers": ["Hot", "Cool", "Archive"],
                        "types": ["Block blobs", "Append blobs", "Page blobs"]
                    },
                    "file_storage": {
                        "name": "Azure Files",
                        "description": "Managed file shares in the cloud",
                        "use_cases": ["Shared application data", "Lift-and-shift scenarios", "Container storage"],
                        "protocols": ["SMB", "NFS", "REST API"],
                        "features": ["Snapshot support", "Azure AD authentication", "Encryption"]
                    },
                    "data_lake_storage": {
                        "name": "Data Lake Storage Gen2",
                        "description": "Massively scalable data lake for big data analytics",
                        "use_cases": ["Big data analytics", "Data warehousing", "IoT data", "Machine learning"],
                        "features": ["Hierarchical namespace", "Fine-grained access control", "Analytics optimization"]
                    }
                }
            },
            "database": {
                "name": "Database Services",
                "description": "Fully managed database services",
                "services": {
                    "sql_database": {
                        "name": "Azure SQL Database",
                        "description": "Managed relational database service",
                        "use_cases": ["Web applications", "SaaS applications", "Data warehousing"],
                        "service_tiers": ["Basic", "Standard", "Premium", "General Purpose", "Business Critical"],
                        "features": ["Automatic tuning", "Threat detection", "Backup and restore", "Geo-replication"]
                    },
                    "cosmos_db": {
                        "name": "Azure Cosmos DB",
                        "description": "Globally distributed multi-model database",
                        "use_cases": ["Global applications", "IoT telemetry", "Gaming", "Social media"],
                        "apis": ["SQL", "MongoDB", "Cassandra", "Gremlin", "Table"],
                        "features": ["Global distribution", "Multi-master", "Automatic scaling", "SLA guarantees"]
                    },
                    "mysql": {
                        "name": "Azure Database for MySQL",
                        "description": "Managed MySQL database service",
                        "use_cases": ["Web applications", "E-commerce", "Content management"],
                        "versions": ["MySQL 5.6", "MySQL 5.7", "MySQL 8.0"],
                        "features": ["Automatic backup", "Point-in-time restore", "SSL enforcement", "Advanced threat protection"]
                    }
                }
            },
            "networking": {
                "name": "Networking Services",
                "description": "Connect and secure your cloud resources",
                "services": {
                    "virtual_network": {
                        "name": "Virtual Network",
                        "description": "Private network in Azure",
                        "use_cases": ["Resource isolation", "Multi-tier applications", "Hybrid connectivity"],
                        "features": ["Subnets", "Network security groups", "Route tables", "VNet peering"]
                    },
                    "load_balancer": {
                        "name": "Load Balancer",
                        "description": "Distribute traffic across multiple resources",
                        "use_cases": ["High availability", "Scalability", "Traffic distribution"],
                        "types": ["Basic", "Standard"],
                        "features": ["Health probes", "Outbound rules", "Multiple frontends", "IPv6 support"]
                    },
                    "application_gateway": {
                        "name": "Application Gateway",
                        "description": "Layer 7 load balancer with web application firewall",
                        "use_cases": ["Web applications", "SSL termination", "URL-based routing"],
                        "features": ["WAF", "SSL offloading", "Cookie-based session affinity", "Multi-site hosting"]
                    }
                }
            },
            "security": {
                "name": "Security & Identity",
                "description": "Secure your applications and data",
                "services": {
                    "active_directory": {
                        "name": "Azure Active Directory",
                        "description": "Cloud-based identity and access management",
                        "use_cases": ["Single sign-on", "Multi-factor authentication", "Identity governance"],
                        "editions": ["Free", "Basic", "Premium P1", "Premium P2"],
                        "features": ["SSO", "MFA", "Conditional access", "Identity protection"]
                    },
                    "key_vault": {
                        "name": "Azure Key Vault",
                        "description": "Secure secrets, keys, and certificates",
                        "use_cases": ["Secret management", "Key management", "Certificate management"],
                        "features": ["Hardware security modules", "Access policies", "Audit logging", "Network access control"]
                    }
                }
            },
            "ai_ml": {
                "name": "AI & Machine Learning",
                "description": "Build intelligent applications",
                "services": {
                    "cognitive_services": {
                        "name": "Cognitive Services",
                        "description": "Pre-built AI capabilities",
                        "categories": ["Vision", "Speech", "Language", "Decision"],
                        "services": ["Computer Vision", "Speech to Text", "Text Analytics", "Anomaly Detector"],
                        "use_cases": ["Image recognition", "Speech recognition", "Language understanding", "Content moderation"]
                    },
                    "machine_learning": {
                        "name": "Azure Machine Learning",
                        "description": "End-to-end machine learning lifecycle",
                        "use_cases": ["Model development", "Model deployment", "MLOps", "AutoML"],
                        "features": ["Automated ML", "Designer", "Notebooks", "Model registry", "Endpoints"]
                    }
                }
            }
        }
    
    def list_categories(self) -> List[str]:
        """List all service categories"""
        return list(self.azure_services.keys())
    
    def get_category_info(self, category: str) -> Dict[str, Any]:
        """Get information about a specific category"""
        return self.azure_services.get(category, {})
    
    def get_service_info(self, category: str, service: str) -> Dict[str, Any]:
        """Get detailed information about a specific service"""
        category_data = self.azure_services.get(category, {})
        services = category_data.get("services", {})
        return services.get(service, {})
    
    def search_services(self, query: str) -> List[Dict[str, Any]]:
        """Search for services by name or description"""
        results = []
        query_lower = query.lower()
        
        for category_key, category_data in self.azure_services.items():
            for service_key, service_data in category_data.get("services", {}).items():
                service_name = service_data.get("name", "").lower()
                service_desc = service_data.get("description", "").lower()
                
                if (query_lower in service_name or 
                    query_lower in service_desc or
                    any(query_lower in use_case.lower() for use_case in service_data.get("use_cases", []))):
                    
                    results.append({
                        "category": category_key,
                        "service_key": service_key,
                        "name": service_data.get("name"),
                        "description": service_data.get("description"),
                        "category_name": category_data.get("name")
                    })
        
        return results
    
    def export_to_json(self, filename: str = "azure_services_catalog.json"):
        """Export the complete catalog to JSON"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.azure_services, f, indent=2, ensure_ascii=False)
        print(f"Azure services catalog exported to {filename}")

def interactive_explorer():
    """Interactive command-line explorer"""
    explorer = AzureResourceExplorer()
    
    print("🌟 Azure Resources Explorer 🌟")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. List all categories")
        print("2. Explore a category")
        print("3. Search services")
        print("4. Export catalog to JSON")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            print("\n📂 Azure Service Categories:")
            categories = explorer.list_categories()
            for i, category in enumerate(categories, 1):
                category_info = explorer.get_category_info(category)
                print(f"{i}. {category_info.get('name', category)} - {category_info.get('description', '')}")
        
        elif choice == "2":
            categories = explorer.list_categories()
            print("\n📂 Select a category:")
            for i, category in enumerate(categories, 1):
                category_info = explorer.get_category_info(category)
                print(f"{i}. {category_info.get('name', category)}")
            
            try:
                cat_choice = int(input("Enter category number: ")) - 1
                if 0 <= cat_choice < len(categories):
                    category = categories[cat_choice]
                    category_info = explorer.get_category_info(category)
                    
                    print(f"\n🔍 {category_info.get('name', category)}")
                    print(f"Description: {category_info.get('description', '')}")
                    print("\nServices:")
                    
                    services = category_info.get("services", {})
                    for service_key, service_data in services.items():
                        print(f"\n• {service_data.get('name', service_key)}")
                        print(f"  {service_data.get('description', '')}")
                        if service_data.get('use_cases'):
                            print(f"  Use cases: {', '.join(service_data['use_cases'])}")
                else:
                    print("Invalid category number!")
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "3":
            query = input("\n🔍 Enter search term: ").strip()
            if query:
                results = explorer.search_services(query)
                if results:
                    print(f"\n📋 Found {len(results)} matching services:")
                    for result in results:
                        print(f"\n• {result['name']} ({result['category_name']})")
                        print(f"  {result['description']}")
                else:
                    print("No services found matching your query.")
            else:
                print("Please enter a search term!")
        
        elif choice == "4":
            filename = input("Enter filename (default: azure_services_catalog.json): ").strip()
            if not filename:
                filename = "azure_services_catalog.json"
            explorer.export_to_json(filename)
        
        elif choice == "5":
            print("Thank you for using Azure Resources Explorer! 👋")
            break
        
        else:
            print("Invalid choice! Please enter 1-5.")

if __name__ == "__main__":
    interactive_explorer()
