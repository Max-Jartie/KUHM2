import os
import csv
import subprocess
import re
import sys
import unittest

def read_config(config_path):
    """Читает конфигурационный файл CSV и возвращает словарь с конфигурацией."""
    config = {}
    with open(config_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            key, value = row
            config[key] = value
    return config

def get_dependencies(package_name):
    """Получает зависимости пакета из setup.py или requirements.txt."""
    try:
        result = subprocess.run(
            ["pip", "show", package_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            raise ValueError(f"Package {package_name} not found.")
        
        output = result.stdout
        dependencies = re.search(r'Requires: (.+)', output)
        if dependencies:
            return dependencies.group(1).split(", ")
    except Exception as e:
        print(f"Error getting dependencies for {package_name}: {e}")
        return []

    return []

def get_transitive_dependencies(package_name, visited=None):
    """Рекурсивно получает все транзитивные зависимости пакета."""
    if visited is None:
        visited = set()
    
    dependencies = get_dependencies(package_name)
    for dependency in dependencies:
        if dependency not in visited:
            visited.add(dependency)
            get_transitive_dependencies(dependency, visited)
    
    return visited

def generate_mermaid(package_name, dependencies):
    """Генерирует код Mermaid для визуализации графа зависимостей."""
    mermaid_code = f'graph TD\n    A["{package_name}"]\n'
    for dependency in dependencies:
        mermaid_code += f'    A --> {dependency}\n'
    return mermaid_code

def main(config_path):
    config = read_config(config_path)
    
    package_name = config['package_name']
    output_file = config['output_file']
    
    dependencies = get_transitive_dependencies(package_name)
    mermaid_code = generate_mermaid(package_name, dependencies)
    
    with open(output_file, 'w') as f:
        f.write(mermaid_code)
    
    print(f"Mermaid code has been written to {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python dependency_visualizer.py <config_file.csv>")
        sys.exit(1)
    
    config_path = sys.argv[1]
    main(config_path)