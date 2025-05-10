import random

def en_Longcode(text):
    message = ""
    for i in range(len(text)):
        r = random.randint(0, ord(text[i]))
        a = chr(ord(text[i]) - r)
        b = chr(r)
        message += a+b
    return message

def de_Longcode(text):
    message = ""
    i = 0
    while i < len(text):
        a = ord(text[i])
        b = ord(text[i+1])
        message += chr(a+b)
        i += 2
    return message

def en_RepeatLongcode(text, key):
    message = text
    for i in range(key):
        message = en_Longcode(message)
    return message

def de_RepeatLongcode(text, key):
    message = text
    for i in range(key):
        message = de_Longcode(message)
    return message
