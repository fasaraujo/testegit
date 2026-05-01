import json

payload = "carga.json"

try:
    with open(payload,"r",encoding="utf-8") as arquivo:
     res = json.load(arquivo)
    print("-" * 40)
    print(f'Dados recebidos da API {payload}')
    print("-" * 40)
    for ler in res:
       print(f'Nome: {ler['nome']}')
       print(f'Sexo: {ler['sexo']}')

       if not ler['e-mail']:
          print('*E-MAIL NÃO CADASTRADO*')
       else:
        print(f'e-mail: {ler['e-mail']}')
       print("-" *30)
    
except FileNotFoundError:
    print(f'Arquivo {payload} não encontrado')
except Exception as e:
    print(f'Ocorreu uo erro {e}')



