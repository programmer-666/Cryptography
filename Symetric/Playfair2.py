# Playfair Cipher
# With ASCII Table
# suhaarslan
import numpy as np
import sys

def findChar(cr, matris):
    for i in range(len(matris)):
        for j in range(len(matris)):
            if matris[i][j] == cr:
                return [i,j]
def findChars(text, matris):
    text = list(text)
    vals = [findChar(i,matris) for i in text]
    return vals
def keyControl(text):
    temp = set()
    temps = ""
    for i in text:
        if i not in temp and i not in temps:
            temp.add(i)
            temps+=i
    return temps
def findTextByBlock(block, matris):
    r = ""
    for i in block:
        r+=matris[i[0],i[1]]
    return r
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
def encrypt(text,matris):
    venc = []
    i = 0
    """
    aynı satır ise sütunlar +1
    aynı sütun ise satır +1
    farklı sütun ve satır ise sütunlar eşitlenir
    """
    while i < len(text):
        if i%2!=1:
            if text[i][0] == (text[(i+1)%5][0])%5:
                venc.append([(text[i][0])%5,(text[i][1]+1)%5])
                venc.append([(text[(i+1)%5][0])%5,(text[(i+1)%5][1]+1)%5])
            if text[i][1] == (text[(i+1)%5][1])%5:
                venc.append([(text[i][0]+1)%5,(text[i][1])%5])
                venc.append([(text[(i+1)][0]+1)%5,(text[(i+1)][1]%5)])
            if text[i][1] != (text[(i+1)%5][1])%5 and text[i][0] != (text[(i+1)%5][0])%5:
                venc.append([text[i][0],(text[(i+1)][1])%5])
                venc.append([(text[(i+1)][0])%5,(text[i][1])%5])
        i+=1
    #print(text)
    #print(venc)
    temp = ""
    for i in venc:
        temp+=str(matris[i[0],i[1]])
    return(temp)
key = 'endor'
matris = matrisCreate(key, 'q')
text = findChars('hayrix', matris)
#print(matris)
print(encrypt(text,matris))

# HAVE SOME ISSUES