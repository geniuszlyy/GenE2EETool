from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def generate_rsa_keys(private_key_path, public_key_path, key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    with open(private_key_path, 'wb') as priv_file:
        priv_file.write(private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))
    with open(public_key_path, 'wb') as pub_file:
        pub_file.write(private_key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))

def load_private_key(private_key_path):
    with open(private_key_path, 'rb') as priv_file:
        return serialization.load_pem_private_key(
            priv_file.read(),
            password=None,
            backend=default_backend()
        )

def load_public_key(public_key_path):
    with open(public_key_path, 'rb') as pub_file:
        return serialization.load_pem_public_key(
            pub_file.read(),
            backend=default_backend()
        )

def rsa_encrypt(public_key, message):
    return public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

def rsa_decrypt(private_key, ciphertext):
    return private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )