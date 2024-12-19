import numpy
import math

def f(x):
    return x**2 -8 * numpy. log(x)

x = numpy.array([1,2,3])
y = f(x)

left = 1
right = 2
precision = 10**(-3)

while right - left >= precision: 
    middle = (right + left) / 2

    if f (middle) == 0:
        break
    elif f(left) * f(middle) < 0:
        right = middle 
    elif f(right) * f(middle) < 0: 
        left = middle


print(middle)
print (f(middle))


