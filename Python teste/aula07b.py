n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
print('A soma vale {}'.format(n1+n2))

soma = n1 + n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {}'.format(soma, multiplicacao, divisao))
print('A divisão inteira vale {} e a potência {}'.format(divisao_inteira, exponenciacao))

# Formatar o número para caber em casas decimais, floating point {:.3f}
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, multiplicacao, divisao))

# Não quebrar a linha após um novo comando end=''  (''.format(), end='')
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(soma, multiplicacao, divisao), end='. ')
print('A divisão inteira vale {} e a potência {}.'.format(divisao_inteira, exponenciacao))

# Quebrar a linha no mesmo comando \n
print('A soma é {}, \n o produto é {} e \n a divisão é {:.2f}'.format(soma, multiplicacao, divisao))
