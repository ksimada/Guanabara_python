# Operadores aritméticos, binários
# Operando: valores da operação
# = atribuição, recebe
# == operador relacional de igualdade, é igual a 
# + adição
5+2==7
# - subtração
5-2==3
# * multiplicação
5*2==10
# / divisão
5/2==2.5
# ** potência
5*2==25
# // divisão inteira
5//2==2
# % módulo, resto da divisão
5%2==1

# Ordem de precedência, o que resolver primeiro:
# 1. ()
# 2. **
# 3. * / // % faz quem aparecer primeiro
# 4. + -
5+3*2 = 5+6 = 11
3*5+4**2 = 3*5+16 = 15+16 = 31
3*(5+4)**2 = 3*9**2 = 3*81 = 243

# função interna de potência pow()
pow(4,3) == 64

81**(1/2) == 9.0
25**(1/2) == 5.0
127**(1/3) == 5.026525695313479

'Oi' + 'Ola' == 'OiOla'
'Oi'*5 == 'OiOiOiOiOi'
'='*20 == '===================='
print('='*20)