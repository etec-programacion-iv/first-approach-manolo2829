import unittest
from operacion import Operacion

class MyTest(unittest.TestCase):
    def test_suma(self):
        operacion = Operacion()
        self.assertEqual(operacion.suma(3,4),7)
        
if __name__ == '__main__':
    unittest.main()
    