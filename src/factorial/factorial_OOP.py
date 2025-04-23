#!/usr/bin/python
#*-------------------------------------------------------------------------*
#* factorial.py                                                            *
#* calcula el factorial de un número                                       *
#* Dr.P.E.Colla (c) 2022                                                   *
#* Creative commons                                                        *
#*-------------------------------------------------------------------------*

import sys

class Factorial:
    """Clase para calcular factoriales en un rango especificado."""

    def __init__(self):
        """Constructor vacío, sin necesidad de parámetros iniciales."""
        pass

    def calcular(self, num):
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

    def run(self, min_num, max_num):
        """Calcula los factoriales entre los números min_num y max_num."""
        for i in range(min_num, max_num + 1):
            print(f"Factorial de {i}! es {self.calcular(i)}")

# Función para procesar argumentos de la línea de comandos
def procesar_argumento(argumento, factorial_obj):
    if argumento.startswith("-") and argumento[1:].isdigit():
        hasta = int(argumento[1:])
        factorial_obj.run(1, hasta)

    elif argumento.endswith("-") and argumento[:-1].isdigit():
        desde = int(argumento[:-1])
        factorial_obj.run(desde, 60)

    elif argumento.isdigit():
        num = int(argumento)
        print(f"Factorial de {num}! es {factorial_obj.calcular(num)}")

    else:
        print("Formato inválido. Use '-hasta', 'desde-', o un número único.")
        sys.exit(1)

# Punto de entrada del programa
if __name__ == "__main__":
    factorial_obj = Factorial()

    if len(sys.argv) > 1:
        procesar_argumento(sys.argv[1], factorial_obj)
    else:
        # Solicitar entrada manual si no se proporciona argumento
        while True:
            entrada = input("Ingrese un número, '-hasta' o 'desde-': ").strip()
            procesar_argumento(entrada, factorial_obj)
            break


# Comentario para realizar la consigna
