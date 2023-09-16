import pywhatkit
import os
from tkinter import *
def Text_to_written():
    TTH=Tk()
    TTH.geometry('800x500')
    TTH.title('Text To Handwriting')
    TTH.configure(background='#A4E775')
    Label(TTH,text='Text To Handwriting',font='Gabriola 25 bold',bg='#A4E775',fg='#0437F6').place(x=230,y=10)
    speech = StringVar()
    Label(TTH, text = 'Type your text here:', font = 'arial 15 bold',bg='#A4E775',fg='#BD61C7').place(x= 260 , y = 100)
    link_enter = Entry(TTH, width = 70,textvariable = speech).place(x = 50, y = 150)

    def Generator():
        text_for_handwriting=str(speech.get())
        pywhatkit.text_to_handwriting(text_for_handwriting, rgb=(0,0,255), save_to='handwriting.jpg')
        os.system("handwriting.jpg")
    Button(TTH,text = 'GENERATE', font = 'arial 15 bold' ,bg = '#BD61C7', padx = 2, command = Generator).place(x=300 ,y = 220)
    TTH.mainloop()

Text_to_written()
