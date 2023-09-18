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

def generate_key(password):
    hash_string = hash_in(password)
    print(hash_string)
    bs = hash_string.encode('ascii')
    tmp = ""
    for char in bs:
        tmp += bin(char)[2:].zfill(8)
    print(tmp)
    return tmp

def main():
    filepath = "test.txt"
    listee = ""
    with open(filepath, 'rb') as f:
        b = f.read()
    for byte in b:
        listee += bin(byte)[2:].zfill(8)
    print(listee)
    generate_key("sicherespasswort")

main()