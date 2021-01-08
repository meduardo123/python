import pyautogui
import time
import libr
import os

file='C:\Program Files\pw3270\pw3270.exe'

rg=str(input('Digite o RG: '))
senha=str(input("Digite a Senha: "))
libr.init(rg, senha)
while True:
    station=str(input('Digite a estação: '))
    seq=str(input('Digite a sequência: '))
    libr.nc(station, seq, rg)






