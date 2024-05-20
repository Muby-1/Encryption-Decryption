import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

# Hash the given data to create a key
data = '9b:a2:64:4e:af:38'
data_bytes = data.encode('utf-8')
hashed_data = hashlib.sha256(data_bytes).digest()

# Ensure the key is 32 bytes long (AES-256)
key = hashed_data[:32]

# Function to encrypt a file
def encrypt_file(file_path, key):
    # Generate a random initialization vector (IV)
    iv = os.urandom(16)

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Read the file contents
    with open(file_path, 'rb') as file:
        file_data = file.read()

    # Pad the file data to be a multiple of the block size
    padded_data = pad(file_data, AES.block_size)

    # Encrypt the padded data
    encrypted_data = cipher.encrypt(padded_data)

    # Write the IV and encrypted data to a new file
    encrypted_file_path = file_path + '.enc'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(iv + encrypted_data)

    return encrypted_file_path

# Example usage
file_path = 'input_file.txt'  # Replace with your file path
encrypted_file_path = encrypt_file(file_path, key)
print(f'File encrypted and saved to: {encrypted_file_path}')
