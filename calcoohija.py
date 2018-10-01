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

        if sys.argv[2] == "suma":
            result = (calchija.plus(operando1, operando2))
        elif sys.argv[2] == "resta":
            result = (calchija.minus(operando1, operando2))
        elif sys.argv[2] == "multiplica":
            result = (calchija.mult(operando1, operando2))
        elif sys.argv[2] == "divide":
            result = (calchija.div(operando1, operando2))
        else:
            sys.exit("Error: La operación sólo puede ser suma"
                     + "resta, multiplica o divide")

    except ValueError:
        sys.exit("Error: Non numerical parameters")
    except ZeroDivisionError:
        sys.exit("Division by zero is not allowed")
    print("El resultado es " + str(result))
