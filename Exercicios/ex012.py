""" Faça um programa que leia o preço de um produto e mostre seu novo preço,
com desconto de 5% """

n1 = float(input('Digite o preço do produto: '))
pr = (n1*5)/100
dsc = n1 -pr
print(' O produto receberá {} de desconto com a promoção de menos 5%  em cima do valor total '.format(pr))
print(' Sendo assim o produto fica  {} '.format(dsc))