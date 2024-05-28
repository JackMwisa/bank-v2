class CustomCrypto:
    @staticmethod
    def encrypt(message, shift=1):
        encrypted_message = ''
        for char in message:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    start = ord('a')
                    encrypted_message += chr((ord(char) - start + shift_amount) % 26 + start)
                elif char.isupper():
                    start = ord('A')
                    encrypted_message += chr((ord(char) - start + shift_amount) % 26 + start)
            else:
                encrypted_message += char
        return encrypted_message

    @staticmethod
    def decrypt(encrypted_message, shift=1):
        decrypted_message = ''
        for char in encrypted_message:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    start = ord('a')
                    decrypted_message += chr((ord(char) - start - shift_amount) % 26 + start)
                elif char.isupper():
                    start = ord('A')
                    decrypted_message += chr((ord(char) - start - shift_amount) % 26 + start)
            else:
                decrypted_message += char
        return decrypted_message


# Here’s an improved version that handles wrapping for lowercase and uppercase alphabetic characters: