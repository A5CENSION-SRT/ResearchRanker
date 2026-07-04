import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

class TestEnvironment(unittest.TestCase):
    def test_directory_structure(self):
        root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        self.assertTrue(os.path.exists(os.path.join(root_dir, 'README.md')))
        self.assertTrue(os.path.exists(os.path.join(root_dir, 'ARCHITECTURE.md')))
        self.assertTrue(os.path.exists(os.path.join(root_dir, 'DIAGRAMS.md')))
        self.assertTrue(os.path.exists(os.path.join(root_dir, 'docs/diagrams/system_architecture.png')))
        self.assertFalse(os.path.exists(os.path.join(root_dir, 'ML_README.md')))
        self.assertFalse(os.path.exists(os.path.join(root_dir, 'docs/images')))

if __name__ == '__main__':
    unittest.main()
