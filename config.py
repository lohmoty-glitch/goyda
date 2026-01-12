# config.py - БЕЗОПАСНАЯ ВЕРСИЯ
# Этот файл НЕ содержит реальных ключей.
# Все секреты устанавливаются через переменные окружения на Render.

import os

# ========== СЕКРЕТНЫЕ ДАННЫЕ (только из переменных окружения) ==========
API_ID = int(os.getenv('API_ID', '0'))  # Значение по умолчанию для локальной разработки
API_HASH = os.getenv('API_HASH', '')
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
CRYPTO_PAY_TOKEN = os.getenv('CRYPTO_PAY_TOKEN', '')  # Если не используется, можно оставить пустым

# ID администраторов через запятую: "12345,67890"
ADMIN_CHAT_IDS_STR = os.getenv('ADMIN_CHAT_IDS', '6934998718,8304483534')  # Ваши ID через запятую

# Преобразуем строку в список чисел
admin_chat_ids = []
if ADMIN_CHAT_IDS_STR:
    admin_chat_ids = [int(id_.strip()) for id_ in ADMIN_CHAT_IDS_STR.split(',') if id_.strip().isdigit()]

# ========== БЕЗОПАСНЫЕ ДАННЫЕ (можно хранить в коде) ==========
# Эти данные не являются критическими секретами

# Приватные пользователи (защищенные от жалоб)
private_users = {
    "ids": [6774068650],  # Ваши реальные ID приватных пользователей
    "usernames": ['nikitak01', 'fagerewaader']  # Ваши реальные username (без @)
}

# SMTP серверы (общедоступная информация)
smtp_servers = {
    "gmail.com": ("smtp.gmail.com", 587),
    "yandex.ru": ("smtp.yandex.ru", 465),
    "mail.ru": ("smtp.mail.ru", 465),
}

# Получатели жалоб (общедоступные адреса Telegram)
receivers = [
    'abuse@telegram.org',
    'dmca@telegram.org',
    'recover@telegram.org',
]

# Для совместимости с вашим текущим кодом бота (бот.py)
# Создаем алиасы с именами, которые импортирует ваш бот.py
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN

# ВАЖНО: Пароли от почтовых аккаунтов ДОЛЖНЫ быть только в переменных окружения Render.
# Для работы бота вам нужно будет добавить их в Render как отдельные переменные,
# например: SMTP_PASSWORD_1, SMTP_PASSWORD_2 и т.д.
# Или переделать логику в боте. Сейчас оставляем пустой словарь.
senders = {}
# Пример структуры, если нужно:
# senders = {
#     "example1@gmail.com": os.getenv('SMTP_PASSWORD_1', ''),
#     "example2@gmail.com": os.getenv('SMTP_PASSWORD_2', ''),
# }
