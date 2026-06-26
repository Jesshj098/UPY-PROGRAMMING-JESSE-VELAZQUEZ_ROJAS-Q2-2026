# Classwork #09 - Spanish Verb Conjugator
# Conjugates a regular Spanish verb (-ar, -er, -ir) in present tense

# INPUT
verbo = input("Ingrese verbo: ")

# PROCESS
pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'ais', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'eis', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'is', 'en']
}

raiz = verbo[:-2]
terminacion_verbo = verbo[-2:]
lista_terminaciones = terminaciones[terminacion_verbo]

# OUTPUT
for i in range(len(pronombres)):
    pronombre = pronombres[i]
    terminacion = lista_terminaciones[i]
    print(pronombre, raiz + terminacion)