import os
from cryptography.fernet import Fernet
from openai import OpenAI

# Read the encrypted API key from the file
with open('encrypted_api_key.txt', 'rb') as file:
    encrypted_api_key = file.read()

# Initialize the Fernet cipher suite with the decryption key
# Replace 'your-decryption-key' with your actual decryption key
decryption_key = b'<DECRYPTION KEY>'  # The decryption key must be in bytes
cipher_suite = Fernet(decryption_key)

# Decrypt the API key
api_key = cipher_suite.decrypt(encrypted_api_key).decode()

# Initialize the OpenAI client with the decrypted API key
client = OpenAI(
    api_key=api_key
)

completion = client.chat.completions.create(
  model = "gpt-3.5-turbo",
  messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
  ]
)

print(completion.choices[0].message.content.strip())
