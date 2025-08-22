#!/usr/bin/env python3
"""
Enhanced Azure Architecture Diagram Generator
Creates modern HTML interactive diagrams and improved PNG diagrams
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Any
import base64
from io import BytesIO

def create_html_interactive_diagram(architecture_file: str, output_file: str = "azure_interactive_diagram.html"):
    """Create an interactive HTML diagram using HTML5 Canvas and CSS"""
    
    # Load architecture data
    try:
        with open(architecture_file, 'r', encoding='utf-8') as f:
            architecture_data = json.load(f)
    except Exception as e:
        print(f"❌ Error loading architecture data: {e}")
        return None
    
    # Categorize resources
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
    
    if 'resources' in architecture_data and 'by_type' in architecture_data['resources']:
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
        
        for resource_type, resources in architecture_data['resources']['by_type'].items():
            resource_type_lower = resource_type.lower()
            categorized = False
            
            for category, keywords in type_mapping.items():
                if any(keyword in resource_type_lower for keyword in keywords):
                    categories[category].extend(resources)
                    categorized = True
                    break
            
            if not categorized:
                categories['other'].extend(resources)
    
    # Get metadata
    metadata = architecture_data.get('metadata', {})
    subscription_id = metadata.get('subscription_id', 'Unknown')
    total_resources = metadata.get('total_resources', 0)
    total_resource_groups = metadata.get('total_resource_groups', 0)
    
    # Create HTML content
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure Architecture Interactive Diagram</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}
        
        .container {{
            max-width: 1400px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }}
        
        .header {{
            background: linear-gradient(135deg, #0078d4 0%, #106ebe 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
        }}
        
        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.9;
        }}
        
        .stats {{
            display: flex;
            justify-content: center;
            gap: 40px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}
        
        .stat {{
            text-align: center;
            background: rgba(255, 255, 255, 0.1);
            padding: 15px 25px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }}
        
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            display: block;
        }}
        
        .stat-label {{
            font-size: 0.9em;
            opacity: 0.8;
        }}
        
        .content {{
            padding: 40px;
        }}
        
        .services-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }}
        
        .service-card {{
            background: white;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
            border-left: 5px solid;
            cursor: pointer;
        }}
        
        .service-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0, 0, 0, 0.15);
        }}
        
        .service-card.compute {{ border-left-color: #0078D4; }}
        .service-card.storage {{ border-left-color: #00BCF2; }}
        .service-card.database {{ border-left-color: #40E0D0; }}
        .service-card.network {{ border-left-color: #107C10; }}
        .service-card.security {{ border-left-color: #D83B01; }}
        .service-card.analytics {{ border-left-color: #5C2D91; }}
        .service-card.ai_ml {{ border-left-color: #E81123; }}
        .service-card.integration {{ border-left-color: #0078D4; }}
        .service-card.monitoring {{ border-left-color: #00188F; }}
        .service-card.other {{ border-left-color: #808080; }}
        
        .service-title {{
            font-size: 1.4em;
            font-weight: bold;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        
        .service-icon {{
            width: 40px;
            height: 40px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2em;
        }}
        
        .service-icon.compute {{ background: #0078D4; }}
        .service-icon.storage {{ background: #00BCF2; }}
        .service-icon.database {{ background: #40E0D0; }}
        .service-icon.network {{ background: #107C10; }}
        .service-icon.security {{ background: #D83B01; }}
        .service-icon.analytics {{ background: #5C2D91; }}
        .service-icon.ai_ml {{ background: #E81123; }}
        .service-icon.integration {{ background: #0078D4; }}
        .service-icon.monitoring {{ background: #00188F; }}
        .service-icon.other {{ background: #808080; }}
        
        .resource-count {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin: 15px 0;
        }}
        
        .resource-types {{
            font-size: 0.9em;
            color: #666;
            line-height: 1.5;
        }}
        
        .resource-groups {{
            margin-top: 40px;
        }}
        
        .section-title {{
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 25px;
            color: #333;
            text-align: center;
        }}
        
        .rg-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 20px;
        }}
        
        .rg-card {{
            background: white;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
            border: 2px solid #e9ecef;
        }}
        
        .rg-header {{
            display: flex;
            align-items: center;
            margin-bottom: 15px;
            padding-bottom: 10px;
            border-bottom: 1px solid #e9ecef;
        }}
        
        .rg-name {{
            font-weight: bold;
            font-size: 1.1em;
            color: #333;
        }}
        
        .rg-location {{
            font-size: 0.9em;
            color: #666;
            margin-left: auto;
        }}
        
        .rg-resources {{
            font-size: 0.85em;
            color: #555;
            line-height: 1.4;
        }}
        
        .timestamp {{
            text-align: center;
            color: #666;
            margin-top: 30px;
            font-size: 0.9em;
        }}
        
        .modal {{
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
        }}
        
        .modal-content {{
            background-color: white;
            margin: 5% auto;
            padding: 30px;
            border-radius: 15px;
            width: 80%;
            max-width: 800px;
            max-height: 80vh;
            overflow-y: auto;
        }}
        
        .close {{
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
        }}
        
        .close:hover {{
            color: #333;
        }}
        
        .resource-detail {{
            margin: 10px 0;
            padding: 10px;
            background: #f8f9fa;
            border-radius: 5px;
            border-left: 3px solid #0078d4;
        }}
        
        @media (max-width: 768px) {{
            .container {{
                margin: 10px;
                border-radius: 10px;
            }}
            
            .header {{
                padding: 20px;
            }}
            
            .header h1 {{
                font-size: 2em;
            }}
            
            .stats {{
                gap: 20px;
            }}
            
            .content {{
                padding: 20px;
            }}
            
            .services-grid {{
                grid-template-columns: 1fr;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏗️ Azure Architecture Overview</h1>
            <div class="subtitle">Interactive Infrastructure Diagram</div>
            <div class="stats">
                <div class="stat">
                    <span class="stat-number">{total_resources}</span>
                    <span class="stat-label">Total Resources</span>
                </div>
                <div class="stat">
                    <span class="stat-number">{total_resource_groups}</span>
                    <span class="stat-label">Resource Groups</span>
                </div>
                <div class="stat">
                    <span class="stat-number">{subscription_id[:8]}...</span>
                    <span class="stat-label">Subscription</span>
                </div>
            </div>
        </div>
        
        <div class="content">
            <div class="services-grid">
"""
    
    # Add service cards
    service_icons = {
        'compute': '💻',
        'storage': '💾',
        'database': '🗄️',
        'network': '🌐',
        'security': '🔒',
        'analytics': '📊',
        'ai_ml': '🤖',
        'integration': '🔗',
        'monitoring': '📈',
        'other': '⚙️'
    }
    
    service_names = {
        'compute': 'Compute Services',
        'storage': 'Storage Services',
        'database': 'Database Services',
        'network': 'Network Services',
        'security': 'Security & Identity',
        'analytics': 'Analytics & Big Data',
        'ai_ml': 'AI & Machine Learning',
        'integration': 'Integration Services',
        'monitoring': 'Monitoring & Management',
        'other': 'Other Services'
    }
    
    for category, resources in categories.items():
        if not resources:  # Skip empty categories
            continue
            
        # Get unique resource types
        resource_types = set()
        for resource in resources:
            service_type = resource.get('type', '').split('/')[-1]
            if service_type:
                resource_types.add(service_type)
        
        resource_types_text = '<br>'.join(f"• {rt}" for rt in sorted(list(resource_types))[:5])
        if len(resource_types) > 5:
            resource_types_text += f"<br>... and {len(resource_types) - 5} more"
        
        html_content += f"""
                <div class="service-card {category}" onclick="showServiceDetails('{category}')">
                    <div class="service-title">
                        <div class="service-icon {category}">{service_icons[category]}</div>
                        {service_names[category]}
                    </div>
                    <div class="resource-count">{len(resources)}</div>
                    <div class="resource-types">{resource_types_text}</div>
                </div>
"""
    
    # Add resource groups section
    html_content += """
            </div>
            
            <div class="resource-groups">
                <h2 class="section-title">📁 Resource Groups</h2>
                <div class="rg-grid">
"""
    
    # Add resource group cards
    resource_groups = architecture_data.get('resource_groups', [])
    resources_by_rg = architecture_data.get('resources', {}).get('by_resource_group', {})
    
    for rg in resource_groups:
        rg_name = rg.get('name', 'Unknown')
        location = rg.get('location', 'Unknown')
        rg_resources = resources_by_rg.get(rg_name, [])
        
        # Get resource types in this RG
        rg_resource_types = {}
        for resource in rg_resources:
            service_type = resource.get('type', '').split('/')[-1]
            if service_type:
                rg_resource_types[service_type] = rg_resource_types.get(service_type, 0) + 1
        
        rg_types_text = '<br>'.join(f"• {rt}: {count}" for rt, count in sorted(list(rg_resource_types.items())[:4]))
        if len(rg_resource_types) > 4:
            rg_types_text += f"<br>... and {len(rg_resource_types) - 4} more types"
        
        html_content += f"""
                    <div class="rg-card" onclick="showRGDetails('{rg_name}')">
                        <div class="rg-header">
                            <div class="rg-name">📁 {rg_name}</div>
                            <div class="rg-location">📍 {location}</div>
                        </div>
                        <div class="rg-resources">
                            <strong>{len(rg_resources)} resources</strong><br><br>
                            {rg_types_text}
                        </div>
                    </div>
"""
    
    # Close HTML and add JavaScript
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_content += f"""
                </div>
            </div>
            
            <div class="timestamp">
                Generated on: {timestamp}
            </div>
        </div>
    </div>
    
    <!-- Modal for detailed views -->
    <div id="detailModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="closeModal()">&times;</span>
            <div id="modalContent"></div>
        </div>
    </div>
    
    <script>
        // Store architecture data for JavaScript access
        const architectureData = {json.dumps(architecture_data, indent=2)};
        
        function showServiceDetails(category) {{
            const resources = getResourcesByCategory(category);
            const categoryNames = {{
                'compute': 'Compute Services',
                'storage': 'Storage Services',
                'database': 'Database Services',
                'network': 'Network Services',
                'security': 'Security & Identity',
                'analytics': 'Analytics & Big Data',
                'ai_ml': 'AI & Machine Learning',
                'integration': 'Integration Services',
                'monitoring': 'Monitoring & Management',
                'other': 'Other Services'
            }};
            
            let content = `<h2>${{categoryNames[category]}}</h2>`;
            content += `<p><strong>Total Resources: ${{resources.length}}</strong></p>`;
            
            // Group by resource type
            const byType = {{}};
            resources.forEach(resource => {{
                const type = resource.type.split('/').pop();
                if (!byType[type]) byType[type] = [];
                byType[type].push(resource);
            }});
            
            Object.keys(byType).sort().forEach(type => {{
                content += `<div class="resource-detail">`;
                content += `<h3>${{type}} (${{byType[type].length}} instances)</h3>`;
                byType[type].slice(0, 5).forEach(resource => {{
                    content += `<div>• ${{resource.name}} (${{resource.location || 'N/A'}})</div>`;
                }});
                if (byType[type].length > 5) {{
                    content += `<div>... and ${{byType[type].length - 5}} more</div>`;
                }}
                content += `</div>`;
            }});
            
            document.getElementById('modalContent').innerHTML = content;
            document.getElementById('detailModal').style.display = 'block';
        }}
        
        function showRGDetails(rgName) {{
            const resources = architectureData.resources.by_resource_group[rgName] || [];
            
            let content = `<h2>📁 ${{rgName}}</h2>`;
            content += `<p><strong>Total Resources: ${{resources.length}}</strong></p>`;
            
            // Group by resource type
            const byType = {{}};
            resources.forEach(resource => {{
                const type = resource.type.split('/').pop();
                if (!byType[type]) byType[type] = [];
                byType[type].push(resource);
            }});
            
            Object.keys(byType).sort().forEach(type => {{
                content += `<div class="resource-detail">`;
                content += `<h3>${{type}} (${{byType[type].length}} instances)</h3>`;
                byType[type].forEach(resource => {{
                    content += `<div>• ${{resource.name}} (${{resource.location || 'N/A'}})</div>`;
                }});
                content += `</div>`;
            }});
            
            document.getElementById('modalContent').innerHTML = content;
            document.getElementById('detailModal').style.display = 'block';
        }}
        
        function closeModal() {{
            document.getElementById('detailModal').style.display = 'none';
        }}
        
        function getResourcesByCategory(category) {{
            const typeMapping = {{
                'compute': ['microsoft.compute', 'microsoft.containerservice', 'microsoft.containerinstance', 'microsoft.web'],
                'storage': ['microsoft.storage'],
                'database': ['microsoft.sql', 'microsoft.documentdb', 'microsoft.dbformysql', 'microsoft.dbforpostgresql', 'microsoft.cache'],
                'network': ['microsoft.network'],
                'security': ['microsoft.keyvault', 'microsoft.security'],
                'analytics': ['microsoft.synapse', 'microsoft.datafactory', 'microsoft.databricks', 'microsoft.streamanalytics'],
                'ai_ml': ['microsoft.cognitiveservices', 'microsoft.machinelearningservices'],
                'integration': ['microsoft.logic', 'microsoft.servicebus', 'microsoft.eventgrid', 'microsoft.eventhub'],
                'monitoring': ['microsoft.insights', 'microsoft.operationalinsights']
            }};
            
            const result = [];
            const keywords = typeMapping[category] || [];
            
            Object.values(architectureData.resources.by_type).forEach(resources => {{
                resources.forEach(resource => {{
                    const resourceType = resource.type.toLowerCase();
                    if (keywords.some(keyword => resourceType.includes(keyword))) {{
                        result.push(resource);
                    }} else if (category === 'other' && !Object.values(typeMapping).flat().some(keyword => resourceType.includes(keyword))) {{
                        result.push(resource);
                    }}
                }});
            }});
            
            return result;
        }}
        
        // Close modal when clicking outside
        window.onclick = function(event) {{
            const modal = document.getElementById('detailModal');
            if (event.target === modal) {{
                modal.style.display = 'none';
            }}
        }}
    </script>
</body>
</html>
"""
    
    # Save HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Created interactive HTML diagram: {output_file}")
    return output_file

def main():
    """Generate enhanced diagrams"""
    
    print("🌟" + "="*70 + "🌟")
    print("        ENHANCED AZURE ARCHITECTURE DIAGRAMS")
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
    
    # Create output directory
    output_dir = "azure_diagrams_enhanced"
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate interactive HTML diagram
    html_file = os.path.join(output_dir, "azure_interactive_diagram.html")
    create_html_interactive_diagram(latest_file, html_file)
    
    print(f"\n🎉 Enhanced diagrams generated!")
    print(f"📁 Files saved in: {output_dir}/")
    print(f"   • azure_interactive_diagram.html - Interactive web-based diagram")
    print(f"\n💡 Open the HTML file in your web browser for an interactive experience!")
    print(f"🌐 You can also share the HTML file with your team for collaborative reviews.")

if __name__ == "__main__":
    main()
