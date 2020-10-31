Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = "Welcome to our python programming class"
>>> x.split(" ")
['Welcome', 'to', 'our', 'python', 'programming', 'class']
>>> x
'Welcome to our python programming class'
>>> x.split("o")
['Welc', 'me t', ' ', 'ur pyth', 'n pr', 'gramming class']
>>> x = "Navya"
>>> len(x)
5
>>> x.center(1)
'Navya'
>>> x.center(5)
'Navya'
>>> x.center(6)
'Navya '
>>> x.center(7)
' Navya '
>>> x.center(10)
'  Navya   '
>>> x.center(20,"*")
'*******Navya********'
>>> x.center(20,"-")
'-------Navya--------'
>>> x
'Navya'
>>> x.zfill(10)
'00000Navya'
>>> x=x.center(20,"*")
>>> x
'*******Navya********'
>>> x.lstrip("*")
'Navya********'
>>> x
'*******Navya********'
>>> x.lstrip('a')
'*******Navya********'
>>> x.rstrip('a')
'*******Navya********'
>>> x.rstrip('*')
'*******Navya'
>>> x
'*******Navya********'
>>> x.strip("*")
'Navya'
>>> x.strip("a")
'*******Navya********'
>>> x="navya"
>>> x.strip('a')
'navy'
>>> x
'navya'
>>> x.startswith('n')
True
>>> x.startswith('z')
False
>>> x.endswith('a')
True
>>> x
'navya'
>>> x.index('v')
2
>>> x.index('n')
0
>>> x.index('a')
1
>>> x.index('a',0)
1
>>> x.index('a',2)
4
>>> x = "python programming"
>>> x.index('p')
0
>>> x.index('p',1)
7
>>> x.find('p')
0
>>> x.find('p',1)
7
>>> x.index('x')
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    x.index('x')
ValueError: substring not found
>>> x.find('x')
-1
>>> #-1 ->value not found
>>> x="Navya"
>>> y="Gosain"
>>> x+y
'NavyaGosain'
>>> x+" "+y
'Navya Gosain'
>>> x
'Navya'
>>> x*5
'NavyaNavyaNavyaNavyaNavya'
>>> #ASCII(American Standard Code for Informtion Interchange) VALUE
>>> #ord & chr
>>> chr(65)#character
'A'
>>> chr(101)
'e'
>>> chr(30)
'\x1e'
>>> chr(40)
'('
>>> ord('a')
97
>>> ord("&")
38
>>> ord("`")
96
>>> #chr->ASCII TO CHARACTER
>>> #ord->CHARACTER TO ASCII
>>> 