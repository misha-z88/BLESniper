import unittest
from blestrike import BLEStrike

class TestBLEStrike(unittest.TestCase):
    def setUp(self):
        self.striker = BLEStrike()
    
    def test_scan_devices(self):
        devices = self.striker.scan_devices(timeout=5)
        self.assertIsInstance(devices, list)