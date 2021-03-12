# Caesar Cipher
# With ASCII Table
# suhaarslan
import sys
t, T, x = [i for i in range(97, 123)], [i for i in range(65, 91)], 2
while x < len(sys.argv):
    if sys.argv[1] == 'e':
        for i in sys.argv[x]:
            if (ord(i) in t or ord(i) in T):
                c = ((ord(i)+3)%123)
                if c < 97:
                    c = c+97
                print(chr(c), end='')
    elif sys.argv[1] == 'd':
        for i in sys.argv[x]:
            if (ord(i) in t or ord(i) in T):
                c = ((ord(i)-3)%123)
                if c < 97:
                    c = c+26
                print(chr(c), end='')
    x = x+1