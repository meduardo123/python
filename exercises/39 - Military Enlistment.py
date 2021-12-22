#Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, 
#se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
while True:
    yr=int(input('\nTell me your year of birth: '))
    age=2021-yr
    if age==18:
        print('well, you must elist this year')
    elif age>18:
        dif=age-18
        print('you are {} years late to enlistment'.format(dif))
    else:
        dif=18-age
        print('you still have {} years before enlistment'.format(dif))