import tkinter as tk
from datetime import datetime
import math
import tkinter.font as TkFont
       
now = datetime.now()
fullScreen = False

current_time = now.strftime("%H:%M:%S")
root = tk.Tk()
root['bg']='black'

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

myFont = TkFont.Font(family="Helvetica",size=600,weight="bold")
myFont_date = TkFont.Font(family="Helvetica",size=300,weight="bold")
myFont['size'] = math.floor(screen_width / 12)
myFont_date['size'] = math.floor(screen_width / 20)
# font_size = str(math.floor(screen_height / 60))
# myFont = "72"

print(screen_width)
root.attributes('-fullscreen', False)


time_label = tk.Label(root, font = myFont, fg = 'white', bg='black')
time_label.pack(anchor='center', fill='both', pady='100')
date_label = tk.Label(root, font = myFont_date, fg = 'white', bg='black')
date_label.pack(anchor='center')

class MouseControl:        
    def __init__(self, canvas):            
        self.canvas = canvas
        self.canvas.bind('<Button-1>', self.clicked)  
        self.canvas.bind('<Double-1>', self.double_click)  
        self.canvas.bind('<ButtonRelease-1>', self.button_released)  
        self.canvas.bind('<B1-Motion>', self.moved)  

    def clicked(self, event):      
        print('single mouse click event at ({}, {})'.format(event.x, event.y))

    def double_click(self, event):
        global fullScreen
        print(fullScreen)
        if (fullScreen):
            fullScreen = False
            root.attributes('-fullscreen', True)
            myFont['size'] = math.floor(screen_width / 12)
            myFont_date['size'] = math.floor(screen_width / 20)
        else:
            fullScreen = True
            root.attributes('-fullscreen', False)
            myFont['size'] = math.floor(screen_width / 12)
            myFont_date['size'] = math.floor(screen_width / 20)

    def button_released(self, event):        
        print('button released')

    def moved(self, event):        
        print('mouse position is at ({:03}. {:03})'.format(event.x, event.y), end='\r')    
        

def clock():
    date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S/%p")
    date,time1 = date_time.split()
    time2,time3 = time1.split('/')
    hour,minutes,seconds =  time2.split(':')
    time = str(hour) + ':' + minutes + ':' + seconds
    time_label.config(text = time)
    date_label.config(text= date)
    time_label.after(1000, clock)
    
clock()
mouse = MouseControl(root)
tk.mainloop()