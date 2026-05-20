import sqlite3
import os
import platform

def conectaDb():
    try:
        arnaPegaPath = os.path.join(os.path.dirname(os.path.abspath(__file__)),"dbteste.db")
        arnaConexao = sqlite3.connect(arnaPegaPath)
        arnaConexao.cursor()
        print(f'Conectado banco -> {arnaPegaPath} com sucesso')
        return arnaConexao
    except Exception as err:
        print(f'Falha na Conexão com o banco..{err}')
        return None
           
def arnaDetectaOs():
    arnaSo = platform.system()
    return arnaSo

def arnaClearscreen():
    if ( arnaDetectaOs == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def arnaTela():
    print('--- TESTE DE CRUD SQLITE3 ---')
    print()
    print('     - (1) Cadastrar - ')
    print('     - (2) Alterar   - ')
    print('     - (3) Excluir   - ')
    print('     - (4) Sair      - ')
    print()
    print('-----------------------------')

def arnaChoice():
    arnaTupla = (1,2,3,4)
    arnaPegachoice = int(input('Entre com a opção desejada ..: '))
    while arnaPegachoice not in arnaTupla:
        arnaPegachoice = int(input('Entre com a opção desejada ..: '))
    if (arnaPegachoice == 1):
        arnaCad()
    elif (arnaPegachoice == 2):
        print('chamou alterar')
    elif (arnaPegachoice == 3):
        print('chamou excluir')
    else:
        print('chamou sair')

def arnaCloseDb(conexao):
    try:
        conexao.close()
        print('Banco fechado com sucesso!!')
    except Exception as errCloseBase:
        print(f'Erro -> {errCloseBase}')

def arnaCad():
    arnaConexao = conectaDb()
    arnaCursor = arnaConexao.cursor()
    arnaLoop = True

    while arnaLoop:

        #arnaCoutLinhas = arnaCursor.rowcount
        #print(f'Total de registros na base: {arnaCoutLinhas}')
        
        arnaNome = str(input('Nome ..: ')).lower()
        arnaCpf = int(input('Cpf ..: '))
        arnaEmail = str(input('email ..: ')).lower()
    
        try:
            arnaCursor.execute(
                "INSERT INTO clientes2 (nome, cpf, email) VALUES (?, ?, ?)",
                (arnaNome, arnaCpf, arnaEmail)
            )
            arnaConexao.commit()
            print('Gravado com sucesso')
           
        except Exception as erroGrava:
            print(f'Erro ao gravar -> {erroGrava}')
        finally:
            arnaSimNao = input('Continua Cadastrando [S/N] ?').lower()
            if (arnaSimNao == 's'):
                continue
            else:
                arnaCloseDb(arnaConexao)
                arnaLoop = False

arnaClearscreen()
arnaTela()
arnaChoice()
