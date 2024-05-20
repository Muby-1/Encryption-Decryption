import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

# Hash the given data to create a key
data = '9b:a2:64:4e:af:38'
data_bytes = data.encode('utf-8')
hashed_data = hashlib.sha256(data_bytes).digest()

# Ensure the key is 32 bytes long (AES-256)
key = hashed_data[:32]

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
encrypted_file_path = 'input_file.txt.enc'  # Replace with your encrypted file path
decrypted_file_path = decrypt_file(encrypted_file_path, key)
print(f'File decrypted and saved to: {decrypted_file_path}')
