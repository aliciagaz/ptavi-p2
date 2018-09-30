#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import csv
from calcoohija import CalculadoraHija

calchija = CalculadoraHija()


if __name__ == "__main__":
    try:
        texto = []

        with open(sys.argv[1]) as Fich:
            fich = csv.reader(Fich)
            for linea in fich:
                elemento = ", ".join(linea)
                texto.append(elemento)

        for linea in texto:
            linea = linea.split(",")
            operador = linea[0]
            operandos = linea[1:]
            print(linea)

            result = 0
            primera_iteracion = True
            for operando in operandos[:-1]:

                if primera_iteracion is True:
                    operando1 = int(operandos[0])
                    operando2 = int(operandos[1])
                    primera_iteracion = False
                else:
                    operandos = operandos[1:]
                    operando1 = int(result)
                    operando2 = int(operandos[1])

                if operador == "suma":
                    result = (calchija.plus(operando1, operando2))
                elif operador == "resta":
                    result = (calchija.minus(operando1, operando2))
                elif operador == "multiplica":
                    result = (calchija.mult(operando1, operando2))
                elif operador == "divide":
                    result = (calchija.div(operando1, operando2))
                else:
                    sys.exit("Error: La operación sólo puede ser suma"
                             + "resta, multiplica o divide")

            print("El resultado es " + str(result))

    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")
