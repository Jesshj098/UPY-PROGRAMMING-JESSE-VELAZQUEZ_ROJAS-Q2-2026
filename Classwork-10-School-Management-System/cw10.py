
# INPUT: Datos iniciales del sistema (usuarios, materias y calificaciones)

usuarios = {
    'jperez':     {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Juan Perez'},
    'amartin':    {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Ana Martin'},
    'ltrochez':   {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Luisa Trochez'},
    'adiaz':      {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Abraham Díaz'},
    'sescamilla': {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Stephan Escamilla'},
    'jrojas':     {'contraseña': '1234', 'rol': 'alumno',      'nombre': 'Jesse Rojas'},
    'mlopez':     {'contraseña': '1234', 'rol': 'maestro',     'nombre': 'Maria Lopez'},
    'rgarcia':    {'contraseña': '1234', 'rol': 'coordinador', 'nombre': 'Rosa Garcia'},
}

materias = ('Matematicas', 'Programación', 'Ingles II', 'Social-Emotional Skills', 'Arquitectura', 'Calculo')

calificaciones = {
    'jperez':     {'Matematicas': 9.0,  'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 7.0, 'Arquitectura': 6.0, 'Calculo': 7.5},
    'amartin':    {'Matematicas': 9.0,  'Programación': 8.0, 'Ingles II': 7.5, 'Social-Emotional Skills': 9.0, 'Arquitectura': 6.0, 'Calculo': 9.5},
    'ltrochez':   {'Matematicas': 10.0, 'Programación': 8.9, 'Ingles II': 8.9, 'Social-Emotional Skills': 9.0, 'Arquitectura': 9.0, 'Calculo': 8.7},
    'adiaz':      {'Matematicas': 9.0,  'Programación': 9.7, 'Ingles II': 9.5, 'Social-Emotional Skills': 9.0, 'Arquitectura': 9.0, 'Calculo': 9.5},
    'sescamilla': {'Matematicas': 9.0,  'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 7.0, 'Arquitectura': 9.6, 'Calculo': 8.5},
    'jrojas':     {'Matematicas': 9.0,  'Programación': 8.7, 'Ingles II': 8.5, 'Social-Emotional Skills': 6.0, 'Arquitectura': 8.0, 'Calculo': 9.5},
}


# PROCESS: Ciclo de inicio de sesión

sesion_activa = False
while not sesion_activa:
    # INPUT
    usuario_ingresado = input('Usuario: ')
    clave_ingresada = input('Contraseña: ')

    # PROCESS
    if usuario_ingresado in usuarios and usuarios[usuario_ingresado]['contraseña'] == clave_ingresada:
        sesion_activa = True
    else:
        # OUTPUT
        print('Usuario o contraseña incorrectos. Intenta de nuevo.\n')

# PROCESS: guardar el rol y el nombre de quien inició sesión
rol_usuario = usuarios[usuario_ingresado]['rol']
nombre_usuario = usuarios[usuario_ingresado]['nombre']

# OUTPUT
print(f'\nBienvenido, {nombre_usuario} ({rol_usuario})\n')



if rol_usuario == 'alumno':

    # OUTPUT
    print(f'Boleta de {nombre_usuario}')

    # PROCESS:
    materias_aprobadas = set()
    for materia_actual in materias:
        calificacion_actual = calificaciones[usuario_ingresado][materia_actual]

        # OUTPUT
        print(f'{materia_actual}: {calificacion_actual}')

        # PROCESS
        if calificacion_actual >= 8.0:
            materias_aprobadas.add(materia_actual)

    # PROCESS
    materias_pendientes = set(materias) - materias_aprobadas

    # OUTPUT
    print('')
    if materias_aprobadas:
        print(f'Materias aprobadas: {materias_aprobadas}')
    else:
        print('Materias aprobadas: Ninguna')

    if materias_pendientes:
        print(f'Materias pendientes: {materias_pendientes}')
    else:
        print('Materias pendientes: Ninguna')

elif rol_usuario == 'maestro':

    # OUTPUT
    print('Lista de alumnos:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'alumno':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    seguir_calificando = 's'
    while seguir_calificando == 's':

        # INPUT
        alumno_seleccionado = input('\nAlumno (usuario): ')
        while alumno_seleccionado not in calificaciones:
            print('Ese alumno no existe.')
            alumno_seleccionado = input('Alumno (usuario): ')

        materia_seleccionada = input('Materia: ')
        while materia_seleccionada not in materias:
            print('Esa materia no existe.')
            materia_seleccionada = input('Materia: ')

        calificacion_nueva = float(input('Nueva calificación: '))

        # PROCESS
        calificaciones[alumno_seleccionado][materia_seleccionada] = calificacion_nueva

        # OUTPUT
        print('Calificación actualizada.')

        # INPUT
        seguir_calificando = input('\n¿Calificar a otro alumno? (s/n): ')

elif rol_usuario == 'coordinador':

    # OUTPUT: lista de maestros
    print('Lista de maestros:')
    for clave_usuario in usuarios:
        if usuarios[clave_usuario]['rol'] == 'maestro':
            print(f"- {clave_usuario}: {usuarios[clave_usuario]['nombre']}")

    # OUTPUT: lista de materias
    print('\nLista de materias:')
    for materia_actual in materias:
        print(f'- {materia_actual}')

    # OUTPUT: lista de alumnos con todas sus calificaciones
    print('\nLista de alumnos con sus calificaciones:')
    for alumno_actual in calificaciones:
        print(f"\n{usuarios[alumno_actual]['nombre']} ({alumno_actual}):")
        for materia_actual in materias:
            print(f'  {materia_actual}: {calificaciones[alumno_actual][materia_actual]}')