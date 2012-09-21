#-*-coding:utf-8-*-s

#2) Crie uma classe que modele um quadrado e permita definir, 
#alterar e consultar o tamanho dos lados e obter a área.

class Quadrado(object):
    def __init__(self, lado):
        self._validar_lado(lado)
        self._lado = lado
    
    def alterar_lado(self, novo_lado):
        self._validar_lado(novo_lado)
        self._lado = novo_lado
    
    def consultar_lado(self):
        return self._lado
    
    def calcular_area(self):
        return self._lado * self.lado
    
    def _validar_lado(self, lado):
        if lado <= 0:
            raise ValueError
    
    lado = property(consultar_lado, alterar_lado)