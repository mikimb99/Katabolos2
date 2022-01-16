import unittest
from Bolos import Bolos


class TestBolos(unittest.TestCase):

    def test_tirada_suman0(self):
        bolos = Bolos()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado= bolos.puntaje(ronda)
        self.assertEqual(resultado,0)
    def test_tirada_1_primeratirada(self): #=
        bolos = Bolos()
        ronda = [(1, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 1)

    def test_sumatirada1(self): #=
        bolos = Bolos()
        ronda = [(1, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 2)

    def test_puntosenotra_tirada(self): #=
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
    def test_pleno_solo(self): #=
        bolos = Bolos()
        ronda = [(0, 0), (10, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 10)
    def test_pleno_ypuntos(self):
        bolos = Bolos()
        ronda = [(0, 0), (10, 0), (4, 5), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 28)
    def testplenosvarios(self):
        bolos = Bolos()
        ronda = [(0, 0), (10, 0), (4, 0), (10, 0), (5, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 14+4+15+5+2)
    def test_semiplenopuntos(self):
        bolos = Bolos()
        ronda = [(0, 0), (8, 2), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 18)
    def test_plenoysemi(self):
        bolos = Bolos()
        ronda = [(0, 0), (8, 2), (4, 0), (0, 0), (10, 0), (8, 2), (4, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 18+10+20+8)
    def test_plenosseguidos(self):
        bolos = Bolos()
        ronda = [(0, 0), (8, 2), (4, 0), (10, 0), (10, 0), (8, 2), (4, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 18+28+20+14+4)
    def test_semiplenosseguidos(self): #bien
        bolos = Bolos()
        ronda = [(0, 0), (3, 2), (4, 0), (4, 6), (4, 6), (2, 2), (4, 0), (0, 0), (0, 0), (0, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 5 + 4 + 10+8+6+4 + 2 +4)
    def test_rondaextra(self):
        bolos = Bolos()
        ronda = [(0, 0), (8, 2), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 0), (2, 1)]
        resultado = bolos.puntaje(ronda)
        print(len(ronda))
        self.assertEqual(resultado, 18+10+6)
    def test_2rondaextra(self):
        bolos = Bolos()
        ronda = [(0, 0), (8, 2), (4, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (10, 0),(10,0),(0,1)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 18+10+10+2)

    def test_partida_con_rondas_extra(self):
        bolos = Bolos()
        ronda = [(10, 0), (10, 0), (10, 0), (10, 0), (10, 0), (2, 1), (0, 0), (0, 0), (0, 0), (10, 0), (10, 0),
                     (10, 0)]
        resultado = bolos.puntaje(ronda)
        self.assertEqual(resultado, 30 + 30 + 30 + 22 + 13 + 3 + 30)
