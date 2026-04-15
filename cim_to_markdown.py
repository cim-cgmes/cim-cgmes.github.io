import json
import os
from collections import defaultdict

def sanitize_filename(name):
    return "".join([c for c in name if c.isalnum() or c in (' ', '.', '_')]).strip().replace(' ', '_')

def main():
    json_path = 'cim_schema_import_test.json'
    output_dir = 'pages/docs'
    classes_dir = os.path.join(output_dir, 'Classes')
    profiles_dir = os.path.join(output_dir, 'Profiles')

    os.makedirs(classes_dir, exist_ok=True)
    os.makedirs(profiles_dir, exist_ok=True)

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # First element is usually namespaces
    namespaces = data[0] if isinstance(data[0], dict) and 'base' in data[0] else {}
    
    classes = {}
    enums = {}
    profiles = defaultdict(list)
    
    # Process objects starting from the third one (0: namespaces, 1: ontology metadata)
    for obj in data[1:]:
        for key, value in obj.items():
            if not isinstance(value, dict):
                continue
            
            rdf_type = value.get('RDFType')
            stereotype = value.get('CIMStereotype', '')
            
            if rdf_type == 'Class':
                if stereotype == 'enumeration':
                    enums[key] = value
                else:
                    classes[key] = value
                
                # Assign to profiles
                categories = value.get('CIMCategories', [])
                for cat in categories:
                    profiles[cat].append(key)
            elif rdf_type == 'Ontology':
                # Skip ontology metadata for now
                pass

    # Build inheritance map
    inheritance = {cls_name: cls_data.get('SuperType') for cls_name, cls_data in classes.items() if cls_data.get('SuperType')}
    subtypes = defaultdict(list)
    for child, parent in inheritance.items():
        subtypes[parent].append(child)

    # Generate Class Pages
    for cls_name, cls_data in classes.items():
        generate_class_page(cls_name, cls_data, classes_dir, inheritance, subtypes, enums, classes)

    # Generate Enum Pages (similar to class pages but with values)
    for enum_name, enum_data in enums.items():
        generate_enum_page(enum_name, enum_data, classes_dir)

    # Generate Profile Pages
    for profile_name, cls_list in profiles.items():
        generate_profile_page(profile_name, cls_list, profiles_dir, classes, enums, inheritance)

    # Generate Index (README.md)
    generate_index(output_dir, profiles, classes, enums)

def generate_class_page(cls_name, cls_data, output_dir, inheritance, subtypes, enums, all_classes):
    filename = os.path.join(output_dir, f"{sanitize_filename(cls_name)}.md")
    label = cls_data.get('Label', cls_name)
    comment = cls_data.get('Comment', 'No description available.')
    super_type = inheritance.get(cls_name)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {label}\n\n")
        f.write(f"{comment}\n\n")
        
        if super_type or subtypes.get(cls_name):
            # Mermaid Inheritance Diagram
            f.write("## Inheritance\n\n")
            f.write("```mermaid\nclassDiagram\n")
            if super_type:
                f.write(f"    {super_type} <|-- {cls_name}\n")
            for sub in subtypes.get(cls_name, []):
                f.write(f"    {cls_name} <|-- {sub}\n")
            f.write("```\n")
            f.write('<button class="mermaid-enlarge-button">Enlarge Diagram</button>\n\n')
        
        # Attributes Table
        f.write("## Attributes\n\n")
        f.write("| Label | Type | Multiplicity | Comment |\n")
        f.write("|-------|------|--------------|---------|\n")
        
        attributes = cls_data.get('Attributes', [])
        for attr in attributes:
            attr_label = attr.get('Label', 'N/A')
            attr_type = attr.get('DataType') or attr.get('RDFRange', 'N/A')
            
            # Simple link if type is a class or enum
            type_link = attr_type
            if attr_type in all_classes or attr_type in enums:
                type_link = f"[{attr_type}]({sanitize_filename(attr_type)}.md)"
            
            multiplicity = attr.get('CIMMultiplicity', '').split('#M:')[-1] if 'CIMMultiplicity' in attr else ''
            attr_comment = attr.get('Comment', '').replace('\n', ' ')
            
            f.write(f"| {attr_label} | {type_link} | {multiplicity} | {attr_comment} |\n")
        
        if not attributes:
            f.write("| No attributes | | | |\n")
        f.write("\n")

def generate_enum_page(enum_name, enum_data, output_dir):
    filename = os.path.join(output_dir, f"{sanitize_filename(enum_name)}.md")
    label = enum_data.get('Label', enum_name)
    comment = enum_data.get('Comment', 'No description available.')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# {label} (Enumeration)\n\n")
        f.write(f"{comment}\n\n")
        
        f.write("## Values\n\n")
        f.write("| Label | Comment |\n")
        f.write("|-------|---------|\n")
        
        values = enum_data.get('Values', [])
        for val in values:
            val_label = val.get('Label', 'N/A')
            val_comment = val.get('Comment', '').replace('\n', ' ')
            f.write(f"| {val_label} | {val_comment} |\n")
        f.write("\n")

def generate_profile_page(profile_name, cls_names, output_dir, all_classes, all_enums, inheritance):
    filename = os.path.join(output_dir, f"{sanitize_filename(profile_name)}.md")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Profile: {profile_name}\n\n")
        
        if len(cls_names) > 1:
            # Mermaid Diagram for Profile
            f.write("## Overview Diagram\n\n")
            f.write("```mermaid\nclassDiagram\n")
        
            relevant_classes = set(cls_names)
        
            for cls_name in cls_names:
                cls_data = all_classes.get(cls_name)
                if not cls_data: continue
                
                # Inheritance within profile
                super_type = inheritance.get(cls_name)
                if super_type in relevant_classes:
                    f.write(f"    {super_type} <|-- {cls_name}\n")
                
                # Associations within profile
                for attr in cls_data.get('Attributes', []):
                    attr_type = attr.get('DataType') or attr.get('RDFRange')
                    if attr_type in relevant_classes:
                        f.write(f"    {cls_name} --> {attr_type} : {attr.get('Label')}\n")
            
            f.write("```\n")
            f.write('<button class="mermaid-enlarge-button">Enlarge Diagram</button>\n\n')
        
        f.write("## Classes\n\n")
        for cls_name in sorted(cls_names):
            label = cls_name
            comment = ""
            if cls_name in all_classes:
                label = all_classes[cls_name].get('Label', cls_name)
                comment = all_classes[cls_name].get('Comment', '').split('.')[0] + '.'
            elif cls_name in all_enums:
                label = all_enums[cls_name].get('Label', cls_name)
                comment = all_enums[cls_name].get('Comment', '').split('.')[0] + '.'
                
            f.write(f"- [{label}](../Classes/{sanitize_filename(cls_name)}): {comment}\n")

def generate_index(output_dir, profiles, classes, enums):
    filename = os.path.join(output_dir, "Overview.md")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("---")
        f.write("sidebar_position: 2")
        f.write("---")

        f.write("# CIM Documentation\n\n")
        
        f.write("## Profiles\n\n")
        for profile in sorted(profiles.keys()):
            f.write(f"- [ {profile} ](Profiles/{sanitize_filename(profile)})\n")
        
        f.write("\n## All Classes\n\n")
        all_entities = {**classes, **enums}
        for name in sorted(all_entities.keys()):
            label = all_entities[name].get('Label', name)
            f.write(f"- [{label}](Classes/{sanitize_filename(name)})\n")

if __name__ == "__main__":
    main()
