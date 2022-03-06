
# imprimir números primos
div = 0
a = int(input ('Entre con o número: '))
for x in range (1, a+1):
    resto = a % x
    print (x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print ('número {} é primo ' .format(a))
else:
    print('número {} não é primo ' .format(a))

# # imprimir um range de 100
# for x in range (1, 101):
#     print(x)