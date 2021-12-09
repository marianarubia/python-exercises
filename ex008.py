#Escreva um programa que leia um valor em metros e o exiba convertidos em centimetros e milimetros

n1 = float(input('Digite um valor em metros: '))

cm = n1 * 100
mm = n1 * 1000
dm = n1 * 10
dam = n1 / 10
hm = n1 / 100
km = n1 / 1000

print('A medida {} equivale a:\n {} em centimetros\n {}em milimetros\n {} em decimetro\n {} em decametro\n {} em hectometro\n {} em kilometro'.format(n1,cm,mm,dm,dam,hm,km))
