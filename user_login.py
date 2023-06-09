import base64
import os 
from Crypto.Cipher import AES

#--------------------
#--Logging Function--
#--------------------

def start(user, password):
    file = open(os.path.dirname(__file__)+"/users.txt")
    for x in file.read().splitlines():
        line = x.split(":")
        if line[0] == user:
            passwd = line[1].encode('utf-8')
            cipher = AES.new(b'0123456789012345')
            passwd = cipher.decrypt(base64.b64decode(passwd))
            passwd = passwd.decode('utf-8').strip()
            if password == passwd:
                file.close()
                return True
    file.close()
    return False