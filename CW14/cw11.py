import sys
config = {}

file = open("config.txt", "r")
parameters = ["ancho", "alto", "max_iter", "real_min", "real_max", "imag_min", "imag_max"]

try:
    for line in file:
        parameter, value = line.strip().split("=")
        config[parameter] = float(value) if "." in value else int(value)
    file.close()
except ValueError:
    print("Incorrect configuration of config.txt")
    sys.exit()

try:
    width, height, max_iter = config["ancho"], config["alto"], config["max_iter"]

    output = open("mandelbrot.csv", "w")
    output.write("row,column,iterations\n")

    for row in range(height):
        for column in range(width):
            real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
            c = complex(real, imag)
            
            z = 0 + 0j
            iterations = 0
            
            while (abs(z) <=2) and (iterations < max_iter):
                z = z * z + c
                iterations += 1
            
            output.write(f"{row},{column},{iterations}\n")

except KeyError:
    for key in config:
        if key in parameters:
            parameters.remove(key)

    if len(parameters) > 0:
        print("There are missing keys: ")
        print(", ".join([word for word in parameters]))
        sys.exit()

except TypeError:
    print("ancho and alto must be integers")
    sys.exit()



print("Done")
