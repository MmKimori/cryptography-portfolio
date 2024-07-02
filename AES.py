from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    while len(data) % 16 != 0:
        data += ' '
    return data

def aes_encrypt(plain_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_text = pad(plain_text)
    encrypted = cipher.encrypt(padded_text.encode())
    return base64.b64encode(encrypted).decode('utf-8')

def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted_bytes = base64.b64decode(encrypted_text)
    decrypted = cipher.decrypt(encrypted_bytes)
    return decrypted.decode('utf-8').strip()

# Example usage
plain_text = "Hello, World!"
key = get_random_bytes(16)  # AES key must be either 16, 24, or 32 bytes long
encrypted_text = aes_encrypt(plain_text, key)
print(f"Encrypted: {encrypted_text}")

decrypted_text = aes_decrypt(encrypted_text, key)
print(f"Decrypted: {decrypted_text}")
