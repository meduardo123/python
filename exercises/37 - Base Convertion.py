#Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o 
#usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
while True:
    dec=int(input('Type a integer: '))
    base=int(input('To what base do you want to convert this number?\n1 - Binary\n2 - Octal\n3 - Hexadecimal\nChoice: '))
    print('-------------------------------')
    if base==1:
        b=bin(dec)
        print('Binary: {}'.format(b))
    elif base==2:
        o=oct(dec)
        print('Octal: {}'.format(o))
    elif base==3:
        h=hex(dec)
        print('Hexadecimal: {}'.format(h))
    else:
        print('This is not an option')
    print('--------------------------------')
    