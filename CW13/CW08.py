import math
import sys

class NotMethod(Exception):
    pass

class LimitsError(Exception):
    pass

a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Select Integration Method (LRM/RRM/MPM/TM): ")

try:
    if "pi" in a:
        a = eval(a.replace("pi", str(math.pi)))
    else:
        a = float(a)

except ValueError:
    print("The lower limit must be numerical")
    sys.exit()

try:    
    if "pi" in b:
        b = eval(b.replace("pi", str(math.pi)))
    else:
        b = float(b)
except ValueError:
    print("The upper limit must be numerical")
    sys.exit()

try:
    if "x" not in f_x:
        raise NameError
except NameError:
    print("The function must be on terms of x")
    sys.exit()

try:
    if b < a:
        raise LimitsError()
except LimitsError:
    print("The inferior limit should be lesser than the superior limir")
    sys.exit()

try:
    if method not in "LRM/RRM/MPM/TM":
        raise NotMethod()
except NotMethod:
    print("The integration method is not valid")
    sys.exit()    

area = 0.0
n = 1000
h = (b -a) / n
constant = 0
shift = 0

if method == "RRM":
    shift = 1 
elif method == "MPM" or method == "TM":
    constant = h / 2
else:
    pass

try:
    if method in "LRM-RRM-MPM":
        for i in range(0 + shift, n + shift):
            xi = a + h * i
            height = eval(f_x.replace("x", str(xi + constant)))
            area += h * height

    elif method == "TM":
        area = eval(f_x.replace("x", str(a))) + eval(f_x.replace("x", str(b)))

        for i in range(1, n):
            xi = a + h * i
            height = 2 * eval(f_x.replace("x", str(xi)))
            area += height
        
        area = (h/2) * area
   
except TypeError:
    print("Invalid function")
    sys.exit()

print(f"The integration of f(x) = {f_x} is {area}")
