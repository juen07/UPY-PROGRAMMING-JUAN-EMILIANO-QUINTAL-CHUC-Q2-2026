import math
#INPUT
while True:
    a = input("Write the left endpoint of the interval: ")
    b = input("Write the right endpoint of the interval: ")

    try:
        if "pi" in a:
            a = eval(a.replace("pi", str(math.pi)))
        else:
            a = float(a)
            
        if "pi" in b:
            b = eval(b.replace("pi", str(math.pi)))
        else:
            b = float(b)
        
        break

    except ValueError:
        print("Invalid endpoints")

f_x = input("Write the function to integrate: ")
method = input("Select Integration Method (LRM/RRM/MPM/TM): ")

area = 0.0
n = 1000
h = (b - a) / n
shift = 0
trap = 0
constant = 0
safety_function = f_x

if method == "RRM":
    shift = 1
elif method == "TM":
    trap = 1
    x0 = a
    xn = b
    f_x0 = eval(f_x.replace("x", str(x0)))
    f_xn = eval(f_x.replace("x", str(xn)))
elif method == "MPM":
    constant = h / 2
else:
    pass


for i in range(0 + shift + trap, n + shift):
    xi = i * h + a
    if "sin" in f_x:
        safety_function = f_x.replace("sin(x)", str(math.sin(xi)))
    if "cos" in f_x:
        safety_function = f_x.replace("cos(x)", str(math.cos(xi)))
        
    height = eval(safety_function.replace("x", str(xi + constant)))
    if method == "TM":
        area += height * 2
    else:
        area += height * h

if method == "TM":
    area = (area + f_x0 + f_xn) * (h/2)


#OUTPUT
print(f"The integration of f(x) = {f_x} is {area}")