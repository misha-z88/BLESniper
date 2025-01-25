"""
Unit Tests for Core Bluetooth Functionality
"""

import unittest
from blestrike import BLEStrike, validate_mac_address

class TestBluetoothCore(unittest.TestCase):
    def setUp(self):
        """
        Initialize test environment
        """
        self.striker = BLEStrike(debug=True)
    
    def test_mac_address_validation(self):
        """
        Test MAC address validation
        """
        valid_macs = [
            '00:11:22:33:44:55',
            'AA:BB:CC:DD:EE:FF'
        ]
        invalid_macs = [
            '00:11:22:33:44',
            'GG:HH:II:JJ:KK:LL'
        ]
        
        for mac in valid_macs:
            self.assertTrue(validate_mac_address(mac))
        
        for mac in invalid_macs:
            self.assertFalse(validate_mac_address(mac))
    
    def test_device_scan(self):
        """
        Test Bluetooth device scanning
        """
        devices = self.striker.scan_devices(timeout=5)
        self.assertIsInstance(devices, list)

if __name__ == '__main__':
    unittest.main()