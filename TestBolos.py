import unittest
from Bolos import Bolos


class TestBolos(unittest.TestCase):

    def test_tirada_suman0(self):
        bolos = Bolos()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado= bolos.puntaje(ronda)
        self.assertEqual(resultado,0)
    def test_tirada_1_primeratirada(self):
        bolos = Bolos()
        ronda = [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 1)

    def test_sumatirada1(self):
        bolos = Bolos()
        ronda = [(1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 2)

    def test_puntosenotra_tirada(self):
        bolos = Bolos()
        ronda = [(0, 0), (2, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 2)

    def test_suma_tirada(self):
        bolos = Bolos()
        ronda = [(0, 0), (2, 4), (0, 3), (0, 0), (2, 4), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        #print(len(ronda)) comprobamos si el len lo está realizando correctamente
        self.assertEqual(resultado, 15)
    def test_pleno_solo(self):
        bolos = Bolos()
        ronda = [(0, 0), ('X', 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 10)