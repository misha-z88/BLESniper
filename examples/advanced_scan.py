import platform
from blestrike import BLEStrike, AndroidBLEStrike

def get_platform_specific_striker():
    system = platform.system()
    
    if system == 'Darwin':
        from blestrike.macos import MacOSBLEStrike
        return MacOSBLEStrike(debug=True)
    elif system == 'Windows':
        from blestrike.windows import WindowsBLEStrike
        return WindowsBLEStrike(debug=True)
    elif system == 'Linux':
        return AndroidBLEStrike(debug=True)
    else:
        return BLEStrike(debug=True)

def main():
    striker = get_platform_specific_striker()
    
    print("[*] Начало расширенного сканирования...")
    devices = striker.scan_devices(timeout=15)
    
    if devices:
        for device in devices:
            print(f"[+] Устройство: {device.get('name', 'Неизвестно')} - {device.get('address', 'н/д')}")
    else:
        print("[!] Устройства не найдены")

if __name__ == "__main__":
    main()