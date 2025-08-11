# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
salario= float(input('Informe o salário:'))
aumento= salario*1.15
print('O salário de {} fica em {} com 15% de aumento'.format(salario, aumento))

# resolução do exercicio
novo = salario+(salario*15/100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salario, novo))