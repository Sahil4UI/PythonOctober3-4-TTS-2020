#print numbers from 1-10
'''
for i in range(5):
    print(i)
#higher-lower->n+1
#lower to high->n-1

for i in range(1,11,3):
    print(i)

for i in range(10,0,-1):
    print(i)
for i in reversed(range(1,11)):
    print(i)
'''
#find the sum of first 10 natural numbers
'''
result = 0
for i in range(1,11):
    result = result+i
print(result)
'''
#find the factorial of a given number
'''
number = int(input("Enter a number : "))
result = 1
for i in range(1,number+1):
    result = result*i
print(result)
'''
#find the sum of digits of number->123->3+2+1=6
'''
number = int(input("Enter a number : "))
result=0

for i in range(len(str(number))):
    rem=number%10
    result = result+rem
    number = number//10
print(result)
'''
#check wether number is armstrong or not?
    
number = int(input("Enter a number : "))
x = number
result=0

for i in range(len(str(number))):
    rem=number%10
    result = result+rem**3
    number = number//10
print(result)

if x==result:
    print(f"{x} is an Amstrong Number")
else:
    print(f"{x} is not an Armstrong Number")

