import re
import uuid

def validate_mac_address(address):
    """
    Валидация MAC адреса
    """
    mac_regex = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
    return re.match(mac_regex, address) is not None

def generate_random_mac():
    """
    Генерация случайного MAC адреса
    """
    return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) 
                     for elements in range(0,2*6,2)][::-1])