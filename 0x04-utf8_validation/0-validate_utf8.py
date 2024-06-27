#!/usr/bin/python3
'''
UTF-8 Validation
'''


def validUTF8(data):
    '''
    Return: True if data is a valid UTF-8 encoding, else return False
    '''
    byt = 0
    for d in data:
        m = 1 << 7
        if not byt:
            while d & m:
                byt += 1
                m >>= 1
            if not byt:
                continue
            if byt == 1 or byt > 4:
                return False
        else:
            if d >> 6 != 0b10:
                return False
        byt -= 1
    return byt == 0
