# Importing Required Modules & libraries
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog
import pygame
import os

pygame.mixer.init()

#display
win = Tk()
win.geometry("500x250")
win.title("Music Player | Mppy")
win.configure(bg='black',padx=110,pady=30)

songname = StringVar()

def mp3path():
	mp3=filedialog.askopenfilename()
	songname.set(mp3)
	listofsongs=[songname.set(mp3)]

#Design a label to show text
txt_lable = Label(win, text = "Music Player", bg = 'orange',font=('Times New Roman',25),justify='center',padx=10,pady=10)
txt_lable.grid(columnspan=5)

def play():
	music = songname.get()
	pygame.mixer.music.load(music)
	pygame.mixer.music.play()

def stop():
	pygame.mixer.music.pause()
	

def resume():
	pygame.mixer.music.unpause()
	



def widgets():
	#box
	box=Entry(win,textvariable=songname,)
	box.grid(row=2,column=0)

	#play
	s=Button(win,text='Search',command=mp3path)
	s.grid(row=2,column=1,padx=10,pady=10)
	

widgets()


#play
play_icon = PhotoImage(file = os.path.join('images','play_button.png'))
button = Button(win, image = play_icon,fg='black',bg='orange',command=play,font=('arial',20,'bold'),justify='center',padx=16, pady=16,bd=0)
button.grid(row=7,column=1)


#pause
pause_icon = PhotoImage(file = os.path.join('images','pause_button.png'))
button = Button(win, image = pause_icon,fg='black',bg='orange',command=stop,font=('arial',20,'bold'),justify='center',padx=16, pady=16,bd=0)
button.grid(row=7,column=2)

#stop
resume_icon = PhotoImage(file = os.path.join('images','resume_button.png'))
button = Button(win, image = resume_icon,fg='black',bg='orange',command=resume,font=('arial',20,'bold'),justify='center',padx=16, pady=16,bd=0)
button.grid(row=7,column=3)


#Design a label to show text
txt_lable = Label(win, text = "Music Player by Utpal | 2020 ",fg='grey',bg='black',font=('Times New Roman',10),justify='center',padx=10,pady=10)
txt_lable.grid(columnspan=5)

win.mainloop()