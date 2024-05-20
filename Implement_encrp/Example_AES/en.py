from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os
import base64

def generate_key(password, salt):
    # Use PBKDF2HMAC for key derivation
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    encoded_key = base64.urlsafe_b64encode(key)
    return encoded_key

def encrypt_file(input_file, output_file, password):
    # Generate a random salt
    salt = os.urandom(16)
    
    # Generate a key from the password and salt
    encoded_key = generate_key(password, salt)
    key = base64.urlsafe_b64decode(encoded_key)
    
    # Generate a random IV (Initialization Vector)
    iv = os.urandom(16)
    
    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    
    # Read the plaintext from the file
    with open(input_file, 'rb') as f:
        plaintext = f.read()
    
    # Pad the plaintext to be a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()
    
    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    
    # Write the salt, iv, and ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(salt + iv + ciphertext)

def main():
    input_file = 'plaintext.txt'
    output_file = 'encrypted.txt'
    password = 'your_password_here'  # Use a strong password
    
    encrypt_file(input_file, output_file, password)
    print(f'File {input_file} encrypted and saved as {output_file}')

if __name__ == "__main__":
    main()
