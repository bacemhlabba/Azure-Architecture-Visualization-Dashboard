#!/usr/bin/env python3
"""
Azure Architecture Extractor
Extracts and documents existing Azure resources from your subscription
"""

import json
import subprocess
import sys
from datetime import datetime
from typing import Dict, List, Any

class AzureArchitectureExtractor:
    """Extract and analyze existing Azure resources"""
    
    def __init__(self):
        self.subscription_id = None
        self.resource_groups = []
        self.resources = {}
        self.architecture_data = {}
        
    def check_azure_cli(self) -> bool:
        """Check if Azure CLI is installed and authenticated"""
        try:
            result = subprocess.run(['az', '--version'], capture_output=True, text=True)
            if result.returncode == 0:
                print("✅ Azure CLI is installed")
                return True
            else:
                print("❌ Azure CLI is not installed")
                return False
        except FileNotFoundError:
            print("❌ Azure CLI is not found. Please install it first.")
            return False
    
    def check_authentication(self) -> bool:
        """Check if user is authenticated to Azure"""
        try:
            result = subprocess.run(['az', 'account', 'show'], capture_output=True, text=True)
            if result.returncode == 0:
                account_info = json.loads(result.stdout)
                self.subscription_id = account_info.get('id')
                print(f"✅ Authenticated to Azure")
                print(f"📋 Subscription: {account_info.get('name')} ({self.subscription_id})")
                return True
            else:
                print("❌ Not authenticated to Azure. Please run 'az login' first.")
                return False
        except Exception as e:
            print(f"❌ Error checking authentication: {e}")
            return False
    
    def get_resource_groups(self) -> List[Dict]:
        """Get all resource groups in the subscription"""
        try:
            result = subprocess.run(['az', 'group', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                self.resource_groups = json.loads(result.stdout)
                print(f"📁 Found {len(self.resource_groups)} resource groups")
                return self.resource_groups
            else:
                print(f"❌ Error getting resource groups: {result.stderr}")
                return []
        except Exception as e:
            print(f"❌ Error getting resource groups: {e}")
            return []
    
    def get_all_resources(self) -> Dict[str, List]:
        """Get all resources in the subscription"""
        try:
            result = subprocess.run(['az', 'resource', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                all_resources = json.loads(result.stdout)
                
                # Group resources by type
                by_type = {}
                by_resource_group = {}
                
                for resource in all_resources:
                    resource_type = resource.get('type', 'Unknown')
                    resource_group = resource.get('resourceGroup', 'Unknown')
                    
                    if resource_type not in by_type:
                        by_type[resource_type] = []
                    by_type[resource_type].append(resource)
                    
                    if resource_group not in by_resource_group:
                        by_resource_group[resource_group] = []
                    by_resource_group[resource_group].append(resource)
                
                self.resources = {
                    'by_type': by_type,
                    'by_resource_group': by_resource_group,
                    'all': all_resources
                }
                
                print(f"🔍 Found {len(all_resources)} resources across {len(by_type)} different types")
                return self.resources
            else:
                print(f"❌ Error getting resources: {result.stderr}")
                return {}
        except Exception as e:
            print(f"❌ Error getting resources: {e}")
            return {}
    
    def analyze_architecture_patterns(self) -> Dict[str, Any]:
        """Analyze the architecture patterns in the current setup"""
        patterns = {
            'web_applications': [],
            'databases': [],
            'storage_accounts': [],
            'networking': [],
            'compute': [],
            'security': [],
            'monitoring': [],
            'devops': []
        }
        
        if not self.resources:
            return patterns
        
        # Categorize resources by service type
        for resource_type, resources in self.resources['by_type'].items():
            if any(keyword in resource_type.lower() for keyword in ['web', 'app', 'function']):
                patterns['web_applications'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['sql', 'cosmos', 'mysql', 'postgresql']):
                patterns['databases'].extend(resources)
            elif 'storage' in resource_type.lower():
                patterns['storage_accounts'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['network', 'vnet', 'subnet', 'nsg', 'lb']):
                patterns['networking'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['vm', 'compute', 'container', 'kubernetes']):
                patterns['compute'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['vault', 'security', 'identity']):
                patterns['security'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['monitor', 'insights', 'log']):
                patterns['monitoring'].extend(resources)
            elif any(keyword in resource_type.lower() for keyword in ['devops', 'pipeline', 'registry']):
                patterns['devops'].extend(resources)
        
        return patterns
    
    def generate_architecture_diagram_text(self) -> str:
        """Generate a text-based architecture diagram of current resources"""
        if not self.resources:
            return "No resources found to diagram."
        
        diagram = f"""
# 🏗️ YOUR CURRENT AZURE ARCHITECTURE
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Subscription: {self.subscription_id}

## 📊 RESOURCE SUMMARY
Total Resources: {len(self.resources.get('all', []))}
Resource Groups: {len(self.resource_groups)}
Resource Types: {len(self.resources.get('by_type', {}))}

## 📁 RESOURCE GROUPS
"""
        
        for rg in self.resource_groups:
            rg_name = rg.get('name', 'Unknown')
            location = rg.get('location', 'Unknown')
            rg_resources = self.resources.get('by_resource_group', {}).get(rg_name, [])
            
            diagram += f"""
┌─────────────────────────────────────────────────────────────────┐
│ 📁 {rg_name:<60} │
│ 📍 Location: {location:<49} │
│ 🔢 Resources: {len(rg_resources):<48} │
├─────────────────────────────────────────────────────────────────┤
"""
            
            # Group resources in this RG by type
            rg_by_type = {}
            for resource in rg_resources:
                r_type = resource.get('type', 'Unknown').split('/')[-1]  # Get just the service name
                if r_type not in rg_by_type:
                    rg_by_type[r_type] = []
                rg_by_type[r_type].append(resource)
            
            for resource_type, type_resources in rg_by_type.items():
                diagram += f"│ • {resource_type:<15} ({len(type_resources)} instances)\n"
                for resource in type_resources[:3]:  # Show first 3 instances
                    name = resource.get('name', 'Unknown')[:40]
                    diagram += f"│   └─ {name:<55} │\n"
                if len(type_resources) > 3:
                    diagram += f"│   └─ ... and {len(type_resources)-3} more\n"
            
            diagram += "└─────────────────────────────────────────────────────────────────┘\n"
        
        # Add resource type summary
        diagram += f"""
## 🔧 RESOURCE TYPES BREAKDOWN
"""
        
        for resource_type, type_resources in sorted(self.resources.get('by_type', {}).items()):
            service_name = resource_type.split('/')[-1]
            diagram += f"• {service_name:<30} : {len(type_resources):>3} instances\n"
        
        return diagram
    
    def generate_cost_analysis_guide(self) -> str:
        """Generate cost analysis guide based on current resources"""
        
        cost_guide = """
# 💰 COST ANALYSIS GUIDE FOR YOUR ARCHITECTURE

## 🎯 COST OPTIMIZATION OPPORTUNITIES

Based on your current Azure resources, here are potential cost optimization areas:

### 💻 COMPUTE RESOURCES
"""
        
        compute_resources = []
        if 'by_type' in self.resources:
            for resource_type, resources in self.resources['by_type'].items():
                if any(keyword in resource_type.lower() for keyword in ['vm', 'compute', 'app']):
                    compute_resources.extend(resources)
        
        if compute_resources:
            cost_guide += f"""
Found {len(compute_resources)} compute resources:
• Consider Reserved Instances for predictable workloads (up to 72% savings)
• Implement auto-scaling to match demand
• Review VM sizes - right-size underutilized resources
• Consider Azure Spot VMs for fault-tolerant workloads (up to 90% savings)
"""
        
        # Add storage analysis
        storage_resources = []
        if 'by_type' in self.resources:
            for resource_type, resources in self.resources['by_type'].items():
                if 'storage' in resource_type.lower():
                    storage_resources.extend(resources)
        
        if storage_resources:
            cost_guide += f"""
### 💾 STORAGE RESOURCES
Found {len(storage_resources)} storage accounts:
• Implement lifecycle management policies
• Move infrequently accessed data to Cool/Archive tiers
• Enable data deduplication where applicable
• Review backup retention policies
"""
        
        cost_guide += """
### 📊 RECOMMENDED ACTIONS
1. Set up Azure Cost Management budgets and alerts
2. Use Azure Advisor for personalized recommendations
3. Implement resource tagging for cost tracking
4. Regular monthly cost reviews
5. Consider Azure Hybrid Benefit for Windows/SQL Server licenses

### 🔍 MONITORING RECOMMENDATIONS
1. Enable Azure Monitor for all critical resources
2. Set up Application Insights for web applications
3. Configure Log Analytics workspace
4. Create custom dashboards for key metrics
"""
        
        return cost_guide
    
    def export_to_json(self, filename: str = None) -> str:
        """Export all architecture data to JSON"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"azure_architecture_export_{timestamp}.json"
        
        export_data = {
            'metadata': {
                'export_date': datetime.now().isoformat(),
                'subscription_id': self.subscription_id,
                'total_resources': len(self.resources.get('all', [])),
                'total_resource_groups': len(self.resource_groups)
            },
            'resource_groups': self.resource_groups,
            'resources': self.resources,
            'architecture_patterns': self.analyze_architecture_patterns()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False, default=str)
        
        return filename

def main():
    """Main extraction process"""
    print("🌟" + "="*70 + "🌟")
    print("        AZURE ARCHITECTURE EXTRACTOR")
    print("🌟" + "="*70 + "🌟")
    print()
    
    extractor = AzureArchitectureExtractor()
    
    # Check prerequisites
    if not extractor.check_azure_cli():
        print("\n❌ Please install Azure CLI first:")
        print("   • Windows: https://aka.ms/installazurecliwindows")
        print("   • macOS: brew install azure-cli")
        print("   • Linux: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash")
        return
    
    if not extractor.check_authentication():
        print("\n❌ Please authenticate first:")
        print("   • Run: az login")
        print("   • Follow the browser authentication process")
        return
    
    print(f"\n🔍 Starting architecture extraction...")
    print("="*50)
    
    # Extract resource groups
    extractor.get_resource_groups()
    
    # Extract all resources
    extractor.get_all_resources()
    
    # Generate outputs
    print(f"\n📄 Generating architecture documentation...")
    
    # Create architecture diagram
    diagram_text = extractor.generate_architecture_diagram_text()
    with open("azure_current_architecture.txt", "w", encoding="utf-8") as f:
        f.write(diagram_text)
    
    # Create cost analysis
    cost_guide = extractor.generate_cost_analysis_guide()
    with open("azure_cost_optimization_guide.txt", "w", encoding="utf-8") as f:
        f.write(cost_guide)
    
    # Export JSON data
    json_filename = extractor.export_to_json()
    
    # Summary
    print(f"\n✅ Architecture extraction complete!")
    print(f"📁 Files generated:")
    print(f"   • azure_current_architecture.txt - Visual architecture diagram")
    print(f"   • azure_cost_optimization_guide.txt - Cost optimization recommendations")
    print(f"   • {json_filename} - Complete resource data (JSON)")
    
    # Display quick summary
    if extractor.resources:
        print(f"\n📊 Quick Summary:")
        print(f"   • Resource Groups: {len(extractor.resource_groups)}")
        print(f"   • Total Resources: {len(extractor.resources.get('all', []))}")
        print(f"   • Resource Types: {len(extractor.resources.get('by_type', {}))}")
        
        print(f"\n🔝 Top Resource Types:")
        by_type = extractor.resources.get('by_type', {})
        sorted_types = sorted(by_type.items(), key=lambda x: len(x[1]), reverse=True)
        for resource_type, resources in sorted_types[:5]:
            service_name = resource_type.split('/')[-1]
            print(f"   • {service_name}: {len(resources)} instances")
    
    print(f"\n💡 Next Steps:")
    print(f"   1. Review the generated architecture diagram")
    print(f"   2. Check cost optimization recommendations")
    print(f"   3. Consider implementing suggested improvements")
    print(f"   4. Set up monitoring and alerting")

if __name__ == "__main__":
    main()
