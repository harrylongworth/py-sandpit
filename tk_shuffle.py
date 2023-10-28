#tk_hello
#REF: https://docs.python.org/3/library/tkinter.html
#grid man:
	# https://www.tcl.tk/man/tcl8.6/TkCmd/grid.html
	
	#tk ref: https://tcl.tk/man/tcl8.6/TkCmd/contents.htm
import random

def next_turn(myLabel):
	nextNum = random.random(1,10)
	myLabel['text']= nextNum
	
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font

#ref for font
# https://www.google.com/amp/s/www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/amp/


root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.configure(background = "black")


Desired_font = tk.font.Font( family = "Comic Sans MS", size = 30, weight = "bold") 

#frm
frm = ttk.Frame(root, padding=50)
frm.grid()
#frm.configure(background="red")
s = ttk.Style()
s.configure('TFrame', background='#7AC5CD')
s.configure('TFrame', background='black')
#s.configure('TLabel', color ='white')

#frm.configure(color= "red")
# set frame back:
# https://www.tutorialspoint.com/how-do-i-change-the-background-of-a-frame-in-tkinter

#BUT with ttk is different:
# https://stackoverflow.com/questions/54476511/setting-background-color-of-a-tkinter-ttk-frame

#with further details here:
# https://web.archive.org/web/20190509211714/http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/ttk-style-layer.html


#bigNumber
bigNumber = tk.Label(frm, text="20")
bigNumber.grid()
#bigNumber.configure(justify="center")

Font_tuple = ("Comic Sans MS", 60, "bold")
Font_tuple = ("Courier", 60, "bold")
Font_tuple = ("Helvetica", 80, "bold")

#bigNumber["font"] = Font_tuple
s.configure('TLabel', font = Font_tuple,backround='black',foreground="white",justify="center")

bigNumber['font'] =Font_tuple
bigNumber['bg'] = 'black'
bigNumber['fg'] = 'white'

#bigNumber["font"] = "courier"

#num2 = ttk.Label(frm,text="2")
#num2.grid()

#btn
btn = ttk.Button(frm, text="Quit", command=root.destroy)
#btn.grid()
button_font = ("Comic Sans MS", 20, "bold")
#s.configure('TButton', font = button_font,backround='#000000',foreground="white",justify="center")

s.configure('TButton', background='#7AC5CD')

btn = tk.Button(root, 
                bg='#000000',
                fg='#b7f731',
                relief='flat',
                text='Quit',
                width=20,
                font= button_font,
                command=root.destroy)
btn.grid()

btn2 = tk.Button(root, 
                bg='#000000',
                fg='#b7f731',
                relief='flat',
                text='Right',
                width=20,
                font= button_font,
                command=next_turn(bigNumber))
btn2.grid()

#btn["font"] = Desired_font

#btn.configure(activeforeground= "red")

#btn["fg"] = "red"
#btn.config(fg="red")

# btn.grid(column=1, row=13)
#print(dir(btn))

#print(btn.configure().keys())

#input("wait")

root.mainloop()



