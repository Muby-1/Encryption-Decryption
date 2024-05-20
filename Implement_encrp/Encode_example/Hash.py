import hashlib

# Data to be hashed
data = '9b:a2:64:4e:af:38'

# Convert the data to a bytes object
data_bytes = data.encode('utf-8')

# Create a SHA-256 hash object
hash_object = hashlib.sha256()

# Update the hash object with the bytes of the data
hash_object.update(data_bytes)

# Retrieve the hexadecimal representation of the hash
hashed_data = hash_object.hexdigest()

print(f'Original data: {data}')
print(f'Hashed data (SHA-256): {hashed_data}')
