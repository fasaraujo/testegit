## Exercicio 01
# Print de inteiros de 3 a 12 com 12 incluido
# 

def tela():
    print('######################')
    print('#     LANCHONETE     #')
    print('######################')
    print()
    print('1 -  Cochinha - R$ 5,00 ')
    print('2 -  Pastel   - R$ 7,00 ')
    print('3 -  Café     - R$ 4,00 ')
    print('4 -  Suco.    - R$ 6,00 ')
    print('5 -  <SAIR>')

print('##### com While ####')
arnaLoop = 3
while (arnaLoop <= 12):
    if (arnaLoop % 2 == 0):
        print(f'Inteiro ..: {arnaLoop}')
    arnaLoop += 1
print('Fim da Execução..')


print('##### com For ####')
for i in range(3,13):
    if (i % 2 == 0):
        print(f'Inteiro ..: {i}')
print('Fim de Execução...')

while True:
    tela()
    arnaPegaMenu = int(input('Entre com a Opção Desejada ..:'))
    if (arnaPegaMenu == 1):
        arnaValor = 5.00
        arnaQuant = int(input('Quantidade ..: '))
        arnaBill = arnaQuant * arnaValor
        print(f'Bill ..: {arnaBill:.2f}')

    elif (arnaPegaMenu == 2):
        arnaValor = 7.00
        arnaQuant = int(input('Quantidade ..: '))
        arnaBill = arnaQuant * arnaValor
        print(f'Bill ..: {arnaBill:.2f}')

    elif (arnaPegaMenu == 3):
        arnaValor = 4.00
        arnaQuant = int(input('Quantidade ..: '))
        arnaBill = arnaQuant * arnaValor
        print(f'Bill ..: {arnaBill:.2f}')

    elif (arnaPegaMenu == 4):
        arnaValor = 6.00
        arnaQuant = int(input('Quantidade ..: '))
        arnaBill = arnaQuant * arnaValor
        print(f'Bill ..: {arnaBill:.2f}')

    elif (arnaPegaMenu == 5):
        break
    else:
        print('Produto Invalido')
print('Fim de Execução...')

