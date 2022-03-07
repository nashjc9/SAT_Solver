def func_to_cnf(f):
    a = f.split("+")
    

def var_count(f):
    a = f.split("+")
    vars = []
    large = -1
    for x in a:
        b = x.split(".")
        for i in b:
            if i.find("~") != -1:
                i = i[1:]
            if i not in vars:
                vars.append(i)
    for k in vars:
        if int(k[1:]) > large:
            large = int(k[1:])
    return large + 1

def and_gate(f,out):
    func = f.split(".")
    return func[0][1:]+" -"+out[1:]+"\n"+func[1][1:]+" -"+out[1:]+"\n"+"-"+func[0][1:]+" -"+func[1][1:]+" "+out[1:]+"\n"

def or_gate(f,out):
    func = f.split("+")
    return "-" + func[0][1:] + " " + out[1:] + "\n" + "-" + func[1][1:] + " " + out[1:] + "\n" + func[0][1:] + " " + func[1][1:] + " -" + out[1:] + "\n"
    
def not_gate(f, out):
    func = f.split("~")
    return "-" + func[1][1:] + " -" + out[1:] + "\n" + func[1][1:] + " " + out[1:] + "\n"


