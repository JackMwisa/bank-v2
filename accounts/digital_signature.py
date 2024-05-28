from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256


def generate_key_pair():
    key = RSA.generate(2048)
    return key

def sign_data(data, private_key):
    h = SHA256.new(data.encode())
    signature = pkcs1_15.new(private_key).sign(h)
    return signature

def verify_signature(data, signature, public_key):
    h = SHA256.new(data.encode())
    try:
        pkcs1_15.new(public_key).verify(h, signature)
        return True
    except (ValueError, TypeError):
        return False
