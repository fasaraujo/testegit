
def validaOp():
    arnaLoop = True
    while arnaLoop:
        arnaPegaOp = int(input('Entre com a Opção Desejada..: '))
        if (arnaPegaOp == 1 or arnaPegaOp ==2 or arnaPegaOp ==3):
            arnaLoop = False
            return arnaPegaOp
        else:
            continue

def arnaMenu():
    print('1 - Cadastro')
    print('2 - Lista   ') 
    print('3 - <Sair>. ')

def grava():
    arnaPegaTexto = input('Chat..: ')
    with open('log.txt','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{arnaPegaTexto}\n')
    print('Contéudo Gravado com Sucesso!')

def ler():
    with open('log.txt','r',encoding='utf-8') as arquivo:
        for i in arquivo:
            print(i.strip())
    print()
    print('Leitura Concluída')

arnaInterrompe = True  
while arnaInterrompe:  
    arnaMenu()
    arnaGatilho = validaOp()
    if ( arnaGatilho ==1 ):
        grava()
    elif (arnaGatilho ==2 ):
        ler()
    else:
        print('Acionado Sair')
        break
print('Fim de Execução...')



          

      




