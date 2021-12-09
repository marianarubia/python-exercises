# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Doláres ela pode comprar considere 1 dolar = 3
real = float(input('Quantos reais você tem na carteira? R$: '))
dolar = 3.27

soma = real / dolar

print('Com R${:.2f} reais você pode comprar US${:.2f} doláres'.format(real, soma))