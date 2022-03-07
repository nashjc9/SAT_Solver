import sys
from cnf import and_gate, or_gate, not_gate

def main():
    x = parser()
    print(x)
    if x:
        k = not_gate(x, "x2")
        print(k)
        




def parser():
    if len(sys.argv)!=2:
        print("Enter Boolean Function")
        return False
    f = sys.argv[1]
    return f


if __name__ == "__main__":
    main()