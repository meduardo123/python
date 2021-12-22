#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
#no final, de acordo com a média atingida:
#– Média abaixo de 5.0: REPROVADO
#– Média entre 5.0 e 6.9: RECUPERAÇÃO
#– Média 7.0 ou superior: APROVADO
while True:
    p1=float(input('your fisrt grade: '))
    p2=float(input('your second grade: '))
    if p1>10.0 or p2>10.0 or p1<0.0 or p2<0.0:
        print('please, type the grades correctly')
    else:
        avg=(p1+p2)/2
        if avg<5.0:
            print('im sorry, but youre repproved\nFinal grade: {:.2}'.format(avg))
        elif avg>=5.0 and avg<7.0:
            print('you got a chance in the retake test.\nFinal Grade: {:.2}'.format(avg))
        elif avg>7.0:
            print('congratulations, youre approved!\nFinal grande: {:.2}'.format(avg)) 
    print('------------------------------------')
