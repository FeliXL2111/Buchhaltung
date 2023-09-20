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

def generate_key(password, anzahl):
    hash_string = hash_in(password)
    bs = hash_string.encode('ascii')
    tmp = ""
    for char in bs:
        tmp += bin(char)[2:].zfill(8)
    tmp2 = tmp
    i = 1
    while i <= anzahl - 1:
        tmp2 += tmp
        i += 1
    return tmp2

def text_to_binary(filepath):
    binary_string = ""
    with open(filepath, 'rb') as f:
        b = f.read()
    for byte in b:
        binary_string += bin(byte)[2:].zfill(8)
    return  binary_string

def extend_key(key_len = int, text_len = int):
    if text_len <= key_len:
        return 1
    else:
        m = text_len/key_len
        # if int(m) <= m:
        #     m += 1
        #     int(m)
        # elif int(m) > m:
        #     int(m)
        return m + 1
    
def xor(bt, bk, bt_len):
    tmp = ""
    i = 0
    while i < bt_len:
        if (bt[i] == "0" and bk[i] == "0") or (bt[i] == "1" and bk[i] == "1"):
            tmp += "0"
        else:
            tmp += "1"
        i += 1
    return tmp

def save_cryp_file(binary):
    with open("cryp.cryp", 'w') as file:
        file.write(binary)

def read_cryp_file():
    with open("cryp.cryp", 'r') as file:
        binary_text = file.read()
    return binary_text

def main():
    binary_key = generate_key("sicherespasswort", 1)
    binary_text = text_to_binary("test.txt")
    m_times_key = extend_key(len(binary_key), len(binary_text))
    long_binary_key = generate_key("sicherespassword", m_times_key)
    cryp_binary = xor(binary_text, long_binary_key, len(binary_text))
    save_cryp_file(cryp_binary[0:len(binary_key)-len(binary_text)])

def demain():
    binary_cryp = read_cryp_file()
    i = 0
    while i <= binary_cryp/8:
        binary_cryp[i:i+7].encode("uft-8")

main()