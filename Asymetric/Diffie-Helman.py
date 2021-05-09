# suhaarslan.com
from random import randbytes
class Client:
    def keyControl(self, x):
        # takes first 32 bytes
        return x[:self.__byte]
    # Control Funtions
    def __init__(self, a, b):
        # a, b 32 bytes public key / a, b string
        self.__byte = 128
        self.public_key_1 = bytes(self.keyControl(a.encode()))
        self.public_key_2 = bytes(self.keyControl(b.encode()))
        self.__createPrivateKey()
    def __createPrivateKey(self):
        # private key 32 bytes
        self.__private_key = randbytes(self.__byte)
    def getPrivateKey(self):
        return self.__private_key
    # Key Functions
    def Make(self, onc = 0):
        if onc == 0:
            self.local = hex((int(self.public_key_1.hex(), 16)^int(self.__private_key.hex(), 16))&int(self.public_key_2.hex(), 16)-1)
            return self.local
        else:
            self.l_onc = hex((int(onc, 16)^int(self.__private_key.hex(), 16))&int(self.public_key_2.hex(), 16)-1)
            return self.l_onc
    # Calcs

public1 = """Ua){jk2#N^=yShan.]}:+#'TZL6s!F!WG8A=&-ML{gJ(B>5$xC=X/]H'[6gyNn6*B`4:UB,~)et[">$9:d#9F6nQjcp,!pm5FPP(=VGTXe6U=Ypta&JjrRfE}"/j~g"/"""
public2 = """rt$}Lu9Gdsu:^&>8[2>waMC}g+q[=g~KJ=ymp5"`=:&M-XUDQ&SB3Yc_B-V/5b@_kt(:[=r`98C(r2rE@wA#c_T8k+D>EMqrG5$\_xUaDx)Tr4_J"b{vud+X<9'N<:sB"""

alpha = Client(public1, public2)
alphaCalc = alpha.Make()

beta = Client(public1, public2)
betaCalc = beta.Make()

print(alpha.Make(onc=betaCalc))
print(beta.Make(onc=alphaCalc))