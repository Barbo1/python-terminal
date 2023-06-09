import os, re

help_s = """Usage: find [OPTION]...
Find a file(s) in the system or in a part to this, showing the path.

OPTIONS:
    -e:, --extension=       specidied extencion(s) of file(s) to find. (finder).
    -w:, --word=            search word in the name of file(s) to find(without consider the
                            extension). (finder).
    -S:, --start=           specified word which the file start. (finder).
    -F:, --finish=          specified word which the file end. (finder).
    -x , --exclusive        find only if name is perfectly equal to the specified.
    -p:, --path=            specified base path to being to find the file.
    -r , --relative         show relative path of the finded file.
    -h , --help             show this help.   

EXEMPLES:
    | find -e txt,exe | shows files who have 'txt' or 'exe' extension in the current file.  
    | find --word=i_like_sweets -p C:/path | shows files named 'i_like_sweets' in 'C:/path'.
    | find -S i_like -r | shows the files who name start with 'i_like' and show him relative
                           path.

NOTES:
    Find need a finder argument like '-e' or '-n' to find anything.
    If '-p' is no specified, the file is finded in the current path.
    '-x' argument necessarily needs a '-n' argument to can work, and only works when this
      argument is present. 
"""

def find(avgs, opts, path_real):
    if avgs:
        raise Exception("option {} is surplus".format(avgs[0]))
    if not len(opts):
        raise Exception("find command needs an argument")
    command_disposable_1 = [x for x, y in opts]
    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        return help_s
    command_disposable_2 = [y for x, y in opts]
    finder = True
    extensions_1 = []
    extensions_2 = []
    word = ""
    S_word = ""
    F_word = ""
    path_1 = ""
    exclusive = False
    relative = False
    for x in command_disposable_1:
        if x in ("-e", "--extension"):
            extensions_1 = command_disposable_2[command_disposable_1.index(x)]
            for y in extensions_1.split(","):
                extensions_2.append(y)    
            finder = False
        if x in ("-w", "--word"):
            word = command_disposable_2[command_disposable_1.index(x)]
            finder = False
        if x in ("-p", "--path"):
            path_1 = command_disposable_2[command_disposable_1.index(x)]
            if not re.search(r"\A[cC]:[\\\/]", path_1):
                path_1 = os.path.abspath(path_real+path_1)
            if not os.path.exists(path_1):
                raise Exception("{} is non-exists path".format(path_1))
        if x in ("-r", "--relative"):
            relative = True
        if x in ("-x", "--exclusive"):
            if "-w" in command_disposable_1 or "--word" in command_disposable_1:
                exclusive = True
            else:
                raise Exception("{} argument needs --word or -w argument to work".format(x))
        if x in ("-S", "--start"):
            S_word = command_disposable_2[command_disposable_1.index(x)]
            finder = False
        if x in ("-F", "--finish"):
            F_word = command_disposable_2[command_disposable_1.index(x)]
            finder = False
    if finder:
        raise Exception("find command needs a finder argument")
    if not len(path_1):
        path_1 = path_real
    command_disposable_1 = os.listdir(path_1)
    path_2 = []
    for x in command_disposable_1:
        if not os.path.isdir(os.path.join(path_1, x)):
            path_2.append(x)
    command_disposable_2 = ""
    command_disposable_3 = []
    for file_1 in command_disposable_1:
        for dat1, _, dat3 in os.walk(os.path.join(path_1, file_1)):
            for dat4 in dat3:
                command_disposable_3.append(os.path.join(dat1, dat4))
    for dat1 in path_2:
        command_disposable_3.append(os.path.join(path_1, dat1))
    for file_2 in command_disposable_3:
        dat = file_2[file_2.rfind("\\")+1:]
        datE = dat[dat.find(".")+1:] 
        dat1 = dat[:dat.find(".")]
        ext_1 = False
        nam_1 = False
        nam_2 = False
        nam_3 = False
        if len(extensions_2):
            for ex in extensions_2:        
                if datE == ex:
                    ext_1 = True
                    break
        else:
            ext_1 = True
        if len(word):
            try:
                if exclusive:
                    if dat1[:dat1.find(".")] == word:
                        nam_1 = True
                elif dat1.find(word) + 1:
                    nam_1 = True
            except ValueError:
                if dat1 == word:
                    nam_1 = True
        else:
            nam_1 = True 
        if len(S_word):
            if dat1.startswith(S_word):
                nam_2 = True
        else:
            nam_2 = True
        if len(F_word):
            if dat1.endswith(F_word):
                nam_3 = True
        else:
            nam_3 = True
        if nam_1 and ext_1 and nam_2 and nam_3:
            if relative and len(path_1):
                path_3 = re.split(r"[\\\/]", path_real)
                path_4 = re.split(r"[\\\/]", file_2)
                path_5 = ""
                if len(path_3) > len(path_4):
                    len_s = len(path_4)
                else:
                    len_s = len(path_3)
                for _ in range(len_s):
                    if path_3[0].lower() == path_4[0].lower():
                        path_4.pop(0)
                        path_3.pop(0)
                    else:
                        break
                for _ in range(len(path_3)):
                    path_5 += "\\.." 
                for pa in path_4:
                    path_5 += "\\"+pa
                command_disposable_2 += path_5
            elif relative:
                command_disposable_2 += "."+file_2[len(path_real):]
            else:
                command_disposable_2 += file_2
            command_disposable_2 += "\n"
    return command_disposable_2
