# EN
A local tool for testing End-to-End Encryption (E2EE) between two parties. **GenE2EETool** simulates the process of message exchange using asymmetric encryption (RSA) for key exchange and symmetric encryption (AES) for encrypting the messages themselves.

## Features

- **RSA Key Generation**: Generates RSA key pairs for the sender and receiver.
- **AES Encryption**: Encrypts messages using AES symmetric encryption.
- **Secure Key Exchange**: Encrypts the AES key with the receiver's RSA public key.
- **Data Integrity**: Uses HMAC to ensure the integrity of the encrypted message.


## Requirements

- Python 3.6 or higher
- `cryptography` library

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/geniuszly/GenE2EETool.git
   cd GenE2EETool
    ```
2. **Install Dependencies**
   ```bash
   pip install cryptography
    ```

## Usage
### Step 1: Generate RSA Key Pairs
Run the `generate_keys.py` script to generate RSA key pairs for both the sender and the receiver.
```bash
python generate_keys.py
```
### Step 2: Prepare Your Message
Create a text file named `plain_message.txt` inside the messages directory with the content you wish to encrypt.

### Step 3: Encrypt the Message
Run the `sender.py` script to encrypt the message and the AES key.
```bash
python sender.py
```
This will generate:

- `encrypted_message.bin`: The AES-encrypted message.
- `encrypted_key.bin`: The RSA-encrypted AES key.
- `message.hmac`: The HMAC of the encrypted message.

### Step 4: Decrypt the Message
Run the `receiver.py` script to decrypt the AES key and then the message.
```bash
python receiver.py
```
The decrypted message will be saved as `decrypted_message.txt` in the `messages/` directory.

## How It Works
1. **Key Generation**
   - RSA keys are generated for both the sender and receiver.
   - Keys are stored in the `keys/` directory.
2. **Encryption Process**
   - The sender generates an AES symmetric key.
   - The message is encrypted using AES.
   - The AES key is encrypted with the receiver's RSA public key.
   - An HMAC is created for the encrypted message.
3. **Decryption Process**
   - The receiver decrypts the AES key using their RSA private key.
   - The receiver verifies the HMAC to ensure data integrity.
   - The message is decrypted using the AES key.

## In the next updates
- Implement message exchange over a network using sockets or WebSockets.
- Extend the tool to support encryption and transfer of files.
- Implement additional security features like key rotation, password-protected keys, and secure key storage.
- Add comprehensive error handling and logging mechanisms.

# RU
Локальный инструмент для тестирования сквозного шифрования (End-to-End Encryption, E2EE) между двумя сторонами. **GenE2EETool** симулирует процесс обмена сообщениями, используя асимметричное шифрование (RSA) для обмена ключами и симметричное шифрование (AES) для шифрования самих сообщений.

## Возможности

- **Генерация ключей RSA**: Создает пары ключей RSA для отправителя и получателя.
- **Шифрование AES**: Шифрует сообщения с использованием симметричного шифрования AES.
- **Безопасный обмен ключами**: Шифрует ключ AES открытым ключом RSA получателя.
- **Целостность данных**: Использует HMAC для обеспечения целостности зашифрованного сообщения.


## Требования

- Python 3.6 или выше
- Библиотека  `cryptography` 

## Установка

1. **Клонируйте репозиторий**

   ```bash
   git clone https://github.com/geniuszly/GenE2EETool.git
   cd GenE2EETool
    ```
2. **Установите зависимости**
   ```bash
   pip install cryptography
    ```

## Использование
### Шаг 1: Генерация пар ключей RSA
Запустите скрипт `generate_keys.py` для генерации пар ключей RSA для отправителя и получателя.
```bash
python generate_keys.py
```
### Шаг 2: Подготовьте сообщение
Создайте текстовый файл с именем `plain_message.txt` в директории `messages/` с содержимым, которое вы хотите зашифровать.

### Шаг 3: Зашифруйте сообщение
Запустите скрипт `sender.py` для шифрования сообщения и ключа AES.
```bash
python sender.py
```
Это сгенерирует следующие файлы:

- `encrypted_message.bin`: Зашифрованное сообщение (AES).
- `encrypted_key.bin`: Зашифрованный ключ AES (RSA).
- `message.hmac`: HMAC зашифрованного сообщения.

### Шаг 4: Расшифруйте сообщение
Запустите скрипт `receiver.py` для расшифровки ключа AES и сообщения.
```bash
python receiver.py
```
Расшифрованное сообщение будет сохранено как  `decrypted_message.txt` в директории `messages/`.

## Как это работает
1. **Генерация ключей**
   - Генерируются ключи RSA для отправителя и получателя.
   - Ключи сохраняются в директории `keys/`.
2. **Процесс шифрования**
   - Отправитель генерирует симметричный ключ AES.
   - Сообщение шифруется с помощью AES.
   - Ключ AES шифруется открытым ключом RSA получателя.
   - Создается HMAC для зашифрованного сообщения.
3. **Процесс расшифровки**
   - Получатель расшифровывает ключ AES с помощью своего закрытого ключа RSA.
   - Проверяет HMAC для обеспечения целостности данных.
   - Сообщение расшифровывается с использованием ключа AES.

## В следующих обновлениях
- Реализовать обмен сообщениями через сеть с использованием сокетов или WebSockets.
- Расширить инструмент для поддержки шифрования и передачи файлов.
- Внедрить дополнительные функции безопасности, такие как ротация ключей, защита ключей паролями и безопасное хранение ключей.
- Добавить полноценную обработку ошибок и механизмы логирования.
