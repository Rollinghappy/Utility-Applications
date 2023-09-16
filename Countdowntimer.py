import time
from tkinter import *
from tkinter import messagebox

def Countdown_timer():
        root = Tk()

        root.geometry("300x250")

        root.title("Time Counter")

        root.configure(background='#708090')

        root.resizable(0,0)

        hour=StringVar()
        minute=StringVar()
        second=StringVar()

        hour.set("00")
        minute.set("00")
        second.set("00")


        hourEntry= Entry(root, width=3, font=("Arial",18,""),bg='#708090',fg='white', bd='0',
                                        textvariable=hour)
        hourEntry.place(x=80,y=20)

        minuteEntry= Entry(root, width=3, font=("Arial",18,""),bg='#708090',fg='white', bd='0',
                                        textvariable=minute)
        minuteEntry.place(x=130,y=20)

        secondEntry= Entry(root, width=3, font=("Arial",18,""),bg='#708090',fg='white', bd='0',
                                        textvariable=second)
        secondEntry.place(x=180,y=20)

        Label(root, text="Hours",font ='arial 8 bold',bg='#708090').place(x=78, y=60)

        Label(root, text="Mins",font ='arial 8 bold',bg='#708090').place(x=128, y=60)

        Label(root, text="Secs",font ='arial 8 bold',bg='#708090').place(x=178, y=60)



        def submit():
                try:
                        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
                except:
                        print("Please input the right value")
                while temp >-1:
                        

                        mins,secs = divmod(temp,60)
                        hours=0
                        if mins >60:
                                hours, mins = divmod(mins, 60)
                        hour.set(hours)
                        minute.set(mins)
                        second.set(secs)
                        root.update()
                        time.sleep(1)
                        if (temp == 0):
                                messagebox.showinfo("Time Countdown", "Time's up ")
                        temp -= 1

        btn = Button(root, text='Set Time Countdown', bd='2', bg='#7B68EE',
                                command= submit)
        btn.place(x = 85,y = 120)

        root.mainloop()
Countdown_timer()
