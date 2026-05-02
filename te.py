''''
Calcula a taxa de juros equivaliente

tx.quero = ((1+txtenho)^txquero/txtenho - 1) *100

'''

from math import pow as e
import os
import platform

def arnaLimpa():
    arnaQualSistema = platform.system()
    if arnaQualSistema == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def arnaCalcTxEq(txtenho,pquero,ptebho):
    arnaConverteTx = 1+(txtenho/100)
    arnaConverteTempo = pquero/ptebho
    resParaRetorno = ((e(arnaConverteTx,arnaConverteTempo)-1)*100)
    return resParaRetorno

def tela():
    print('------------------------------------------')
    print('- Calculadora de Taxa Juros Equivalentes -')
    print('-       Copyright fasaraujo 2026.        -')
    print('------------------------------------------')

def arnaValidaResp():
    j = input('Deseja Realizar Outro Calculo [S/N] ..:').lower()
    while (j != 's' and j != 'n'):
        j = input('Deseja Realizar Outro Calculo [S/N] ..:').lower()
    return j

#resposta = arnaCalcTxEq(1.0,12,1)
#print(f'{resposta:.4f} %')

while True:
    arnaLimpa()
    tela()
    print()
    x = float(input('Qual a taxa que você tem ? ..: '))
    y = int(input('Qual periodo que você tem ? ..: '))
    z = int(input('Qual periodo que você Quer ? ..: '))
    print('-'* 30)
    print()
    arnaTxEquivalente = arnaCalcTxEq(x,z,y)
    print(f'Taxa Equivalente é -> {arnaTxEquivalente:.4f} %')
    print()
    resp = arnaValidaResp()
    if (resp == 's'):
        continue
    else:
        break
print('Obrigado Por Utilizar Nosso Serviço!!')    
