# Faça um algoritmo que leia o preço de um produto e de 5% de desconto

preço = float(input('Valor do produto original? R$ '))
novo = preço - (preço * 5 / 100)


print('O produto de valor {:.2f} com 5% de desconto será {:.2f}'.format(preço, novo))