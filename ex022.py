# Crie um programa que leia o nome completo de uma pessoa e mostre:
# >O nome com todas as letras maiusculas
# >O nome com todas as letras minusculas
# >Quantas letras tem sem considerar espaço
# >Quantas letras tem o primeiro nome

nome = str(input('Qual é o seu nome completo? ')).strip()
print('Analisando o seu nome...')
print('Com todas as letras maiusculas será {}'.format(nome.upper()))
print('O seu nome com todas as letras minusculas será {}'.format(nome.lower()))
print('O seu nome tem {} letras ao todo'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))