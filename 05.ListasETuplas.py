lista = [12, 10, 5, 7]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']


## TUPLAS NÃO PODEM SER ALTERADAS. A SINTAXE SE ESCREVE COM PARÊNTESES "()"
tupla  = (1, 10, 12, 14)
print(tupla[2])
## QUANTOS ELEMENTOS EXISTEM NA LISTA OU TUPLA
print(len(tupla))
print (len(lista_animal))
# tupla[0] = 12 # Ao tentar alterar o valor pelo índice ocorre um erro

## CONVERTER UMA LISTA PARA UMA TUPLA
tupla_animal = tuple (lista_animal)
print(type(tupla_animal))
print(tupla_animal)

## CONVERTER TUPLA EM LISTA
lista_numerica = list (tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)



## LISTAS
#print(lista_animal[1])

## ALTERAR ITEM DA LISTA POR ÍNDICE
# lista_animal[0] = 'macaco'
# print(lista_animal)

## MULTIPLICAR NA LISTA
# nova_lista = lista_animal * 3
# print(nova_lista)

## ORDENAR AS LISTAS COM "SORT"
# lista.sort()
# lista_animal.sort()
# print(lista)
# print(lista_animal)
## REVERTENDO (INVERTENDO) ORDENAÇÃO
# lista_animal.reverse()
# print(lista_animal)


## PERCORRER LISTA
# for x in lista_animal:
#     print(x)

## ENCONTRAR VALORES (MÁXIMO, MÍNIMO E SOMA) NA LISTA
# print(sum(lista))
# print(max(lista))
# print(min(lista))

## ENCONTRAR E, CASO NÃO TENHA, INCLUIR ITEM NA LISTA
# if 'gato' in lista_animal:
#     print ('Existe um gato na lista')
# else:
#     print('Não existe um lobo na lista')
#
# if 'lobo' in lista_animal:
#     print('Existe um gato na lista')
# else:
#     print('Não existe um lobo na lista. Será incluído. ')
#     lista_animal.append('lobo') # "append" adiciona o item
#     print (lista_animal)

## RETIRAR ÚLTIMO ITEM DA LISTA COM "POP"
# lista_animal.pop(1) # Podemos colocar índice no parâmetro
# print(lista_animal)

## REMOVENDO UM ELEMENTO CONHECIDO COM "REMOVE"
# lista_animal.remove('elefante')
# print(lista_animal)


