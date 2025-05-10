import math
import sys
sys.path.append("./../Cipher")

from BasicCipher import en_BasicCipher, de_BasicCipher
from Longcode import en_RepeatLongcode, de_RepeatLongcode

def en_KeyCipher(keytext, key):
    key = int(key)
    key1 = (key % 10) + 2
    key2 = (key % 8) + 2
    key3 = (key % 2) + 2
    return en_RepeatLongcode(en_BasicCipher(keytext, key1, key2), key3)

def de_KeyCipher(keytext, key):
    key = int(key)
    key1 = (key % 10) + 2
    key2 = (key % 8) + 2
    key3 = (key % 2) + 2
    return de_BasicCipher(de_RepeatLongcode(keytext, key3), key1, key2)
