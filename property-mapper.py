import yaml
import re

def parse_properties(file_path):
    properties = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                properties[key.strip()] = value.strip()
    return properties

def parse_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def flatten_dict(d, parent_key='', sep='.'):
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

def compare_properties(properties, yaml_data):
    flat_yaml = flatten_dict(yaml_data)
    missing_in_yaml = set(properties.keys()) - set(flat_yaml.keys())
    return missing_in_yaml

def main():
    properties_file = 'application.properties'
    yaml_file = 'application.yml'

    try:
        properties = parse_properties(properties_file)
        yaml_data = parse_yaml(yaml_file)
        missing_properties = compare_properties(properties, yaml_data)

        print(f"Properties missing in {yaml_file}:")
        for prop in missing_properties:
            print(f"  - {prop}")

    except FileNotFoundError as e:
        print(f"Error: {e.filename} not found. Please make sure both files exist in the current directory.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
