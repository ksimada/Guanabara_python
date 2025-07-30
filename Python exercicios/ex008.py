#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
metro = int(input('Digite o tamanho:'))
centimetro = metro*100
milimetro = metro*1000
print('{} metros equivalem a {} centímetros e {} milímetros'.format(metro, centimetro, milimetro))
