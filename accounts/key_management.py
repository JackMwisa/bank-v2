from Cryptodome.Random import get_random_bytes

def generate_symmetric_key():
    return get_random_bytes(16)  # 16 bytes for AES-128

def generate_rsa_key_pair():
    return RSA.generate(2048)
