import unittest


class Bolos(unittest.TestCase):

    def puntaje(self, ronda):
        suma = 0
        if len(ronda) <= 12:
            for i in range(0, len(ronda)):
                if i < 9:
                    if ronda[i][0] == 10:  # hay un pleno o más
                        suma = suma + sum(ronda[i]) + sum(ronda[i + 1])
                    elif sum(ronda[i]) == 10:  # hay semipleno
                        suma = suma + sum(ronda[i]) + ronda[i + 1][0]
                    else:
                        suma = suma + sum(ronda[i])
                elif i==9:  #pleno en la 10 cuando no hay otro seguido
                        suma = suma + sum(ronda[i])+ 2*sum(ronda[i+1])
                elif i==9 and ronda[10][0]==10: #pleno en la 11 tb
                    suma = suma + sum(ronda[i]) + sum(ronda[i + 1])+ sum(ronda[i+2])

        return suma
