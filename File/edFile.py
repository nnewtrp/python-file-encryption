import sys
sys.path.append("./Cipher")

from Cipher import *

def Encrypt(filename, key):
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    k = key%256
    
    data = bytearray(data)
    for i, v in enumerate(data):
        data[i] = v^k
        
    data = data.hex()
    c_data = en_Cipher(data, key)

    c_data = c_data.encode()
    
    file = open(filename, 'wb')
    file.write(c_data)
    file.close()

def Decrypt(filename, key):
    file = open(filename, 'rb')
    data = file.read()
    file.close()

    data = data.decode()
    
    m_data = de_Cipher(data, key)

    k = key%256
    
    data = bytearray.fromhex(m_data)      
    for i, v in enumerate(data):
        data[i] = v^k

    file = open(filename, 'wb')
    file.write(data)
    file.close()


