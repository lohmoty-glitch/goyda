# config.py - ДЛЯ ПРОДАКШЕНА (Render)
# НИКАКИХ РЕАЛЬНЫХ КЛЮЧЕЙ ЗДЕСЬ НЕ ДОЛЖНО БЫТЬ!
# Все секреты устанавливаются через переменные окружения в Render

import os

# ================= СЕКРЕТНЫЕ ДАННЫЕ =================
# Читаем из переменных окружения (в Render)
# Для локальной разработки: создайте файл .env с этими значениями

API_ID = int(os.getenv('API_ID', '0'))  # 0 для разработки
API_HASH = os.getenv('API_HASH', '')    # пусто для разработки
BOT_TOKEN = os.getenv('BOT_TOKEN', '')  # пусто для разработки
CRYPTO_PAY_TOKEN = os.getenv('CRYPTO_PAY_TOKEN', '')  # если используется

# ID администраторов через запятую: "12345,67890"
ADMIN_CHAT_IDS_STR = os.getenv('ADMIN_CHAT_IDS', '')

# Преобразуем строку в список чисел
admin_chat_ids = []
if ADMIN_CHAT_IDS_STR:
    admin_chat_ids = [int(id_.strip()) for id_ in ADMIN_CHAT_IDS_STR.split(',') if id_.strip().isdigit()]

# Если admin_chat_ids пуст, добавляем ваш ID для локальной разработки
if not admin_chat_ids:
    admin_chat_ids = [0]  # замените 0 на ваш ID для локального тестирования

# ================= БЕЗОПАСНЫЕ ДАННЫЕ =================
# Эти данные не секретные, их можно хранить в коде

# Почта для отправки жалоб
senders = {
    "example1@gmail.com": "app_password_here",  # Замените на свои данные для локальной разработки
    "example2@gmail.com": "app_password_here",  # Или оставьте пустые значения
}

# Получатели жалоб
receivers = [
    'abuse@telegram.org',
    'dmca@telegram.org',
    'recover@telegram.org',
    'support@telegram.org',
    'security@telegram.org',
    'spam@telegram.org',
    'info@telegram.org',
]

# SMTP серверы
smtp_servers = {
    "gmail.com": ("smtp.gmail.com", 587),
    "yandex.ru": ("smtp.yandex.ru", 465),
    "mail.ru": ("smtp.mail.ru", 465),
    "outlook.com": ("smtp.office365.com", 587),
    "yahoo.com": ("smtp.mail.yahoo.com", 465),
}

# Для веб-форм
mail = ['user@example.com']  # тестовые почты
phone_numbers = ['+79123456789']  # тестовые номера

# Приватные пользователи (защищенные от жалоб)
private_users = {
    "ids": [0],  # замените на реальные ID
    "usernames": ['example_user']  # без @
}

# Алиасы для импорта (чтобы бот.py мог импортировать как раньше)
api_id = API_ID
api_hash = API_HASH
bot_token = BOT_TOKEN
