""" Faça um programa que leia uma largura e a altura de uma parede
em metros, calcule a sua área e a quantidade de tinta necessaria 
para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m**2"""

altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
a = altura*largura
tinta = a/2
print('A quantidade de tinta nescessária para pintar essa parede é de {} litros'.format(tinta))