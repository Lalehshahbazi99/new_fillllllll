def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr((ord(char) + key) % 128)
    return encrypted_text

def decrypt(encrypted_text, key):
    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += chr((ord(char) - key) % 128)
    return decrypted_text

message = "Hello, World!"
encryption_key = 3
encrypted_message = encrypt(message, encryption_key)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypt(encrypted_message, encryption_key))
