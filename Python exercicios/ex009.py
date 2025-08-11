#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada
numero = int(input('Digite um número inteiro:'))
numero1= numero*1
numero2= numero*2
numero3= numero*3
numero4= numero*4
numero5= numero*5
numero6= numero*6
numero7= numero*7
numero8= numero*8
numero9= numero*9
numero10= numero*10
print('Tabuada de {0}: \n {0} x 1 = {1} \n {0} x 2 = {2} \n {0} x 3 = {3}\n'.format(numero, numero1, numero2, numero3))

print('-' * 12)
# {:2} todos terão 2 digitos
print('{} x {:2} = {}'.format(numero, 1, numero*1))
print('{} x {:2} = {}'.format(numero, 2, numero*2))
print('{} x {:2} = {}'.format(numero, 3, numero*3))
print('{} x {:2} = {}'.format(numero, 4, numero*4))
print('{} x {:2} = {}'.format(numero, 5, numero*5))
print('{} x {:2} = {}'.format(numero, 6, numero*6))
print('{} x {:2} = {}'.format(numero, 7, numero*7))
print('{} x {:2} = {}'.format(numero, 8, numero*8))
print('{} x {:2} = {}'.format(numero, 9, numero*9))
print('{} x {:2} = {}'.format(numero, 10, numero*10))
print('-' * 12)