#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
preco= float(input('Digite o preço:'))
desconto= preco*0.95
print('O produto no valor de {} com 5% de desconto fica por {}'.format(preco, desconto))

#Resolução da aula
novo = preco-(preco*5/100)
print('O produto que custava R${:.2f} na promoção com desconto de 5% vai custar R${:.2f}'.format(preco,novo))