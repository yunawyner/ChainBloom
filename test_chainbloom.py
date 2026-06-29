# test_chainbloom.py
"""
Tests for ChainBloom module.
"""

import unittest
from chainbloom import ChainBloom

class TestChainBloom(unittest.TestCase):
    """Test cases for ChainBloom class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ChainBloom()
        self.assertIsInstance(instance, ChainBloom)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ChainBloom()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
