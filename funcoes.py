import math

def fatorial(n):
    ''''
    Param 1: Passe o número que deseja calcular o fatorial
    ex: fatorial(5) 

    '''
    fatorial = 1
    for i in range(1,n+1):
        fatorial *= i
    return fatorial

def valida(dado):
    if (dado >= 0):
        return True
    else:
        return False

arnaLoop = True
while (arnaLoop):
    arnaPegaNumero = int(input('Entre com o número ..: '))
    if valida(arnaPegaNumero):
        print(f'Fatorial de {arnaPegaNumero} é ..:',fatorial(arnaPegaNumero))
        print()
    else:
        print('Dado invalido ...')
        continue
    arnaContinua = input('Continua S/N ? ')
    if (arnaContinua.upper() == "S"):
        continue
    else:
        break
print('Fim de Execução ...')

# testando pela biblioteca math
#pegaNum2 = int(input('Entre com o Numero ..: '))
#print(math.factorial(pegaNum2))
#help(fatorial)


