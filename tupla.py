
# ESTRUTURA DE TUPLAS
t = ('um','um','dois',3,4,5)

print(f'Tupla -> {t} ')
print(f'Tamanho da tupla -> {len(t)} ')
print(f'Quantas vezes UM se repete -> {t.count("um")} ')

arnaContaElemento = ()
for index,i in enumerate(t):
    #print(f'Elemento -> {i} posição na tupla {index}')
    if (i not in arnaContaElemento):
        arnaContaElemento += (i,)
print(arnaContaElemento)
#################

# ESTRUTURA DE DICIONARIOS 
# chave:valor

arnaStore = [] 
arnaContinua = True
while arnaContinua:
    arnaDict = {}
    arnaNome = input('Produto ..: ').lower()
    if (arnaNome == 'x'):
        arnaContinua = False
    else:
        arnaPreco = float(input('Preço ..: '))
        arnaDict['produto'] = arnaNome
        arnaDict['preco'] = arnaPreco
        #continue
        arnaStore.append(arnaDict)
print('Listando produtos cadastrados')


for i in arnaStore:
    print(i)






