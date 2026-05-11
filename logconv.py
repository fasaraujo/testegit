from math import log10
from math import sqrt
import os
import platform

def arnaPegaSo():
    arnaOs = platform.system()
    return arnaOs

def arnaLimpaTela(qualos):
    if (qualos == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

arnaLimpaTela(arnaPegaSo)
print('-'*40)
print('LOGARITMOS BASE 10')
arnaPassalista = [0.01,0.1,1,10,100,1000]
arnalistaLogaritimiza = [log10(i) for i in arnaPassalista]

for valor,log in zip(arnaPassalista,arnalistaLogaritimiza):
    print(f'Valor {valor} -> log {log}')

arnaValoresParaRaiz = [23,45,11,34,73,81,3459]
arnaRaizesQuafradas = [sqrt(i) for i in arnaValoresParaRaiz]

print('-'*40)
print('RAIZ QUADRADA')
for ponto,raiz in zip(arnaValoresParaRaiz,arnaRaizesQuafradas):
    print(f'Ponto -> {ponto} Raiz Quadrada {raiz:.2f}')
print('-'*40)

# minhanovalita = [processa(i) for i in lista]




