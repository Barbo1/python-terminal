import stat, os, re

help_s = """Usage: ls [OPTION]...
Shows all the files in the current path

OPTIONS:
    -p ,--privileges        shows the privileges of the file(using UNIX sintax).
    -t ,--type              shows the type of the file.
    -s ,--size              shows the size of the file in bytes.
    -u ,--unities           convert the size of the file to any unity to be can.

NOTES:
    '-u' argument necessarily needs a '-s' argument to can work.
"""

def ls(avgs, opts, path_real): 
    if len(avgs) > 1:
        raise Exception("option {} is surplus".format(avgs[1]))
    command_disposable_1 = [x for x, y in opts]
    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        return help_s
    privileges_b = False
    type_b = False
    size_b = False
    unit_b = False
    for x in command_disposable_1:
        if x in ("-p", "--privileges"):
            privileges_b = True
        if x in ("-t", "--type"):
            type_b = True
        if x in ("-s", "--size"):
            size_b = True
        if x in ("-u", "--unities"):
            if "-s" in command_disposable_1 or "--size" in command_disposable_1:
                unit_b = True 
            else:
                raise Exception("{} argument needs -s or --size to work".format(x))
    if size_b:
        size = []
        for file_2 in os.listdir(path_real):
            path_file_2 = "{}\\{}".format(path_real, file_2)
            size.append(str(os.path.getsize(path_file_2)))
        if not unit_b:
            mayor_size = len(max(size, key=len))
        else:
            mayor_size = 4
    else:
        size = ""
        mayor_size = 0
    mayor_privileges = len(max(os.listdir(path_real), key=len))
    files_2 = os.listdir(path_real)
    command_disposable_2 = ""
    for file_2 in range(len(files_2)):
        path_file_2 = "{}\\{}".format(path_real, files_2[file_2])
        if type_b:
            if os.path.ismount(path_file_2):
                typef = "m "
            elif os.path.isfile(path_file_2):
                typef = "f "
            elif os.path.isdir(path_file_2):
                typef = "d "
        else:
            typef = ""
        if privileges_b:
            privileges = stat.filemode(os.stat(path_file_2)[0])[1:]+" "
        else:
            privileges = ""
        if size_b:
            size = os.path.getsize(path_file_2)
            unit = "b"
            if unit_b:
                while size >= 1024:
                    size /= 1024
                    if unit == "b":
                        unit = "K"
                    elif unit == "K":
                        unit = "M"
                    elif unit == "M":
                        unit == "G"
                if type(size) == float:
                    size = str(size)[:3]
                    h = re.findall(r"\d+.(\d)", size)
                    if not h or int(h[0]) == 0:
                        size = int(float(size))
        else:
            size = ""
            unit = ""
        command_disposable_2 += "{0}{1}{2:{3}}{4:>{5}}{6}\n".format(typef, privileges, files_2[file_2], mayor_privileges+1, "{} ".format(size), mayor_size+1, unit)
    return command_disposable_2
