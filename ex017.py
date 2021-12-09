#Faça um programa que leia o comprimento do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da
#hipotenusa
import math

ca = float(input('Comprimeto do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
#hi = (co ** 2 + ca ** 2) ** (1/2) modo convencional
hi = math.hypot(ca,co)

print('O comprimento da hipotenusa será {:.2f}'.format(hi))
