import os
import platform

def arnaPegaOs():
    arnaOs = platform.system()
    return arnaOs

def arnaClear():
    x = arnaPegaOs()

    if (x == "Windows"):
        os.system("cls")
    else:
        os.system("clear")

def cadastro_livros():
    arnaLivro = input('Livro ..:')
    arnaAutor = input('Autor..: ')
    arnaEditora = input('Editora..: ')
    arnaIsbn = input('Isbn ..: ')

    arnaDict = {
        "nome": arnaLivro,
        "autor": arnaAutor,
        "editora": arnaEditora,
        "isbn": arnaIsbn
    }
    return arnaDict

arnalista = []

while True:
    arnaClear()
    y = cadastro_livros()
    arnaGrava = input('Grava os dados [s/n] ').lower()
    if (arnaGrava == "n"):
        break
    else:
        arnalista.append(y)
        arnaContinua = input('Continua Cadastro s/n ').lower()
        if (arnaContinua == "n"):
            break
        else:
            continue
        
for i in arnalista:
    print(i)
    
print('Fim de execução')

