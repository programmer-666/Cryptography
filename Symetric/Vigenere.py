# Vigenere/Vernam Cipher
# With ASCII Table
# suhaarslan
# python Vigenere.py e/d key text
import sys
def encrypt(x,k):
    return ((ord(str(x).lower())-97)+(ord(str(k).lower())-97))%26+97
def decrypt(x,k):
    return ((ord(str(x).lower())+97)-(ord(str(k).lower())+97))%26+97
def Balancer(key, textLen):
    new = ""
    for i in range(textLen):
        new+=key[i%len(key)]
    return new
text = ""
for x in range(3,len(sys.argv)):
    text+=sys.argv[x]
stat = sys.argv[1]
key = Balancer(sys.argv[2], len(text))
if stat == 'e':
    for i in range(len(text)):
        print(chr(encrypt(text[i], key[i])), end='')
elif stat == 'd':
    for i in range(len(text)):
        print(chr(decrypt(text[i], key[i])), end='')