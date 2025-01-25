"""
Bluetooth Security Audit Tool for BLEStrike
Performs comprehensive security assessment of Bluetooth devices
"""

import sys
from blestrike import BLEStrike, validate_mac_address

class BluetoothSecurityAudit:
    def __init__(self, debug=True):
        """
        Initialize Bluetooth Security Audit
        
        Args:
            debug (bool): Enable debug logging
        """
        self.striker = BLEStrike(debug=debug)
    
    def perform_security_scan(self, mac_address):
        """
        Conduct security assessment on a specific Bluetooth device
        
        Args:
            mac_address (str): Target device MAC address
        
        Returns:
            dict: Security assessment results
        """
        if not validate_mac_address(mac_address):
            print(f"[ERROR] Invalid MAC address: {mac_address}")
            return None
        
        try:
            # Retrieve device information
            device_info = self.striker.bluetooth_info(mac_address)
            
            # Perform security assessment
            security_results = self.striker.security_assessment(mac_address)
            
            # Comprehensive security report
            print("\n[BLUETOOTH SECURITY AUDIT]")
            print(f"Device: {device_info.get('name', 'Unknown')}")
            print(f"MAC Address: {mac_address}")
            print("\nSecurity Assessment:")
            print(f"Pairing Mode: {security_results.get('pairing_mode', 'Unknown')}")
            print(f"Encryption Support: {security_results.get('encryption_support', 'No')}")
            
            vulnerabilities = security_results.get('potential_vulnerabilities', [])
            if vulnerabilities:
                print("\nPotential Vulnerabilities:")
                for vuln in vulnerabilities:
                    print(f"  - {vuln}")
            else:
                print("\nNo immediate vulnerabilities detected.")
            
            return security_results
        
        except Exception as e:
            print(f"[ERROR] Security audit failed: {e}")
            return None

def main():
    """
    Main execution for Bluetooth security audit
    """
    if len(sys.argv) < 2:
        print("Usage: python security_audit.py <bluetooth_mac_address>")
        sys.exit(1)
    
    mac_address = sys.argv[1]
    audit = BluetoothSecurityAudit()
    audit.perform_security_scan(mac_address)

if __name__ == "__main__":
    main()