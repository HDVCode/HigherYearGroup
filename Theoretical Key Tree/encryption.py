from cryptography.fernet import Fernet


# ---------------- Encryption / Decryption ----------------

# Encrypts a message with a key and outputs the result
def encrypt(key, message):
    cipher = Fernet(key)
    return cipher.encrypt(message.encode())

# Decrypts a message with a key and outputs the result
def decrypt(key, encrypted_message):
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_message).decode()
