""" Elabore um programa que calcule o valor a ser pago por um produto,
 considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros """

print('{:=^40}'.format(' Lojas Diego '))
preço = float(input('Digite o preço das compras: R$ '))
print('''Formas de pagamento: 
[ 1 ] À vista dinheiro / cheque
[ 2 ] À vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão ''')
opção = int(input('Qual é a opção ? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra parcelada em 2x de R${:.2f} SEM JUTOS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc =  int(input('Quantas parcelas ? '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcela))
else:
    total = preço
    print('Opção invalida de pagamento')    
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))  
