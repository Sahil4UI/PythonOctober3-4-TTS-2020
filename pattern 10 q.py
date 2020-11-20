"""
1
10
101
1010
10101


for i in range(1,6):
    for j in range(1,i+1):
        print(j%2 ,end="")
    print()

1
01
010
1010
10101
"""
x=0
for i in range(1,6):
    for j in range(i):
        x+=1
        if x%2==0:
            print(0,end="")
        else:
            print(1,end="")
    print()
