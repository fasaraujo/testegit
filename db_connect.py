import sqlite3
import os

arnaBanco = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dbteste.db")
def arnaConectaDb():
    try:
        arnaSocketdb = sqlite3.connect(arnaBanco)
        arnaSocketdb.cursor()
        print(f'Conexão com o banco {arnaBanco} estabelecida com sucesso')
        return arnaSocketdb
    except Exception as arnaError:
        print(f'Falhao ao conectar no banco {arnaBanco} error -> {arnaError}')
        return None

def arnaCriaTabelas(conexao):
    try:
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS cliente (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL
            )
        """)
        conexao.commit()
        print('Tabela cliente pronta')
    except Exception as arnaError:
        print(f'Erro ao criar tabela -> {arnaError}')


def arnaCloseDb(conexao):
    conexao.close()
    print(f'Conexão com o banco {arnaBanco} encerrada')


def arnaInsereClientes(conexao):
    clientes = [
        ("Ana Silva",),
        ("Bruno Costa",),
    ]
    try:
        cursor = conexao.cursor()
        cursor.executemany("INSERT INTO cliente (nome) VALUES (?)", clientes)
        conexao.commit()
        print(f'{cursor.rowcount} clientes inseridos com sucesso')
    except Exception as arnaError:
        conexao.rollback()
        print(f'Erro ao inserir clientes -> {arnaError}')


def main():
    conexao = arnaConectaDb()
    if conexao:
        arnaCriaTabelas(conexao)
        arnaInsereClientes(conexao)
        print("Banco ok fechando conexão e encerrando")
        arnaCloseDb(conexao)
    else:
        print("Não abriu")

main()