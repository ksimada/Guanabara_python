#Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média
nota1 = int(input('Digite a primeira nota:'))
nota2 = int(input('Digite a segunda nota:'))
media = (nota1 + nota2)/2
print('A média das notas {} e {} é {}'.format(nota1, nota2, media))
