# Classwork #14 - Error Handling
# Classwork #12 - The Mandelbrot Set (Visualization)

from PIL import Image

resultado_ok = True

# INPUT
try:
    file = open("config.txt", "r")
except FileNotFoundError:
    print("No se encontró el archivo config.txt")
    resultado_ok = False

if resultado_ok:
    config = {}
    try:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parameter, value = line.split("=")
            config[parameter.strip()] = float(value) if "." in value else int(value)
    except ValueError:
        print("El archivo config.txt está mal formado")
        resultado_ok = False
    finally:
        file.close()

if resultado_ok:
    try:
        archivo = open("mandelbrot.csv", "r")
    except FileNotFoundError:
        print("No se encontró el archivo mandelbrot.csv")
        resultado_ok = False

if resultado_ok:
    lineas = archivo.readlines()
    archivo.close()

    if lineas:
        lineas.pop(0)  # NO OLVIDAR QUITAR ENCABEZADO

    try:
        max_iter = config["max_iter"]
        ancho, alto = int(config["ancho"]), int(config["alto"])
    except KeyError as error:
        print(f"Falta el parámetro {error} en config.txt")
        resultado_ok = False

if resultado_ok:
    # PROCESS
    try:
        img = Image.new("HSV", (ancho, alto))

        for linea in lineas:
            row, column, iterations = linea.strip().split(",")
            iterations = int(iterations)
            row = int(row)
            column = int(column)

            if not (0 <= row < alto and 0 <= column < ancho):
                raise IndexError

            if iterations == max_iter:
                brillo = 40
            else:
                brillo = int((iterations / max_iter) * 255)

            img.putpixel((column, row), (brillo, 255, 255))

        # OUTPUT
        img_rgb = img.convert("RGB")
        img_rgb.save("mandelbrot.png")
        print("DONE")

    except IndexError:
        print("El archivo mandelbrot.csv no es consistente con el ancho/alto de config.txt")
    except ValueError:
        print("El archivo mandelbrot.csv está mal formado")
