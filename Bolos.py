import unittest

class Bolos(unittest.TestCase):

    def puntaje(self,ronda):
        suma=0
        for i in range(0,len(ronda)):

            suma= suma+ sum(ronda[i])

        return suma
