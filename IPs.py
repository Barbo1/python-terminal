import os
import re
import socket
import urllib.request

def IPss():
    ip = str(urllib.request.urlopen("http://checkip.dyndns.org").read())
    ip = re.findall(r"\d{3}\.\d{2,3}\.\d{2,3}.\d{2,3}", ip)
    ip_public = ip[0]
    ip_public = "PcIP4="+ip_public

    ip = str(urllib.request.urlopen("https://es.piliapp.com/what-is-my/ipv6/").read())
    ip = re.findall(r"[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{1,4}\:[0-9a-fA-F]{4}", ip)
    ip_private = ip[0]
    ip_private = "PcIP6="+ip_private

    arch = open(os.path.dirname(__file__)+"\\IPs.txt", "+w")
    message = "PvIP4="+socket.gethostbyname(socket.gethostname())+"\n"+ip_public+"\n"+ip_private
    arch.write(message)
    arch.flush()
    arch.close()
