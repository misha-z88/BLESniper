import winreg
import pythoncom
import win32com.client
from .core import BLEStrike

class WindowsBLEStrike(BLEStrike):
    def __init__(self, debug=False):
        super().__init__(debug)
        self._check_bluetooth_availability()
    
    def _check_bluetooth_availability(self):
        """
        Проверка доступности Bluetooth в Windows
        """
        try:
            key = winreg.OpenKey(
                winreg.HKEY_LOCAL_MACHINE, 
                r"SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters"
            )
            winreg.CloseKey(key)
        except Exception as e:
            self.logger.warning("Bluetooth not fully configured")
    
    def advanced_scan(self):
        """
        Расширенное сканирование для Windows
        """
        try:
            shell = win32com.client.Dispatch("WScript.Shell")
            bluetooth_devices = shell.Exec("cmd /c wmic path win32_bluetoothdevice get name")
            return bluetooth_devices.StdOut.ReadAll()
        except Exception as e:
            self.logger.error(f"Windows Bluetooth scan error: {e}")
            return []