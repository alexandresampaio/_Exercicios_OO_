#-*-coding:utf-8-*-s

#2) Crie uma classe que modele um quadrado e permita definir, 
#alterar e consultar o tamanho dos lados e obter a área.

class Quadrado(object):
    def __init__(self,lado):
        self.lado = lado
    
    def alterar_lado(self, novo_lado):
        self.lado = novo_lado
        