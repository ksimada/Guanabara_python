#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dias = int(input('Quantos dias alugados?'))
km = float(input('Quantos kilometros percorridos?'))
preco = (60*dias)+(0.15*km)
print('O carro alugado percorreu {} km em {} dias e o preço a pagar é R${:.2f}'.format(km, dias, preco))

#resolução do exercicio
diaria = dias*60
uso_km = km*0.15
total = diaria+uso_km
print('O total a pagar é R${:.2f}'.format(total))