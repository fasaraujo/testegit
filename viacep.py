
import requests
import os
import platform

def arnaLimpaTela():
    arnaSo = platform.system()
    if arnaSo == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

while True:
    arnaLimpaTela()
    arnaCep = int(input('Digite o CEP ..: '))
    url = f'http://viacep.com.br/ws/{arnaCep}/json/'

    try:
        print('Comunicando com a api..')
        arnaResp = requests.get(url)

        if (arnaResp.status_code == 200):
            dados = arnaResp.json()
            print(f'Captura de dados para o CEP - {arnaCep} ...Ok \u2705')

            print('-' * 30)
            print(f'CEP -> {dados['cep']}')
            print(f'LOGRADOURO -> {dados['logradouro']}')
            print(f'COMPLEMENTO -> {dados['complemento']}')
            print(f'BAIRRO -> {dados['bairro']}')
            print(f'LOCALIDADE -> {dados['localidade']}')
            print(f'UF -> {dados['uf']}')
            print(f'ESTADO -> {dados['estado']}')
            print('-' * 30)

            print('Deseja realizar uma nova consulta [S/N]')
            arnaContinua = input().upper()
            if (arnaContinua == 'S'):
                continue
            else:
                break

        elif (arnaResp.status_code == 404):
            print(f'Cep informado {arnaCep} não encontrado')
        else:
            print(f'Erro no retorno da api -> {arnaResp.status_code}')

    except Exception as e:
        print(f'Erro --> {e}')
                
print('Obrigado por utilizar nosso serviço \U0001F600')
          


