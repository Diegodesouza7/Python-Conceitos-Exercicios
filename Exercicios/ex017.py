""" Faça um programa que leia o comprimento 
do cateto oposto de um cateto adjacente de um trinagulo
calcule e mostre o comprimento da hipotenusa"""

from math import hypot
co = float(input('Coomprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))