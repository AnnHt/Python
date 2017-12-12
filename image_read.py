
class f_i:
    fu = ""
    ins = ""

    def __init__(self, fu, ins):
        if fu != "" and ins != "":
            self.fu = fu
            self.ins = ins


tp = f_i("A", "B")

print(tp.fu)

