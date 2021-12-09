#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
num = float(input('Digite um numero: '))
print('A porção inteira do numero {} é {}'.format(num, trunc(num)))

