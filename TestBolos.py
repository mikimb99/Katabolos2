import unittest
from Bolos import Bolos


class TestBolos(unittest.TestCase):

    def test_tiradassuman0(self):
        bolos = Bolos()
        ronda = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
        resultado= bolos.puntaje(ronda)
        self.assertEqual(resultado,0)
