from BasicCipher import en_BasicCipher, de_BasicCipher
from Longcode import en_RepeatLongcode, de_RepeatLongcode

def en_Cipher(text, key):
    key = str(key)
    key1 = int(key[0]) + int(key[1]) + int(key[2])
    key2 = (int(key) % 8) + 2
    key3 = (int(key[0]) % 2) + 2
    return en_RepeatLongcode(en_BasicCipher(text, key1, key2), key3)

def de_Cipher(text, key):
    key = str(key)
    key1 = int(key[0]) + int(key[1]) + int(key[2])
    key2 = (int(key) % 8) + 2
    key3 = (int(key[0]) % 2) + 2
    return de_BasicCipher(de_RepeatLongcode(text, key3), key1, key2)
