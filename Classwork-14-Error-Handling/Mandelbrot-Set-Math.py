# Classwork #14 - Error Handling
# Classwork #11 - The Mandelbrot Set (Math)

REQUIRED_KEYS = ['ancho', 'alto', 'real_min', 'real_max', 'imag_min', 'imag_max', 'max_iter']

resultado_ok = True

# INPUT
# Read config.txt line by line and store every "clave=valor" pair.
try:
    archivo = open('config.txt', 'r')
except FileNotFoundError:
    print('No se encontró el archivo config.txt')
    resultado_ok = False

if resultado_ok:
    config = {}
    try:
        for numero_linea, linea in enumerate(archivo, start=1):
            linea = linea.strip()
            if linea == '':
                continue
            clave, valor = linea.split('=')
            config[clave.strip()] = valor.strip()
    except ValueError:
        print(f'El archivo config.txt está mal formado (revisa la línea {numero_linea})')
        resultado_ok = False
    finally:
        archivo.close()

if resultado_ok:
    for clave in REQUIRED_KEYS:
        if clave not in config:
            print(f'Falta el parámetro "{clave}" en config.txt')
            resultado_ok = False
            break

if resultado_ok:
    try:
        if '.' in config['ancho'] or '.' in config['alto']:
            raise ValueError
        ancho = int(config['ancho'])
        alto = int(config['alto'])
    except ValueError:
        print('"ancho" y "alto" deben ser números enteros')
        resultado_ok = False

if resultado_ok:
    try:
        real_min = float(config['real_min'])
        real_max = float(config['real_max'])
        imag_min = float(config['imag_min'])
        imag_max = float(config['imag_max'])
        max_iter = int(float(config['max_iter']))
    except ValueError:
        print('Los límites del plano complejo y max_iter deben ser números válidos')
        resultado_ok = False

if resultado_ok:
    # PROCESS
    # Open the CSV output file and write the header first.
    # Then use two nested loops (row, column) to sweep the whole
    # grid: map each pixel to a complex number c, run the
    # Mandelbrot iteration on it, and write how many iterations
    # it took to escape (or max_iter if it never escaped).

    salida = open('mandelbrot.csv', 'w')
    salida.write('row,column,iterations\n')

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
