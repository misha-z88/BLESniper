from blestrike import BLEStrike, AndroidBLEStrike
import platform

def main():
    system = platform.system()
    
    if system == 'Linux':
        striker = AndroidBLEStrike(debug=True)
    else:
        striker = BLEStrike(debug=True)
    
    print("[*] Начало сканирования...")
    devices = striker.scan_devices()
    
    for device in devices:
        print(f"[+] Устройство: {device['name']} - {device['address']}")

if __name__ == "__main__":
    main()