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
    # bs = hash_string.encode('utf-8')
    # tmp = ""
    # for char in bs:
    #     tmp += bin(char)[2:].zfill(8)
    # tmp2 = tmp
    # i = 1
    # while i <= anzahl - 1:
    #     tmp2 += tmp
    #     i += 1
    # return 
    l = ""
    
    i = 1
    for char in hash_string:
        tmpp = toBinary(ord(char))
        l += extend_b(tmpp)
    ll = l
    while i <= anzahl - 1:
        ll += l
        i += 1
    return ll
    

def text_to_binary(filepath):
    binary_string = ""
    # with open(filepath, 'rb') as f:
    #     b = f.read()
    # for byte in b:
    #     binary_string += bin(byte)[2:].zfill(8)
    # return binary_string
    tmp = ''
    with open("main.db", 'rb') as file:
        binary_text = file.read()
    for char in binary_text:
        tmp += bin(char)[2:].zfill(8)
    #print(tmp)
    return tmp

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
        n = int(m)
        return n + 1
    
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

def bits_in_string_umwandeln(bit_string):
        bit_gruppen = [bit_string[i:i+8] for i in range(0, len(bit_string), 8)]
        buchstaben_string = ""
        for bit_gruppe in bit_gruppen:
            dezimalwert = int(bit_gruppe, 2)
            buchstabe = bit_gruppe.decode()
            buchstaben_string += buchstabe

        return buchstaben_string

def save_file(text):
    with open("decryp.db", 'w+') as file:
            file.write(text)

def main():
    binary_key = generate_key("sicherespasswort", 1)
    binary_text = text_to_binary("test.txt")
    print(len(binary_key), len(binary_text), binary_key)
    m_times_key = extend_key(len(binary_key), len(binary_text))
    long_binary_key = generate_key("sicherespassword", m_times_key)
    print(len(long_binary_key))
    cryp_binary = xor(binary_text, long_binary_key, len(binary_text))
    save_cryp_file(cryp_binary[0:len(binary_text)])

def demain():
    binary_key = generate_key("sicherespasswort", 1)
    binary_cryp = read_cryp_file()
    print(len(binary_key), len(binary_cryp), binary_key)
    m_times_key = extend_key(len(binary_key), len(binary_cryp))
    long_binary_key = generate_key("sicherespassword", m_times_key)
    print(len(long_binary_key))
    unxor_bits = xor(binary_cryp, long_binary_key, len(binary_cryp))
    decryp_text = bits_in_string_umwandeln(unxor_bits)
    save_file(decryp_text)

def toBinary(i):
    r = ""
    while i != 0:
        if i%2 == 0:
            r += "0"
        else:
            r += "1"
        i = int(i/2)
    return r

def extend_b(i):
    l = len(i)
    j = 8-l
    while j > 0:
        i = "0" + i
        j -= 1
    #print(i, l)
    return i

demain()
