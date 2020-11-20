"""
A
BC
DEF
GHIJ
JKLMN
"""

x = ord("A")
for i in range(1,6):
    for j in range(i):
        print(chr(x),end="")
        x=x+1
    print()
