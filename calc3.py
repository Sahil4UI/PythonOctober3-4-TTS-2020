def calc(x,opr,y):
    result=x+opr+y
    print(eval(result))

a=input("Enter Number 1:")
b=input("Enter Number 2:")

print("""
Press + for addition
Press - for subtraction
Press * for Multiplication
Press / for division
""")
choice = input("Enter choice")

calc(a,choice,b)
