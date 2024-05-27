

class SimpleCrypt:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        # Implement encryption algorithm here
        # For demonstration, let's assume simple XOR encryption
        encrypted_data = ''.join(chr(ord(c) ^ self.key) for c in data)
        return encrypted_data

    def decrypt(self, encrypted_data):
        # Implement decryption algorithm here
        # For demonstration, let's assume simple XOR decryption
        decrypted_data = ''.join(chr(ord(c) ^ self.key) for c in encrypted_data)
        return decrypted_data
