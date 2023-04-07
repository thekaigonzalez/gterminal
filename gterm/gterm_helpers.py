def get_arg(listf: list, num: int, default = ""):
    if (len(listf) > num): return listf[num]
    else: return default