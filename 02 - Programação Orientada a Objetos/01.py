class bicicleta:
    def __init__(self,cor,modelo,ano,valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
    def buzinar(self):
        print("Plim Plim...")
    def parar(self):
        print("Parando")
        print("Bicicleta parada")
    def correr(self):
        print("Vrummmm....")
    def __str__(self) -> str:
        return f"Bicicleta:{self.cor}.{self.ano},{self.valor}"
    def _str_(self):
        return f"{self.__class__.__name__}:{', '.join([f"{chave}={valor}"for chave,valor in self.__dict__.items()])}"        

b1 = bicicleta("vermelha","caloi",2022,600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor,b1.modelo,b1.valor,b1.ano)

b2 = bicicleta("verde","Monarc",2000,1988)
bicicleta.buzinar(b2)
print(b2)