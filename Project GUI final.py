from tkinter import *
import os


root = Tk()

root.geometry('1200x600')
root.title('Utility Window')
root.configure(background='black')
root.resizable(0,0)
Label(root,text="Utility Applications",font='Gabriola 50 bold', bg='black',fg='yellow').place(x=400,y=20)



calculator_photo=PhotoImage(file="calculator png.png").subsample(4,4)
calendar_photo=PhotoImage(file="calendar png.png").subsample(2,2)
QR_code_photo=PhotoImage(file="QR Code png.png").subsample(3,3)
TTH_photo=PhotoImage(file="text to handwriting png.png").subsample(5,5)
TTS_photo=PhotoImage(file="text to speech png.png").subsample(4,4)
Timer_Photo=PhotoImage(file="timer png.png").subsample(3,3)
YVD_photo=PhotoImage(file="youtube video downloader png.png").subsample(4,4)



def calculator():
    os.startfile('Calculator.py')
def calendarcreator():
    os.startfile('Calendarmaker.py')
def QR():
    os.startfile('QRcodegenerator.py')
def TTS():
    os.startfile('texttospeech.py')
def TTH():
    os.startfile('texttohandwriting.py')
def timer():
    os.startfile('Countdowntimer.py')
def Yt():
    os.startfile('youtubevideodownloader.py')




Button(root,text="Calculator",image=calculator_photo,bg='black',bd=0, command=calculator).place(x=80,y=170)
Button(root,text="Calendar",image=calendar_photo,bg='black',bd=0, command=calendarcreator).place(x=350,y=170)
Button(root,text="QR Code",image=QR_code_photo,bg='black',bd=0, command=QR).place(x=620,y=185)
Button(root,text="TTH",image=TTH_photo,bg='black',bd=0, command=TTH).place(x=890,y=185)
Button(root,text="TTS",image=TTS_photo,bg='black',bd=0, command=TTS).place(x=215,y=400)
Button(root,text="Timer",image=Timer_Photo,bg='black',bd=0, command=timer).place(x=485,y=390)
Button(root,text="YVD",image=YVD_photo,bg='black',bd=0, command=Yt).place(x=755,y=380)


Label(root, text='Calculator',font='Arial 12 bold',bg='black',fg='white').place(x=145,y=325)
Label(root, text='Calendar',font='Arial 12 bold',bg='black',fg='white').place(x=395,y=328)
Label(root, text='QR Code Generator',font='Arial 12 bold',bg='black',fg='white').place(x=640,y=330)
Label(root, text='Text To Handwriting',font='Arial 12 bold',bg='black',fg='white').place(x=950,y=330)
Label(root, text='Text To Speech',font='Arial 12 bold',bg='black',fg='white').place(x=290,y=550)
Label(root, text='Timer',font='Arial 12 bold',bg='black',fg='white').place(x=600,y=550)
Label(root, text='Youtube Video Downloader',font='Arial 12 bold',bg='black',fg='white').place(x=810,y=550)








root.mainloop()
