import os

#--------------------
#--Logging Function--
#--------------------

def start(user, password):
    file = open(os.path.dirname(__file__)+"/users.txt")
    for x in file.read().splitlines():
        lines = x.split(":")
        if lines[0] == user and password == lines[1]:
            file.close()
            return True
    file.close()
    return False