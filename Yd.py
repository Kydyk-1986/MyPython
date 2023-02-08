import tkinter as tk
import pytube
from pathlib import Path
from moviepy import editor


win = tk.Tk()
win['bg'] = 'white'
win.title('Video Saver')


def main():
    global link, place
    lab = tk.Label(win, text='Путь до видео:', font='Times 20', bg='white', fg='black')
    lab.grid(row=0, column=0)
    link = tk.Entry(win, width=35, bg='yellow', bd=3)
    link.grid(row=2, column=0)

   # lab2 = tk.Label(win, text='Путь для сохранения:', font='Times 20', bg='white', fg='black')
   # lab2.grid(row=5, column=0)
   # place = tk.Entry(win, width=35, bg='yellow', bd=3)
   # place.grid(row=7, column=0)

def converter():
    #video_file = Path(link.get())
    #video = pytube.YouTube(link.get())
    #quality = video.streams.get_highest_resolution()
    #quality.download('C:/Users/user/Desktop/yt')
    video_file = Path(link.get())

    video = editor.VideoFileClip(f'{video_file}')
    video_file = video_file.name.replace('', '_').split('.')

    audio = video.audio
    audio.write_audiofile(f'C:/Users/user/Desktop/Converted_audio/{video_file[0]}.mp3')

do = tk.Button(win, text='Конвертировать', fg='red', command=converter)
do.grid(row=8, column=0)


main()
win.mainloop()

