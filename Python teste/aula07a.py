nome = input('Qual é o seu nome?')
print('Prazer em te conhecer {}!'.format(nome))

# {:20} aparecer em 20 caracteres
print('Prazer em te conhecer {:20}!'.format(nome))

# {:>20} > alinhamento a direita, < alinhado a esquerda e ^ alinhado no centro
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))

# {:=^20} = preenche o caractere vazio
print('Prazer em te conhecer {:=^20}!'.format(nome))
print('Prazer em te conhecer {:~^20}!'.format(nome))
