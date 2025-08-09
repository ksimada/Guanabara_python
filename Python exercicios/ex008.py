#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
# 0.0001 km = 0.001 hm = 0.01 dam = 1m = 10 dm = 100cm = 1000mm
metro = float(input('Digite o tamanho:'))
centimetro = metro*100
milimetro = metro*1000
print('{} metros equivalem a {} centímetros e {} milímetros'.format(metro, centimetro, milimetro))
# {:.0f} um número flutuante sem casas decimais
print('{} metros equivalem a: \n{} kilometros \n{} hectometros \n{} decametros \n{}decimetros \n{}centimetros \n{} milímetros'.format(metro,(metro/1000), (metro/100), (metro/10), (metro*10), centimetro, milimetro))