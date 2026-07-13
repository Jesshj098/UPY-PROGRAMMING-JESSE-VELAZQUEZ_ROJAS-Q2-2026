# Classwork #13 - Error Handling
# Classwork #08 - Numerical Integration

import math
import re

MATH_FUNCS = {
    "sin", "cos", "tan", "asin", "acos", "atan", "atan2",
    "exp", "log", "log10", "log2", "sqrt", "fabs", "pi", "e"
}


def parsear_limite(texto):
    if texto.strip() == "pi":
        return math.pi
    return float(texto)


def f(x, f_x):
    return eval(f_x, {"math": math, "__builtins__": {}}, {"x": x})


# INPUT
a_str = input("Write the left endpoint of the interval: ")
b_str = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Select Integration Method (LRM/RRM/MPM/TM): ").strip().upper()
n_str = input("Write the number of subintervals: ")
exact_str = input("Write the exact value (or press Enter if unknown): ")

# PROCESS
resultado = None
try:
    try:
        a = parsear_limite(a_str)
    except ValueError:
        raise ValueError("El límite inferior debe ser numérico")

    try:
        b = parsear_limite(b_str)
    except ValueError:
        raise ValueError("El límite superior debe ser numérico")

    if a >= b:
        raise ValueError("El límite inferior debe ser menor que el límite superior")

    if f_x.strip() == "":
        raise ValueError("La función ingresada no es válida")

    if "^" in f_x:
        raise ValueError("La función ingresada no es válida")

    variables = set(re.findall(r"[a-zA-Z_]+", f_x.replace("math.", "")))
    for var in variables:
        if var != "x" and var not in MATH_FUNCS:
            raise ValueError("La función debe estar escrita en términos de x")

    if method not in ("LRM", "RRM", "MPM", "TM"):
        raise ValueError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")

    try:
        n = int(n_str)
    except ValueError:
        raise ValueError("El número de subintervalos debe ser un entero")

    if n <= 0:
        raise ValueError("El número de subintervalos debe ser mayor a cero")

    exact = None
    if exact_str.strip() != "":
        try:
            exact = float(exact_str)
        except ValueError:
            raise ValueError("El valor exacto debe ser numérico")

    h = (b - a) / n
    area = 0

    try:
        if method == "TM":
            area = f(a, f_x) + f(b, f_x)
            for i in range(1, n):
                xi = a + i * h
                area += 2 * f(xi, f_x)
            area *= h / 2
        else:
            shift = 0
            constant = 0
            if method == "RRM":
                shift = 1
            elif method == "MPM":
                constant = h / 2

            for i in range(shift, n + shift):
                xi = a + i * h + constant
                area += f(xi, f_x) * h
    except ZeroDivisionError:
        raise ValueError("La función no está definida en algún punto del intervalo")
    except (NameError, SyntaxError, TypeError):
        raise ValueError("La función ingresada no es válida")

    resultado = f"\nThe integration of {f_x} is {area:.6f}"

    if exact is not None:
        abs_error = abs(exact - area)
        rel_error = abs_error / abs(exact) * 100 if exact != 0 else float("inf")
        resultado += (
            f"\nExact value: {exact:.6f}"
            f"\nAbsolute error: {abs_error:.6f}"
            f"\nRelative error: {rel_error:.4f}%"
        )

except ValueError as error:
    resultado = str(error)

# OUTPUT
print(resultado)
