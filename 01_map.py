import  array
import  string
from socket import socket

encryptedText = r"g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
#encryptedText = r"http://www.pythonchallenge.com/pc/def/map.html"
print(encryptedText)


def soluzione_01():
    charArray = list(encryptedText)
    print(charArray)
    plainText = ""
    newCharArray = array.array('b')
    for c in charArray:
        charToAppend = c
        if (c >= 'a' and c <= 'z'):
            oldValue = ord(c)-ord('a')
            newValue = oldValue + 2
            newValue = newValue % 26
            newChar = (ord('a') + newValue)
            charToAppend = chr(newChar)
        plainText += charToAppend
    print(plainText)

def soluzione_02():
    table = encryptedText.maketrans(string.ascii_lowercase,string.ascii_lowercase[2:]+string.ascii_lowercase[:2])
    print(encryptedText.translate(table))

soluzione_02()
