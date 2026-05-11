x = 5
while( x <= 25):
    print(x)
    x+=5

list1 = []
list2 = []
for i in range(100,1000,10):
    list1.append(i)

i = 100
while( i <= 1000):
    list2.append(i)
    i+= 10

# funcao qque compara se as duas listas sao iguais.

def valida(lista1,lista2):
    for a,b in zip(lista1,lista2):
        if (a==b):
            #x = True
            print('Sao Iguais....')
        else:
            #x = False
            print('Sao Diferentes....')
        #return x

valida(list1,list2)

def testa(palavra):
    if (palavra != "casa"):
        return 1
    else:
        return 0

resp = testa("casa")
print(resp)


for i in range(7,25,3):
    print(f'Número ..: {i}')


for i in range(10,20):
    for j in range(10,20,2):
        print(f'{i} - {j} i+j >= {i+j}')
              
y = (1,3,4,6)
z = (1,7,0,6)

for p,s in zip(y,z):
    if ( p == s):
        print(f'Valor {p} é == ao valor {s}')
    else:
        print(f'Valor {p} é # ao valor {s}')