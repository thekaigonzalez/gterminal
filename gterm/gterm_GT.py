# the GTerm language

"""
code examples:

# nice
define a "Goodbye"
define s "Hello, world"
define b %a

"""

# simple language designed for the end user to make simple calculations

from bashlex import split

parse = (lambda text: 
         list(split(text)))

"""

def get_arg(listf: list, num: int, default = ""):
    if (len(listf) > num): return listf[num]
    else: return default
    
"""
class Arguments:
    def __init__(self, argv: list[str]) -> None:
        self.args = argv
    def at(self, pos: int, conv: type = str, default = None):
        if (len(self.args) > pos): return conv(self.args[pos])
        else: return default

def variablize(code: str, vars: dict):
    if (vars.get(code[1:]) == None): return "none"
    return vars.get(code[1:])

def printFunc(args: Arguments, variables: dict):
    print(args.at(0, str, ""))

def defineFunc(args: Arguments, variables: dict):
    variables[args.at(0, str)] = args.at(1, str)

glob_funcs = {
    "print": printFunc,
    "define": defineFunc
}

def runGTM(code: str, var: dict):
    state = 0

    if not (code.endswith("\n")):
        code = code + "\n"
    
    func = ""
    args = []

    temp = ""

    token: str
    i = 0

    for index, token in enumerate(parse(code)):
        L = len(args)
        if (token.startswith("$")):
            temp = variablize(token, var)
        elif (token == '\n'):
            if (len(args) >0):
                func = args.pop(0)
                if (glob_funcs.get(func) == None):
                    print("error: function does not exist")
                    break
                glob_funcs[func](Arguments(args), var)
                
                temp = ""
                args = []
                func = ""
        else:
            temp = token
        
        if (len(temp.strip()) > 0):
            args.append(temp)
