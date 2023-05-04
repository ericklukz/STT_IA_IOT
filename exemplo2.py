import speech_recognition as sr

reconhecedor = sr.Recognizer()

microfone = sr.Microphone()
while True:
    try:
        with microfone as mic:
            reconhecedor.adjust_for_ambient_noise(mic)
            print("Fala ai")
            audio = reconhecedor.listen(mic)
            print("Reconhecendo...")
            texto = reconhecedor.recognize_google(audio, language = 'pt')
            print(texto)
    except:
        print("Não rolou :/")
