import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import uuid

# Function to get the MAC address and hash it to create a key
def get_hashed_mac_key():
    # Get the MAC address
    mac = uuid.getnode()
    # Convert the MAC address to a string
    mac_str = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1])
    # Encode the MAC string to bytes
    mac_bytes = mac_str.encode('utf-8')
    # Hash the MAC address using SHA-256
    hashed_mac = hashlib.sha256(mac_bytes).digest()
    # Ensure the key is 32 bytes long (AES-256)
    key = hashed_mac[:32]
    return key

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
key = get_hashed_mac_key()
file_path = 'input_file.txt'  # Replace with your file path
encrypted_file_path = encrypt_file(file_path, key)
print(f'File encrypted and saved to: {encrypted_file_path}')


"""
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os
import uuid

# Function to get the MAC address and hash it to create a key
def get_hashed_mac_key():
    # Get the MAC address
    mac = uuid.getnode()
    # Convert the MAC address to a string
    mac_str = ':'.join(['{:02x}'.format((mac >> elements) & 0xff) for elements in range(0, 2 * 6, 8)][::-1])
    # Encode the MAC string to bytes
    mac_bytes = mac_str.encode('utf-8')
    # Hash the MAC address using SHA-256
    hashed_mac = hashlib.sha256(mac_bytes).digest()
    # Ensure the key is 32 bytes long (AES-256)
    key = hashed_mac[:32]
    return key

# Function to encrypt a file and save the encrypted data back to the same file
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

    # Write the IV and encrypted data back to the same file
    with open(file_path, 'wb') as file:
        file.write(iv + encrypted_data)

    return file_path

# Example usage
key = get_hashed_mac_key()
file_path = 'input_file.txt'  # Replace with your file path
encrypted_file_path = encrypt_file(file_path, key)
print(f'File encrypted and saved to: {encrypted_file_path}')
"""
