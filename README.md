# TeleAuth

TeleAuth is a Telegram tool for creating .session files using the [Telethon](https://github.com/LonamiWebs/Telethon) library. The project supports two authentication methods: via code (SMS/Telegram message) and via QR code. It also provides flexible settings through the `config.json` file.

## Features

- Authentication via code (SMS/Telegram message).
- Authentication via QR code.
- Localization (English and Russian languages).
- Configurable session file naming priority (by phone number or user ID).
- Hidden password input for 2FA.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shishkin-github/TeleAuth.git
   cd TeleAuth-1.0.0
   ```

2. Make sure you have Python 3.7 or higher installed.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Open a `config.json` file in the root directory of the project with the following content:

```json
{
  "api_id": "api_id",
  "api_hash": "api_hash",
  "language": "en",
  "session_priority": "id",
  "hide_password_input": true
}
```

- `api_id` and `api_hash` can be obtained from [my.telegram.org](https://my.telegram.org/).
- `language`: interface language (`en` for English, `ru` for Russian).
- `session_priority`: session file naming priority (`id` for user ID, `phone` for phone number).
- `hide_password_input`: whether to hide password input for 2FA (default is `true`).

## Usage

Run the script:

```bash
python TeleAuth.py
```

Follow the console instructions for authentication.

## Dependencies

- [Telethon](https://github.com/LonamiWebs/Telethon) — library for working with Telegram API.
- [qrcode](https://pypi.org/project/qrcode/) — for generating QR codes in the console.

## Project Structure

```plaintext
├── TeleAuth.py         # Main script
├── config.json         # Configuration file
├── requirements.txt    # List of dependencies
└── README.md           # Project documentation
```

## License

This project is distributed under the MIT License. See the `LICENSE` file for details.

---

## TeleAuth

TeleAuth — это Telegram инструмент для создания файлов .session с использованием библиотеки [Telethon](https://github.com/LonamiWebs/Telethon). Проект поддерживает два метода авторизации: через код (SMS/сообщение Telegram) и через QR-код. Также он предоставляет гибкие настройки через файл `config.json`.

### Возможности

- Авторизация через код (SMS/сообщение Telegram).
- Авторизация через QR-код.
- Локализация (английский и русский языки).
- Настраиваемый приоритет имени файла сессии (по номеру телефона или ID пользователя).
- Скрытый ввод пароля для 2FA.

### Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/shishkin-github/TeleAuth.git
   cd TeleAuth-1.0.0
   ```

2. Убедитесь, что у вас установлен Python 3.7 или выше.

3. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```

### Настройка

Откройте файл `config.json` в корневой директории проекта со следующим содержимым:

```json
{
  "api_id": "api_id",
  "api_hash": "api_hash",
  "language": "en",
  "session_priority": "id",
  "hide_password_input": true
}
```

- `api_id` и `api_hash` можно получить на [my.telegram.org](https://my.telegram.org/).
- `language`: язык интерфейса (`en` для английского, `ru` для русского).
- `session_priority`: приоритет имени файла сессии (`id` для ID пользователя, `phone` для номера телефона).
- `hide_password_input`: скрывать ли ввод пароля для 2FA (по умолчанию `true`).

### Использование

Запустите скрипт:

```bash
python TeleAuth.py
```

Следуйте инструкциям в консоли для авторизации.

### Зависимости

- [Telethon](https://github.com/LonamiWebs/Telethon) — библиотека для работы с Telegram API.
- [qrcode](https://pypi.org/project/qrcode/) — для генерации QR-кодов в консоли.

### Структура проекта

```plaintext
├── TeleAuth.py         # Основной скрипт
├── config.json         # Конфигурационный файл
├── requirements.txt    # Список зависимостей
└── README.md           # Документация проекта
```

### Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле `LICENSE`.
