regex_replace = (("\\n", "\n"), ("\\t", "\t"), ("\\v", "\v"), ("\\b", "\b"), ("\\\"", "\""))

""

def echo(avgs, opts, _):
    command_disposable_1 = [x for x, y in opts]
    if len(avgs) > 1:
        raise Exception("option {} is surplus".format(avgs[1]))
    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        return "ayuda"+"\n"
    if len(avgs) == 0:
        return "\n"
    respose = avgs[0]
    if "-r" in command_disposable_1 or "--regex" in command_disposable_1:
        for x, y in regex_replace:
            respose = respose.replace(x, y)
    return respose+"\n"