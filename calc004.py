#calculator-add,sub,mul,div
def add(a,b):
    print(a+b)

def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    if b!=0:
        print(a/b)
    else:
        print("Zerro Division Error")
        
x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))

print("""
Press + for addition
Press -  for Subtraction
Press * for Multiplication
Press / for division
""")

choice = input("Enter choice : ")
d={"+":add,"-":sub,"*":mul,"/":div}
d.get(choice)(x,y)
