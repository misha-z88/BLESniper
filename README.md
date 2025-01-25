
## 🚀 Подготовка к установке

### Системные требования
- Python 3.7+
- pip
- Операционная система: 
  * Windows
  * macOS
  * Linux (включая Termux)
- Bluetooth-адаптер

### Предварительная подготовка

1. Установка системных зависимостей:

#### Windows:
```bash
pip install pywin32
```

#### MacOS:
```bash
xcode-select --install
brew install python
```

#### Linux/Termux:
```bash
pkg install python bluetooth
```

## 📦 Установка библиотеки

### Варианты установки:

1. Через pip (рекомендованный способ):
```bash
pip install git+https://github.com/misha-z88/BLEStrike.git
```

2. Клонирование репозитория:
```bash
git clone https://github.com/misha-z88/BLEStrike.git
cd BLEStrike
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

## 🔍 Первичная настройка

### Проверка установки
```python
from blestrike import BLEStrike

# Базовое сканирование
striker = BLEStrike(debug=True)
devices = striker.scan_devices()

for device in devices:
    print(f"Устройство: {device['name']} - {device['address']}")
```

## 🛡️ Основные сценарии использования

### 1. Сканирование устройств
```python
# Базовое сканирование
devices = striker.scan_devices(timeout=15)

# Расширенное сканирование
advanced_devices = striker.advanced_scan()
```

### 2. Информация об устройстве
```python
# Получение информации о конкретном устройстве
device_info = striker.bluetooth_info('00:11:22:33:44:55')
```

### 3. Безопасность
```python
# Базовая оценка безопасности
security_report = striker.security_assessment('00:11:22:33:44:55')
```

## 🧪 Тестирование

### Запуск тестов:
```bash
python3 -m unittest discover tests/
```

## ⚠️ Важные предупреждения

1. Всегда получайте согласие на тестирование устройств
2. Соблюдайте локальные законы о кибербезопасности
3. Используйте библиотеку только в исследовательских целях

## 🆘 Устранение проблем

- Проверьте совместимость Bluetooth-адаптера
- Убедитесь в наличии необходимых прав
- Обновите библиотеки в случае ошибок

## 📚 Документация

Полная документация будет доступна в README.md в репозитории проекта.

## 🤝 Вклад в развитие

1. Форкните репозиторий
2. Создайте свою ветку (`git checkout -b feature/AmazingFeature`)
3. Закоммитьте изменения (`git commit -m 'Add some AmazingFeature'`)
4. Запушьте в репозиторий (`git push origin feature/AmazingFeature`)
5. Откройте Pull Request

## 📞 Поддержка

По вопросам и предложениям: 
- Создавайте Issue в GitHub-репозитории
- Отправляйте Pull Requests

---

🔒 **ВНИМАНИЕ**: Библиотека предназначена исключительно для легальных исследовательских целей!

