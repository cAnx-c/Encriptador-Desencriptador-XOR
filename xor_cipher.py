import random

def encrypt(text):
    bin_text = ''.join(format(ord(c), '08b') for c in text)
    key = ''.join(random.choice('01') for _ in range(8))
    keystream = (key * (len(bin_text) // len(key) + 1))[:len(bin_text)]
    xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(bin_text, keystream))
    return xor_result, key

def decrypt(encrypted, key):
    keystream = (key * (len(encrypted) // len(key) + 1))[:len(encrypted)]
    xor_result = ''.join(str(int(a) ^ int(b)) for a, b in zip(encrypted, keystream))
    return ''.join(chr(int(xor_result[i:i+8], 2)) for i in range(0, len(xor_result), 8))

text = input("Ingresa el texto: ")
encrypted, key = encrypt(text)
print("Clave generada:", key)
print("Texto encriptado:", encrypted)
decrypted = decrypt(encrypted, key)
print("Texto desencriptado:", decrypted)
