import os, requests
from cryptography.fernet import Fernet
from openai import OpenAI

# Read the encrypted API key from the file
with open('encrypted_api_key.txt', 'rb') as file:
    encrypted_api_key = file.read()

# Initialize the Fernet cipher suite with the decryption key
# Replace 'your-decryption-key' with your actual decryption key
decryption_key = b'6a1Qwe9aZg08Hj-BeoZA5c0tw0CjmoIha8KDFDkSY6s='  # The decryption key must be in bytes
cipher_suite = Fernet(decryption_key)

# Decrypt the API key
api_key = cipher_suite.decrypt(encrypted_api_key).decode()

# Initialize the OpenAI client with the decrypted API key
client = OpenAI(
    api_key=api_key
)

# Define the API endpoint
endpoint = "https://api.openai.com/v1/chat/completions"

# Define the request payload
payload = {
    "model": "gpt-3.5-turbo-0125",
    "messages": [{"role": "user", "content": "Say this is a test!"}],
    "temperature": 0.7
}

# Make the API request
response = requests.post(endpoint, json=payload, headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

# Print the response
print(response.json())
