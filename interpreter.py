#--------------------------
#--Starting Configuration--
#--------------------------
import getopt, os, re, colorama
import command_s

commands_file = open(os.path.dirname(__file__)+"/commands.txt", "r")
commands = commands_file.readlines()
commands_file.close()
error = colorama.Fore.RED+"[ERROR]: "+colorama.Fore.WHITE
danger = colorama.Fore.YELLOW+"[DANGER]: "+colorama.Fore.WHITE
doublequotes = re.compile(r"\".+\s.+\"")

#-----------------------
#--Descompress Command--
#-----------------------

def Separe(com):
    command_disposable_2 = com.rstrip()
    command_1 = []
    canSplit = False
    step_1 = 0
    step_2 = 0
    while step_1 < len(command_disposable_2):
        if command_disposable_2[step_1] == "\"":
            if canSplit: 
                canSplit = False
            else: 
                command_1.append(command_disposable_2[step_2:step_1])
                step_2 = step_1 + 1
                canSplit = True
        if command_disposable_2[step_1] == " " and not canSplit:
            command_1.append(command_disposable_2[step_2:step_1])
            step_2 = step_1 + 1
        if step_1 == len(command_disposable_2) - 1:
            command_1.append(command_disposable_2[step_2:step_1+1])
        step_1 += 1
    if canSplit:
        raise Exception("too many doble quotes")
    step_1 = 0
    while step_1 < len(command_1):
        if command_1[step_1] == "":
            command_1.pop(step_1)
        else:
            step_1+=1
    for x in range(len(command_1)):
        if command_1[x].startswith("\""):
            command_1[x] = command_1[x][1:]
        if command_1[x].endswith("\""):
            command_1[x] = command_1[x][:len(command_1[x])-1]
    command_primary = command_1[0]
    command_disposable_1 = 0
    for x in commands:
        if re.search("com="+command_primary, x):
            command_disposable_1 = eval(x.split("|")[1])
            command_disposable_2 = eval(x.split("|")[2])
            break
    if command_disposable_1 == 0:
        raise Exception("command {} not recognized".format(command_primary))
    command_secondary = command_1[1:]
    opts, avgs = getopt.getopt(command_secondary, command_disposable_1, command_disposable_2)

    return (command_primary, opts, avgs)

#-----------------------
#--Interprete Function--
#-----------------------
def console(command, path_real):   
    if not len(command):
        return ""

    command_disposable_1 = Separe(command)
    if type(command_disposable_1) == str:
        return command_disposable_1
    command_primary, opts, avgs = command_disposable_1

    #
    #--Command Selection--
    #
    
    try:
        return eval("command_s.{0}(avgs, opts, path_real)".format(command_primary))
    except AttributeError:
        return danger+"the comand is recognized but no have implemented a function\n"
    except Exception as err:
        return error+str(err)+"\n"