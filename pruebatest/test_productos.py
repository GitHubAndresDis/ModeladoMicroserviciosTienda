import unittest
from productos import *

class TestProductos(unittest.TestCase):

    def test_nombre(self):
        productos = Productos()
        assert productos.nombreProducto("Manzana", 12)is None
       
        
    def test_precio(self):   
        productos = Productos()
        assert  5 == productos.listarPrecio(5)
