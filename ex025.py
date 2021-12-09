#Crie um programa que leia o nome da pessoa e diga se ela tem o nome SILVA

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva? {}'. format('SILVA' in nome.upper()))