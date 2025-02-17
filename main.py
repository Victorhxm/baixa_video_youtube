import PySimpleGUI as sg
from pytubefix import YouTube
from pytubefix.cli import on_progress

sg.theme('Dark Blue 16')
interface = [
    [sg.Titlebar("Youtube DOWNLOAD",None, 'red', 'white')],
    [sg.Text("URL")],
    [sg.Input(size=(50, 1), key="url")],
    [sg.Button('download')]
       
]
janela = sg.Window('Windown', interface)
while True:
    evento, valor = janela.read()

    if valor == sg.WIN_CLOSED:
        break
    if evento == 'download':
        link = janela['url'].get()
        video = YouTube(link,on_progress_callback=on_progress)
        stream = video.streams.get_highest_resolution()
        stream.download()
    print('Download completado!')
janela.close()
exit()