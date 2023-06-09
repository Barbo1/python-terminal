import time

help_s = ""

def date(avgs, opts, _):
    command_disposable_1 = [x for x, y in opts]
    command_disposable_2 = [y for x, y in opts]
    if avgs:
        raise Exception("option {} is surplus".format(avgs[0]))
    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        return "ayuda"+"\n"
    try:
        try:
            option = command_disposable_2[command_disposable_1.index("-l")]
        except ValueError:
            option = command_disposable_2[command_disposable_1.index("--localization")]
        if option == "local":
            option = time.localtime()
        elif option == "greenwich":
            option = time.gmtime()
        else:
            return "{} not is a recognized localization".format(option)+"\n"
    except ValueError:
        option = time.localtime()
    try:
        try:
            option_1 = command_disposable_2[command_disposable_1.index("-s")]
        except ValueError:
            option_1 = command_disposable_2[command_disposable_1.index("--structure")]
        return time.strftime(option_1, option)+"\n"
    except ValueError:
        option_1 = "%a__%Y/%m/%d__%H:%M:%S"
        return time.strftime(option_1.replace("_", " "), option)+"\n"