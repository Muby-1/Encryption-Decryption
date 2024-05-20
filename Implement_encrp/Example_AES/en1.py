from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Step 1: Encode the Key
key = "e8:6a:64:25:fb:e6".encode('utf-8')
# Ensure the key is 16, 24, or 32 bytes long. We'll pad it to 16 bytes.
key = pad(key, 16)

# Function to encrypt data
def encrypt_file(input_file, output_file, key):
    # Initialize AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Read the plaintext from the file
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    # Pad the plaintext to be a multiple of the block size
    padded_plaintext = pad(plaintext, AES.block_size)
    
    # Encrypt the plaintext
    ciphertext = cipher.encrypt(padded_plaintext)
    
    # Write the ciphertext to the output file
    with open(output_file, 'wb') as f:
        f.write(ciphertext)

# Example usage
input_file = 'input_file.txt'  # replace with your input file
output_file = 'encrypted_example.txt'  # replace with your desired output file
encrypt_file(input_file, output_file, key)

print(f"File '{input_file}' has been encrypted and saved as '{output_file}'")
