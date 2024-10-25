from tkinter import Label, Tk 
import time
import random

app_window = Tk() 
app_window.title("Digital Clock") 
app_window.geometry("420x150") 
app_window.resizable(1, 1)

border_width = 25

text_font = ("Boulder", 68, 'bold')

label = Label(app_window, font=text_font, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
    current_time = time.strftime("%I:%M:%S %p")  
    
    foreground = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    background = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    label.config(text=current_time, fg=foreground, bg=background)  
    label.after(1000, digital_clock) 
digital_clock()
app_window.mainloop()