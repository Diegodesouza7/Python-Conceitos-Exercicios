""" Escreva um programa que leia um valor em metros
e o exiba convertendo em cemtimetros e milimetros """

m = float(input('Digite uma distância em metros: '))
c = m*100
mil = m*1000
print('A distância em milímetros de {} é de {} e em centímetros é de {}'.format(m,mil,c))