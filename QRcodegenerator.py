import qrcode
from tkinter import *
import os
def QR_Code():
    QR=Tk()
    QR.geometry('500x300')
    QR.title('QR Code Generator')
    QR.configure(background='black')
    Label(QR,text='QR Code Generator',font='Gabriola 25 bold',bg='black',fg='white').pack()
    link = StringVar()
    Label(QR, text = 'Paste Link Here:', font = 'arial 15 bold',bg='black',fg='white').place(x= 160 , y = 60)
    link_enter = Entry(QR, width = 70,textvariable = link).place(x = 32, y = 90)

    def Generator():
        url=str(link.get())
        img = qrcode.make(url)
        img.save("youtubeQR.jpg")
        os.startfile("youtubeQR.jpg")
    Button(QR,text = 'GENERATE', font = 'arial 15 bold' ,bg = '#441AD1', padx = 2, command = Generator).place(x=180 ,y = 150)
    QR.mainloop()

QR_Code()
