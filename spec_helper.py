import unittest
from should_dsl import should
from bola import Bola
from quadrado import Quadrado
from retangulo import Retangulo


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
        self.quadrado = Quadrado(6)
    
    def test_alterar_lado(self):
        self.quadrado.alterar_lado(3)
        self.quadrado.consultar_lado() |should| equal_to(3)
        
    def test_consultar_lado(self):
        self.quadrado.consultar_lado() |should| equal_to(6)
    
    def test_nao_aceita_valor_lado_negativo_nem_0(self):
        (self.quadrado._validar_lado, 0) |should| throw(ValueError)
    
    def test_faz_tudo_e_mostra_a_area(self):
        self.quadrado.consultar_lado() |should| equal_to(6)
        self.quadrado.alterar_lado(20) 
        self.quadrado.calcular_area() |should| equal_to(400)
        self.quadrado.consultar_lado() |should| equal_to(20)
        
class TestRetangulo(unittest.TestCase):
     def setUp(self):
         self.retangulo = Retangulo(3,5)
     
     def test_alterar_e_consltar_altura(self):
         self.retangulo.alterar_altura(2)
         self.retangulo.consultar_altura() |should| equal_to(2)
     
     def test_alterar_e_consultar_base(self):
         self.retangulo.alterar_base(6)
         self.retangulo.consultar_base() |should| equal_to(6)
     
     def test_calcular_area(self):
         self.retangulo.calcular_area() |should| equal_to(15)
         
     def test_nao_aceita_valores_negativos_nem_0(self):
         (self.retangulo._validar_altura_, 0) |should| throw(ValueError)
         (self.retangulo._validar_base_, -6)  |should| throw(ValueError)
     
     def test_calcular_area_e_obter_perimetro(self):
         self.retangulo.alterar_altura(5)
         self.retangulo.alterar_base(4)
         self.retangulo.consultar_altura() |should| equal_to(5)
         self.retangulo.consultar_base() |should| equal_to(4)
         self.retangulo.calcular_area() |should| equal_to(20)
         self.retangulo.obter_perimetro() |should| equal_to(18)
         
         
         
         
         
         

if __name__ == "__main__":
    unittest.main()