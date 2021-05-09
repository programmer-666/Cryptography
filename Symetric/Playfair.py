# Playfair Cipher
# With ASCII Table
# suhaarslan
import numpy as np
import sys

def keyControl(text):
    temp = set()
    temps = ""
    for i in text:
        if i not in temp and i not in temps:
            temp.add(i)
            temps+=i
    return temps
def checkTextLen(text, c):# text kontrol eder, çift değilse c değerini ekler
    if len(text)%2!=0:
        text+=str(c)
    return text
def textToBlock(text): 
    block = []
    text = checkTextLen(text, 'x')
    f = True
    r = ""
    for i in text:
        if f:
            r+=str(i)
            f = False
        else:
            r+=str(i)
            block.append(r)
            r=""
            f=True
    return block
def matrisCreate(key, extC):
    chrs = [chr(i) for i in range(97, 123)]
    temps = ""
    temps+=key
    for i in chrs:
        if i != extC:
            temps+=i
    return np.array(list(keyControl(temps))).reshape(5,5)
def findChars(text, matris):
    def findChar(cr, matris):
        for i in range(len(matris)):
            for j in range(len(matris)):
                if matris[i][j] == cr:
                    return [i,j]
    text = list(text)
    vals = [findChar(i,matris) for i in text]
    return vals
def encrypt(text, matris):
    f = True
    vals = findChars(text, matris)
    vals2 = findChars(text, matris)
    temp = ""
    temp2 = ""
    for i in range(0,len(vals)):
        #print(i,vals[i],vals[i][0],vals[i][1])
        if i%2==0:
            if vals2[i][0] == vals2[(i+1)%5][0]:
                vals[i][1] = (vals2[i][1]+1)%5
                vals[(i+1)%5][1] = (vals2[(i+1)%5][1]+1)%5
            elif vals2[i][1] == (vals2[i+1][1]):
                vals[i][0] = vals2[i][0]+1
                vals[(i+1)%5][0] = (vals2[(i+1)%5][0]+1)%5
            else:
                r = vals[i][1]
                vals[i][1] = vals[i+1][1]
                vals[i+1][1] = r
    print(vals2,'\n',vals)
    for i in vals:
        temp+=str(matris[i[0],i[1]])
    for i in vals2:
        temp2+=str(matris[i[0],i[1]])
    return temp2,temp
    
# functions
key = keyControl('endor')
text = list('deneme')
matris = matrisCreate(key,'q')
# general defs
print(matris)
print(encrypt(text, matris))