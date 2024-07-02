import random

class RSA:
    def __init__(self):
        self.p = self.generate_prime()
        self.q = self.generate_prime()
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = self.generate_e(self.phi)
        self.d = self.mod_inverse(self.e, self.phi)

    def is_prime(self, num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    def generate_prime(self):
        while True:
            num = random.randint(100, 999)
            if self.is_prime(num):
                return num

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def generate_e(self, phi):
        e = random.randint(2, phi - 1)
        while self.gcd(e, phi) != 1:
            e = random.randint(2, phi - 1)
        return e

    def mod_inverse(self, a, m):
        m0, x0, x1 = m, 0, 1
        if m == 1:
            return 0
        while a > 1:
            q = a // m
            m, a = a % m, m
            x0, x1 = x1 - q * x0, x0
        if x1 < 0:
            x1 += m0
        return x1

    def encrypt(self, message):
        return [pow(ord(char), self.e, self.n) for char in message]

    def decrypt(self, ciphertext):
        return ''.join([chr(pow(char, self.d, self.n)) for char in ciphertext])

    def get_public_key(self):
        return (self.e, self.n)

    def get_private_key(self):
        return (self.d, self.n)

rsa = RSA()

public_keys = [rsa.get_public_key() for _ in range(3)]
private_keys = [rsa.get_private_key() for _ in range(3)]

message = "MELCHIZEDEK"
print(f"Original Message: {message}")

# Encrypt the message using the public key
ciphertext = rsa.encrypt(message)
print(f"Encrypted Message: {ciphertext}")

# Decrypt the message using the private key
decrypted_message = rsa.decrypt(ciphertext)
print(f"Decrypted Message: {decrypted_message}")

print(f"Public Keys: {public_keys}")
print(f"Private Keys: {private_keys}")
