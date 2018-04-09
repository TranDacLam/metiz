from Crypto.Cipher import AES
import base64
from Crypto import Random
from django.conf import settings

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class MetizAESCipher:

    def __init__( self ):
        self.key = settings.SECRET_KEY[:32]

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) )

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))


# SECRET_KEY = '2+@8!9c)(s11nt^ox20nkvu7)_wqh6=g(p54jlsjytizbuz(4y'
# cipher = MetizAESCipher(SECRET_KEY[:32])
# encrypted = cipher.encrypt(msg_text)
# decrypted = cipher.decrypt(encrypted)
# print encrypted
# print decrypted