#basic Calc-add,sub,mul,div
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    if y==0:
        print("Zero Divison Error")
    else:
        return x/y

def main():
    a = float(input("Enter Number 1 : "))
    b = float(input("Enter Number 2 : "))
    print("""
    Press + for Addition
    Press - for Subtraction
    Press * for Multiplication
    Press / for Division
    """)
    choice = input("Enter your choice : ")
    
    if choice=="+":
        print(add(a,b))
    elif choice == "-":
        print(sub(a,b))
    elif choice == "*":
        print(mul(a,b))
    elif choice == "/":
        print(div(a,b))
    else:print("invalid Choice")

main()
    



