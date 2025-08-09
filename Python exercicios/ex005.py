# Faça um programa que leia um número inteiro e mostre na tela o seu sucessos e seu antecessor
numero=int(input('digite um número:'))
antecessor=numero-1
sucessor=numero+1
print('O número que antecede {} é {} e o sucessor é {}'.format(numero, antecessor, sucessor))

print('O número que antecede {} é {} e o sucessor é {}'.format(numero,(numero-1), (numero+1)))