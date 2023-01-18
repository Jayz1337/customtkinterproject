import sys
sys.path.append("customtkinter") # customtkinter lib
import customtkinter
import random
from time import sleep
import datetime


# -- Appearence
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")
root = customtkinter.CTk()
root.geometry("500x350")
root.resizable(False,False)

# Today's datetime
today = datetime.date.today()
d1 = today.strftime("%d/%m/%Y")
root.title("Photovoltaic Meter | " + d1)


def updateNumbers():
    
    global volt
    global amp
    volt.destroy()
    amp.destroy()
    volt = customtkinter.CTkLabel(master=root, text="Voltage:   {}".format(random.randint(1,100)), font=("Arial",24))
    volt.place(x=0,y=0)
    amp = customtkinter.CTkLabel(master=root, text="Amp:   {}".format(random.randint(1,100)), font=("Arial", 24))
    amp.place(x=32,y=30)

def newUpdateNums():
    
    if condition:
        global volt
        global amp
        volt.configure(text="Voltage:   {} V".format(random.randint(1,100)))
        amp.configure(text="     Amp:   {} A".format(random.randint(1,100)))
        root.after(1000,newUpdateNums)


condition=True   
   
def startLoop():
    global condition
    condition=True
    root.after(1000,newUpdateNums)

def stopLoop():
    global condition
    condition=False
    
def timeNow():
    global timenow
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    timenow.configure(text=current_time)
    root.after(1000,timeNow)
    


# -- Labels
volt = customtkinter.CTkLabel(master=root, text="Voltage:   {} V".format(random.randint(1,100)), font=("Arial",24))
volt.place(x=0,y=60)

amp = customtkinter.CTkLabel(master=root, text="     Amp:   {} A".format(random.randint(1,100)), font=("Arial", 24))
amp.place(x=0,y=90)

date = customtkinter.CTkLabel(master=root, text="{}".format(d1),font=("Arial bold", 17))
date.place(x=400,y=10)


now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")
timenow = customtkinter.CTkLabel(master=root, text=current_time,font=("Arial", 17))
timenow.place(x=409,y=30)
# -- Buttons
start_button = customtkinter.CTkButton(master=root,text="Start loop",width=100, height=32,border_width=0,corner_radius=30,command=startLoop)
start_button.place(x=100,y=300)
stop_button = customtkinter.CTkButton(master=root,text="Stop loop",width=100, height=32,border_width=0,corner_radius=30, command=stopLoop)
stop_button.place(x=220,y=300)
quit_button = customtkinter.CTkButton(master=root,width=80,height=32,border_width=0,corner_radius=30,text="Quit",font=("Arial",12),hover_color="Red", command=root.destroy)
quit_button.place(x=380,y=300)
root.after(1000,newUpdateNums)
root.after(1000,timeNow)
root.mainloop()
