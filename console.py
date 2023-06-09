#--------------------------
#--Starting Configuration--
#--------------------------
import getpass, os, time, threading, re, sys, colorama
import IPs, interpreter, user_login

path_current = "C:\\Users\\joaqu\\OneDrive\\Escritorio"
tread_1 = threading.Thread(target=IPs.IPss)
colorama.init()
error = interpreter.error

def commandRespose(command):
    if len(command):
        command_disposable_1 = re.findall(r"\$\(.+\)", command)
        command_disposable_2 = re.sub(r"\$\(.+\)", "{}", command)
        for x in command_disposable_1:
            y = x[2:len(x)-1]
            if re.search(r"\$\(.+\)", y):
                y = commandRespose(y)
            command_disposable_2 = command_disposable_2.format(commandRespose2(y))
        return commandRespose2(command_disposable_2)
    else:
        return ""

def commandRespose2(command):
    global path_current
    try:
        command_primary, opts, avgs = interpreter.Separe(command)

        #---------E-X-I-T---------
        if command_primary == "exit":
            if avgs:
                raise Exception("option '{}' is surplus".format(avgs[0]))
            print("goodbye!")
            sys.exit(0)

        #---------P-W-D---------
        elif command_primary == "pwd":
            return path_current+"\n"

        #---------C-D---------
        elif command_primary == "cd":
            if len(avgs) > 1:
                raise Exception("option '{}' is surplus".format(avgs[1]))
            if re.search(r"\A[cC]:[\\\/]", avgs[0]):
                if os.path.exists(avgs[0]):
                    path_current = avgs[0]
                else:
                    raise Exception("non-exists path")
            else:
                path_new = os.path.abspath(path_current+avgs[0])
                if os.path.exists(path_new):
                    path_current = path_new
                else:
                    raise Exception("non-exists path")
        else :
            return interpreter.console(command, path_current)
    except Exception as err:
        return error+str(err)+"\n"

#-----------------
#--Start Program--
#-----------------
print(colorama.Fore.YELLOW, end="")
print("user: ", end="")
print(colorama.Fore.WHITE, end="")
user = str(input())
print(colorama.Fore.YELLOW, end="")
password = getpass.getpass()
print(colorama.Fore.WHITE, end="")
if user_login.start(user, password):
    tread_1.start()
    print("\n###################"+"#"*len(user))
    time.sleep(0.5)
    print("####|"+colorama.Fore.GREEN+"welcome "+user+"!"+colorama.Fore.WHITE+"|####")
    time.sleep(0.5)
    print("###################"+"#"*len(user), end="\n\n")
    time.sleep(1)
    while True:
        print(colorama.Fore.GREEN, end="")
        print("<{} | {}> ".format(time.strftime("%H:%M:%S", time.localtime()), user), end="")
        print(colorama.Fore.WHITE, end="")
        command = str(input())
        respose = commandRespose(command)
        if (respose == None):
            print("", end="")
        else:
            print(respose, end="")
else:
    print()
    print(error+"the credentials not coincide, press enter...")

os.system("PAUSE>nul")
sys.exit(0)
  