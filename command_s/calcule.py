import re
from math import e, pi, gamma, log, tan, sin, cos, sqrt

simbols = (["π", "pi"], ["^", "**"], ["sen", "sin"], ["√", "sqrt"])
helps = """Usage: calcule [OPTION] [EXPRESSION]
calcule the [EXPRESSION] and return the outcome in all the real numbers

OPTIONS:
    -h, --help          show this help.

[EXPRESSION]:
    whit this command you can calculate:
        --> sqrt(x) (square root), sen(x), cos(x), tan(x), log(x)
        --> + (sum), - (sustraction), * (multiplication), / (division), ! (factiorial of any real number)
        --> Euler constant (e), Pi constant (π or pi)
"""

def calcule(avgs, opts, _):

    command_disposable_1 = [x for x, y in opts]

    if "-h" in command_disposable_1 or "--help" in command_disposable_1:
        print()

    operation = ""
    for x in range(len(avgs)):
        operation += avgs[x]

    try:
        if len(operation):    
            operation = operation.replace(" ", "")
            if not re.search(r"[^\da-z√π\!\+\-\/\*\(\)\^\,\√\°]", operation):
                if re.search(r"\(\)", operation):
                    step = 0
                    for x in operation:
                        if x == "(":
                            step += 1
                        elif x == ")":
                            step -= 1
                        if step == -1:
                            raise Exception()
                    if step != 0:
                        raise Exception()
                for x, y in simbols:
                    operation = operation.replace(x, y)
                return str(calcule_2(operation))+"\n"
        return 0
    except ValueError as err:
        return str(err)+"\n"
    except Exception:
        return "Invalid syntax\n"

def calcule_2(operation):
    #_Recursive_
    if re.search(r"[^a-z]\(\)", operation):
        step_1 = re.sub(r"[^a-z]\((.+)\)", "{}", operation)
        step_2 = re.findall(r"[^a-z]\((.+)\)", operation)
        for x in step_2:
            y = x
            if y.find("("):
                y = calcule_2(y)
            step_1 = step_1.format(y)  
        operation = step_1

    #_Factorial(with gamma)_
    if operation.find("!"):
        if re.search(r"[^\d\)]\!", operation) or re.search(r"\![a-z\d]", operation):
            raise Exception()
        if re.search(r"\d+\!", operation):
            step_2 = re.findall(r"(\d+)\!", operation)
            step_1 = re.sub(r"\d+\!", "{}", operation)
            operation = step_1.format(*[gamma(eval(n)+1) for n in step_2])
        if re.search(r"\)\!", operation):
            step_2 = re.findall(r"([a-z].+)\!", operation)
            step_1 = re.sub(r"[a-z].+\!", "{}", operation)
            operation = step_1.format(*[gamma(eval(n)+1) for n in step_2])

    operation = float(eval(operation))
    
    if operation.is_integer(): 
        return int(operation)
    else: 
        return operation