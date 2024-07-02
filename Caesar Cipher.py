def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Example usage
text = "Hello, World!"
shift = 3
encrypted = caesar_encrypt(text, shift)
print(f"Encrypted: {encrypted}")

decrypted = caesar_decrypt(encrypted, shift)
print(f"Decrypted: {decrypted}")
