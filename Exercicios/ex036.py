""" Escreva um programa para aprovar o empréstimo bancário
    para a compra de uma casa. Pergunte o valor da casa,
    o salário do comprador e em quantos anos ele vai pagar.
    A prestação mensal não pode exceder 30% do salário ou
    então o empréstimo será negado."""


casa = float(input('Qual o valor da casa ? '))
salario = float(input('Qual é o seu salário ? '))
parc = int(input('Em quantos anos irá parcelar ? '))
prest = casa / (parc * 12) 
minimo = salario * 30 / 100
print('Para pagar uma casa de R$ {:.2f} em {} anos'.format(casa,parc), end = '')
print(' a prestação será de R$ {:.2f}'.format(prest))
if prest  <= minimo:
    print('Emprestimo pode ser concedido')
else:
    print('Emprestimo Negado')    
