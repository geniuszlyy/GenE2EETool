import os
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

def generate_aes_key(key_size=32):
    return os.urandom(key_size)

def aes_encrypt(key, plaintext):
    iv = os.urandom(16)
    padder = sym_padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext  # Присоединяем IV для дальнейшей расшифровки

def aes_decrypt(key, iv_ciphertext):
    iv = iv_ciphertext[:16]
    ciphertext = iv_ciphertext[16:]

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    unpadder = sym_padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext