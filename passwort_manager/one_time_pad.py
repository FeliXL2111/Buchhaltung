from hash_imput import hash_in
import os

def strech(file_bytes, hash):
    hash_normal = hash
    while (file_bytes > bytes(hash)):
        hash += hash_normal
        print(hash, bytes(hash))
    return hash 

def cryp(file, key, filepath = None, keypath = None):
    file_bytes = bytes(file)
    pass_hash = hash_in(key)
    long_hash = strech()
    return True

def decryp(file, filepath, key):
    cryp(file, filepath, key)

def generate_key(file, password, filepath = None):
    hashed_password = hash_in(password)

def main():
    filepath = "test.txt"
    listee = []
    with open(filepath, 'rb') as f:
        b = f.read()
    for byte in b:
        m = 0
        for i in range(8):
            listee.insert(m, 2**i & byte)
            m += 1
    print(listee)

main()