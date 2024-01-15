import pyttsx3

robo = pyttsx3.init()
msg = input('Escreva o texto que sera convertido para audio: ')
robo.say(msg)
robo.runAndWait()
