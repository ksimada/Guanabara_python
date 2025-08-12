#Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python. Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

# Para importar uma biblioteca
# import nome_da_biblioteca

# Para importar um item da biblioteca
# from nome_da_biblioteca import item

# biblioteca math: comandos de matemática
# ceil: arredondar para cima
# floor: arredondar para baixo
# trunc: truncar o numero, eliminar da virgula para frente
# pow: potencia **
# sqrt: raiz quadrada
# factorial: fatorial
import math
from math import sqrt, ceil

print('-'*10)

import math
num = int(input('Digite um numero:'))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))

print('-'*10)

# from + import: traz o método diretamente para a pasta, sem precisar referenciar a biblioteca junto com a função (math.função)
# ctrl + space: mostra a lista de funcionalidades da biblioteca
from math import sqrt, floor
num = int(input('Digite um numero:'))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, raiz))
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

print('-'*10)

# Para encontrar todas as bibliotecas padrões do Python, acessar o site do python.org > docs > escolher versão > library reference
import random
num = random.random()
print(num)
num_int = random.randint(1,10)
print(num_int)

# acessar o site do python.org > py PI (Package index, indice de pacotes extras)
import emoji
print(emoji.emojize('Olá mundo :earth_americas:', language="alias"))