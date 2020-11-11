""" Crie um programa que leia quanto de dinheiro uma 
pessoa tem na carteira e mostre quantos dólares ela pode comprar
considere Dolar 1 = 3,27 """

print('Considere: R$ 1,00 = US 3,27')
rs = float(input('Digite quantos reais você tem: '))
us = rs/3.27
print('Com R${} você pode comprar {:.2f} Dólar(es)'.format(rs, us))