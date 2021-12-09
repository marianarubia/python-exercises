# Faça um programa que leia uma frase pelo teclado e mostre
# > Quantas vezes aparece o 'a'
# Em que posição ela aparece a primeira vez
# Em que posicação ela aparece a ultima vez

frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra a aparece {} vezes.'.format(frase.count('A')))
print('A letra a aparece a primeira vez na posição {}.'.format(frase.find('A')+1))
print('A letra a apareceu a ultima vez na posição {}.'.format(frase.rfind('A')+1))