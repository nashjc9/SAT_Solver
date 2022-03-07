import sys
from cnf import func_to_cnf, and_gate, or_gate, not_gate

def main():
    x = parser()
    print(x)
    if x:
        func_to_cnf(x)
       
        




def parser():
    if len(sys.argv)!=2:
        print("Enter Boolean Function")
        return False
    f = sys.argv[1]
    return f


if __name__ == "__main__":
    main()