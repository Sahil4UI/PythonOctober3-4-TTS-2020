'''
for i in range(1,11):
    print(i)
'''
'''
x = 1
while x<=10:
    print(x)
    x+=1
x= int(input("Enter a number : "))
i=2
prime = 0
while x>=i:
    if x%2==0:
        prime=0
        break
    else:
        prime=1
    i+=1

if prime==0:
    print("Not Prime")
elif prime==1:
    print("prime")
'''
#find the sum of digits of number using while loop
'''
x= int(input("Enter a number : "))
result=0
while x>0:
    rem=x%10
    result+=rem
    x=x//10

print(result)    
'''
#find the hcf of two number
a=250
b=150
if a>b:
    small=b
else:
    small=a

i=1
while i<=small:
    if (a%i==0) and (b%i==0):
        gcd=i
    i+=1
print(gcd)
    
