import os
import platform
import requests
import time

def limpatela():
    qualOs = platform.system()
    print(f'Sistema operaciona detectado .. {qualOs}')
    time.sleep(3)

    if (qualOs == 'Windows'): # eita trem ruim 
        os.system('cls')
    else:
        os.system('clear')

arnaPegaUrl = 'http://url.com'
arnaRes = requests.get(arnaPegaUrl)
if (arnaRes.status_code == 503):
    # servico indisponivel
    pass
elif (arnaRes.status_code == 404):
    pass
    # nao encontrado
else:
    pass
    # ok
    dados = arnaRes.json()


# --- versão melhorada ---
#
# ERROS_HTTP = {
#     400: 'Requisição inválida',
#     401: 'Não autorizado',
#     403: 'Acesso proibido',
#     404: 'Recurso não encontrado',
#     429: 'Muitas requisições — limite excedido',
#     500: 'Erro interno no servidor',
#     502: 'Bad gateway',
#     503: 'Serviço indisponível',
#     504: 'Timeout do gateway',
# }
#
# try:
#     arnaRes = requests.get(arnaPegaUrl, timeout=10)
#     codigo = arnaRes.status_code
#
#     if 200 <= codigo < 300:
#         dados = arnaRes.json()
#     elif codigo in ERROS_HTTP:
#         print(f'Erro {codigo}: {ERROS_HTTP[codigo]}')
#     elif 400 <= codigo < 500:
#         print(f'Erro do cliente ({codigo})')
#     elif 500 <= codigo < 600:
#         print(f'Erro do servidor ({codigo})')
#     else:
#         print(f'Status inesperado: {codigo}')
#
# except requests.exceptions.ConnectionError:
#     print('Erro: não foi possível conectar ao servidor')
# except requests.exceptions.Timeout:
#     print('Erro: tempo de resposta esgotado')
# except requests.exceptions.RequestException as e:
#     print(f'Erro na requisição: {e}')



xdict = {
    200:'Tudo certo mano',
    400: 'Ops!! Algo deu errado mano',
    300: 'Não faco a manor ideia mamo'
}


for chave,valor in xdict.items():
    if 'Ops!!' in valor:
        print(f'Encontrei (Ops!!) em {chave} > {valor}')
    
    print('Nada encontrado dentro da estrutura de dados')

