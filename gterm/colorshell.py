import colorama


def print_with_name(text: str, shellname: str):
    print(colorama.Fore.BLUE + shellname + colorama.Style.RESET_ALL + ": " +
          text)
