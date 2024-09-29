import os
from crypto_utils import rsa_utils, aes_utils, hmac_utils

# Пути к ключам и сообщениям
SENDER_PRIVATE_KEY = 'keys/sender_private_key.pem'
SENDER_PUBLIC_KEY = 'keys/sender_public_key.pem'
RECEIVER_PUBLIC_KEY = 'keys/receiver_public_key.pem'

MESSAGE_PATH = 'messages/plain_message.txt'
ENCRYPTED_MESSAGE_PATH = 'messages/encrypted_message.bin'
ENCRYPTED_KEY_PATH = 'messages/encrypted_key.bin'
HMAC_PATH = 'messages/message.hmac'

# Проверка существования ключей
if not os.path.exists(SENDER_PRIVATE_KEY):
    print("Ошибка: Приватный ключ отправителя не найден. Пожалуйста, запустите generate_keys.py для генерации ключей.")
    exit()

if not os.path.exists(RECEIVER_PUBLIC_KEY):
    print("Ошибка: Публичный ключ получателя не найден. Пожалуйста, запустите generate_keys.py для генерации ключей.")
    exit()

# Загрузка ключей
receiver_public_key = rsa_utils.load_public_key(RECEIVER_PUBLIC_KEY)

# Генерация симметричного ключа AES
aes_key = aes_utils.generate_aes_key()

# Чтение исходного сообщения
with open(MESSAGE_PATH, 'rb') as f:
    plaintext = f.read()

# Шифрование сообщения с помощью AES
encrypted_message = aes_utils.aes_encrypt(aes_key, plaintext)

# Создание HMAC для зашифрованного сообщения
message_hmac = hmac_utils.create_hmac(aes_key, encrypted_message)

# Шифрование симметричного ключа с помощью открытого ключа получателя
encrypted_key = rsa_utils.rsa_encrypt(receiver_public_key, aes_key)

# Сохранение зашифрованного сообщения, ключа и HMAC
with open(ENCRYPTED_MESSAGE_PATH, 'wb') as f:
    f.write(encrypted_message)

with open(ENCRYPTED_KEY_PATH, 'wb') as f:
    f.write(encrypted_key)

with open(HMAC_PATH, 'wb') as f:
    f.write(message_hmac)

print("Сообщение успешно зашифровано и готово к отправке.")