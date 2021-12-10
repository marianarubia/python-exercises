# Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 e peça para
# o usuário tentar descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu

from random import randint
from time import sleep

numero = randint(0,5) #faz o computador "PENSAR"
print('Vou sortear um numero de 0 a 5.')
jogador = int(input('Tente adivinhar o número que eu estou pensando: '))
print('PROCESSANDO....')
sleep(2)
if jogador == numero:
    print('Parabéns, você conseguiu me vencer!')
else:
    print('EU GANHEI! Eu pensei no número {}.'.format(numero))