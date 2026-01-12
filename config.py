# config.py - БЕЗ РЕАЛЬНЫХ КЛЮЧЕЙ!
import os

# === СЕКРЕТНЫЕ ДАННЫЕ ===
api_id = int(os.getenv('API_ID', '0'))
api_hash = os.getenv('API_HASH', '')
bot_token = os.getenv('BOT_TOKEN', '')
CRYPTO_PAY_TOKEN = os.getenv('CRYPTO_PAY_TOKEN', '')

# ID администраторов
admin_ids_str = os.getenv('ADMIN_CHAT_IDS', '')
admin_chat_ids = [int(id_.strip()) for id_ in admin_ids_str.split(',') if id_.strip()]

# === БЕЗОПАСНЫЕ ДАННЫЕ ===
# Только примеры, заполните своими данными или оставьте пустыми
senders = {
    "example@gmail.com": "app_password_here",  # Замените на свои
}

receivers = [
    'abuse@telegram.org',
    'dmca@telegram.org',
    'recover@telegram.org',
]

smtp_servers = {
    'gmail.com': ('smtp.gmail.com', 587),
    'mail.ru': ('smtp.mail.ru', 465),
    'yandex.ru': ('smtp.yandex.ru', 465),
}

# Приватные пользователи
private_users = {
    "ids": [6774068650],  # Ваши реальные ID
    "usernames": ['nikitak01', 'fagerewaader']
}
