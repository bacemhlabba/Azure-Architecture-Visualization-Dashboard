#!/usr/bin/env python3
"""
Modern Azure Architecture PNG Diagram Generator
Creates beautiful, modern PNG diagrams from Azure architecture data
"""

import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np
from datetime import datetime
import os
from typing import Dict, List, Any, Tuple
from collections import defaultdict
import seaborn as sns

# Set modern style
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class ModernAzureDiagramGenerator:
    """Generate modern, beautiful PNG diagrams of Azure architecture"""
    
    def __init__(self, architecture_file: str):
        self.architecture_file = architecture_file
        self.architecture_data = {}
        self.color_scheme = {
            'compute': '#0078D4',      # Azure Blue
            'storage': '#00BCF2',      # Light Blue
            'database': '#40E0D0',     # Turquoise
            'network': '#107C10',      # Green
            'security': '#D83B01',     # Orange/Red
            'analytics': '#5C2D91',    # Purple
            'ai_ml': '#E81123',        # Red
            'integration': '#0078D4',  # Blue
            'monitoring': '#00188F',   # Dark Blue
            'background': '#F8F9FA',   # Light Gray
            'text': '#323130',         # Dark Gray
            'border': '#D2D0CE'        # Medium Gray
        }
        self.load_architecture_data()
    
    def load_architecture_data(self):
        """Load architecture data from JSON file"""
        try:
            with open(self.architecture_file, 'r', encoding='utf-8') as f:
                self.architecture_data = json.load(f)
            print(f"✅ Loaded architecture data: {self.architecture_data['metadata']['total_resources']} resources")
        except Exception as e:
            print(f"❌ Error loading architecture data: {e}")
            self.architecture_data = {}
    
    def categorize_resources(self) -> Dict[str, List]:
        """Categorize resources by service type"""
        categories = {
            'compute': [],
            'storage': [],
            'database': [],
            'network': [],
            'security': [],
            'analytics': [],
            'ai_ml': [],
            'integration': [],
            'monitoring': [],
            'other': []
        }
        
        if 'resources' not in self.architecture_data or 'by_type' not in self.architecture_data['resources']:
            return categories
        
        type_mapping = {
            'compute': ['microsoft.compute', 'microsoft.containerservice', 'microsoft.containerinstance', 'microsoft.web'],
            'storage': ['microsoft.storage'],
            'database': ['microsoft.sql', 'microsoft.documentdb', 'microsoft.dbformysql', 'microsoft.dbforpostgresql', 'microsoft.cache'],
            'network': ['microsoft.network'],
            'security': ['microsoft.keyvault', 'microsoft.security'],
            'analytics': ['microsoft.synapse', 'microsoft.datafactory', 'microsoft.databricks', 'microsoft.streamanalytics'],
            'ai_ml': ['microsoft.cognitiveservices', 'microsoft.machinelearningservices'],
            'integration': ['microsoft.logic', 'microsoft.servicebus', 'microsoft.eventgrid', 'microsoft.eventhub'],
            'monitoring': ['microsoft.insights', 'microsoft.operationalinsights']
        }
        
        for resource_type, resources in self.architecture_data['resources']['by_type'].items():
            resource_type_lower = resource_type.lower()
            categorized = False
            
            for category, keywords in type_mapping.items():
                if any(keyword in resource_type_lower for keyword in keywords):
                    categories[category].extend(resources)
                    categorized = True
                    break
            
            if not categorized:
                categories['other'].extend(resources)
        
        return categories
    
    def create_overview_diagram(self, output_file: str = "azure_architecture_overview.png"):
        """Create a modern overview diagram of the entire architecture"""
        
        categories = self.categorize_resources()
        
        # Create figure with modern styling
        fig, ax = plt.subplots(figsize=(16, 12))
        fig.patch.set_facecolor(self.color_scheme['background'])
        ax.set_facecolor(self.color_scheme['background'])
        
        # Title
        metadata = self.architecture_data.get('metadata', {})
        title = f"Azure Architecture Overview\nSubscription: {metadata.get('subscription_id', 'Unknown')[:8]}... | {metadata.get('total_resources', 0)} Resources | {metadata.get('total_resource_groups', 0)} Resource Groups"
        ax.text(0.5, 0.95, title, ha='center', va='top', transform=ax.transAxes,
                fontsize=16, fontweight='bold', color=self.color_scheme['text'])
        
        # Calculate positions for category boxes
        cols = 3
        rows = 4
        box_width = 0.25
        box_height = 0.15
        
        positions = []
        for row in range(rows):
            for col in range(cols):
                if len(positions) < len(categories):
                    x = 0.1 + col * 0.3
                    y = 0.8 - row * 0.2
                    positions.append((x, y))
        
        # Draw category boxes
        category_names = list(categories.keys())
        for i, (category, resources) in enumerate(categories.items()):
            if i >= len(positions):
                break
                
            x, y = positions[i]
            
            # Create fancy box
            box = FancyBboxPatch(
                (x, y), box_width, box_height,
                boxstyle="round,pad=0.01",
                facecolor=self.color_scheme.get(category, '#808080'),
                edgecolor=self.color_scheme['border'],
                linewidth=2,
                alpha=0.8
            )
            ax.add_patch(box)
            
            # Add category label
            ax.text(x + box_width/2, y + box_height - 0.03, 
                   category.replace('_', ' ').title(),
                   ha='center', va='center', fontsize=12, fontweight='bold',
                   color='white')
            
            # Add resource count
            ax.text(x + box_width/2, y + 0.05,
                   f"{len(resources)} resources",
                   ha='center', va='center', fontsize=10,
                   color='white', style='italic')
            
            # Add some example resource types
            if resources:
                example_types = set()
                for resource in resources[:3]:  # Show up to 3 example types
                    service_type = resource.get('type', '').split('/')[-1]
                    if service_type:
                        example_types.add(service_type)
                
                examples_text = '\n'.join(list(example_types)[:2])  # Show 2 examples
                ax.text(x + box_width/2, y + box_height/2 - 0.02,
                       examples_text,
                       ha='center', va='center', fontsize=8,
                       color='white', alpha=0.9)
        
        # Add legend
        legend_y = 0.02
        ax.text(0.02, legend_y + 0.06, "Resource Categories:", 
               fontsize=10, fontweight='bold', color=self.color_scheme['text'])
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ax.text(0.98, 0.02, f"Generated: {timestamp}", 
               ha='right', va='bottom', fontsize=8, 
               color=self.color_scheme['text'], alpha=0.7)
        
        # Remove axes
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        # Save with high DPI
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight', 
                   facecolor=self.color_scheme['background'])
        plt.close()
        
        print(f"✅ Created overview diagram: {output_file}")
        return output_file
    
    def create_resource_groups_diagram(self, output_file: str = "azure_resource_groups.png"):
        """Create a diagram showing resource groups and their contents"""
        
        fig, ax = plt.subplots(figsize=(20, 14))
        fig.patch.set_facecolor(self.color_scheme['background'])
        ax.set_facecolor(self.color_scheme['background'])
        
        # Title
        metadata = self.architecture_data.get('metadata', {})
        title = f"Azure Resource Groups Layout\n{metadata.get('total_resource_groups', 0)} Resource Groups"
        ax.text(0.5, 0.97, title, ha='center', va='top', transform=ax.transAxes,
                fontsize=18, fontweight='bold', color=self.color_scheme['text'])
        
        resource_groups = self.architecture_data.get('resource_groups', [])
        resources_by_rg = self.architecture_data.get('resources', {}).get('by_resource_group', {})
        
        if not resource_groups:
            ax.text(0.5, 0.5, "No resource groups found", ha='center', va='center',
                   fontsize=16, color=self.color_scheme['text'])
            ax.axis('off')
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            plt.close()
            return output_file
        
        # Calculate grid layout
        cols = min(3, len(resource_groups))
        rows = (len(resource_groups) + cols - 1) // cols
        
        box_width = 0.28
        box_height = 0.18
        
        for i, rg in enumerate(resource_groups):
            row = i // cols
            col = i % cols
            
            x = 0.05 + col * 0.32
            y = 0.85 - row * 0.22
            
            # Resource group box
            rg_box = FancyBboxPatch(
                (x, y), box_width, box_height,
                boxstyle="round,pad=0.01",
                facecolor='white',
                edgecolor=self.color_scheme['network'],
                linewidth=2,
                alpha=0.9
            )
            ax.add_patch(rg_box)
            
            # RG name and location
            rg_name = rg.get('name', 'Unknown')
            location = rg.get('location', 'Unknown')
            
            ax.text(x + box_width/2, y + box_height - 0.03,
                   f"📁 {rg_name}",
                   ha='center', va='center', fontsize=11, fontweight='bold',
                   color=self.color_scheme['text'])
            
            ax.text(x + box_width/2, y + box_height - 0.06,
                   f"📍 {location}",
                   ha='center', va='center', fontsize=9,
                   color=self.color_scheme['text'], alpha=0.8)
            
            # Resources in this RG
            rg_resources = resources_by_rg.get(rg_name, [])
            
            # Group resources by type
            resource_types = defaultdict(int)
            for resource in rg_resources:
                service_type = resource.get('type', '').split('/')[-1]
                if service_type:
                    resource_types[service_type] += 1
            
            # Display top resource types
            y_offset = 0.10
            for j, (resource_type, count) in enumerate(list(resource_types.items())[:4]):
                ax.text(x + 0.02, y + y_offset - j * 0.025,
                       f"• {resource_type}: {count}",
                       ha='left', va='center', fontsize=8,
                       color=self.color_scheme['text'])
            
            if len(resource_types) > 4:
                ax.text(x + 0.02, y + y_offset - 4 * 0.025,
                       f"... and {len(resource_types) - 4} more types",
                       ha='left', va='center', fontsize=8,
                       color=self.color_scheme['text'], style='italic')
            
            # Total resources count
            ax.text(x + box_width - 0.02, y + 0.02,
                   f"{len(rg_resources)} resources",
                   ha='right', va='bottom', fontsize=9, fontweight='bold',
                   color=self.color_scheme['compute'])
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ax.text(0.98, 0.02, f"Generated: {timestamp}", 
               ha='right', va='bottom', fontsize=8, 
               color=self.color_scheme['text'], alpha=0.7)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight',
                   facecolor=self.color_scheme['background'])
        plt.close()
        
        print(f"✅ Created resource groups diagram: {output_file}")
        return output_file
    
    def create_network_topology_diagram(self, output_file: str = "azure_network_topology.png"):
        """Create a network topology diagram"""
        
        fig, ax = plt.subplots(figsize=(18, 12))
        fig.patch.set_facecolor(self.color_scheme['background'])
        ax.set_facecolor(self.color_scheme['background'])
        
        # Title
        title = "Azure Network Topology"
        ax.text(0.5, 0.95, title, ha='center', va='top', transform=ax.transAxes,
                fontsize=18, fontweight='bold', color=self.color_scheme['text'])
        
        # Get network resources
        network_resources = []
        if 'resources' in self.architecture_data and 'by_type' in self.architecture_data['resources']:
            for resource_type, resources in self.architecture_data['resources']['by_type'].items():
                if 'microsoft.network' in resource_type.lower():
                    network_resources.extend(resources)
        
        if not network_resources:
            ax.text(0.5, 0.5, "No network resources found", ha='center', va='center',
                   fontsize=16, color=self.color_scheme['text'])
            ax.axis('off')
            plt.savefig(output_file, dpi=300, bbox_inches='tight')
            plt.close()
            return output_file
        
        # Group network resources by type
        network_by_type = defaultdict(list)
        for resource in network_resources:
            service_type = resource.get('type', '').split('/')[-1]
            network_by_type[service_type].append(resource)
        
        # Create network diagram layout
        y_positions = {
            'virtualNetworks': 0.8,
            'networkSecurityGroups': 0.7,
            'loadBalancers': 0.6,
            'applicationGateways': 0.5,
            'publicIPAddresses': 0.4,
            'vpnGateways': 0.3,
            'networkInterfaces': 0.2
        }
        
        for service_type, resources in network_by_type.items():
            y = y_positions.get(service_type, 0.1)
            
            # Service type header
            ax.text(0.05, y + 0.05, f"🌐 {service_type} ({len(resources)})",
                   fontsize=12, fontweight='bold', color=self.color_scheme['network'])
            
            # Draw resource boxes
            for i, resource in enumerate(resources[:5]):  # Show max 5 per type
                x = 0.1 + i * 0.15
                
                # Resource box
                box = FancyBboxPatch(
                    (x, y), 0.12, 0.04,
                    boxstyle="round,pad=0.005",
                    facecolor=self.color_scheme['network'],
                    edgecolor=self.color_scheme['border'],
                    alpha=0.7
                )
                ax.add_patch(box)
                
                # Resource name
                name = resource.get('name', 'Unknown')[:12]
                ax.text(x + 0.06, y + 0.02, name,
                       ha='center', va='center', fontsize=8,
                       color='white', fontweight='bold')
            
            if len(resources) > 5:
                ax.text(0.85, y + 0.02, f"... +{len(resources) - 5} more",
                       fontsize=8, color=self.color_scheme['text'], style='italic')
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ax.text(0.98, 0.02, f"Generated: {timestamp}", 
               ha='right', va='bottom', fontsize=8, 
               color=self.color_scheme['text'], alpha=0.7)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.axis('off')
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight',
                   facecolor=self.color_scheme['background'])
        plt.close()
        
        print(f"✅ Created network topology diagram: {output_file}")
        return output_file
    
    def create_cost_analysis_chart(self, output_file: str = "azure_cost_analysis.png"):
        """Create a cost analysis visualization"""
        
        categories = self.categorize_resources()
        
        # Filter out empty categories
        non_empty_categories = {k: v for k, v in categories.items() if v}
        
        if not non_empty_categories:
            print("❌ No resources found for cost analysis")
            return None
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
        fig.patch.set_facecolor(self.color_scheme['background'])
        
        # Pie chart of resource distribution
        labels = [k.replace('_', ' ').title() for k in non_empty_categories.keys()]
        sizes = [len(v) for v in non_empty_categories.values()]
        colors = [self.color_scheme.get(k, '#808080') for k in non_empty_categories.keys()]
        
        wedges, texts, autotexts = ax1.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%',
                                          startangle=90, textprops={'fontsize': 10})
        ax1.set_title('Resource Distribution by Category', fontsize=14, fontweight='bold',
                     color=self.color_scheme['text'], pad=20)
        
        # Bar chart of resource counts
        ax2.bar(range(len(labels)), sizes, color=colors, alpha=0.8)
        ax2.set_xlabel('Service Categories', fontsize=12, color=self.color_scheme['text'])
        ax2.set_ylabel('Number of Resources', fontsize=12, color=self.color_scheme['text'])
        ax2.set_title('Resource Counts by Category', fontsize=14, fontweight='bold',
                     color=self.color_scheme['text'], pad=20)
        ax2.set_xticks(range(len(labels)))
        ax2.set_xticklabels(labels, rotation=45, ha='right')
        
        # Style the charts
        for ax in [ax1, ax2]:
            ax.set_facecolor(self.color_scheme['background'])
            for spine in ax.spines.values():
                spine.set_color(self.color_scheme['border'])
        
        # Add timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        fig.text(0.98, 0.02, f"Generated: {timestamp}", 
                ha='right', va='bottom', fontsize=8, 
                color=self.color_scheme['text'], alpha=0.7)
        
        plt.tight_layout()
        plt.savefig(output_file, dpi=300, bbox_inches='tight',
                   facecolor=self.color_scheme['background'])
        plt.close()
        
        print(f"✅ Created cost analysis chart: {output_file}")
        return output_file
    
    def generate_all_diagrams(self):
        """Generate all available diagrams"""
        
        output_dir = "azure_diagrams_png"
        os.makedirs(output_dir, exist_ok=True)
        
        print("🎨 Generating modern PNG diagrams...")
        print("="*50)
        
        generated_files = []
        
        # Overview diagram
        overview_file = os.path.join(output_dir, "azure_architecture_overview.png")
        self.create_overview_diagram(overview_file)
        generated_files.append(overview_file)
        
        # Resource groups diagram
        rg_file = os.path.join(output_dir, "azure_resource_groups.png")
        self.create_resource_groups_diagram(rg_file)
        generated_files.append(rg_file)
        
        # Network topology diagram
        network_file = os.path.join(output_dir, "azure_network_topology.png")
        self.create_network_topology_diagram(network_file)
        generated_files.append(network_file)
        
        # Cost analysis chart
        cost_file = os.path.join(output_dir, "azure_cost_analysis.png")
        cost_result = self.create_cost_analysis_chart(cost_file)
        if cost_result:
            generated_files.append(cost_file)
        
        return generated_files

def main():
    """Main diagram generation process"""
    
    print("🌟" + "="*70 + "🌟")
    print("        MODERN AZURE ARCHITECTURE PNG DIAGRAMS")
    print("🌟" + "="*70 + "🌟")
    print()
    
    # Find the most recent architecture export file
    architecture_files = [f for f in os.listdir('.') if f.startswith('azure_architecture_export_') and f.endswith('.json')]
    
    if not architecture_files:
        print("❌ No architecture export file found!")
        print("💡 Please run 'python3 azure_architecture_extractor.py' first")
        return
    
    # Use the most recent file
    latest_file = sorted(architecture_files)[-1]
    print(f"📁 Using architecture data: {latest_file}")
    
    # Create diagram generator
    generator = ModernAzureDiagramGenerator(latest_file)
    
    # Generate all diagrams
    generated_files = generator.generate_all_diagrams()
    
    print(f"\n🎉 Generated {len(generated_files)} modern PNG diagrams!")
    print(f"📁 Files saved in: azure_diagrams_png/")
    print()
    for file in generated_files:
        print(f"   • {os.path.basename(file)}")
    
    print(f"\n💡 Open the PNG files to view your modern Azure architecture diagrams!")

if __name__ == "__main__":
    main()
