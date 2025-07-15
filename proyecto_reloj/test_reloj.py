import unittest
from reloj.reloj_24h import Reloj24h

class TestReloj24h(unittest.TestCase):
    def test_mostrar(self):
        reloj = Reloj24h(9, 5, 7)
        self.assertEqual(reloj.mostrar(), "09:05:07")

    def test_adelantar_minuto_simple(self):
        reloj = Reloj24h(10, 15, 0)
        reloj.adelantar_minuto()
        self.assertEqual(reloj.mostrar(), "10:16:00")

    def test_adelantar_minuto_cambio_hora(self):
        reloj = Reloj24h(14, 59, 0)
        reloj.adelantar_minuto()
        self.assertEqual(reloj.mostrar(), "15:00:00")

    def test_adelantar_minuto_reseteo_medianoche(self):
        reloj = Reloj24h(23, 59, 59)
        reloj.adelantar_minuto()
        self.assertEqual(reloj.mostrar(), "00:00:59")

    def test_actualizar_hora(self):
        reloj = Reloj24h(0, 0, 0)
        reloj.actualizar_hora(12, 30, 45)
        self.assertEqual(reloj.mostrar(), "12:30:45")

    def test_es_igual_true(self):
        reloj1 = Reloj24h(10, 20, 30)
        reloj2 = Reloj24h(10, 20, 30)
        self.assertTrue(reloj1.es_igual(reloj2))

    def test_es_igual_false(self):
        reloj1 = Reloj24h(10, 20, 30)
        reloj2 = Reloj24h(11, 20, 30)
        self.assertFalse(reloj1.es_igual(reloj2))

if __name__ == '__main__':
    unittest.main()
