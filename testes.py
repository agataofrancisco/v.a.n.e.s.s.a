import pyaudio
import speech_recognition as sr
import pyttsx3

# Configuração do reconhecimento de fala
recognizer = sr.Recognizer()

# Configuração do motor de síntese de fala
engine = pyttsx3.init()

def capture_and_repeat():
    with sr.Microphone() as source:
        print("Diga algo:")
        engine.say("Diga algo:")
        engine.runAndWait()
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
            engine.say(f"Você disse: {text}")
            engine.runAndWait()
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio.")
        except sr.RequestError as e:
            print(f"Ocorreu um erro durante o reconhecimento de fala: {e}")

if __name__ == "__main__":
    capture_and_repeat()
