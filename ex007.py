# Desenvolva um programa que leia as duas notas de um aluno e calcule a media
n1 = float(input('Nota um: '))
n2 = float(input('Nota dois: '))

d = (n1 + n2) / 2
print('A média do aluno é {:.1f}'.format(d))