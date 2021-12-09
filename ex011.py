#Faça um programa que leia a largura e a altura da parede em metros, calcule sua area e a quantidade de tinta para pinta-la.
# 1 litro = 2m²

altura = float(input('Qual é a altura?'))
largura = float(input('Qual é a largura?'))
area = altura * largura
m2_por_litro = 2


s = area / m2_por_litro

print('Sua parede tem {:.1f} de altura e {:.1f} de largura, logo a área será {:.1f}m² e a quantidade de tinta necessária será {:.1f}L'.format(altura, largura, area, s))

