# Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule sua área e a quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2m²
largura=float(input('Informe a largura da parede em metros:'))
altura=float(input('Informe a altura da parede em metros:'))
area = largura*altura
tinta = area/2
print('Para uma parede de {} m² são necessários {} litros de tinta'.format(area, tinta))

print('Sua parede tem a dimensão de {:.2f}m x {:.2f}m e sua área é de {:.2f}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {:.3f}l de tinta.'.format(tinta))