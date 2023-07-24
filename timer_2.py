import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pyglet
from playsound import playsound
from threading import Thread


pyglet.font.add_file('DS-DIGI.ttf')
# creating Tk window
root = Tk()
  
# setting geometry of tk window
root.geometry("1920x1080")
  
# Using title() to display a message in
# the dialogue box of the message in the
# title bar.
root.title("Time Counter")
  
# Declaration of variables
hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("00")
# Use of Entry class to take input from the user
hourEntry= Entry(root, width=3, font=("Arial",18,""),
                 textvariable=hour)
hourEntry.place(x=1300,y=20)
  
minuteEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=minute)
minuteEntry.place(x=1350,y=20)
  
secondEntry= Entry(root, width=3, font=("Arial",18,""),
                   textvariable=second)
secondEntry.place(x=1400,y=20)
Font_tuple =("digital-7",160)
L1=Label(root,font=Font_tuple,text="00:00:00")
L1.place(x=420,y=230)
# pused varible
global pused
pused = False
# puse func
def puse(its_unpused):
    global pused
    pused = its_unpused
    if pused == False:
        pused=True
    elif pused == True:
        pused =False

        
    
        
    return pused


p1000 = ttk.Progressbar(root, length=1200)
p1000.place(x=200,y=700)



global alarm
alarm = False

def alarm(my_alarm):
    global alarm
    alarm = my_alarm
    if alarm:
        alarm = False
    else:
        alarm = True






def submeted():
    p1000.stop()
    Thread(target=submit).start()
    Thread(target=pro).start()

def submit():
    
    try:
        # the input provided by the user is
        # stored in here :temp
        
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
        
        
    except:
        print("Please input the right value")

    while temp >-1:
        if pused == False:
            up = True
        if pused == True:
            up = False
             
        if pused:
            p1000.stop()
            while True:

                if up:
                    break        

        #     for x in range(x):
        #         time.sleep(xx)
        # else:
        #     pass
                
        
            
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places
        houra=("{0:2d}".format(hours))
        minutea=("{0:2d}".format(mins))
        seconda=("{0:2d}".format(secs))
        L1.config(text=f"{houra}:{minutea}:{seconda}",)
        # updating the GUI window after decrementing the
        # temp value every time
        root.update()
        time.sleep(1)


        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        if (temp == 0):
            p1000.stop()
            if alarm:
                playsound("Clock-chimes-sounds.mp3")
            messagebox.showinfo("Time Countdown", "Time's up ")
            
            
                
                
            
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

    

def pro():
    temped = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    sl = temped/100
    sl *=1000
    sl =round(sl)
    p1000.start(sl)

    

# button widget
btn = Button(root, text='start again', bd='5',
             command= submeted)
btn.place(x = 260,y = 30)
btn2 = Button(root,text="stop",bd='5',command=lambda:puse(pused))
btn2.place(x=400,y=30)
btn1 = Button(root, text='Set Time Countdown', bd='5',
             command= submeted)
btn1.place(x = 70,y = 30)
btn4= Button(root,text="alarm" ,command=alarm,bd='5')
btn4.place(x=450,y=30)

  
# infinite loop which is required to
# run tkinter program infinitely
# until an interrupt occurs
root.mainloop()