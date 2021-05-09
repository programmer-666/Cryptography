# Polybius Cipher
# With ASCII Table
# suhaarslan
# python Polybius.py <csv> <e/d> <text>
import numpy as np
import sys
from numpy import genfromtxt

def encrypt(csvName="polyMatrix.csv", text='lorem'):
    st = ""
    dataMatris = genfromtxt(csvName, delimiter=',')
    for x in text:
        for j in range(len(dataMatris)):
            for i in range(len(dataMatris)):
                if dataMatris[j,i] == ord(x):
                    st+=str(j+1);st+=str(i+1)
    return st
def findRC(psw,csvName="polyMatrix.csv"):
    blocks = []
    f = True
    r = ""
    for i in psw:
        if f:
            f = False
            r+=str(i)   
        else:
            f = True
            r+=str(i)
            blocks.append(r)
            r = ""
    return blocks
def decrypt(psw,csvName="polyMatrix.csv"):
    blocks = findRC(psw,csvName="polyMatrix.csv")
    text = ""
    dataMatris = genfromtxt(csvName, delimiter=',')
    for ch in blocks:
        for j in range(len(dataMatris)):
            for i in range(len(dataMatris)):
                if str(j+1)+str(i+1) == ch:
                    text+=chr(int(dataMatris[j][i]))
    return text
x = 3
while x < len(sys.argv):
    if sys.argv[2] == 'e':
        print(encrypt(sys.argv[1], sys.argv[x]),end='')
    elif sys.argv[2] == 'd':
        print(decrypt(sys.argv[x], sys.argv[1]))
    x=x+1
