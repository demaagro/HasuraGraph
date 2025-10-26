# test_hasuragraphql.py
"""
Tests for HasuraGraphQL module.
"""

import unittest
from hasuragraphql import HasuraGraphQL

class TestHasuraGraphQL(unittest.TestCase):
    """Test cases for HasuraGraphQL class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HasuraGraphQL()
        self.assertIsInstance(instance, HasuraGraphQL)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HasuraGraphQL()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
