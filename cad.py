""""
Criar uma rotina de cadastro e armazenar em um dicionario com os
seguintes campos:
1. Nome
2. Sexo
3. e-mail

"""
import json

def menu():
    print(" 1 - Cadastrar")
    print(" 2 -  Sair" )

baseDeDados = []
while True:
    menu()
    arnaOpcao = int(input("Selecione a Opção Desejada : "))
    if ( arnaOpcao == 2):
        break
    else:
        # Selecionou 1 - Cadastrar
        arnaPegaNome = input("Nome ..: ").upper()
        arnaPegasexo = input("Sexo ..: ").upper()
        arnaPegaEmail = input("e-mail ..: ").lower()

        # cria dicionario e adiciona os elementos

        dict = {"nome": arnaPegaNome,
                "sexo": arnaPegasexo,
                "e-mail": arnaPegaEmail
        }

        baseDeDados.append(dict)

        print(f'Adicionado {arnaPegaNome} - {arnaPegasexo} - {arnaPegaEmail}')
        print()
        continue
    
with open("carga.json","w",encoding="utf-8") as f:
    json.dump(baseDeDados,f,indent=4,ensure_ascii=False)

print("Dados exportados")
print("FIM DE OPERAÇÃO")

#print(json.dumps(baseDeDados, indent=4))










