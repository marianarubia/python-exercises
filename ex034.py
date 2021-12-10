# Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento.
# Para salários superiores a 1.250,00, calcule um aumento de 10%
# Para salários inferiores, calcule um aumento de 15%

salario = float(input('Digite o valor do seu salário: R$ '))
if salario <= 1.250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)
print('Seu salário é {:.2f} e com aumento será R${:.2f}'.format(salario, novo))
