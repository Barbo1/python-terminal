import os

help_s = """Usage: ip [OPTION]
shows the ip what is requires

OPTIONS:
    -p ,--private           show the private ip.
    -u ,--public4           show the public ipv4.
    -v ,--public6           show the public ipv6
"""

def ip(avgs, opts, path_real):
    if avgs:
        raise Exception("option '{}' is surplus".format(avgs[0]))
    command_disposable_1 = [x for x, y in opts]
    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        return help_s+"\n"
    command_disposable_1 = command_disposable_1[0]
    file = open(os.path.abspath(os.path.dirname(__file__)+"\\..\\IPs.txt"))
    command_disposable_2 = file.read().splitlines()
    if command_disposable_1 in ("-p", "--private"):
        command_disposable_2 = command_disposable_2[0].split("=")[1]
    if command_disposable_1 in ("-u", "--public"):
        command_disposable_2 = command_disposable_2[1].split("=")[1]
    if command_disposable_1 in ("-v", "--public6"):
        command_disposable_2 = command_disposable_2[2].split("=")[1]
    file.close()
    return command_disposable_2+"\n"