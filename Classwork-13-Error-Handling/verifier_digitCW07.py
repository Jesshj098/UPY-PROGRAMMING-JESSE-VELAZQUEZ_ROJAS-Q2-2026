# Classwork #13 - Error Handling
# Classwork #07 - Verifier Digit (ROL UTFSM)

def calcular_digito_verificador(rol):
    rol_invertido = rol[::-1]
    secuencia = [2, 3, 4, 5, 6, 7]
    suma = 0
    for i, digito in enumerate(rol_invertido):
        multiplicador = secuencia[i % len(secuencia)]
        suma += int(digito) * multiplicador

    resto = suma % 11
    dv = 11 - resto

    if dv == 11:
        dv = 0
    elif dv == 10:
        dv = "K"

    return dv


# INPUT
entrada = input("Ingresa el rol UTFSM (formato XXXXXXXXX-X): ")

# PROCESS
try:
    partes = entrada.split("-")

    if len(partes) != 2:
        raise ValueError("Rol inválido: No tiene el formato XXXXXXXXX-X")

    rol, dv_ingresado = partes

    if not rol.isdigit():
        raise ValueError("Los digitos del rol deben ser numéricos")

    if not dv_ingresado.isdigit():
        raise ValueError("El digito verificador debe ser numérico")

    dv_calculado = calcular_digito_verificador(rol)

    if int(dv_ingresado) != dv_calculado:
        raise ValueError(
            f"Error: El dígito verificador no conicide, se esperaba {dv_calculado}"
        )

    resultado = f"{rol}-{dv_ingresado}"

except ValueError as error:
    resultado = str(error)

# OUTPUT
print(resultado)
