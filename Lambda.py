
## LAMBDA
## COM LAMBDA PODEMOS REESCREVER O CÓDIGO ABAIXO:
def contador_letras(lista_palavras):
    contador = []
    for x  in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador
## EM APENAS UMA LINHA UTILIZANDO DESTA FORMA COM LAMBDA
contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

## CALCULADORA CO LAMBDA
soma = lambda a,b: a + b
subtracao = lambda a, b: a -b

print(soma(5, 10))
print(subtracao(10, 5))

## CALCULADORA COMPLETA COM LAMBDA
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicacao']
print('A soma é: {} ' .format(soma(10, 5)))
print('A multiplicacao é: {} ' .format(multiplicacao(10, 2)))