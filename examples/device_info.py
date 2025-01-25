"""
Device Information Retrieval Example for BLEStrike
This script demonstrates how to collect detailed information about Bluetooth devices
"""

import sys
import platform
from blestrike import BLEStrike, validate_mac_address

def get_device_details(mac_address):
    """
    Retrieve comprehensive details about a specific Bluetooth device
    
    Args:
        mac_address (str): MAC address of the target device
    
    Returns:
        dict: Detailed device information
    """
    striker = BLEStrike(debug=True)
    
    if not validate_mac_address(mac_address):
        print(f"[ERROR] Invalid MAC address: {mac_address}")
        return None
    
    try:
        # Attempt to retrieve device information
        device_info = striker.bluetooth_info(mac_address)
        
        # Enhanced information logging
        print("\n[DEVICE INFORMATION]")
        print(f"Name: {device_info.get('name', 'Unknown')}")
        print(f"MAC Address: {mac_address}")
        print("Services:")
        for service in device_info.get('services', []):
            print(f"  - {service}")
        
        return device_info
    
    except Exception as e:
        print(f"[ERROR] Could not retrieve device information: {e}")
        return None

def main():
    """
    Main execution for device information retrieval
    """
    if len(sys.argv) < 2:
        print("Usage: python device_info.py <bluetooth_mac_address>")
        sys.exit(1)
    
    mac_address = sys.argv[1]
    device_details = get_device_details(mac_address)

if __name__ == "__main__":
    main()