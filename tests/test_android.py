"""
Unit Tests for Android-specific Bluetooth Functionality
"""

import unittest
import platform
from blestrike import AndroidBLEStrike

class TestAndroidBluetooth(unittest.TestCase):
    def setUp(self):
        """
        Initialize test environment
        """
        if platform.system() != 'Linux':
            self.skipTest("Android tests only run on Linux/Termux")
        
        self.striker = AndroidBLEStrike(debug=True)
    
    def test_termux_bluetooth_scan(self):
        """
        Test advanced Bluetooth scanning in Termux
        """
        result = self.striker.advanced_scan()
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()