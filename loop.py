
from datetime import datetime

def log(humano,bot):
    with open('log.arn','a',encoding='utf-8') as arquivo:
        arquivo.write(f'{humano}\n')
        arquivo.write(f'{bot}\n')
def lstlog():
    with open('log.arn','r',encoding='utf-8') as log:
        for i in log:
            print(i.strip())

print('Bem Vindo ao arnaBot ver 1.0 para sair tecle x')

mensagens = []
while True:
    arnaPergunta = input('Humano: ...: ')
    arnaPerguntaBot = input('Bot: ')
    if arnaPerguntaBot.lower() == 'x':
        log('Interrompido','Pelo Usuário')
        break
    else:
        tempo = datetime.now()
        arnaTimeStamp = tempo
        mensagens.append(f'Humano: {arnaPergunta} {arnaTimeStamp}')
        mensagens.append(f'Bot: {arnaPerguntaBot} {arnaTimeStamp} ')
        log(f'{arnaTimeStamp} Humano: {arnaPergunta}',f'{arnaTimeStamp} Bot: {arnaPerguntaBot}')
        continue
print('Chat encerrado')

y = input('Deseja ver o log [S/N] ? ')
if y.lower() == 's':
    lstlog()
print('So, Bye Bye')

print(mensagens) # imprime conteudo armazenado na lista
print(f'Interações Armazenadas ..: {len(mensagens)}')
