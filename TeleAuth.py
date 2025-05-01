import asyncio
import os
import json
import getpass
from telethon import TelegramClient

async def main():
    config_file = 'config.json'
    if not os.path.exists(config_file):
        print(f"Файл {config_file} не найден!")
        return

    with open(config_file, 'r', encoding='utf-8') as f:
        try:
            config = json.load(f)
            api_id = int(config['api_id'])
            api_hash = config['api_hash']
            lang = config.get('language', 'en')
            session_priority = config.get('session_priority', 'id')
            hide_pwd = config.get('hide_password_input', True)
        except KeyError as e:
            print(f"Отсутствует ключ {e} в файле конфигурации!")
            return
        except ValueError:
            print("Неверное значение для api_id в файле конфигурации!")
            return

    en_msgs = {
        'enter_phone': 'Enter your phone number (with country code): ',
        'choose_auth': 'Choose authentication method:',
        'method_code': '1. By code (SMS/Telegram message)',
        'method_qr': '2. By QR code',
        'enter_choice': 'Enter 1 or 2: ',
        'enter_code': 'Enter the received code: ',
        'enter_password': '2FA is enabled, enter your password: ',
        'auth_success': 'Authentication successful!',
        'qr_install': 'Please install qrcode package to display QR in console:',
        'qr_manual': 'Scan URL: ',
        'qr_scan': 'Scan the QR code in your Telegram app and confirm login',
        'session_renamed': 'Session file renamed to ',
        'temp_not_found': 'Temporary session file not found!'
    }
    ru_msgs = {
        'enter_phone': 'Введите ваш номер телефона (с кодом страны): ',
        'choose_auth': 'Выберите способ авторизации:',
        'method_code': '1. По коду (SMS/сообщение Telegram)',
        'method_qr': '2. По QR-коду',
        'enter_choice': 'Введите 1 или 2: ',
        'enter_code': 'Введите полученный код: ',
        'enter_password': 'У вас включён 2FA, введите пароль: ',
        'auth_success': 'Авторизация прошла успешно!',
        'qr_install': 'Установите пакет qrcode для отображения QR в консоли:',
        'qr_manual': 'URL для сканирования: ',
        'qr_scan': 'Отсканируйте QR-код в приложении Telegram и подтвердите вход',
        'session_renamed': 'Файл сессии переименован в ',
        'temp_not_found': 'Временный файл сессии не найден!'
    }
    msgs = ru_msgs if lang == 'ru' else en_msgs



    phone = input(msgs['enter_phone'])

    temp_session_name = 'temp_session'
    client = TelegramClient(temp_session_name, api_id, api_hash)

    await client.connect()
    if not await client.is_user_authorized():
        print(msgs['choose_auth'])
        print(msgs['method_code'])
        print(msgs['method_qr'])
        choice = input(msgs['enter_choice']).strip()
        if choice == '2':
            # Авторизация по QR
            qr_login = await client.qr_login()
            try:
                import qrcode
                qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
                qr.add_data(qr_login.url)
                qr.make()
                qr.print_ascii(invert=True)
            except ImportError:
                print(msgs['qr_install'])
                print(f"pip install qrcode\\n{msgs['qr_manual']}{qr_login.url}")
            print(msgs['qr_scan'])
            from telethon.errors import SessionPasswordNeededError
            try:
                await qr_login.wait()
            except SessionPasswordNeededError:
                if hide_pwd:
                    pwd = getpass.getpass(msgs['enter_password'])
                else:
                    pwd = input(msgs['enter_password'])
                await client.sign_in(password=pwd)
        else:
            await client.send_code_request(phone)
            code = input(msgs['enter_code'])
            from telethon.errors import SessionPasswordNeededError
            try:
                await client.sign_in(phone, code)
            except SessionPasswordNeededError:
                if hide_pwd:
                    pwd = getpass.getpass(msgs['enter_password'])
                else:
                    pwd = input(msgs['enter_password'])
                await client.sign_in(password=pwd)
    print(msgs['auth_success'])

    me = await client.get_me()

    if session_priority == 'phone':
        session_filename = f"{phone}.session"
    else:
        if me and hasattr(me, 'id'):
            session_filename = f"{me.id}.session"
        else:
            session_filename = f"{phone}.session"

    await client.disconnect()

    temp_file = temp_session_name + '.session'
    if os.path.exists(temp_file):
        os.rename(temp_file, session_filename)
        print(msgs['session_renamed'] + session_filename)
    else:
        print(msgs['temp_not_found'])

if __name__ == '__main__':
    asyncio.run(main())
