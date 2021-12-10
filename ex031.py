#Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço
# da passagem, cobrando 0,50 por Km para viagens até 200Km, e 0,45 para viagens mais longas.

distancia = int(input('Qual a distância da sua viagem? '))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
