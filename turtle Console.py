Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.Screnn()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    turtle.Screnn()
AttributeError: module 'turtle' has no attribute 'Screnn'
>>> turtle.Screen()
<turtle._Screen object at 0x10d66c7f0>
>>> turtle.pen()
{'shown': True, 'pendown': True, 'pencolor': 'black', 'fillcolor': 'black', 'pensize': 1, 'speed': 3, 'resizemode': 'noresize', 'stretchfactor': (1.0, 1.0), 'shearfactor': 0.0, 'outline': 1, 'tilt': 0.0}
>>> turtle.shape('turtle')
>>> x = 0
>>> for i in range(3000):
	turtle.forward(x)
	turtle.left(90)
	x=x+50

