# Copyright fasaraujo 
import math

""""
Obs: Código não considera o impacto da componente vertical e horizontal 
da influência do vento.

Definicao de Constantes

Peso do cabo km/m -> 0.100
flecha = 1% do vão -> Calculo dinamico

T = (pxv2)/(8*flecha) Kgf

"""
def vao():
    arnaLoop = True
    arnaAcumuladorVao = 0
    arnaCuboTrecho = 0
    while (arnaLoop):
        try:
            arnaPegaVao = float(input('Entre com o Vão ..: '))
            arnaAcumuladorVao += arnaPegaVao
            arnaPegacubo = math.pow(arnaPegaVao,3)
            arnaCuboTrecho += arnaPegacubo
            arnaVaoRegulador = math.sqrt(arnaCuboTrecho/arnaAcumuladorVao)
        except ValueError:
            print('Valor tem que ser númerico <Press Any key to continue>')
        finally:
            arnaContinua = input('Continua S/N ').upper()
            if (arnaContinua == 'S'):
                continue
            else:
                break
    return arnaVaoRegulador

arnaVaoReg = vao()
arnaFlecha = arnaVaoReg * 0.01
arnaPesoCabo = 0.100
arnaTracaoCabo = ((arnaPesoCabo*(arnaVaoReg**2))/(8*arnaFlecha))
arnaFr = math.sqrt(math.pow(arnaTracaoCabo,2) + math.pow(arnaTracaoCabo,2))
#print(f'Vão Acumulado em (Mtrs) do trecho -> {arnaVao:.2f}')
print(f'Vão Regulador no trecho -> {arnaVaoReg:.2f} Mtrs')
print(f'Tração/Esforço no Cabo (Passagem) -> {arnaTracaoCabo:.2f} Kgf')
print(f'Esforço Resultante (Poste de Esquina) -> {arnaFr:.2f} Kgf')
