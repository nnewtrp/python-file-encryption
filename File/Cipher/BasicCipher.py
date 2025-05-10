import math

def en_Caesar(text, key):
    message = ""
    i = 0
    for i in range(len(text)):
        num = ord(text[i])
        num += key
        message += chr(num)
        i += 1
    return message

def de_Caesar(text, key):
    message = ""
    i = 0
    for i in range(len(text)):
        num = ord(text[i])
        num -= key
        message += chr(num)
        i += 1
    return message

def en_Railfence(text, key):
    message = ""
    i = 0
    for i in range(key):
        j = 0
        for j in range(len(text)):
            if j%key == i:
                message += text[j]
            j += 1
        i += 1
    return message

def de_Railfence(text, key):
    message = ""
    i = 0
    col = math.ceil(len(text)/key)
    for i in range(col):
        j = 0
        row = key
        count = 0
        pos = i
        if len(text)%key != 0:
            if i == col-1:
                row = len(text)%key
            for j in range(row):
                message += text[pos]
                if count < len(text)%key:
                    pos += col
                    count += 1
                else:
                    pos += col-1
                j += 1
        else:
            for j in range(row):
                message += text[pos]
                pos += col
                j += 1
        i += 1
    return message

def en_BasicCipher(text, key1, key2):
    return en_Railfence(en_Caesar(text,key1),key2)

def de_BasicCipher(text, key1, key2):
    return de_Caesar(de_Railfence(text,key2),key1)
