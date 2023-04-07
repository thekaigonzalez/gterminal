import colorama

def print_with_name(text: str, shellname: str):
    print(colorama.Fore.YELLOW + colorama.Style.BRIGHT + shellname + colorama.Style.RESET_ALL + ": " +
          text)
    
def print_error(text: str, shellname: str):
    print(colorama.Fore.RED + colorama.Style.BRIGHT + "error" + colorama.Style.RESET_ALL + ": " +
          text)