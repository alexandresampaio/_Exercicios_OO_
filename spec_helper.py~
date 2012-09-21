import unittest
from should_dsl import should
from bola import Bola
from quadrado import Quadrado


class Teste_Bola(unittest.TestCase):
    def test_criar_bola(self):
        bola = Bola("Verde")
    
    def test_alterar_cor_da_bola(self):
        bola = Bola("Verde")
        bola.alterar_cor("Vermelha")
        bola.obter_cor() |should| equal_to("Vermelha")
    def test_consultar_cor_da_bola(self):
        bola = Bola("lilas")
        bola.obter_cor() |should| equal_to("lilas")

class Test_Quadrado(unittest.TestCase):
    def setUp(self):
        self.quadrado = Quadrado(6):
    
    def alterar_lado(self, lado):
        self.quadrado.alterar_lado(3)
        self.quadrado.obter_lado() |should| equal_to(3)
        

if __name__ == "__main__":
    unittest.main()