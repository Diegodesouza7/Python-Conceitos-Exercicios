""" Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso. """

n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NÚMEROS
        [ 5 ] SAIR DO PROGRAMA''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        s = n1 + n2
        print('A Soma entre {} e {} é {}'.format(n1, n2, s))
    elif opção == 2:
        m = n1 * n2
        print('A Multiplicação entre {} e {} é {}'.format(n1,n2,m))
    elif opção == 3:
        if n1 > n2:
            print("O {} é maior que {}".format(n1,n2))
        elif n1 == n2:
            print('Entre {} e {} não existe número maior pq ambos são iguais'.format(n1,n2))    
        else:
            print('O {} é maior que {}'.format(n2,n1))   
            
    elif opção == 4:
        print('Informe os números novamente')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção invalida. Tente novamente') 
                       
print('Fim do programa')
