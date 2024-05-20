import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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

# Function to decrypt a file
def decrypt_file(encrypted_file_path, key):
    # Read the encrypted file contents
    with open(encrypted_file_path, 'rb') as encrypted_file:
        iv = encrypted_file.read(16)  # The first 16 bytes are the IV
        encrypted_data = encrypted_file.read()

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_padded_data = cipher.decrypt(encrypted_data)

    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)

    # Write the decrypted data to a new file
    decrypted_file_path = encrypted_file_path.replace('.enc', '.dec')
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_data)

    return decrypted_file_path

# Example usage
key = get_hashed_mac_key()
encrypted_file_path = 'input_file.txt.enc'  # Replace with your encrypted file path
decrypted_file_path = decrypt_file(encrypted_file_path, key)
print(f'File decrypted and saved to: {decrypted_file_path}')


"""
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
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

# Function to decrypt a file and overwrite the encrypted file with the decrypted content
def decrypt_file(encrypted_file_path, key):
    # Read the encrypted file contents
    with open(encrypted_file_path, 'rb') as encrypted_file:
        iv = encrypted_file.read(16)  # The first 16 bytes are the IV
        encrypted_data = encrypted_file.read()

    # Create an AES cipher object with the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the data
    decrypted_padded_data = cipher.decrypt(encrypted_data)

    # Unpad the decrypted data
    decrypted_data = unpad(decrypted_padded_data, AES.block_size)

    # Overwrite the encrypted file with the decrypted content
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(decrypted_data)

    return encrypted_file_path

# Example usage
key = get_hashed_mac_key()
encrypted_file_path = 'input_file.txt.enc'  # Replace with your encrypted file path
decrypted_file_path = decrypt_file(encrypted_file_path, key)
print(f'File decrypted and saved to: {decrypted_file_path}')
"""