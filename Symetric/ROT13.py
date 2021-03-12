# ROT13 Cipher
# With ASCII Table
# suhaarslan
import sys
x, TABLE = 1, [[i for i in range(97, 123)], [i for i in range(65, 91)]]
while x < len(sys.argv):
    for i in sys.argv[x]:
        if (ord(i) in TABLE[0] or ord(i) in TABLE[1]):
            c = ((ord(i)+13)%123)
            if c < 97:
                c = c+97
            print(chr(c), end='')
    x = x+1