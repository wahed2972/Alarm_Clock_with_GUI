from tkinter import *
import time
from pygame import mixer
from tkinter import messagebox

root =Tk()
root.title("Alarm Clock")
root.geometry("530x330")

time_alarm = StringVar()
msgi = StringVar()

head = Label(root,text="Alarm Clock",font=('comic sans',20))
head.grid(row=0,columnspan=3,pady=10)

mixer.init()

def alarm():
    a = time_alarm.get()
    at = a
    CurrentTime = time.strftime("%H:%M")
    
    while a != CurrentTime:
        CurrentTime = time.strftime("%H:%M")
    
    if a == CurrentTime:
        mixer.music.load('alarm_ringtone.mp3')
        mixer.music.play()
        msg = messagebox.askokcancel('Info',f'{msgi.get()}')
        if msg:
            mixer.music.stop()
        
    

Clockimg = PhotoImage(file="alarm_img.png")

img = Label(root,image=Clockimg)
img.grid(rowspan=4,column=0,padx=10)

input_time = Label(root,text="Input Time",font=('comic sans',18))
input_time.grid(row=1,column=1)

alarm_time = Entry(root,textvariable=time_alarm,font=('comic sans',18),width=6)
alarm_time.grid(row=1,column=2)

msg = Label(root,text="Message",font=('comic sans',18))
msg.grid(row=2,column=1,columnspan=5)

msg_input = Entry(root,textvariable=msgi,font=('comic sans',16))
msg_input.grid(row=3,column=1,columnspan=3)

submit = Button(root,text="SUBMIT",font=('comic sans',18),command=alarm)
submit.grid(row=4,column=1,columnspan=2)

root.mainloop()