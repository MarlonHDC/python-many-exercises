## CONJUNTOS SÃO CARACTERIZADOS POR "{}"
# conjunto = {1, 2, 3, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print (conjunto)


## UNINDO DOIS CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {} ' .format(conjunto_uniao))

## INTERCECÇÃO DE CONJUNTTOS
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Intersecção: {} '.format(conjunto_interseccao))

## CONJUNTO DIFERENÇA
conjunto_diferenca = conjunto.difference(conjunto2) # Só o que consta no conjunto um
print('Diferença entre 1 e 2: {} ' .format(conjunto_diferenca))
conjunto_diferenca = conjunto2.difference(conjunto) # Só o que consta no conjunto dois
print('Diferença entre 2 e 1: {} ' .format(conjunto_diferenca))

## DIFERENÇA SIMÉTRICA
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simétrica: {} ' .format(conjunto_diff_simetrica))

## PERTINENCIA SUBSET
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print ('A é subconjunto de B: {} ' .format(conjunto_subset))

## SUPERSET
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {} ' .format(conjunto_superset))

## CONVERTER UMA LISTA PARA CONJUNTO PARA RETIRAR DUPLICIDADE
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista) # "set" converte para conjunto
print(conjunto_animais)
## INVERTENDO CONVERSÃO DE LISTA PARA CONJUNTO
lista_animais = list(conjunto_animais) # "list" retorna para lista
print(lista_animais)


