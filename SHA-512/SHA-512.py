import hashlib

def calculate_sha512(file_path):
    sha512_hash = hashlib.sha512()

    with open(file_path, 'rb') as file:
        # Read the file in small chunks to handle large files
        while True:
            data = file.read(8192)  # 8KB chunks
            if not data:
                break
            sha512_hash.update(data)

    return sha512_hash.hexdigest()

# Provide the path to the file you want to hash
file_path = 'C:\Users\ACER\Downloads\SHA.py'
sha512_hash = calculate_sha512(file_path)

print("SHA-512 Hash:", sha512_hash)
