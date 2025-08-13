# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random
Aluno1 = str(input('Nome do aluno 01:'))
Aluno2 = str(input('Nome do aluno 02:'))
Aluno3 = str(input('Nome do aluno 03:'))
Aluno4 = str(input('Nome do aluno 04:'))
alunos = [Aluno1, Aluno2, Aluno3, Aluno4]
sorteado = random.choice(alunos)
print('O aluno sorteado para apagar o quadro é {}'.format(sorteado))
