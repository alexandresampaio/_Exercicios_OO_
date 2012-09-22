#-*-coding:utf-*-

#4) Crie uma classe que modele uma pessoa e permita definir e obter a idade,
# peso e altura da pessoa e que permita fazer a pessoa envelhecer, engordar e #emagrecer. #A cada ano que a pessoa envelhece, sendo a idade dela menor que 21 anos, #ela deve #crescer 1,5 cm.

class Pessoa(object):
    def __init__(self, idade, peso, altura, sexo):
        self._validar_idade_peso_altura_(idade, peso, altura)
        self._idade = idade
        self._peso  = peso
        self._altura = altura
        self._sexo = sexo
    
    def obter_idade(self):
        return self._idade
    
    def envelhecer(self):
        self._idade += 1
        if self._idade <= 21:
            self._altura += 0.15
    
    def engordar(self, kgs):
        self._validar_peso_(kgs)
        self._peso += kgs
    
    def emagrecer(self, kgs):
        self._validar_peso_(kgs)
        self._peso -= kgs
    
    def consultar_peso(self):
        return self._peso
    
    def consultar_peso_e_altura(self):
        return (self.peso, self.altura)
    
    def consultar_altura(self):
        return self._altura
    
    def calcular_peso_ideal(self):
        if self._sexo in ["F", "f", "feminino", "Feminino", "FEMININO"]:
            return round((((62.1)*self._altura) - 44.7),2)
        elif self._sexo in ["M", "m", "masculino", "Masculino", "MASCULINO"]:
            return round((((72.6)*self._altura) - 58),2)
            
    def _validar_idade_peso_altura_(self, idade, peso, altura):
        if idade <= 0 and peso <=0 and altura <=0:
            raise ValueError
   
    def _validar_peso_(self, peso):
        if peso <=0:
            raise ValueError
    
    peso = property(consultar_peso, consultar_peso_e_altura, engordar)
    altura = property(consultar_altura, consultar_peso_e_altura ,envelhecer)
        