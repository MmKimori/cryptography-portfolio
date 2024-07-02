def xor_encrypt_decrypt(data, key):
    return ''.join(chr(ord(c) ^ ord(key)) for c in data)

# Example usage
data = "Hello, World!"
key = "K"  # Key must be a single character
encrypted = xor_encrypt_decrypt(data, key)
print(f"Encrypted: {encrypted}")

decrypted = xor_encrypt_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")
