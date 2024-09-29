import hmac
import hashlib

def create_hmac(key, message):
    return hmac.new(key, message, hashlib.sha256).digest()

def verify_hmac(key, message, hmac_to_verify):
    expected_hmac = create_hmac(key, message)
    return hmac.compare_digest(expected_hmac, hmac_to_verify)