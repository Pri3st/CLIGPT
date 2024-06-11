from cryptography.fernet import Fernet

# Generate a key for encryption and decryption
# You must store this key securely; do not lose it
key = Fernet.generate_key()
print(f"Encryption Key (store this securely): {key.decode()}")

# Initialize the Fernet cipher suite
cipher_suite = Fernet(key)

# Encrypt the API key
api_key = b'<API_KEY>'  # The API key must be in bytes
encrypted_api_key = cipher_suite.encrypt(api_key)
print(f"Encrypted API Key: {encrypted_api_key.decode()}")

# Save the encrypted API key to a file (optional)
with open('encrypted_api_key.txt', 'wb') as file:
    file.write(encrypted_api_key)
