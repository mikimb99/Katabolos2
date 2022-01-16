import unittest


class Bolos(unittest.TestCase):

    def puntaje(self, ronda):
        suma = 0
        if len(ronda) <= 12:
            for i in range(0, len(ronda)):
                if i < 9: #no hay rondas extras
                    if ronda[i][0] == 10:  # hay un pleno
                        #if ronda[i+1][0] ==10: # hay mas de un pleno
                        suma = suma + sum(ronda[i]) + sum(ronda[i + 1])
                    elif sum(ronda[i]) == 10:  # hay semipleno
                        suma = suma + sum(ronda[i]) + ronda[i + 1][0]
                    else:
                        suma = suma + sum(ronda[i])
                elif i==9: #1 ronda extra
                    suma = suma + sum(ronda[i])
                else:
                    if sum(ronda[9])==10 and ronda[9][0]!= 10: #hay semi
                        suma= suma + ronda[9+1][0]
                    else:
                        suma = suma + sum(ronda[i])


        return suma
