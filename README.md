# CIM CGMES Documentation Generator

This script converts a CIM (Common Information Model) schema in JSON format into a structured Markdown documentation site with Mermaid diagrams.

## Prerequisites

- **Python 3.x**: Ensure you have Python installed.
- **CIM Schema**: The script expects a file named `cim_schema_import_test.json` in the same directory.
- **Mermaid Support**: The generated diagrams require a Markdown viewer that supports [Mermaid](https://mermaid.js.org/) (e.g., GitHub, VS Code with extensions, or Docusaurus).

## Usage

1. Place your `cim_schema_import_test.json` file in the root directory.
2. Run the generation script:
   ```bash
   python3 cim_to_markdown.py
   ```

## Output Structure

The script generates a `docs/` folder with the following structure:

- `docs/Overview.md`: The main index page listing all profiles and classes.
- `docs/Profiles/`: Overview pages for each CIM profile, including a Mermaid diagram showing inheritance and associations within that profile.
- `docs/Classes/`: Individual pages for every class and enumeration, including detailed attribute tables and inheritance diagrams.

## Features

- **Profile Overviews**: Automatically groups classes by their `CIMCategories` and generates relationship diagrams.
- **Inheritance Diagrams**: Visualizes the class hierarchy using Mermaid `classDiagram` syntax.
- **Cross-Linking**: Attributes that reference other classes or enumerations are automatically turned into clickable links.
- **Enumerations**: Detailed lists of all enumeration values and their descriptions.
- **Diagram Zooming**: Each diagram includes an "Enlarge Diagram" button for detailed inspection.
