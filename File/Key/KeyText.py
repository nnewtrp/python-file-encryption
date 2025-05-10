from KeyGen import *
from bitSeq import *

def EncryptKeyText(key):
    keygen = PUKeyGen(key)
    PU = keygen[0]
    phiOfn = keygen[1]
    
    binkey = rsaEncrypt(PU, bin(key))

    keytext = 'TE' + str(PU[0]) + 'N' + str(PU[1]) + 'P' + str(phiOfn) + 'K' + binkey

    return keytext

def DecryptKeyText(keytext):
    e = ''
    n = ''
    phiOfn = ''
    key = ''

    count = 0

    for i in range(len(keytext)):
        if keytext[i].isnumeric():
            if count == 1:
                e += keytext[i]
            elif count == 2:
                n += keytext[i]
            elif count == 3:
                phiOfn += keytext[i]
            elif count == 4:
                key += keytext[i]
        else:
            if keytext[i] == 'E':
                count = 1
            elif keytext[i] == 'N':
                count = 2
            elif keytext[i] == 'P':
                count = 3
            elif keytext[i] == 'K':
                count = 4

    PR = PRKey((int(e), int(n)), int(phiOfn))
    realkey = int(rsaDecrypt(PR,key), 2)

    return realkey
