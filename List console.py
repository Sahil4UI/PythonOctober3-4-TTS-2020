Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #List
>>> #Python Data Collection
>>> #List->list is a mutable python data collection
>>> #mutable -> which can be changed -> create,update,delete
>>> x = [1,2,6.8,9.8,True,False,"Navya"]
>>> type(x)
<class 'list'>
>>> x[0]
1
>>> x[1]
2
>>> x[3]
9.8
>>> x[-1]
'Navya'
>>> x = [1,2,3,[4,5,6,[7,8,9]]]
>>> x[3][3][1]
8
>>> x = [1,2,[3,4],5,[6,7,8,9,[10,11,12,"Navya",13,14]]]
>>> x[2]
[3, 4]
>>> x[2][0]
3
>>> x[4]
[6, 7, 8, 9, [10, 11, 12, 'Navya', 13, 14]]
>>> x[4][4]
[10, 11, 12, 'Navya', 13, 14]
>>> x[4][4][3]
'Navya'
>>> #slicing
>>> x=[1,2,3,4,5,897,5676,54543]
>>> x[2,7]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x[2,7]
TypeError: list indices must be integers or slices, not tuple
>>> x[2:7]
[3, 4, 5, 897, 5676]
>>> x[::-1]
[54543, 5676, 897, 5, 4, 3, 2, 1]
>>> #list methods
>>> x=[]
>>> x.append("navya")
>>> x
['navya']
>>> x.append(1)
>>> x
['navya', 1]
>>> x.append(2)
>>> x
['navya', 1, 2]
>>> x.insert(0,"hi")
>>> x
['hi', 'navya', 1, 2]
>>> x
['hi', 'navya', 1, 2]
>>> x[-1]=10000
>>> x
['hi', 'navya', 1, 10000]
>>> x
['hi', 'navya', 1, 10000]
>>> x.pop()
10000
>>> x
['hi', 'navya', 1]
>>> x.pop(0)
'hi'
>>> x.remove("navya")
>>> x
[1]
>>> x=[1,1,1,1]
>>> x.remove(1)
>>> x
[1, 1, 1]
>>> x.rem
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x.rem
AttributeError: 'list' object has no attribute 'rem'
>>> x.remove(1,2)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    x.remove(1,2)
TypeError: list.remove() takes exactly one argument (2 given)
>>> x
[1, 1, 1]
>>> x.remove(1)
>>> x
[1, 1]
>>> del x[0]