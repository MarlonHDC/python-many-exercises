## PARA FAZER IMPORTAÇÕES DE OUTRAS CLASSES
from Televisao import Televisao
from Calculadora1 import  Calculadora

## ACESSANDO DIRETAMENTE O MÉTODO (SEM CLASSE) "CONTADOR_LETRAS"
from ContadorLetras import contador_letras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    calculadora = Calculadora(5, 10)
    print(calculadora.soma())

    lista = ['cachorro', 'gato', 'elefante']
    total_letras = contador_letras(lista)
    print('total de letras por palavra da lista: {} ' .format(total_letras))



