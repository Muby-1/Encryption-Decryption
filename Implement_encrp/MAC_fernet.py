from cryptography.fernet import Fernet
import hashlib
import uuid

# Get MAC address (example: replace with actual method to get MAC address)
def get_mac_address():
  
    mac_address = ':'.join(format(x, '02x') for x in uuid.getnode().to_bytes(6, 'big'))
    return mac_address

# Derive key from MAC address
def derive_key_from_mac(mac_address):
    hash_object = hashlib.sha256(mac_address.encode())
    return hash_object.digest()

# Combine MAC-derived key with Fernet key
def combine_keys(fernet_key, mac_derived_key):
    combined_key = bytes(a ^ b for a, b in zip(fernet_key, mac_derived_key))
    return combined_key

# Example usage
if __name__ == "__main__":
    fernet_key = Fernet.generate_key()
    mac_address = get_mac_address()
    mac_derived_key = derive_key_from_mac(mac_address)
    combined_key = combine_keys(fernet_key, mac_derived_key)

    print("Fernet Key:", fernet_key)
    print("MAC-derived Key:", mac_derived_key)
    print("Combined Key:", combined_key)
    print("MAC address:", mac_address)


