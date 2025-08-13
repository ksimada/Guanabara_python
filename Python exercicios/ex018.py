# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math
angulo = math.radians(float(input('Informe o ângulo:')))
seno = math.asin(angulo)
cosseno = math.acos(angulo)
tangente = math.atan(angulo)
print('Sendo o ângulo de {:.2f} radianos: \nSeno: {:.2f} \nCosseno: {:.2f} \nTangente: {:.2f}'.format(angulo, seno, cosseno, tangente))