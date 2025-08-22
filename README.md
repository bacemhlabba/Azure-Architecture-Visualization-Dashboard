# Azure Architecture Visualization & Dashboard

This project provides a suite of tools to extract, analyze, and visualize your Azure cloud architecture. It generates a modern, interactive HTML dashboard that includes a resource explorer, a network topology graph, and security rule summaries.

## Features

- **Automated Extraction**: Scripts to pull Azure resource information using the Azure CLI.
- **Interactive Dashboard**: A dynamic HTML dashboard with filtering capabilities.
- **Network Topology**: A visual graph of how resources are interconnected.
- **Resource Explorer**: A filterable table of all your Azure resources.
- **Security Overview**: A clear view of Network Security Group (NSG) rules.
- **Modern UI**: A clean, professional, and responsive light-mode interface.

## Project Structure

```
/
├── azure_architecture_extractor.py   # Extracts resource data from Azure
├── azure_dashboard_generator.py      # Generates the interactive HTML dashboard
├── azure_dependency_analyzer.py      # Analyzes relationships between resources
├── azure_diagram_simplified.py       # Generates a basic PNG diagram
├── azure_enhanced_diagram_generator.py # Generates an interactive HTML diagram
├── azure_modern_png_generator.py     # Generates a styled PNG diagram
├── azure_main_menu.py                # An interactive menu to run scripts
├── setup_azure_extraction.sh         # Sets up Azure CLI and permissions
├── azure_dashboard/                  # Output directory for the HTML dashboard
│   ├── index.html
│   └── assets/
│       └── *.svg
├── azure_diagrams_png/               # Output for PNG diagrams
├── azure_diagrams_enhanced/          # Output for enhanced HTML diagrams
└── azure_architecture_export_*.json  # Raw extracted data
```

## How to Use

### 1. Prerequisites

- **Azure CLI**: You must have the Azure CLI installed and configured.
- **Python 3**: The scripts are written in Python 3.
- **Dependencies**: Install the required Python libraries:
  ```bash
  pip install azure-cli diagrams diagrams-ext
  ```

### 2. Setup & Extraction

First, run the setup script to ensure you are logged into Azure and have the necessary permissions.

```bash
bash setup_azure_extraction.sh
```

Next, run the main menu to extract your Azure architecture data. This will create a JSON file (`azure_architecture_export_*.json`).

```bash
python3 azure_main_menu.py
```
Select the option to **"Extract Azure Architecture"**.

### 3. Generate the Dashboard

Once the data is extracted, run the dashboard generator:

```bash
python3 azure_dashboard_generator.py
```

This will create the `azure_dashboard/index.html` file.

### 4. View the Dashboard

Open `azure_dashboard/index.html` in your web browser to explore your Azure architecture.

## Dashboard Features

- **Global Filters**: Filter all views by Resource Group, Resource Type, Location, or Name.
- **Dashboard View**: See charts summarizing your resources by type and location.
- **Resource Explorer**: Browse a detailed table of your resources. Click on any row to see the full JSON details.
- **Network Topology**: An interactive graph showing resources and their connections. Click on a node to see its details.
- **Security View**: Review all Network Security Group rules, sorted by NSG.

## Script Descriptions

- `azure_architecture_extractor.py`: Connects to Azure, fetches all resources, and saves them to a timestamped JSON file.
- `azure_dashboard_generator.py`: Takes the JSON data and builds the `index.html` dashboard. It includes all the CSS and JavaScript needed for the interactive experience.
- `azure_dependency_analyzer.py`: Scans the resource data to find connections (e.g., a VM's NIC, a subnet's NSG) and enriches the data with this information.
- `azure_main_menu.py`: Provides a simple command-line interface to run the different parts of the project.
- `setup_azure_extraction.sh`: A helper script to guide you through logging into Azure.
- Diagram Generators: Various scripts to create static and interactive diagrams as alternative visualizations.

This project is designed to be easily extensible. You can modify the `azure_dashboard_generator.py` script to add new views, charts, or data visualizations.
