# Classwork #13 - Error Handling
# Classwork #09 - Spanish Verb Conjugator

# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
pronombres = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]

terminaciones = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"],
}

lineas = []

try:
    if verbo != verbo.strip():
        raise ValueError("El verbo no debe tener espacios extra")

    if verbo != verbo.lower() and verbo.lower()[-2:] in terminaciones:
        raise ValueError("El verbo debe escribirse en minúsculas")

    terminacion_verbo = verbo[-2:]

    if len(verbo) < 2 or terminacion_verbo not in terminaciones:
        raise ValueError("El verbo debe terminar en ar, er o ir")

    raiz = verbo[:-2]
    lista_terminaciones = terminaciones[terminacion_verbo]

    for i in range(len(pronombres)):
        pronombre = pronombres[i]
        terminacion = lista_terminaciones[i]
        lineas.append(f"{pronombre} {raiz + terminacion}")

except ValueError as error:
    lineas.append(str(error))

# OUTPUT
for linea in lineas:
    print(linea)
