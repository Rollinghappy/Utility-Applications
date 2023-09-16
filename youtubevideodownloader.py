from tkinter import *
from pytube import YouTube
import os
def Youtube_vid():
    root = Tk()
    root.geometry('500x300')
    root.resizable(0,0)
    root.title("Youtube Video Downloader")
    root.configure(background="#440416")
    Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold', bg='#440416', fg='white').pack()
    link = StringVar()
    Label(root, text = 'Paste Link Here:', font = 'arial 15 bold',bg='#440416', fg='#D3F759').place(x= 160 , y = 60)
    link_enter = Entry(root, width = 70,textvariable = link, bg='#C585C3').place(x = 32, y = 90)
    def Downloader():     
        url =YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        video.download()
        vid_name=video.title
        vid_name2=vid_name+'.mp4'
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)
        os.startfile(vid_name2)
    Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = '#D3F759', padx = 2, command = Downloader).place(x=180 ,y = 150)
    root.mainloop()
Youtube_vid()
