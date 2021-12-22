#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#– Não existe valor maior, os dois são iguais
while True:
    n1=int(input('type the first integer: '))
    n2=int(input('type the second integer: '))
    print('-------------------------------')
    if n1>n2:
        print('the first one is higher')
    elif n2>n1:
        print('the second one is higher')
    elif n1==n2:
        print('there is no higher number, they are equal')              