from gtts import gTTS
import os
from tkinter import *
def Text_to_voice():
    TTS=Tk()
    TTS.geometry('500x300')
    TTS.title('Text To Speech')
    TTS.configure(background='#46A3CD')
    Label(TTS,text='Text To Speech',font='Gabriola 25 bold',bg='#46A3CD',fg='#0437F6').pack()
    speech = StringVar()
    Label(TTS, text = 'Type your text here:', font = 'arial 15 bold',bg='#46A3CD',fg='#F6427D').place(x= 160 , y = 60)
    link_enter = Entry(TTS, width = 70,textvariable = speech).place(x = 32, y = 90)

    def Generator():
        mytext=str(speech.get())
        language = 'en'
        myobj = gTTS(text=mytext, lang=language)
        myobj.save("AISpeech.mp3")
        os.system("AISpeech.mp3")
    Button(TTS,text = 'GENERATE', font = 'arial 15 bold' ,bg = '#F6427D', padx = 2, command = Generator).place(x=180 ,y = 150)
    TTS.mainloop()
Text_to_voice()
