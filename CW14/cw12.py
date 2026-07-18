"""
Classwork 12 – The Mandelbrot Set (Visualization)
Reads config.txt and mandelbrot.csv, maps iteration counts to pixel brightness,
and saves a PNG image.
"""

# ------------------------------------------------------------
# INPUT – Read config and CSV files
# ------------------------------------------------------------
from PIL import Image
import sys

config = {}
try:
    with open("config.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            parameter, value = line.strip().split("=")
            config[parameter] = float(value) if "." in value else int(value)
except FileNotFoundError:
    sys.exit("The file config.txt wasn´t found")

try:
    with open("mandelbrot.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    sys.exit("The file mandelbrot.csv wasn´t found")

# Remove header row
lineas.pop(0)

# Unpack variables
max_iter = config["max_iter"]
ancho = int(config["ancho"])
alto = int(config["alto"])

# ------------------------------------------------------------
# PROCESS – Create image from CSV data
# ------------------------------------------------------------
img = Image.new("HSV", (ancho, alto))

try:
    for linea in lineas:
        row, column, iterations = linea.strip().split(",")
        iterations = int(iterations)
        row = int(row)
        column = int(column)
        
        if iterations == max_iter:
            brightness = 0
        else:
            brightness = int((iterations / max_iter) * 255)
        
        img.putpixel((column, row), (brightness, 255, 255))

except IndexError:
    sys.exit("Inconsistent ancho and alto")

except ValueError:
    sys.exit("Bad configuration of mandelbrot.csv")
# ------------------------------------------------------------
# OUTPUT – Convert to RGB and save
# ------------------------------------------------------------
img_rgb = img.convert("RGB")
img_rgb.save("mandelbrot_valle.png")
print("DONE")