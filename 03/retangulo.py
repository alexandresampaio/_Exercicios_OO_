#-*-coding:utf-8-*-

#3) Crie uma classe que modele um retângulo e permita alterar e consultar os valores 
#dos lados, obter a área e obter o perímetro. 
#Os valores dos lados são obrigatórios. O #retângulo não deve aceitar 
#valores zero nem negativos.


class Retangulo(object):
    def __init__(self,base, altura):
        self._validar_altura_(altura)
        self._validar_base_(base)
        self._base = base
        self._altura = altura
    
    def alterar_altura(self, altura):
        self._validar_altura_(altura)
        self._altura = altura
    
    def consultar_altura(self):
        return self._altura
    
    def alterar_base(self, base):
        self._validar_base_(base)
        self._base = base
    
    def consultar_base(self):
        return self._base
    
    def calcular_area(self):
        return self.base * self.altura
        
    def _validar_altura_(self, altura):
        if altura <= 0:
            raise ValueError
    
    def _validar_base_(self, base):
        if base <= 0:
            raise ValueError
    
    def obter_perimetro(self):
        return ((self.altura*2) + (self.base*2))
    
    base = property(consultar_base, alterar_base)
    altura = property(consultar_altura, alterar_altura) 
        
        