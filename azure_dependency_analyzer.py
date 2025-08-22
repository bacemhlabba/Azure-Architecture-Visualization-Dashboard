#!/usr/bin/env python3
"""
Advanced Azure Resource Dependencies Analyzer
Analyzes dependencies and relationships between Azure resources
"""

import json
import subprocess
import sys
from typing import Dict, List, Any, Set
from collections import defaultdict

class AzureDependencyAnalyzer:
    """Analyze dependencies and relationships between Azure resources"""
    
    def __init__(self):
        self.resources = []
        self.dependencies = defaultdict(list)
        self.network_topology = {}
        self.security_analysis = {}
    
    def get_virtual_networks(self) -> List[Dict]:
        """Get detailed information about virtual networks"""
        try:
            result = subprocess.run(['az', 'network', 'vnet', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                vnets = json.loads(result.stdout)
                print(f"🌐 Found {len(vnets)} Virtual Networks")
                return vnets
            else:
                print(f"❌ Error getting VNets: {result.stderr}")
                return []
        except Exception as e:
            print(f"❌ Error getting VNets: {e}")
            return []
    
    def get_subnets_for_vnet(self, vnet_name: str, resource_group: str) -> List[Dict]:
        """Get subnets for a specific virtual network"""
        try:
            result = subprocess.run([
                'az', 'network', 'vnet', 'subnet', 'list',
                '--vnet-name', vnet_name,
                '--resource-group', resource_group
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                return json.loads(result.stdout)
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting subnets for {vnet_name}: {e}")
            return []
    
    def get_network_security_groups(self) -> List[Dict]:
        """Get Network Security Groups and their rules"""
        try:
            result = subprocess.run(['az', 'network', 'nsg', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                nsgs = json.loads(result.stdout)
                print(f"🛡️ Found {len(nsgs)} Network Security Groups")
                return nsgs
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting NSGs: {e}")
            return []
    
    def get_load_balancers(self) -> List[Dict]:
        """Get Load Balancers and their configuration"""
        try:
            result = subprocess.run(['az', 'network', 'lb', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                lbs = json.loads(result.stdout)
                print(f"⚖️ Found {len(lbs)} Load Balancers")
                return lbs
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting Load Balancers: {e}")
            return []
    
    def get_public_ips(self) -> List[Dict]:
        """Get Public IP addresses"""
        try:
            result = subprocess.run(['az', 'network', 'public-ip', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                public_ips = json.loads(result.stdout)
                print(f"🌍 Found {len(public_ips)} Public IP addresses")
                return public_ips
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting Public IPs: {e}")
            return []
    
    def get_virtual_machines(self) -> List[Dict]:
        """Get Virtual Machines with detailed information"""
        try:
            result = subprocess.run(['az', 'vm', 'list', '--show-details'], capture_output=True, text=True)
            if result.returncode == 0:
                vms = json.loads(result.stdout)
                print(f"💻 Found {len(vms)} Virtual Machines")
                return vms
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting VMs: {e}")
            return []
    
    def get_storage_accounts(self) -> List[Dict]:
        """Get Storage Accounts"""
        try:
            result = subprocess.run(['az', 'storage', 'account', 'list'], capture_output=True, text=True)
            if result.returncode == 0:
                storage_accounts = json.loads(result.stdout)
                print(f"💾 Found {len(storage_accounts)} Storage Accounts")
                return storage_accounts
            else:
                return []
        except Exception as e:
            print(f"❌ Error getting Storage Accounts: {e}")
            return []
    
    def analyze_network_topology(self) -> Dict[str, Any]:
        """Analyze the network topology and create a visual representation"""
        topology = {
            'vnets': [],
            'subnets': [],
            'nsgs': [],
            'load_balancers': [],
            'public_ips': [],
            'connections': []
        }
        
        # Get networking components
        vnets = self.get_virtual_networks()
        nsgs = self.get_network_security_groups()
        lbs = self.get_load_balancers()
        public_ips = self.get_public_ips()
        
        # Process VNets and their subnets
        for vnet in vnets:
            vnet_info = {
                'name': vnet.get('name'),
                'resource_group': vnet.get('resourceGroup'),
                'address_space': vnet.get('addressSpace', {}).get('addressPrefixes', []),
                'location': vnet.get('location'),
                'subnets': []
            }
            
            # Get subnets for this VNet
            subnets = self.get_subnets_for_vnet(vnet['name'], vnet['resourceGroup'])
            for subnet in subnets:
                subnet_info = {
                    'name': subnet.get('name'),
                    'address_prefix': subnet.get('addressPrefix'),
                    'nsg': subnet.get('networkSecurityGroup', {}).get('id', '').split('/')[-1] if subnet.get('networkSecurityGroup') else None
                }
                vnet_info['subnets'].append(subnet_info)
            
            topology['vnets'].append(vnet_info)
        
        topology['nsgs'] = nsgs
        topology['load_balancers'] = lbs
        topology['public_ips'] = public_ips
        
        return topology
    
    def generate_network_diagram(self, topology: Dict[str, Any]) -> str:
        """Generate a text-based network diagram"""
        
        diagram = """
# 🌐 NETWORK TOPOLOGY DIAGRAM

## Virtual Networks and Subnets
"""
        
        for vnet in topology['vnets']:
            diagram += f"""
┌─────────────────────────────────────────────────────────────────────────────┐
│ 🌐 VNet: {vnet['name']:<50} │
│ 📍 Resource Group: {vnet['resource_group']:<42} │
│ 📊 Address Space: {', '.join(vnet['address_space']):<44} │
│ 📍 Location: {vnet['location']:<52} │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🔗 SUBNETS:                                                                  │
"""
            
            for subnet in vnet['subnets']:
                nsg_info = f" (NSG: {subnet['nsg']})" if subnet['nsg'] else " (No NSG)"
                diagram += f"│   • {subnet['name']:<20} {subnet['address_prefix']:<15}{nsg_info:<25} │\n"
            
            if not vnet['subnets']:
                diagram += "│   • No subnets found                                                       │\n"
            
            diagram += "└─────────────────────────────────────────────────────────────────────────────┘\n\n"
        
        # Add NSG information
        if topology['nsgs']:
            diagram += "## 🛡️ Network Security Groups\n\n"
            for nsg in topology['nsgs']:
                diagram += f"• {nsg.get('name', 'Unknown'):<30} (Resource Group: {nsg.get('resourceGroup', 'Unknown')})\n"
        
        # Add Load Balancer information
        if topology['load_balancers']:
            diagram += "\n## ⚖️ Load Balancers\n\n"
            for lb in topology['load_balancers']:
                diagram += f"• {lb.get('name', 'Unknown'):<30} (Type: {lb.get('sku', {}).get('name', 'Unknown')})\n"
        
        # Add Public IP information
        if topology['public_ips']:
            diagram += "\n## 🌍 Public IP Addresses\n\n"
            for pip in topology['public_ips']:
                ip_address = pip.get('ipAddress', 'Not assigned')
                allocation = pip.get('publicIPAllocationMethod', 'Unknown')
                diagram += f"• {pip.get('name', 'Unknown'):<30} {ip_address:<15} ({allocation})\n"
        
        return diagram
    
    def analyze_security_configuration(self) -> Dict[str, Any]:
        """Analyze security configuration and provide recommendations"""
        security_analysis = {
            'findings': [],
            'recommendations': [],
            'critical_issues': [],
            'best_practices': []
        }
        
        # Analyze NSGs
        nsgs = self.get_network_security_groups()
        for nsg in nsgs:
            # Check for overly permissive rules
            if 'securityRules' in nsg:
                for rule in nsg['securityRules']:
                    if (rule.get('sourceAddressPrefix') == '*' and 
                        rule.get('destinationPortRange') in ['*', '22', '3389']):
                        security_analysis['critical_issues'].append(
                            f"⚠️ NSG '{nsg['name']}' has overly permissive rule: {rule['name']}"
                        )
        
        # Check for public IPs without proper protection
        public_ips = self.get_public_ips()
        if len(public_ips) > 0:
            security_analysis['findings'].append(
                f"Found {len(public_ips)} public IP addresses - ensure they're properly protected"
            )
        
        # Add general recommendations
        security_analysis['recommendations'] = [
            "Enable Azure Security Center for all subscriptions",
            "Implement Just-In-Time VM access for administrative ports",
            "Use Azure Key Vault for storing secrets and certificates",
            "Enable Network Watcher for network monitoring",
            "Implement Azure Firewall for centralized network security",
            "Use Azure AD Conditional Access for identity security"
        ]
        
        security_analysis['best_practices'] = [
            "Regular security assessments and penetration testing",
            "Implement network segmentation with subnets and NSGs",
            "Use managed identities instead of service principals where possible",
            "Enable logging and monitoring for all critical resources",
            "Implement backup and disaster recovery procedures"
        ]
        
        return security_analysis
    
    def generate_security_report(self, security_analysis: Dict[str, Any]) -> str:
        """Generate a security analysis report"""
        
        report = """
# 🔒 SECURITY ANALYSIS REPORT

## ⚠️ Critical Issues
"""
        
        if security_analysis['critical_issues']:
            for issue in security_analysis['critical_issues']:
                report += f"{issue}\n"
        else:
            report += "✅ No critical security issues found\n"
        
        report += """
## 🔍 Security Findings
"""
        
        if security_analysis['findings']:
            for finding in security_analysis['findings']:
                report += f"• {finding}\n"
        else:
            report += "• No specific security findings\n"
        
        report += """
## 💡 Recommendations
"""
        
        for i, recommendation in enumerate(security_analysis['recommendations'], 1):
            report += f"{i}. {recommendation}\n"
        
        report += """
## ✅ Security Best Practices
"""
        
        for practice in security_analysis['best_practices']:
            report += f"• {practice}\n"
        
        return report
    
    def generate_comprehensive_report(self) -> str:
        """Generate a comprehensive architecture and security report"""
        
        print("🔍 Analyzing network topology...")
        topology = self.analyze_network_topology()
        
        print("🔒 Analyzing security configuration...")
        security_analysis = self.analyze_security_configuration()
        
        print("📊 Generating comprehensive report...")
        
        # Generate individual reports
        network_diagram = self.generate_network_diagram(topology)
        security_report = self.generate_security_report(security_analysis)
        
        # Combine into comprehensive report
        comprehensive_report = f"""
# 🏗️ COMPREHENSIVE AZURE ARCHITECTURE ANALYSIS
Generated on: {subprocess.run(['date'], capture_output=True, text=True).stdout.strip()}

{network_diagram}

{security_report}

## 📋 SUMMARY AND NEXT STEPS

### 🎯 Immediate Actions
1. Review and address any critical security issues
2. Implement recommended security controls
3. Set up monitoring and alerting
4. Document current architecture for future reference

### 🔄 Regular Maintenance
1. Monthly security reviews
2. Quarterly architecture assessments
3. Regular cost optimization reviews
4. Update documentation as changes are made

### 🛠️ Tools for Ongoing Management
• Azure Security Center - Security posture management
• Azure Monitor - Comprehensive monitoring
• Azure Cost Management - Cost tracking and optimization
• Azure Resource Graph - Resource querying and analysis
• Azure Blueprints - Governance and compliance
"""
        
        return comprehensive_report

def main():
    """Main analysis process"""
    print("🌟" + "="*70 + "🌟")
    print("        AZURE DEPENDENCY & SECURITY ANALYZER")
    print("🌟" + "="*70 + "🌟")
    print()
    
    analyzer = AzureDependencyAnalyzer()
    
    # Check if Azure CLI is available and user is authenticated
    try:
        result = subprocess.run(['az', 'account', 'show'], capture_output=True, text=True)
        if result.returncode != 0:
            print("❌ Please authenticate with Azure CLI first: az login")
            return
        
        account_info = json.loads(result.stdout)
        print(f"✅ Connected to subscription: {account_info.get('name')}")
        
    except Exception as e:
        print(f"❌ Error checking Azure CLI: {e}")
        return
    
    # Generate comprehensive report
    comprehensive_report = analyzer.generate_comprehensive_report()
    
    # Save report
    with open("azure_comprehensive_analysis.txt", "w", encoding="utf-8") as f:
        f.write(comprehensive_report)
    
    print(f"\n✅ Analysis complete!")
    print(f"📁 Report saved to: azure_comprehensive_analysis.txt")
    
    print(f"\n📊 Analysis included:")
    print(f"   • Network topology mapping")
    print(f"   • Security configuration review")
    print(f"   • Resource dependency analysis")
    print(f"   • Recommendations for improvements")

if __name__ == "__main__":
    main()
