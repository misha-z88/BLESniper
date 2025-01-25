import bluetooth
import platform
import logging

class BLEStrike:
    def __init__(self, debug=False):
        self.logger = self._setup_logger(debug)
        self.platform = platform.system()
    
    def _setup_logger(self, debug):
        logging.basicConfig(
            level=logging.DEBUG if debug else logging.INFO,
            format='[BLEStrike] %(levelname)s: %(message)s'
        )
        return logging.getLogger(__name__)
    
    def scan_devices(self, timeout=10):
        """
        Универсальный метод сканирования bluetooth устройств
        """
        try:
            devices = bluetooth.discover_devices(
                duration=timeout, 
                lookup_names=True
            )
            return [
                {
                    'address': addr, 
                    'name': name or 'Unknown'
                } for addr, name in devices
            ]
        except Exception as e:
            self.logger.error(f"Scanning error: {e}")
            return []
    
    def connect_device(self, mac_address, port=1):
        """
        Подключение к bluetooth устройству
        """
        try:
            sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
            sock.connect((mac_address, port))
            return sock
        except Exception as e:
            self.logger.error(f"Connection error: {e}")
            return None