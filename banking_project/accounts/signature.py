
import hashlib

class SimpleSign:
    def __init__(self, key):
        self.key = key

    def sign(self, data):
        # Implement digital signature algorithm here
        # For demonstration, let's assume simple hashing
        hashed_data = hashlib.sha256(data.encode()).hexdigest()
        return hashed_data

    def verify(self, data, signature):
        # Implement verification algorithm here
        # For demonstration, let's assume simple hashing and comparison
        return hashlib.sha256(data.encode()).hexdigest() == signature
