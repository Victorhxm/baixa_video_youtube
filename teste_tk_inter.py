#Imports
from tkinter import *
import functions
from pytubefix import YouTube
from pytubefix.cli import on_progress
#Menu
menu_inicial = Tk()
menu_inicial.title("APP Baixar Video Do Youtube Para Professora Luanna Martins")
menu_inicial.geometry("500x250+200+200")
menu_inicial.resizable(False,False)
menu_inicial.iconbitmap("icon/icon.ico")
#menu_inicial['bg'] = "white"

#Label
Label(menu_inicial,text="URL:").grid(row=0, sticky=W)

#Imput Text
url = Entry(menu_inicial).grid(row=0,column=1)
#Function

#button
btn_down = Button(menu_inicial, text="Baixar").grid(row=2, column=1,sticky=E)

menu_inicial.mainloop()

