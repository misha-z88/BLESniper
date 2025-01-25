import subprocess
from .core import BLEStrike

class AndroidBLEStrike(BLEStrike):
    def __init__(self, debug=False):
        super().__init__(debug)
        self._check_termux_permissions()
    
    def _check_termux_permissions(self):
        """
        Проверка прав в Termux
        """
        try:
            subprocess.run(['termux-bluetooth-scan'], check=True)
        except Exception:
            self.logger.warning("Limited Termux Bluetooth permissions")
    
    def advanced_scan(self):
        """
        Расширенное сканирование для Android
        """
        result = subprocess.run(
            ['termux-bluetooth-scan', '-t', '15'], 
            capture_output=True, 
            text=True
        )
        return result.stdout