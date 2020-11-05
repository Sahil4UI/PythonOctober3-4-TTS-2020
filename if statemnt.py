#Conditional Statements :
'''
x = int(input("Enter a number :"))

if x%2 ==0:
    print("Even")
else:
    print("odd")
'''
'''
a = int(input("Enter no 1 :"))
b = int(input("Enter no 2 :"))
c = int(input("enter no 3 :"))

if (a>b and a>c):
    print(f"{a} is greator")
elif (b>c):
    print(f"{b} is greator")
else:
    print(f"{c} is greator")
'''
a = int(input("Enter side 1 :"))
b = int(input("Enter side 2 :"))
c = int(input("enter side 3 :"))

#equilateral /  isoceles/scalene
if (a>b+c and b>c+a and c>a+b):
    if (a==b==c):
        print("Equilateral Traingle")
    elif (a==b or b==c or c==a):
        print("Isoceles Traingle")
    elif (a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==a**2+b**2):
        print("right angled traingle")
    else:
        print("Scalene Triangle")
else:
    print("traingle cannot be formed")


