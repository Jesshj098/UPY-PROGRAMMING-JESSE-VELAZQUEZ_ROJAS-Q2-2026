# DÍGITO VERIFICADOR - ROL UTFSM

rol = input("Ingresa el rol UTFSM (sin guión ni dígito verificador): ")

rol_invertido = rol[::-1]
secuencia = [2, 3, 4, 5, 6, 7]
suma = 0

for i, digito in enumerate(rol_invertido):
    multiplicador = secuencia[i % len(secuencia)]
    suma += int(digito) * multiplicador

modulo = suma % 11
digito_verificador = 11 - modulo

print(f"\nRol invertido:      {rol_invertido}")
print(f"Suma total:         {suma}")
print(f"Suma % 11:          {modulo}")
print(f"11 - {modulo}:             {digito_verificador}")
print(f"\nROL completo: {rol}-{digito_verificador}")