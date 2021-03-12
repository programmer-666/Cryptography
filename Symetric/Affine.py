# Affine Cipher
# With ASCII Table
# suhaarslan
import sys
keys = (15,21)
def encrypt(chr):
    global keys
    formula = lambda a,b,c,m:(a*(c-m)+b)%26+m
    if chr < 97:
        return formula(keys[0],keys[1],chr,65)
    elif chr > 90:
        return formula(keys[0],keys[1],chr,97)
def decrypt(chr):
    global keys
    z = 0
    formula = lambda z,y,b,m: z*((y-m)-b)%26+m
    # a^-1 
    while (keys[0]*z)%26 != 1:
        z=z+1
    if chr < 97:
        return formula(z, chr, keys[1], 65)
    elif chr > 90:
        return formula(z, chr, keys[1], 97)
x = 2
while x < len(sys.argv):
    if sys.argv[1] == 'e':
        for i in sys.argv[x]:
            if ord(i) in [i for i in range(97, 123)] or ord(i) in [i for i in range(65, 91)]:
                print(chr(encrypt(ord(i))), end='')
    elif sys.argv[1] == 'd':
        for i in sys.argv[x]:
            if ord(i) in [i for i in range(97, 123)] or ord(i) in [i for i in range(65, 91)]:
                print(chr(decrypt(ord(i))), end='')
    x=x+1

