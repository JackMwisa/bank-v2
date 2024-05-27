import hashlib

def calculate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()
