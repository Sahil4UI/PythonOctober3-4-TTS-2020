Python 3.9.0 (v3.9.0:9cf6752276, Oct  5 2020, 11:29:23) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a+bj
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a+bj
NameError: name 'bj' is not defined
>>> a = 5+7j
>>> type(a)
<class 'complex'>
>>> b = 1+2j
>>> type(a)
<class 'complex'>
>>> type(b)
<class 'complex'>
>>> a+b
(6+9j)
>>> a-b
(4+5j)
>>> a*b
(-9+17j)
>>> a/b
(3.8-0.6j)
>>> a
(5+7j)
>>> a**2
(-24+70j)
>>> a%3
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a%3
TypeError: can't mod complex numbers.
>>> a/b
(3.8-0.6j)
>>> a//b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a//b
TypeError: can't take floor of complex number.
>>> import math
>>> math.sqrt(a)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    math.sqrt(a)
TypeError: can't convert complex to float
>>> import cmath
>>> cmath.sqrt(a)
(2.60790387735463+1.342074004487574j)
>>> help(math)
Help on module math:

NAME
    math

MODULE REFERENCE
    https://docs.python.org/3.9/library/math
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to the mathematical functions
    defined by the C standard.

FUNCTIONS
    acos(x, /)
        Return the arc cosine (measured in radians) of x.
        
        The result is between 0 and pi.
    
    acosh(x, /)
        Return the inverse hyperbolic cosine of x.
    
    asin(x, /)
        Return the arc sine (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    asinh(x, /)
        Return the inverse hyperbolic sine of x.
    
    atan(x, /)
        Return the arc tangent (measured in radians) of x.
        
        The result is between -pi/2 and pi/2.
    
    atan2(y, x, /)
        Return the arc tangent (measured in radians) of y/x.
        
        Unlike atan(y/x), the signs of both x and y are considered.
    
    atanh(x, /)
        Return the inverse hyperbolic tangent of x.
    
    ceil(x, /)
        Return the ceiling of x as an Integral.
        
        This is the smallest integer >= x.
    
    comb(n, k, /)
        Number of ways to choose k items from n items without repetition and without order.
        
        Evaluates to n! / (k! * (n - k)!) when k <= n and evaluates
        to zero when k > n.
        
        Also called the binomial coefficient because it is equivalent
        to the coefficient of k-th term in polynomial expansion of the
        expression (1 + x)**n.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    copysign(x, y, /)
        Return a float with the magnitude (absolute value) of x but the sign of y.
        
        On platforms that support signed zeros, copysign(1.0, -0.0)
        returns -1.0.
    
    cos(x, /)
        Return the cosine of x (measured in radians).
    
    cosh(x, /)
        Return the hyperbolic cosine of x.
    
    degrees(x, /)
        Convert angle x from radians to degrees.
    
    dist(p, q, /)
        Return the Euclidean distance between two points p and q.
        
        The points should be specified as sequences (or iterables) of
        coordinates.  Both inputs must have the same dimension.
        
        Roughly equivalent to:
            sqrt(sum((px - qx) ** 2.0 for px, qx in zip(p, q)))
    
    erf(x, /)
        Error function at x.
    
    erfc(x, /)
        Complementary error function at x.
    
    exp(x, /)
        Return e raised to the power of x.
    
    expm1(x, /)
        Return exp(x)-1.
        
        This function avoids the loss of precision involved in the direct evaluation of exp(x)-1 for small x.
    
    fabs(x, /)
        Return the absolute value of the float x.
    
    factorial(x, /)
        Find x!.
        
        Raise a ValueError if x is negative or non-integral.
    
    floor(x, /)
        Return the floor of x as an Integral.
        
        This is the largest integer <= x.
    
    fmod(x, y, /)
        Return fmod(x, y), according to platform C.
        
        x % y may differ.
    
    frexp(x, /)
        Return the mantissa and exponent of x, as pair (m, e).
        
        m is a float and e is an int, such that x = m * 2.**e.
        If x is 0, m and e are both 0.  Else 0.5 <= abs(m) < 1.0.
    
    fsum(seq, /)
        Return an accurate floating point sum of values in the iterable seq.
        
        Assumes IEEE-754 floating point arithmetic.
    
    gamma(x, /)
        Gamma function at x.
    
    gcd(*integers)
        Greatest Common Divisor.
    
    hypot(...)
        hypot(*coordinates) -> value
        
        Multidimensional Euclidean distance from the origin to a point.
        
        Roughly equivalent to:
            sqrt(sum(x**2 for x in coordinates))
        
        For a two dimensional point (x, y), gives the hypotenuse
        using the Pythagorean theorem:  sqrt(x*x + y*y).
        
        For example, the hypotenuse of a 3/4/5 right triangle is:
        
            >>> hypot(3.0, 4.0)
            5.0
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two floating point numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them
        must be smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard.  That
        is, NaN is not close to anything, even itself.  inf and -inf are
        only close to themselves.
    
    isfinite(x, /)
        Return True if x is neither an infinity nor a NaN, and False otherwise.
    
    isinf(x, /)
        Return True if x is a positive or negative infinity, and False otherwise.
    
    isnan(x, /)
        Return True if x is a NaN (not a number), and False otherwise.
    
    isqrt(n, /)
        Return the integer part of the square root of the input.
    
    lcm(*integers)
        Least Common Multiple.
    
    ldexp(x, i, /)
        Return x * (2**i).
        
        This is essentially the inverse of frexp().
    
    lgamma(x, /)
        Natural logarithm of absolute value of Gamma function at x.
    
    log(...)
        log(x, [base=math.e])
        Return the logarithm of x to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of x.
    
    log10(x, /)
        Return the base 10 logarithm of x.
    
    log1p(x, /)
        Return the natural logarithm of 1+x (base e).
        
        The result is computed in a way which is accurate for x near zero.
    
    log2(x, /)
        Return the base 2 logarithm of x.
    
    modf(x, /)
        Return the fractional and integer parts of x.
        
        Both results carry the sign of x and are floats.
    
    nextafter(x, y, /)
        Return the next floating-point value after x towards y.
    
    perm(n, k=None, /)
        Number of ways to choose k items from n items without repetition and with order.
        
        Evaluates to n! / (n - k)! when k <= n and evaluates
        to zero when k > n.
        
        If k is not specified or is None, then k defaults to n
        and the function returns n!.
        
        Raises TypeError if either of the arguments are not integers.
        Raises ValueError if either of the arguments are negative.
    
    pow(x, y, /)
        Return x**y (x to the power of y).
    
    prod(iterable, /, *, start=1)
        Calculate the product of all the elements in the input iterable.
        
        The default start value for the product is 1.
        
        When the iterable is empty, return the start value.  This function is
        intended specifically for use with numeric values and may reject
        non-numeric types.
    
    radians(x, /)
        Convert angle x from degrees to radians.
    
    remainder(x, y, /)
        Difference between x and the closest integer multiple of y.
        
        Return x - n*y where n*y is the closest integer multiple of y.
        In the case where x is exactly halfway between two multiples of
        y, the nearest even value of n is used. The result is always exact.
    
    sin(x, /)
        Return the sine of x (measured in radians).
    
    sinh(x, /)
        Return the hyperbolic sine of x.
    
    sqrt(x, /)
        Return the square root of x.
    
    tan(x, /)
        Return the tangent of x (measured in radians).
    
    tanh(x, /)
        Return the hyperbolic tangent of x.
    
    trunc(x, /)
        Truncates the Real x to the nearest Integral toward 0.
        
        Uses the __trunc__ magic method.
    
    ulp(x, /)
        Return the value of the least significant bit of the float x.

DATA
    e = 2.718281828459045
    inf = inf
    nan = nan
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/math.cpython-39-darwin.so


>>> help(cmath)
Help on module cmath:

NAME
    cmath

MODULE REFERENCE
    https://docs.python.org/3.9/library/cmath
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to mathematical functions for complex
    numbers.

FUNCTIONS
    acos(z, /)
        Return the arc cosine of z.
    
    acosh(z, /)
        Return the inverse hyperbolic cosine of z.
    
    asin(z, /)
        Return the arc sine of z.
    
    asinh(z, /)
        Return the inverse hyperbolic sine of z.
    
    atan(z, /)
        Return the arc tangent of z.
    
    atanh(z, /)
        Return the inverse hyperbolic tangent of z.
    
    cos(z, /)
        Return the cosine of z.
    
    cosh(z, /)
        Return the hyperbolic cosine of z.
    
    exp(z, /)
        Return the exponential value e**z.
    
    isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
        Determine whether two complex numbers are close in value.
        
          rel_tol
            maximum difference for being considered "close", relative to the
            magnitude of the input values
          abs_tol
            maximum difference for being considered "close", regardless of the
            magnitude of the input values
        
        Return True if a is close in value to b, and False otherwise.
        
        For the values to be considered close, the difference between them must be
        smaller than at least one of the tolerances.
        
        -inf, inf and NaN behave similarly to the IEEE 754 Standard. That is, NaN is
        not close to anything, even itself. inf and -inf are only close to themselves.
    
    isfinite(z, /)
        Return True if both the real and imaginary parts of z are finite, else False.
    
    isinf(z, /)
        Checks if the real or imaginary part of z is infinite.
    
    isnan(z, /)
        Checks if the real or imaginary part of z not a number (NaN).
    
    log(...)
        log(z[, base]) -> the logarithm of z to the given base.
        
        If the base not specified, returns the natural logarithm (base e) of z.
    
    log10(z, /)
        Return the base-10 logarithm of z.
    
    phase(z, /)
        Return argument, also known as the phase angle, of a complex.
    
    polar(z, /)
        Convert a complex from rectangular coordinates to polar coordinates.
        
        r is the distance from 0 and phi the phase angle.
    
    rect(r, phi, /)
        Convert from polar coordinates to rectangular coordinates.
    
    sin(z, /)
        Return the sine of z.
    
    sinh(z, /)
        Return the hyperbolic sine of z.
    
    sqrt(z, /)
        Return the square root of z.
    
    tan(z, /)
        Return the tangent of z.
    
    tanh(z, /)
        Return the hyperbolic tangent of z.

DATA
    e = 2.718281828459045
    inf = inf
    infj = infj
    nan = nan
    nanj = nanj
    pi = 3.141592653589793
    tau = 6.283185307179586

FILE
    /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/lib-dynload/cmath.cpython-39-darwin.so


>>> #String
>>> #String-Group of characters(numbers,alphabets,special character) whic must be enclosed inside single,double or triple quotes
>>> x = "Navya Gosain"
>>> type(x)
<class 'str'>
>>> x = 'Navya Gosain'
>>> type(x)
<class 'str'>
>>> x = """Navya Gosain"""
>>> type(x)
<class 'str'>
>>> x = "Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Pythons design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[29]

Python was created in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting.

Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3."
SyntaxError: EOL while scanning string literal
>>> x = """Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[29]

Python was created in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting.

Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3."""
>>> print(x)
Python is an interpreted, high-level and general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[28]

Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented, and functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.[29]

Python was created in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system with reference counting.

Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
>>> # hello everyone
>>> print("hello everyone")
hello everyone
>>> #hello "everyone"
>>> print("hello "everyone"")
SyntaxError: invalid syntax
>>> print("hello 'everyone'")
hello 'everyone'
>>> print('hello "everyone"')
hello "everyone"
>>> #Indexing
>>> x = "Navya"
>>> x[0]
'N'
>>> x[1]
'a'
>>> x[3]
'y'
>>> x[5]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    x[5]
IndexError: string index out of range
>>> x = "hello everyone, welcome to our python class"
>>> x[-1]
's'
>>> x[-2]
's'
>>> x[-3]
'a'
>>> #slicing
>>> #finding substring of a string
>>> x
'hello everyone, welcome to our python class'
>>> #x[Starting Index:ending index]
>>> x[0:13]
'hello everyon'
>>> x[0:14]
'hello everyone'
>>> x[5:16]
' everyone, '
>>> x[0:]
'hello everyone, welcome to our python class'
>>> x = " hello ''' "
>>> x[-1]
' '
>>> x[-2]
"'"
>>> x = "Navya Gosain"
>>> x[:5]
'Navya'
>>> x
'Navya Gosain'
>>> x[0:12]
'Navya Gosain'
>>> x[0:12:1]
'Navya Gosain'
>>> x[0:12:2]
'NvaGsi'
>>> x[0:12:3]
'NyGa'
>>> x
'Navya Gosain'
>>> x[-1::1]
'n'
>>> x[-1::-1]
'niasoG ayvaN'
>>> 
>>> #String Methods
>>> x
'Navya Gosain'
>>> x.lower()
'navya gosain'
>>> x.casefold()
'navya gosain'
>>> x
'Navya Gosain'
>>> x = x.lower()
>>> x
'navya gosain'
>>> x.upper()
'NAVYA GOSAIN'
>>> x="Navya GOSAIN"
>>> x.swapcase()
'nAVYA gosain'
>>> x
'Navya GOSAIN'
>>> x = x.lower()
>>> x
'navya gosain'
>>> x.capitalize()
'Navya gosain'
>>> x.title()
'Navya Gosain'
>>> x="navya kumar"
>>> x.replace("kumar","gosain")
'navya gosain'
>>> x = "aabbccdd"
>>> x.replace("a","x")
'xxbbccdd'
>>> x.replace("a","x",1)
'xabbccdd'
>>> x = "aaaaaaa"
>>> x.replace("a","z",4)
'zzzzaaa'
>>> x
'aaaaaaa'
>>> len(x)
7
>>> x = "Navya"
>>> len(x)
5
>>> x="N"
>>> len(x)
1
>>> x = ""
>>> len(x)
0
>>> x
''
>>> x = "aabbccccccdddeeeeeeeeeeee"
>>> x.count('e')
12
>>> 
