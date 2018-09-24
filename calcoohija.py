#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import calcoo


class CalculadoraHija(calcoo.Calculadora):

    def mult(self, op1, op2):
        return op1 * op2

    def div(self, op1, op2):
        return op1 / op2


calchija = CalculadoraHija()

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = (calchija.plus(operando1, operando2))
    elif sys.argv[2] == "resta":
        result = (calchija.minus(operando1, operando2))
    elif sys.argv[2] == "multiplicar":
        result = (calchija.mult(operando1, operando2))
    elif sys.argv[2] == "dividir":
        result = (calchija.div(operando1, operando2))
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
