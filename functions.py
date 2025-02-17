from pytubefix import YouTube
from pytubefix.cli import on_progress
#Function
def down_video(url):
    
    imput_url  = YouTube(url,on_progress_callback=on_progress)
    stream = imput_url.streams.get_highest_resolution()
    stream.download()
    