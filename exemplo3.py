import speech_recognition as sr
#from gtts import gTTS
from playsound import playsound

reconhecedor = sr.Recognizer()
microfone = sr.Microphone()

resultado = ""
with microfone as mic:
    reconhecedor.adjust_for_ambient_noise(mic)
    try:
        print("Fale o que deseja calcular...")
        audio = reconhecedor.listen(mic)
        print("Aguarde...")
        conta = reconhecedor.recognize_google(audio, language='pt')
        print(conta)

        conta = conta.split()
        if conta[1] == "+":
            resultado = str(int(conta[0]) + int(conta[2]))
            print(resultado)
        elif conta[1] == "-":
            resultado = str(int(conta[0]) - int(conta[2]))
            print(resultado)
        elif conta[1] == "/":
            resultado = str(int(conta[0]) / int(conta[2]))
            print(resultado)
        elif conta[1] == "x" and conta[2] != "0":
            resultado = str(int(conta[0]) * int(conta[2]))
            print(resultado)
        else:
            print("Não é uma conta")


        #audio = gTTS(resultado, lang='pt')
        #audio.save("conta.mp3")
        #print("Carregando audio...")
        #playsound("conta.mp3")


    except:
        print("Travou")
