#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km, mostre uma
# mensagem dizendo que ele foi multado; A multa vai custar 7,00 por cada Km acima do limite.

v = float(input('Informe a velocidade do carro: '))
multa = (v - 80) * 7
if v > 80:
    print('VOCÊ FOI MULTADO! O valor a ser pago é R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança :)')
