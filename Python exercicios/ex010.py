#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere US$1.00 = R$3.27
dinheiro=float(input('Quanto dinheiro você tem na carteira?'))
dolar= dinheiro/3.27
print('A quantia de {:.2f} reais equivalem a {:.2f} dolares'.format(dinheiro, dolar))