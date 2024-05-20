"""from cryptography.fernet import Fernet


import sys
sys.path.append("C:/Users/mubeena.m/Desktop/My Workspace/Implement_encrp/grades.txt")
#key = Fernet.generate_key()
#with open('mykey.key','wb') as mykey:
#    mykey.write(key)

with open('mykey.key','rb') as mykey:
    key = mykey.read()
print(key)

f = Fernet(key)

with open('grades.txt','rb') as original_file:
    original = original_file.read()

encrypted = f.encrypt(original)

with open('enc_grades.txt','wb') as encryptes_file:
    encryptes_file.write(encrypted)"""
from cryptography.fernet import Fernet

def generate_key():
    """
    Generates a key and saves it into a file
    """
    key = Fernet.generate_key()  # Generates a secret key
    with open("secret.key", "wb") as key_file:  # Opens a file named "secret.key" for writing in binary mode
        key_file.write(key)  # Writes the generated key to the file

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()  # Opens the "secret.key" file and reads its content (the key)

def encrypt_file(file_path):
    """
    Encrypts the content of a file and overwrites the original file with encrypted content
    """
    key = load_key()  # Loads the key from the "secret.key" file
    f = Fernet(key)  # Creates a Fernet cipher object using the key
    
    with open(file_path, "rb") as file:  # Opens the file to be encrypted for reading in binary mode
        content = file.read()  # Reads the content of the file
        encrypted_content = f.encrypt(content)  # Encrypts the content using the Fernet cipher
    
    with open(file_path, "wb") as file:  # Opens the same file for writing in binary mode
        file.write(encrypted_content)  # Writes the encrypted content back to the file

if __name__ == "__main__":
    generate_key()  # Generates a new key and saves it to "secret.key"
    encrypt_file("C:/Users/mubeena.m/Desktop/My Workspace/Implement_encrp/input_file.txt")  # Encrypts the specified file
