import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    audio = r.listen(source)

data = r.recognize_google(audio)
print(data)
