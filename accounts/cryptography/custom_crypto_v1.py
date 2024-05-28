

# basic Caesar cipher algorithm for encryption and decryption.

# ceasar cypher

class CustomCrypto:
    @staticmethod
    def encrypt(message):
        # Your custom encryption logic goes here
        encrypted_message = ''.join(chr(ord(char) + 1) for char in message)
        return encrypted_message

    @staticmethod
    def decrypt(encrypted_message):
        # Your custom decryption logic goes here
        decrypted_message = ''.join(chr(ord(char) - 1) for char in encrypted_message)
        return decrypted_message
