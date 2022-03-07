def func_to_cnf(f):
    a = f.split("+")
    

def and_gate(f,out):
    func = f.split(".")
    return func[0][1:]+" -"+out[1:]+"\n"+func[1][1:]+" -"+out[1:]+"\n"+"-"+func[0][1:]+" -"+func[1][1:]+" "+out[1:]+"\n"

def or_gate(f,out):
    func = f.split("+")
    return "-" + func[0][1:] + " " + out[1:] + "\n" + "-" + func[1][1:] + " " + out[1:] + "\n" + func[0][1:] + " " + func[1][1:] + " -" + out[1:] + "\n"
    
def not_gate(f, out):
    func = f.split("~")
    return "-" + func[1][1:] + " -" + out[1:] + "\n" + func[1][1:] + " " + out[1:] + "\n"


