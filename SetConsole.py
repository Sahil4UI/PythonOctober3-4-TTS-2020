Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #SET -python's unordered Data Collection
>>> set1 = {'a','b','c','d','e','f'}
>>> set1
{'f', 'c', 'b', 'a', 'd', 'e'}
>>> set1 = {}
>>> type(set1)
<class 'dict'>
>>> set1 = set()
>>> #empty set
>>> set1
set()
>>> set1.add('a')
>>> set1
{'a'}
>>> set1.add('b')
>>> set1
{'b', 'a'}
>>> set1.add('c')
>>> set1
{'b', 'a', 'c'}
>>> set1.discard('a')
>>> set1
{'b', 'c'}
>>> set1.discard('b')
>>> set1
{'c'}
>>> set1
{'c'}
>>> set1={1,2,3}
>>> set2={5,6,7}
>>> set1.update(set2)
>>> set1
{1, 2, 3, 5, 6, 7}
>>> x={1,1,1,2,5,6,6,6}
>>> x
{1, 2, 5, 6}
>>> #set must not contain any duplicate values
>>> x = {'a','b','c','d','e'}
>>> y = {'c','d','e','f','g'}
>>> x.union(y)#all
{'c', 'b', 'g', 'd', 'f', 'a', 'e'}
>>> x = {'a','b'}
>>> y = {'c','d'}
>>> x.union(y)
{'b', 'a', 'c', 'd'}
>>> x.intersection(y)
set()
>>> x={'a','b','c','d'}
>>> y={'b','c','d','e'}
>>> x.intersection(y)
{'b', 'c', 'd'}
>>> 
>>> #difference
>>> x
{'b', 'a', 'c', 'd'}
>>> y
{'b', 'c', 'd', 'e'}
>>> x.difference(y)
{'a'}
>>> y.difference(x)
{'e'}
>>> 