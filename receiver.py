import os
from crypto_utils import rsa_utils, aes_utils, hmac_utils

# Пути к ключам и сообщениям
RECEIVER_PRIVATE_KEY = 'keys/receiver_private_key.pem'
RECEIVER_PUBLIC_KEY = 'keys/receiver_public_key.pem'

ENCRYPTED_MESSAGE_PATH = 'messages/encrypted_message.bin'
ENCRYPTED_KEY_PATH = 'messages/encrypted_key.bin'
HMAC_PATH = 'messages/message.hmac'
DECRYPTED_MESSAGE_PATH = 'messages/decrypted_message.txt'

# Проверка существования ключа
if not os.path.exists(RECEIVER_PRIVATE_KEY):
    print("Ошибка: Приватный ключ получателя не найден. Пожалуйста, запустите generate_keys.py для генерации ключей.")
    exit()

# Загрузка приватного ключа получателя
receiver_private_key = rsa_utils.load_private_key(RECEIVER_PRIVATE_KEY)

# Чтение зашифрованного симметричного ключа
with open(ENCRYPTED_KEY_PATH, 'rb') as f:
    encrypted_key = f.read()

# Расшифрование симметричного ключа
aes_key = rsa_utils.rsa_decrypt(receiver_private_key, encrypted_key)

# Чтение зашифрованного сообщения и HMAC
with open(ENCRYPTED_MESSAGE_PATH, 'rb') as f:
    encrypted_message = f.read()

with open(HMAC_PATH, 'rb') as f:
    received_hmac = f.read()

# Проверка целостности данных с использованием HMAC
if not hmac_utils.verify_hmac(aes_key, encrypted_message, received_hmac):
    print("Ошибка: HMAC не соответствует. Данные были изменены.")
    exit()

# Расшифрование сообщения с помощью AES
plaintext = aes_utils.aes_decrypt(aes_key, encrypted_message)

# Сохранение расшифрованного сообщения
with open(DECRYPTED_MESSAGE_PATH, 'wb') as f:
    f.write(plaintext)

print("Сообщение успешно расшифровано.")