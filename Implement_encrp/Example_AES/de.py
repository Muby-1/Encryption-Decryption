from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Step 1: Encode the Key
key = "e8:6a:64:25:fb:e6".encode('utf-8')
# Ensure the key is 16, 24, or 32 bytes long. We'll pad it to 16 bytes.
key = pad(key, 16)

# Function to decrypt data
def decrypt_file(input_file, output_file, key):
    # Initialize AES cipher in ECB mode
    cipher = AES.new(key, AES.MODE_ECB)
    
    # Read the ciphertext from the file
    with open(input_file, 'rb') as f:
        ciphertext = f.read()
    
    # Decrypt the ciphertext
    decrypted_padded_plaintext = cipher.decrypt(ciphertext)
    
    # Unpad the decrypted plaintext
    plaintext = unpad(decrypted_padded_plaintext, AES.block_size)
    
    # Write the plaintext to the output file
    with open(output_file, 'wb') as f:
        f.write(plaintext)

# Example usage
input_file = 'encrypted_example.txt'  # replace with your encrypted file
output_file = 'decrypted_example.txt'  # replace with your desired output file
decrypt_file(input_file, output_file, key)

print(f"File '{input_file}' has been decrypted and saved as '{output_file}'")
