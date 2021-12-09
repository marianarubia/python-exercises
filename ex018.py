#Faça um exercicio que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo
from math import sin,cos,tan,radians

ang = float(input('Qual o angulo desejado? '))
print('Seno: {:.2f}'.format(sin(radians(ang))))
print('Cosseno: {:.2f}'.format(cos(radians(ang))))
print('Tangente: {:.2f}'.format(tan(radians(ang))))