#Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
import random

print('Escolha 4 alunos para serem sorteados')

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]
print('O aluno sorteado é {}'.format(random.choice(lista)))