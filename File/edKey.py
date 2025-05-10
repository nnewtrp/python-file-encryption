import sys
sys.path.append("./Cipher")
sys.path.append("./Key")

from KeyText import *
from KeyCipher import *

def EncryptKey(key, num):
    return en_KeyCipher(EncryptKeyText(key), num)

def DecryptKey(keytext, num):
    return DecryptKeyText(de_KeyCipher(keytext, num))
