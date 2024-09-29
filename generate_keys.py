import os
from crypto_utils import rsa_utils

KEYS_DIR = 'keys'

if not os.path.exists(KEYS_DIR):
    os.makedirs(KEYS_DIR)

# Пути к ключам
SENDER_PRIVATE_KEY = os.path.join(KEYS_DIR, 'sender_private_key.pem')
SENDER_PUBLIC_KEY = os.path.join(KEYS_DIR, 'sender_public_key.pem')
RECEIVER_PRIVATE_KEY = os.path.join(KEYS_DIR, 'receiver_private_key.pem')
RECEIVER_PUBLIC_KEY = os.path.join(KEYS_DIR, 'receiver_public_key.pem')

# Генерация ключей отправителя
if not os.path.exists(SENDER_PRIVATE_KEY) or not os.path.exists(SENDER_PUBLIC_KEY):
    rsa_utils.generate_rsa_keys(SENDER_PRIVATE_KEY, SENDER_PUBLIC_KEY)
    print("Ключи отправителя сгенерированы.")
else:
    print("Ключи отправителя уже существуют.")

# Генерация ключей получателя
if not os.path.exists(RECEIVER_PRIVATE_KEY) or not os.path.exists(RECEIVER_PUBLIC_KEY):
    rsa_utils.generate_rsa_keys(RECEIVER_PRIVATE_KEY, RECEIVER_PUBLIC_KEY)
    print("Ключи получателя сгенерированы.")
else:
    print("Ключи получателя уже существуют.")