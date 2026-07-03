
# Classwork #11 - The Mandelbrot Set


# INPUT
# Read config.txt line by line and store every "clave=valor"
# pair in a dictionary. Values are saved as floats since some
# of them (real_min, real_max, imag_min, imag_max) are decimals.

config = {}
archivo = open('config.txt', 'r')

for linea in archivo:
    clave, valor = linea.strip().split('=')
    config[clave] = float(valor)

archivo.close()

# Pull the settings out of the dictionary. ancho, alto and max_iter
# are used as counters/limits, so they are converted to int.
ancho = int(config['ancho'])
alto = int(config['alto'])
real_min = config['real_min']
real_max = config['real_max']
imag_min = config['imag_min']
imag_max = config['imag_max']
max_iter = int(config['max_iter'])


# PROCESS
# Open the CSV output file and write the header first.
# Then use two nested loops (row, column) to sweep the whole
# grid: map each pixel to a complex number c, run the
# Mandelbrot iteration on it, and write how many iterations
# it took to escape (or max_iter if it never escaped).

salida = open('mandelbrot.csv', 'w')
salida.write('fila,columna,iteraciones\n')

fila = 0
while fila < alto:

    columna = 0
    while columna < ancho:

        # map the (fila, columna) pixel to a point c on the complex plane
        real = real_min + (columna / ancho) * (real_max - real_min)
        imag = imag_min + (fila / alto) * (imag_max - imag_min)
        c = complex(real, imag)

        # Mandelbrot iteration: z(n+1) = z(n)^2 + c, starting at z0 = 0
        z = 0 + 0j
        iteraciones = 0

        while abs(z) <= 2 and iteraciones < max_iter:
            z = z * z + c
            iteraciones += 1

        # save this grid point's result
        salida.write(f'{fila},{columna},{iteraciones}\n')

        columna += 1

    fila += 1

salida.close()


# OUTPUT

print('Listo. Resultados guardados en mandelbrot.csv')