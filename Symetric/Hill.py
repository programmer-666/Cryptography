# Hill Cipher
# With ASCII Table
# suhaarslan
import sys
import numpy as np
# 115 97 109 115 117 110 -> samsun
# 18 0 12 18 20 13 -> samsun
# benzersiz asallar: 9091 9901 333667 909091

alphabetAscii = np.array([i for i in range(97,123)])
alphabet = np.array([i-97 for i in range(97,123)])
createKey = lambda a,b,c,d: np.array([[int(a),int(b)],[int(c),int(d)]])
def textControl(text):
    if len(text)%2!=0:
        return text+'z' # changable
    else:
        return text
def textCutter(text):
    return [text[2*i-2:2*i] for i in range(int(len(text)/2)+1)][1:]
def textConverter(text):
    text = textCutter(textControl(text))
    tmp = []
    main = []
    for i in text:
        for j in range(len(i)):
            if j < 2:
                tmp.append(ord(i[j])-97)
                if j == 1:
                    main.append(tmp)
                    tmp = []
    return main
def encrypt(text, keys):
    keys = np.array(keys)
    dataList = np.array(textConverter(text))
    e = []
    for i in dataList:
        e.append((np.matrix('{} {}; {} {}'.format(keys[0][0],keys[0][1],keys[1][0],keys[1][1]))*np.matrix('{};{}'.format(i[0],i[1]))%26+97).tolist())
    for i in e:
        print(chr(i[0][0]), chr(i[1][0]), end='', sep='')
def determinant(matrixKey):
    return ((matrixKey[0][0]*matrixKey[1][1])-(matrixKey[0][1]*matrixKey[1][0]))**-1
def adjoint(matrixKey):
    return [ [matrixKey[1][1], -matrixKey[0][1]], [-matrixKey[1][0], matrixKey[0][0]] ]
def decrypt(text, keys):
    revMatrixKey = (determinant(keys)*np.array(adjoint(keys))).tolist()
    dataList = np.array(textConverter(text)).tolist()
    main = []
    for i in dataList:
        main.append([[ ((revMatrixKey[0][0]*i[0])+(revMatrixKey[0][1]*i[1]))%26 ],[ ((revMatrixKey[1][0]*i[0])+(revMatrixKey[1][1]*i[1]))%26 ]][0][0]+97)
        main.append([[ ((revMatrixKey[0][0]*i[0])+(revMatrixKey[0][1]*i[1]))%26 ],[ ((revMatrixKey[1][0]*i[0])+(revMatrixKey[1][1]*i[1]))%26 ]][1][0]+97)
    
    for i in main:
        print(chr(int(i)), end='')
# DEFs
keys = [[int(sys.argv[1]),int(sys.argv[2])],[int(sys.argv[3]),int(sys.argv[4])]]
text = ""
for i in range(len(sys.argv)):
    if i > 5:
        text+=sys.argv[i]
if sys.argv[5] == 'e':
    encrypt(text, keys)
elif sys.argv[5] == 'd':
    decrypt(text, keys)