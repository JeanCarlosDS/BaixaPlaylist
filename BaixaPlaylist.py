# pip install pytube
# pip install moviepy
# pip install win10toast

from pytube import Playlist
from win10toast import ToastNotifier
from os import system
from time import sleep
import moviepy.editor as mp
import os
import re

system('title Baixador de Playlist @jean_carlos.019')
system('color a')
system('cls')
print('-='*30,'\n')
print(' '*12,'Download de músicas/vídeos (Playlist)')
print(' '*19,'By: @jean_carlos.019')
print("""                                                            
      ,´ `.                                               
______|___|______________________________________________
      |  /                       _..-´|                  
      | /                  _..-´´_..-´|                  
______|/__________________|_..-´´_____|__________|\______
     ,|                   |           |          | \     
    / |                   |           |          | ´     
___/__|___________________|___________|__________|_______
  / ,´| `.                |      ,d88b|          |       
 | .  |   \            __ |      88888|       __ |       
_|_|__|____|_________,d88b|______`Y88P'_____,d88b|_______
 |  ` |    |         88888|                 88888|       
 `.   |   /          `Y88P'                 `Y88P'       
___`._|_.´_______________________________________________
      |                                                  
    , |                                                  
    '.´""")
print('-='*30)
sleep(4)

def opcao_invalida():
    system('color 4')
    print('-='*30)
    print('Opção inválida! Tente novamente!\n')
    system('pause')

def notificar(notificacao):
    notificacao.show_toast(
        "Baixa Playlist", 
        "Ei! Seu download terminou!", 
        threaded=True, 
        icon_path='C:\Windows\WinSxS\wow64_microsoft-windows-onedrive-setup_31bf3856ad364e35_10.0.19041.1_none_e585f901f9ce93e6/OneDrive.ico', 
        duration=7,
        )
        
while True:
    system('cls')
    system('color e')
    print('-='*30)
    formato = input("Deseja baixar música ou vídeo? (M/V) ").strip().upper()[0]
    system('cls')
    
    if formato not in 'MV':
        opcao_invalida()
        continue
    
    print('-='*30)
    link = Playlist(input("Digite o link da playlist que deseja baixar: "))
    system('cls')  
    print('-='*30)
    diretorio = input("Digite o diretório em que deseja salvar: ").strip()
    system('cls')
    
    if diretorio in '':
        opcao_invalida()
        continue

    # → Faz o Download.
    for indice, video in enumerate(link.videos):
        system('color 2')
        print('-='*30)
        print('Aguarde... Isso pode levar um tempo. Avisarei quando terminar!\n')
        print(f'Baixando... {indice + 1}/{len(link)}')

        if formato == 'M':
            video.streams.get_highest_resolution().download(diretorio)
            system('color e')
            print('\nConvertendo...')
            # → Converte mp4 para mp3.
            for file in os.listdir(diretorio):
                if re.search('mp4', file):
                    mp4_arquivo = os.path.join(diretorio, file)
                    mp3_arquivo = os.path.join(diretorio, os.path.splitext(file)[0]+'.mp3')
                    novo_arquivo = mp.AudioFileClip(mp4_arquivo)
                    novo_arquivo.write_audiofile(mp3_arquivo)
                    os.remove(mp4_arquivo)
        elif formato == 'V':
            video.streams.get_highest_resolution().download(diretorio)
        system('cls')
        
    system('color a')
    print('-='*30)
    print('Sucesso!')
    print('-='*30,'\n')
    
    notificacao = ToastNotifier()
    notificar(notificacao)
    
    repetir = ' '
    while repetir not in 'SN':
        repetir = input('Deseja repetir o programa? (S/N) ').strip().upper()[0]
    if repetir == 'N':
        break    
