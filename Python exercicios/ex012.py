#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco= float(input('Digite o preço:'))
desconto= preco*0.95
print('O produto no valor de {} com 5% de desconto fica por {}'.format(preco, desconto))