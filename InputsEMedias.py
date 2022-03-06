
# EXERCÍCIO DE MÉDIA COM IF E INPUTS DE NOTAS
a = int(input('Primeiro bimestre'))
if a > 10:
    a = int(input('Você digitou errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre'))
if b > 10:
    b = int(input('Você digitou errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre'))
if c > 10:
    c = int(input('Você digitou errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre'))
if d > 10:
    d = int(input('Você digitou errado. Quarto bimestre: '))

media = (a + b + c + d) /4
print ('média: {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print ('média: {}' .format(media))
# else:
#     print ('foi informada alguma nota errada')


#EXERCÍCIO DE IF + ACHAR O NÚMERO PAR
# a = int(input ('Entre com o primeiro valor: '))
# b = int(input ('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
#
# if resto_a == 0 or not resto_b > 0:
#     print ('foi digitado um número par')
# else:
#     print('nenhum número par foi digitado')

# EXERCÍCIO DE IF
# a = int (input('Peimeiro valor: '))
# b = int (input('Segundo valor: '))
# c = int (input('Terceiro valor: '))
#
# if a > b and a > c:
#     print ('o maior número é {} ' .format(a))
# elif b> a and b > c:
#     print('o maior número é {} ' .format(b))
# else:
#     print ('o maior número ´r {} ' .format(c))
# print ('final do programa') # a identação indica qual bloco a funcionalidade está inserida