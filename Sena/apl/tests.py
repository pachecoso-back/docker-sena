from django.test import TestCase
from apl.models import  Categoria

class PruebaBasica(TestCase):
    def test_verificar_entorno(self):
        self.assertEqual(1+1,2)
    
    def test_crear_categoria(self):
        categoria = Categoria.objects.create(nombre='Froijol')
        consulta = Categoria.objects.get(nombre='Froijol')
        self.assertTrue(consulta.exists())
