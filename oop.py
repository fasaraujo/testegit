# Exercicio de criacao e manipulacao de classes e objetos.
# Criar a classe Televisao c/ os atributos (ligada,canal)
# instanciar um objeto tv1 e verificar os atributos.

class Televisao():
    def __init__(self): # chama construtor
        self.ligada = True
        self.canal = 4
    def canaDown(self): # cria método
        self.canal -=1
    def canalUp(self): # cria método
        self.canal +=1
    def turnOnOff(self, status): # cria método
        self.ligada = status

tv1 = Televisao()
print(f'A televisão está -> {tv1.ligada} no canal: {tv1.canal}')
tv1.canaDown()
print(f'A televisão está -> {tv1.ligada} no canal: {tv1.canal}')
# era canal 4 espero canal 3

tv1.ligada = False
tv1.canal = 8

print(f'A televisão está -> {tv1.ligada} no canal: {tv1.canal}')
tv1.canalUp()
print(f'A televisão está -> {tv1.ligada} no canal: {tv1.canal}')
# era canal 8 espero canal 9

# HERANÇA
# Criar uma classe chamada Tvnova / herdar os atributos e métodos de Televião
# e incluir dois novos atributos chamados Marca e Modelo.

class Tvnova(Televisao): # herda atributos e comportamentos 
    def __init__(self,marca,modelo):
        super().__init__()
        self.marca = marca
        self.modelo = modelo

tv2 = Tvnova('Sony','Smart 8k 44pol')
print(f'A televisão {tv2.marca} {tv2.modelo} -> {tv2.ligada} no canal: {tv2.canal}') 
tv2.canalUp()
print(f'A televisão {tv2.marca} {tv2.modelo} -> {tv2.ligada} no canal: {tv2.canal}')


 
        