import factorial.factorial
import logarithm.logarithm 
import exp_root.exponentiation
import exp_root.root
def validation(txt, i, y):
    while(True):
        x = input(txt)
        try:
            if i == "int":
                x = int(x)
            if i == "float":
                x = float(x)
            if y > 0:
                if x <= 0:
                    raise TypeError
            break
        except ValueError:
            print(f"Your number is not {i}")
        except TypeError:
            print("Write a positive number.")
    return x

def validation1(txt, i, a):
    while(True):
        x = validation(txt, i, a)
        if x != 1:
            break
        else:
            print("The number cant be 1.")
    return x

def main():
    a = input("What function do you want to use? fact, log, lg, ln, exp2, exp3, root2, root3")
    if a == "fact":
        p = validation("Write a number", "int", 3)
        print(factorial.factorial.fact(p))
    elif a == "log":
        p = validation("Write a number", "float", 3)
        y = validation1("Write a number", "float", 3)
        print(logarithm.logarithm.log(y, p))
    elif a == "lg":
        p = validation("Write a number", "float", 3)
        print(logarithm.logarithm.lg(p))
    elif a == "ln":
        p = validation("Write a number", "float", 3)
        print(logarithm.logarithm.ln(p))
    elif a == "exp2":
        p = validation("Write a number", "float", 0)
        print(exp_root.exponentation.exp2(p))
    elif a == "exp3":
        p = validation("Write a number", "float", 0)
        print(exp_root.exponentiation.exp3(p))
    elif a == "root2":
        p = validation("Write a number", "float", 3)
        print(exp_root.root.root2(p))
    elif a == "root3":
        p = validation("Write a number", "float", 0)
        print(exp_root.root.root3(p))
    else:
        print("Write sth normal.")
main()

if __name__ == "main.py":
    main()