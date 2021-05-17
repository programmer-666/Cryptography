import math
class RSAn:
    # RSA For Numeric
    def __init__(self, p, q):
        self.prime_1 = p
        self.prime_2 = q
        self.n = p*q
        self.z = (p-1)*(q-1)
        self.__findOpenKey()
        self.__findPrivateKey()
    def __findOpenKey(self):
        i = 2
        while True:
            if math.gcd(i, self.z) == 1:
                self.e = i
                break
            i+=1
    def __findPrivateKey(self):
        i = 1
        while True:
            if (i*self.e)%self.z == 1:
                self.d = i
                break
            i+=1
    def encryptInt(self, x):
        return (x**self.e)%self.n
    def decryptInt(self, x, private):
        return (x**private)%self.n
    
r = RSAn(131, 151)
text = "Lorem"
enc = []
for i in text:
    enc.append(r.encryptInt(ord(i)))
print(enc)

for i in enc:
    print(r.decryptInt(i, r.d))
