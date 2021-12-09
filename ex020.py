#Sorteie a ordem de apresentação dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre a ordem sorteada
from random import shuffle

print('Sorteie a ordem de apresentação dos alunos')
a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]
shuffle(lista)

print('A ordem de apresentação é')
print(lista)
