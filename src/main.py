import speech_recognition as sr
import pyttsx3

# Criação do objeto Recognizer, ou seja, o elemento que fará o reconhecimento da vp«oz
recognizer = sr.Recognizer()

engine = pyttsx3.init()

#definição da velocidade de fala do sistema (pesonalizavel)
engine.setProperty('rate', 250)

# definição do microfone como fonte de áudio
with sr.Microphone() as source:
    audio = recognizer.listen(source)

#Definição do loop para a captura da voz
    while True:
        try:
            texto = "Olá, isso é um exemplo de texto para fala em Python."
            print(texto)
            engine.say(texto)

            engine.runAndWait()
            # Use o reconhecimento de fala para converter o áudio em texto
            # texto = recognizer.recognize_google(audio, language='pt-pt')  # Idioma: Português (Brasil)
            texto = input("tu: ")
            resposta = ("Você disse: " + texto)
            print(resposta)
            engine.say(resposta)
        except sr.UnknownValueError:
            erro = "Não foi possível entender o áudio."
            print(erro)
            engine.say(erro)
        except sr.RequestError as e:
            erro = "Erro na solicitação: {0}".format(e)
            print(erro)
            engine.say(erro)
