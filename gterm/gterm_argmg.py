import gterm.gterm_helpers as gh

class ArgumentManage:
    def __init__(self, arglist: list) -> None:
        self.args = arglist
    def arg_length(self):
        return len(self.args)
    def arg(self, pos):
        return gh.get_arg(self.args, pos, None)