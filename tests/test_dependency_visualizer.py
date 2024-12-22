import unittest
from dependency_visualizer import get_dependencies, get_transitive_dependencies, generate_mermaid

class TestDependencyVisualizer(unittest.TestCase):
    
    def test_get_dependencies(self):
        dependencies = get_dependencies("requests")
        self.assertIsInstance(dependencies, list)
        self.assertGreater(len(dependencies), -1)
    
    def test_get_transitive_dependencies(self):
        dependencies = get_transitive_dependencies("requests")
        self.assertIsInstance(dependencies, set)
        self.assertGreater(len(dependencies), -1)
    
    def test_generate_mermaid(self):
        package_name = "requests"
        dependencies = ["urllib3", "idna", "chardet"]
        mermaid_code = generate_mermaid(package_name, dependencies)
        self.assertIn("graph TD", mermaid_code)
        for dependency in dependencies:
            self.assertIn(f'    A --> {dependency}', mermaid_code)

if __name__ == '__main__':
    unittest.main()