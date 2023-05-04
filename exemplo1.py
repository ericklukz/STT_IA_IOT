#C:/Users/Erick/Desktop/agenda.txt
from gtts import gTTS
from playsound import playsound
import os

caminho = input("Digite o caminho do arquivo: ")
teste = os.path.isfile(caminho)

if teste:
    with open(caminho, 'r') as arquivo:
        print("Carregando arquivo...")
        texto = arquivo.read()
        audio = gTTS(texto, lang='pt')
        audio.save("agenda.mp3")
        print("Carregando audio...")
        playsound("agenda.mp3")
else:
    print("Caminho inválido")
