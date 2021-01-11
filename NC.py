import pyautogui
import time
import libr
import os
station=[]
rg=[]
senha=[]
os='a'
while True:
    rg = str(input('Digite o RG: '))
    ims=str(input('Abrir IMS? (S/N) '))
    if ims=='s' or ims=='S':
        senha=str(input("Digite a Senha: "))
        libr.init(rg, senha)
    func=str(input('Qual função você quer executar?\n Apontamentos(A)\n Não Conformidades(NC)\n NC parcial(NCP)\n'))
    if func=='NC' or func=='nc':
        station=str(input('Digite a estação: '))
        #seq=str(input('Digite a sequência: '))
        while not os.isspace() and station!='esc' and station!='ESC':
            libr.nc(station, rg)
    elif func=='ncp' or func=='NCP':
        libr.ncp(rg)


    #elif func=='a' or func=='A':
        #False
        #while True:
            #seq = str(input('Digite a sequência: '))
            #Empregados separados por espaço:






