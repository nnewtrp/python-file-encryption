import random
import sys
sys.path.append("./File/Cipher")
sys.path.append("./File/Key")
sys.path.append("./File")
sys.path.append("./StoredKey")

from edFile import *
from edKey import *

loop = True

while loop:
    print('1.Encrypt 2.Decrypt Other-->Exit')
    menu = input('Type number to choose menu: ')

    if menu == '1':
        filename = input('Type the file name you want to encrypt: ')

        key = random.randint(100,400)
        keytext = EncryptKey(key, len(filename))

        Encrypt(filename,key)
        
        filekey = open('StoredKey/'+filename+'key.txt', 'wb')
        filekey.write(keytext.encode())
        filekey.close()

        print('Encryption Success')
        print()

    elif menu == '2':
        filename = input('Type the file name you want to decrypt: ')

        filekey = open('StoredKey/'+filename+'key.txt', 'rb')
        keytext = filekey.read()
        filekey.close()

        key = DecryptKey(keytext.decode(), len(filename))

        Decrypt(filename,key)

        print('Decryption Success')
        print()

        filekey = open('StoredKey/'+filename+'key.txt', 'w')
        filekey.write('')
        filekey.close()

    else:
        print('Exit')
        loop = False
