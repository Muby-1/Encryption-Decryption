from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_file(file_path):
    """
    Decrypts the content of an encrypted file and overwrites the original file with decrypted content
    """
    key = load_key()
    f = Fernet(key)
    
    with open(file_path, "rb") as file:
        encrypted_content = file.read()
        decrypted_content = f.decrypt(encrypted_content)
    
    with open(file_path, "wb") as file:
        file.write(decrypted_content)

if __name__ == "__main__":
    decrypt_file("C:/Users/mubeena.m/Desktop/My Workspace/Implement_encrp/input_file.txt")
