
lista = [1, 10]

try:
    arquivo = open('teste.txt', 'r')
    divisao = 10 / 1
    numero = lista[1]

# sempre adicionar excessões das mais especializadas para as mais genéricas
except ZeroDivisionError:
    print('Não é possível realizar uma divisão por 0')
except ArithmeticError:
    print('Houve um erro ao realizar uma operação aritimética')
except IndexError:
    print('Erro ao acessar um ídice inválido da lista')
except BaseException as ex: # BASE EXCEPT É A MÃE DAS CLASSES DE EXCESSÕES
    print('erro desconhecido. Erro: {} '.format(ex))
else: # EXECUTA CASO NÃO ACONTECA NENHUMA EXCESSÃO.
    print('Executa quando não ocorre excessão')
finally: # TUDO O QUE ESTÁ NO FINALLY SERÁ EXECUTADO, DANDO ERRO, OU NÃO
    print ('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()