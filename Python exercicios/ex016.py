#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.
#Ex: digite um numero: 6.127
# O numero 6.127 tem a parte inteira 6

import math
numero = float(input('Digite um número real:'))
inteiro = math.trunc(numero)
print('O número {} tem a parte inteira {}'.format(numero, inteiro))