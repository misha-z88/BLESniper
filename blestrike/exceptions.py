"""
Custom Exceptions for BLEStrike Library
"""

class BluetoothScanError(Exception):
    """
    Exception raised when Bluetooth scanning fails
    
    Attributes:
        message (str): Explanation of the error
        error_code (int, optional): Specific error code
    """
    def __init__(self, message, error_code=None):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)

class ConnectionError(Exception):
    """
    Exception raised when Bluetooth connection fails
    
    Attributes:
        message (str): Explanation of the connection failure
        device_address (str, optional): MAC address of the device
    """
    def __init__(self, message, device_address=None):
        self.message = message
        self.device_address = device_address
        super().__init__(self.message)

class PermissionDeniedError(Exception):
    """
    Exception raised when insufficient permissions are detected
    
    Attributes:
        message (str): Description of permission issue
        required_permissions (list): Permissions needed
    """
    def __init__(self, message, required_permissions=None):
        self.message = message
        self.required_permissions = required_permissions or []
        super().__init__(self.message)