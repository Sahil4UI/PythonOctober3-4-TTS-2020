#C->F
#F = 9/5*C+32

def TempConv(c):
    return 9/5*c+32
#result=TempConv(30)
x = [30,35,39.5,24,2,1,-10]
'''
for data in x:
    print(TempConv(data))

y = list(map(TempConv,x))
print(y)
'''


def Even(x):
    if x%2==0:
        return True
    else:
        return False
'''
numbers = [1,2,98,5,4,6,7,100,13,12,15,19,90]

result = list(filter(Even,numbers))
print(result)
'''
x = lambda a:True if a%2==0 else False
print(x(12))





#lambda function
x = lambda a,b,c:a+b+c
#print(x(1,2,3))


