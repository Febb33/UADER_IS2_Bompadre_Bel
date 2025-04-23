#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

def factorial(num):
    """Calcula el factorial de un número."""
    if num < 0:
        print(f"Factorial de un número negativo ({num}) no existe")
        return None
    elif num == 0:
        return 1
    else:
        fact = 1
        while num > 1:
            fact *= num
            num -= 1
        return fact

def calcular_factoriales(inicio, fin):
    """Calcula y muestra los factoriales en un rango dado."""
    for i in range(inicio, fin + 1):
        print(f"Factorial de {i}! es {factorial(i)}")

# Verificar si se proporcionó un argumento
if len(sys.argv) > 1:
    argumento = sys.argv[1]

    # Caso "-hasta" (ejemplo: "-10" → 1 a 10)
    if argumento.startswith("-") and argumento[1:].isdigit():
        hasta = int(argumento[1:])
        calcular_factoriales(1, hasta)

    # Caso "desde-" (ejemplo: "5-" → 5 a 60)
    elif argumento.endswith("-") and argumento[:-1].isdigit():
        desde = int(argumento[:-1])
        calcular_factoriales(desde, 60)

    # Caso número único (ejemplo: "5")
    elif argumento.isdigit():
        num = int(argumento)
        print(f"Factorial de {num}! es {factorial(num)}")

    else:
        print("Formato inválido. Use '-hasta', 'desde-', o un número único.")
        sys.exit(1)

else:
    # Solicitar entrada manual si no se proporciona argumento
    while True:
        entrada = input("Ingrese un número, '-hasta' o 'desde-': ").strip()

        if entrada.startswith("-") and entrada[1:].isdigit():
            hasta = int(entrada[1:])
            calcular_factoriales(1, hasta)
            break

        elif entrada.endswith("-") and entrada[:-1].isdigit():
            desde = int(entrada[:-1])
            calcular_factoriales(desde, 60)
            break

        elif entrada.isdigit():
            num = int(entrada)
            print(f"Factorial de {num}! es {factorial(num)}")
            break

        else:
            print("Entrada inválida. Intente nuevamente.")


# Comentario para realizar la consigna
