# Faça um algoritmo que leia o salário de um funcionário com 15% de aumento

salario = int(input('Qual o seu atual salário? R$ '))
novo = (salario * 15 / 100)
aumento = novo + salario

print('O salário de R$ {:.2f} com 15% de aumento é R$ {:.2f}'.format(salario, aumento))