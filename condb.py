import sqlite3
import os

arnaBanco = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbteste.db")

def arnaConnectaDb():
    try:
        arnaSocketDb = sqlite3.connect(arnaBanco)
        arnaSocketDb.cursor()
        print(f'Conexão com a base {arnaBanco} estabelecida')
        return arnaSocketDb
    except Exception as arnaErrorCon:
        print(f'Falha ao conectar no {arnaBanco} -> {arnaErrorCon}')
        return None
    
def arnaCloseDb(conexao):
    conexao.close()
    print("Conexão Encerreda com sucesso")

def arnaCriaTabela(conexao):
    conexao.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT
        )
    """)
    conexao.commit()

def arnaMain():
    arnaStream = arnaConnectaDb()
    if arnaStream:
        print(f'Conexão estabelecida com sucesso pronto para uso')
        arnaCriaTabela(arnaStream)
        arnaCursor = arnaStream.cursor()
        arnaCursor.execute("SELECT * FROM cliente")
        arnaListaRecs = arnaCursor.fetchall()
        print(f'Total de registros existentes {len(arnaListaRecs)}')
        for i in arnaListaRecs:
            print(f'Usuario: {i[1]}') # usa o iterador com a posição da tupla de interesse

        arnaPeganome = input('Digite o nome: ')
        arnaCursor.execute("INSERT INTO cliente (nome) VALUES (?)",(arnaPeganome,))      
        arnaStream.commit()
        arnaCloseDb(arnaStream)
        print('Gravado com sucesso..')
    else:
        print("Falha! não abriu")

arnaMain()
