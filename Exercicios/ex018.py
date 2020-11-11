""" Faça um programa que leia um angulo
quaquer e mostre na tela o valor de seno,
cosseno e tangente desse angulo. """

from math import radians, sin, cos, tan
an = float(input('Digite o ângulo: '))
se = sin(radians(an))
print('O ângulo de {} tem SENO de {:.2f}'.format(an,se))
co = cos(radians(an))
print('O ângulo de {} tem COSSENO de {:.2f}'.format(an,co))
ta = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an,ta))