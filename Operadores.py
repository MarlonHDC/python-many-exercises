# a = 10
# b = 5

a = int (input('Entre com o primeiro valor: '))
b = int (input('Entre com o segundo valor: '))
print (type(a))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print ('soma: ' + str (soma)) #str para converter int em string
print ('soma: {}' .format (soma)) # "{} .format" faz a concatenação de tudo já convertendo o necessário
print (subtracao)
print (multiplicacao)
print (divisao)
print (resto)