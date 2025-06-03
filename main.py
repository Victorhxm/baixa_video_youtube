from tkinter import *
from tkinter import ttk
import time
from pytubefix import YouTube
from pytubefix.cli import on_progress

#Function
def down():
    link = url.get()
    video = YouTube(link,on_progress_callback=on_progress)
    stream = video.streams.get_highest_resolution()
    stream.download('Downloads')
    Label(window, text="Download completo!").grid(row=3, column=1,sticky=W)
    
    
#Menu
window = Tk()
window.title("APP baixar video do Youtube")
window.geometry("600x250+200+200")
window.resizable(False,False)


#Label
Label(window,text="URL:").grid(row=0, sticky=W)

#Imput Text
url = StringVar()
entry_url = Entry(window, textvariable=url, width=90).grid(row=0, column=1)

#button
btn_down = Button(window, text="Baixar", command=down).grid(row=2, column=1,sticky=E)

window.mainloop()
