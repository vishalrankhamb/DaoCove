# test_daocove.py
"""
Tests for DaoCove module.
"""

import unittest
from daocove import DaoCove

class TestDaoCove(unittest.TestCase):
    """Test cases for DaoCove class."""

    def test_initialization(self):
        """Test class initialization."""
        instance = DaoCove()
        self.assertIsInstance(instance, DaoCove)

    def test_run_method(self):
        """Test the run method."""
        instance = DaoCove()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
