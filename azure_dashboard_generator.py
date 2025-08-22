#!/usr/bin/env python3
"""
Azure Interactive Dashboard Generator
Creates a comprehensive, filterable, and dynamic HTML dashboard for Azure architecture.
"""

import json
import os
from datetime import datetime
import html
from weasyprint import HTML, CSS

class AzureDashboardGenerator:
    """Generates an interactive HTML dashboard from Azure architecture data."""

    def __init__(self, architecture_file: str):
        self.architecture_file = architecture_file
        self.architecture_data = {}
        self.load_architecture_data()

    def load_architecture_data(self):
        """Load architecture data from the JSON file."""
        try:
            with open(self.architecture_file, 'r', encoding='utf-8') as f:
                self.architecture_data = json.load(f)
            print(f"✅ Loaded architecture data: {self.architecture_data.get('metadata', {}).get('total_resources', 0)} resources")
        except Exception as e:
            print(f"❌ Error loading architecture data: {e}")
            self.architecture_data = {}

    def generate_dashboard(self, output_file: str):
        """Generate the full HTML dashboard file."""
        if not self.architecture_data:
            print("❌ Cannot generate dashboard due to missing data.")
            return

        print("🚀 Generating interactive HTML dashboard...")
        
        # Prepare data for embedding into HTML
        # Using html.escape to prevent issues with quotes and special characters in the JSON
        escaped_json_data = html.escape(json.dumps(self.architecture_data), quote=True)

        # Get the HTML template
        html_template = self._get_html_template()

        # Inject data and metadata into the template using replace to avoid format string errors
        metadata = self.architecture_data.get('metadata', {})
        final_html = html_template.replace(
            '{json_data}', escaped_json_data
        ).replace(
            '{subscription_id}', metadata.get('subscription_id', 'N/A')
        ).replace(
            '{generation_timestamp}', datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        # Write to output file
        try:
            output_dir = os.path.dirname(output_file)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            
            # Create assets directory for icons
            assets_dir = os.path.join(output_dir, "assets")
            os.makedirs(assets_dir, exist_ok=True)
            self._create_svg_icons(assets_dir)

            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(final_html)
            print(f"✅ Successfully created dashboard: {output_file}")
        except Exception as e:
            print(f"❌ Error writing dashboard file: {e}")

    def _create_svg_icons(self, assets_dir: str):
        """Creates SVG icon files in the assets directory."""
        icons = {
            "virtualMachine": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 16h-4v-4h4m0-2H4v10h16v-2h-4v-2h4v-2h-4v-2h4V8m-6 6h-4v-4h4m-2-2H8v4h4V8M6 6H4v4h2V6m14-4v2H2V2h18z"/></svg>""",
            "virtualNetwork": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10 10-4.5 10-10S17.5 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8zm-1-13h2v2h-2v-2zm-2 4h6v2H9v-2zm-2 4h10v2H7v-2z"/></svg>""",
            "networkInterface": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M20 6h-4V4c0-1.1-.9-2-2-2h-4c-1.1 0-2 .9-2 2v2H4c-1.1 0-2 .9-2 2v10c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V8c0-1.1-.9-2-2-2zM10 4h4v2h-4V4zm10 16H4V8h16v12z"/></svg>""",
            "networkSecurityGroup": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>""",
            "publicIpAddress": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5c-1.38 0-2.5-1.12-2.5-2.5s1.12-2.5 2.5-2.5 2.5 1.12 2.5 2.5-1.12 2.5-2.5 2.5z"/></svg>""",
            "storageAccount": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M6 2h12v5H6zM5 8h14v14H5zm2 2v2h10v-2H7zm0 4v2h10v-2H7zm0 4v2h10v-2H7z"/></svg>""",
            "default": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 18c-4.41 0-8-3.59-8-8s3.59-8 8-8 8 3.59 8 8-3.59 8-8 8z"/></svg>"""
        }
        for name, content in icons.items():
            with open(os.path.join(assets_dir, f"{name}.svg"), 'w') as f:
                f.write(content)

    def generate_pdf(self, html_file: str, pdf_file: str):
        """
        Generates a static PDF snapshot from the HTML dashboard.
        NOTE: The PDF is a static report. Interactive elements like the filterable
        cards and the dynamic network graph will not be interactive in the PDF.
        The network topology view will be empty as it is rendered by JavaScript.
        """
        print("📄 Generating static PDF of the dashboard...")
        print("⚠️ Note: The PDF is a static snapshot. Interactive features will not be available.")
        try:
            # We need to provide a base_url for WeasyPrint to find local assets like icons
            base_url = os.path.dirname(html_file)
            
            # Custom CSS to make all sections visible for printing
            pdf_css = CSS(string='''
                @page { size: A2; margin: 1cm; }
                body { background: #fff; }
                .tab-content { display: block !important; } /* Show all tabs */
                #network-view::before { 
                    content: "Note: The interactive network topology graph is not available in this static PDF export.";
                    display: block;
                    padding: 50px;
                    text-align: center;
                    font-size: 1.2em;
                    color: #888;
                    border: 2px dashed #ccc;
                    border-radius: 10px;
                    background-color: #f9f9f9;
                }
                #network-topology { display: none; } /* Hide the empty div */
            ''')
            
            HTML(html_file, base_url=base_url).write_pdf(pdf_file, stylesheets=[pdf_css])
            print(f"✅ Successfully created PDF: {pdf_file}")
        except Exception as e:
            print(f"❌ Error generating PDF: {e}")

    def _get_html_template(self) -> str:
        """Returns the HTML, CSS, and JavaScript for the dashboard as a string template."""
        
        # This is a large multi-line string containing the full frontend code.
        return """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Azure Modern Dashboard</title>
    <!-- External Libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" rel="stylesheet" type="text/css" />
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* New design inspired by azure_interactive_diagram.html */
        :root {
            --primary-color: #0078d4;
            --card-bg: #ffffff;
            --text-color: #333333;
            --shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            --border-color: #e9ecef;
        }
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
            padding: 20px;
            display: block; /* Override flex */
            overflow-y: auto; /* Allow body to scroll */
        }
        .container {
            max-width: 1600px;
            margin: 0 auto;
            background: rgba(255, 255, 255, 0.98);
            border-radius: 20px;
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
            overflow: hidden;
        }
        .header {
            background: linear-gradient(135deg, #0078d4 0%, #106ebe 100%);
            color: white;
            padding: 30px;
            text-align: center;
            border-bottom: none;
        }
        .header h1 {
            font-size: 2.2em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
        }
        .header .subtitle {
            font-size: 1.1em;
            opacity: 0.9;
            margin-bottom: 20px;
        }
        .stats-grid {
            display: flex;
            justify-content: center;
            gap: 30px;
            flex-wrap: wrap;
        }
        .stat-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 15px 25px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
            text-align: center;
        }
        .stat-card .value {
            font-size: 2em;
            font-weight: 700;
        }
        .stat-card h3 {
            font-size: 0.9em;
            opacity: 0.9;
            font-weight: 400;
            margin: 0;
        }
        #reset-filters {
            background-color: rgba(255, 255, 255, 0.2);
            color: white;
            border: 1px solid white;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            transition: background-color 0.2s;
            margin-top: 20px;
        }
        #reset-filters:hover {
            background-color: rgba(255, 255, 255, 0.3);
        }
        .main-content {
            padding: 25px;
        }
        .tabs {
            display: flex;
            justify-content: center;
            border-bottom: 1px solid var(--border-color);
            background: none;
            padding: 0;
            margin-bottom: 25px;
        }
        .tab-button {
            padding: 15px 25px;
            cursor: pointer;
            border: none;
            background: none;
            font-size: 1.1em;
            font-weight: 600;
            color: #555;
            border-bottom: 3px solid transparent;
            transition: color 0.2s, border-color 0.2s;
        }
        .tab-button:hover {
            color: var(--primary-color);
        }
        .tab-button.active {
            color: var(--primary-color);
            border-bottom-color: var(--primary-color);
        }
        .tab-content {
            padding: 0;
        }
        .service-cards-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 25px;
        }
        .service-card {
            background: var(--card-bg);
            border-radius: 15px;
            padding: 25px;
            box-shadow: var(--shadow);
            transition: all 0.3s ease;
            border-left: 5px solid;
            cursor: pointer;
        }
        .service-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 35px rgba(0,0,0,0.15);
        }
        .service-card.selected {
            box-shadow: 0 0 0 3px var(--primary-color);
            transform: translateY(-2px);
        }
        .service-card-title {
            font-size: 1.4em;
            font-weight: bold;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .service-card-icon {
            width: 40px;
            height: 40px;
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2em;
        }
        .service-card-count {
            font-size: 2em;
            font-weight: bold;
            color: #333;
            text-align: center;
            margin: 15px 0;
        }
        /* Category Colors */
        .service-card.Compute { border-left-color: #0078D4; }
        .service-card-icon.Compute { background: #0078D4; }
        .service-card.Storage { border-left-color: #00BCF2; }
        .service-card-icon.Storage { background: #00BCF2; }
        .service-card.Database { border-left-color: #40E0D0; }
        .service-card-icon.Database { background: #40E0D0; }
        .service-card.Network { border-left-color: #107C10; }
        .service-card-icon.Network { background: #107C10; }
        .service-card.Security { border-left-color: #D83B01; }
        .service-card-icon.Security { background: #D83B01; }
        .service-card.Monitoring { border-left-color: #00188F; }
        .service-card-icon.Monitoring { background: #00188F; }
        .service-card.Integration { border-left-color: #5C2D91; }
        .service-card-icon.Integration { background: #5C2D91; }
        .service-card.Other { border-left-color: #808080; }
        .service-card-icon.Other { background: #808080; }

        #network-topology {
            height: calc(100vh - 100px); /* Adjust height */
        }
        .resource-table th {
            background-color: #f1f5f9;
        }
        pre {
            background-color: #f1f5f9;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🏗️ Azure Architecture Dashboard</h1>
            <div class="subtitle">Interactive Overview of Subscription: <span id="subscription-id">{subscription_id}</span></div>
            <div class="stats-grid" id="stats-container">
                <!-- Stats will be injected here -->
            </div>
            <button id="reset-filters">Reset Selections</button>
        </div>

        <div class="main-content">
            <div class="tabs">
                <button class="tab-button active" onclick="openTab(event, 'dashboard-view')">Dashboard</button>
                <button class="tab-button" onclick="openTab(event, 'resources-view')">Resource Explorer</button>
                <button class="tab-button" onclick="openTab(event, 'network-view')">Network Topology</button>
                <button class="tab-button" onclick="openTab(event, 'security-view')">Security Rules</button>
            </div>

            <div id="dashboard-view" class="tab-content active">
                <div class="service-cards-grid" id="service-cards-container">
                    <!-- Service category cards will be injected here -->
                </div>
            </div>

            <div id="resources-view" class="tab-content">
                <table class="resource-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Type</th>
                        <th>Resource Group</th>
                        <th>Location</th>
                    </tr>
                </thead>
                <tbody id="resource-table-body"></tbody>
            </table>
            </div>

            <div id="network-view" class="tab-content">
                <div id="network-topology"></div>
            </div>
            
            <div id="security-view" class="tab-content">
                <h3>Network Security Groups & Rules</h3>
                <div id="nsg-rules-container"></div>
            </div>
        </div>

        <div id="details-modal" class="modal">
            <div class="modal-content">
                <span class="modal-close" onclick="closeModal()">&times;</span>
                <h3>Resource Details</h3>
                <pre id="modal-details-content"></pre>
            </div>
        </div>

        <script>
            // Embedded JavaScript for interactivity
            const rawJsonData = '{json_data}';
            const architectureData = JSON.parse(rawJsonData.replace(/&quot;/g, '"'));
            let allResources = [];
            let resourceMap = new Map();
            let network = null;
            let activeFilters = {
                category: null
            };

            const serviceCategories = {
                "Microsoft.Compute": "Compute",
                "Microsoft.Storage": "Storage",
                "Microsoft.DBforMySQL": "Database",
                "Microsoft.DBforPostgreSQL": "Database",
                "Microsoft.Sql": "Database",
                "Microsoft.Network": "Network",
                "Microsoft.Security": "Security",
                "Microsoft.Insights": "Monitoring",
                "Microsoft.OperationalInsights": "Monitoring",
                "Microsoft.Logic": "Integration",
                "Microsoft.ApiManagement": "Integration",
                "Microsoft.EventGrid": "Integration"
            };

            function getCategory(type) {
                for (const prefix in serviceCategories) {
                    if (type.startsWith(prefix)) {
                        return serviceCategories[prefix];
                    }
                }
                return "Other";
            }

            const iconMap = {
                "Compute": "💻",
                "Storage": "💾",
                "Database": "🗄️",
                "Network": "🌐",
                "Security": "🛡️",
                "Monitoring": "📈",
                "Integration": "🔗",
                "Other": "⚙️"
            };

            function getCategoryIcon(category) {
                return iconMap[category] || "⚙️";
            }

            function initializeDashboard() {
                if (architectureData.resources && architectureData.resources.by_type) {
                    for (const type in architectureData.resources.by_type) {
                        allResources.push(...architectureData.resources.by_type[type]);
                    }
                }
                allResources.forEach(r => {
                    r.category = getCategory(r.type);
                    resourceMap.set(r.id.toLowerCase(), r);
                });

                document.getElementById('reset-filters').addEventListener('click', () => {
                    activeFilters = { category: null };
                    applyFilters();
                });

                applyFilters();
            }

            function applyFilters() {
                const filteredResources = allResources.filter(r => 
                    (!activeFilters.category || r.category === activeFilters.category)
                );

                renderStats(filteredResources);
                renderDashboardView(allResources); // Pass all resources to render all cards
                highlightSelectedCard();
                renderResourceExplorer(filteredResources);
                renderNetworkTopology(filteredResources);
                renderSecurityView(filteredResources);
            }

            function renderStats(resources) {
                const container = document.getElementById('stats-container');
                const rgSet = new Set(resources.map(r => r.resourceGroup));
                const locSet = new Set(resources.map(r => r.location));

                container.innerHTML = `
                    <div class="stat-card">
                        <div class="value">${resources.length}</div>
                        <h3>Total Resources</h3>
                    </div>
                    <div class="stat-card">
                        <div class="value">${rgSet.size}</div>
                        <h3>Resource Groups</h3>
                    </div>
                    <div class="stat-card">
                        <div class="value">${locSet.size}</div>
                        <h3>Locations</h3>
                    </div>
                `;
            }

            function renderDashboardView(resources) {
                const container = document.getElementById('service-cards-container');
                if (container.children.length > 0) return; // Only render cards once

                const categoryCounts = {};
                resources.forEach(r => {
                    const category = r.category;
                    categoryCounts[category] = (categoryCounts[category] || 0) + 1;
                });

                container.innerHTML = '';
                Object.keys(categoryCounts).sort().forEach(category => {
                    const count = categoryCounts[category];
                    const card = document.createElement('div');
                    card.className = `service-card ${category}`;
                    card.onclick = () => {
                        activeFilters.category = (activeFilters.category === category) ? null : category;
                        applyFilters();
                    };
                    card.innerHTML = `
                        <div class="service-card-title">
                            <div class="service-card-icon ${category}">${getCategoryIcon(category)}</div>
                            ${category}
                        </div>
                        <div class="service-card-count">${count}</div>
                    `;
                    container.appendChild(card);
                });
            }

            function highlightSelectedCard() {
                const cards = document.querySelectorAll('.service-card');
                cards.forEach(card => {
                    card.classList.remove('selected');
                    if (activeFilters.category && card.classList.contains(activeFilters.category)) {
                        card.classList.add('selected');
                    }
                });
            }
            
            function renderResourceExplorer(resources) {
                const tableBody = document.getElementById('resource-table-body');
                tableBody.innerHTML = '';
                resources.forEach(r => {
                    const row = document.createElement('tr');
                    row.style.cursor = 'pointer';
                    row.innerHTML = `
                        <td>${r.name}</td>
                        <td>${r.type}</td>
                        <td>${r.resourceGroup}</td>
                        <td>${r.location}</td>
                    `;
                    row.onclick = () => showDetails(r);
                    tableBody.appendChild(row);
                });
            }

            function renderNetworkTopology(resources) {
                const nodes = [];
                const edges = [];
                const addedNodes = new Set();
                const filteredResourceIds = new Set(resources.map(r => r.id.toLowerCase()));

                resources.forEach(r => {
                    if (!addedNodes.has(r.id)) {
                        nodes.push({ 
                            id: r.id, 
                            label: r.name, 
                            title: r.type, 
                            shape: 'image',
                            image: getIcon(r.type),
                            group: r.resourceGroup
                        });
                        addedNodes.add(r.id);
                    }

                    // Enhanced connection logic: scan properties for any resource ID
                    const scanProperties = (obj) => {
                        for (const key in obj) {
                            if (typeof obj[key] === 'string') {
                                const val = obj[key].toLowerCase();
                                if (val.startsWith('/subscriptions/') && resourceMap.has(val) && filteredResourceIds.has(val)) {
                                    if (r.id.toLowerCase() !== val) { // Avoid self-loops
                                        edges.push({ from: r.id, to: resourceMap.get(val).id, arrows: 'to' });
                                    }
                                }
                            } else if (typeof obj[key] === 'object' && obj[key] !== null) {
                                scanProperties(obj[key]);
                            }
                        }
                    };
                    scanProperties(r.properties);
                });

                const container = document.getElementById('network-topology');
                const data = { nodes: new vis.DataSet(nodes), edges: new vis.DataSet(edges) };
                const options = {
                    nodes: {
                        borderWidth: 2,
                        size: 30,
                        color: {
                            border: '#e0e0e0',
                            background: '#ffffff'
                        },
                        font: { color: '#333' }
                    },
                    edges: {
                        color: '#0078d4',
                        smooth: {
                            type: 'continuous'
                        },
                        arrows: {
                            to: { enabled: true, scaleFactor: 0.8 }
                        },
                        width: 2
                    },
                    physics: {
                        barnesHut: {
                            gravitationalConstant: -40000,
                            springConstant: 0.05,
                            springLength: 170
                        },
                        stabilization: { iterations: 250 }
                    },
                    interaction: { 
                        hover: true,
                        tooltipDelay: 200
                    },
                    layout: {
                        improvedLayout: true
                    }
                };
                
                if (network) {
                    network.destroy();
                }
                network = new vis.Network(container, data, options);

                network.on("click", function (params) {
                    if (params.nodes.length > 0) {
                        const nodeId = params.nodes[0];
                        const resource = resourceMap.get(nodeId.toLowerCase());
                        if (resource) {
                            showDetails(resource);
                        }
                    }
                });
            }
            
            function renderSecurityView(resources) {
                const container = document.getElementById('nsg-rules-container');
                container.innerHTML = '';
                const nsgs = resources.filter(r => r.type === 'Microsoft.Network/networkSecurityGroups');
                
                nsgs.forEach(nsg => {
                    const nsgDiv = document.createElement('div');
                    nsgDiv.className = 'nsg-card';
                    nsgDiv.innerHTML = `<h4>${nsg.name} (${nsg.resourceGroup})</h4>`;
                    
                    const rules = (nsg.properties.securityRules || []).concat(nsg.properties.defaultSecurityRules || []);
                    rules.sort((a, b) => a.properties.priority - b.properties.priority);

                    const table = document.createElement('table');
                    table.className = 'resource-table';
                    table.innerHTML = `<thead><tr><th>Priority</th><th>Name</th><th>Direction</th><th>Access</th><th>Protocol</th><th>Source</th><th>Destination</th></tr></thead>`;
                    const tbody = document.createElement('tbody');
                    rules.forEach(rule => {
                        const r = rule.properties;
                        const sourcePort = r.sourcePortRange || (r.sourcePortRanges && r.sourcePortRanges.join(',')) || '*';
                        const destPort = r.destinationPortRange || (r.destinationPortRanges && r.destinationPortRanges.join(',')) || '*';
                        const sourceAddr = r.sourceAddressPrefix || (r.sourceAddressPrefixes || []).join(',') || '*';
                        const destAddr = r.destinationAddressPrefix || (r.destinationAddressPrefixes || []).join(',') || '*';

                        tbody.innerHTML += `
                            <tr style="color:${r.access === 'Deny' ? '#d9534f' : '#5cb85c'}">
                                <td>${r.priority}</td>
                                <td>${rule.name}</td>
                                <td>${r.direction}</td>
                                <td>${r.access}</td>
                                <td>${r.protocol}</td>
                                <td>${sourceAddr}:${sourcePort}</td>
                                <td>${destAddr}:${destPort}</td>
                            </tr>
                        `;
                    });
                    table.appendChild(tbody);
                    nsgDiv.appendChild(table);
                    container.appendChild(nsgDiv);
                });
            }

            function showDetails(resource) {
                document.getElementById('modal-details-content').textContent = JSON.stringify(resource, null, 2);
                document.getElementById('details-modal').style.display = 'flex';
            }

            function closeModal() {
                document.getElementById('details-modal').style.display = 'none';
            }

            function openTab(evt, tabName) {
                let i, tabcontent, tablinks;
                tabcontent = document.getElementsByClassName("tab-content");
                for (i = 0; i < tabcontent.length; i++) {
                    tabcontent[i].style.display = "none";
                }
                tablinks = document.getElementsByClassName("tab-button");
                for (i = 0; i < tablinks.length; i++) {
                    tablinks[i].className = tablinks[i].className.replace(" active", "");
                }
                document.getElementById(tabName).style.display = "block";
                evt.currentTarget.className += " active";
                
                if (tabName === 'network-view' && network) {
                    network.fit(); // Recenter the network graph when tab is viewed
                }
            }

            window.onload = initializeDashboard;
        </script>
    </div>
</body>
</html>
        """;

def main():
    """Main function to generate the dashboard."""
    # Define paths
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(script_dir, 'azure_architecture_export_20250820_112805.json')
    output_html_path = os.path.join(script_dir, 'azure_dashboard', 'index.html')
    output_pdf_path = os.path.join(script_dir, 'azure_dashboard', 'azure_dashboard.pdf')

    # Create and run the generator
    generator = AzureDashboardGenerator(json_file_path)
    generator.generate_dashboard(output_html_path)
    generator.generate_pdf(output_html_path, output_pdf_path)

if __name__ == "__main__":
    main()
