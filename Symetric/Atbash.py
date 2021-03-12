# Atbash Cipher
# With ASCII Table
# suhaarslan
import sys
def encrypt(chr):
    e = ((123-1)*chr+(123-1))%123
    if chr < 97:
        return e+65
    elif chr > 90:
        return e+97
x = 1
while x < len(sys.argv):
    for i in sys.argv[x]:
        if ord(i) in [i for i in range(97, 123)] or ord(i) in [i for i in range(65, 91)]:
            print(chr(encrypt(ord(i))), end='')
    x=x+1
