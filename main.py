import functools
import json
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

text = os.system("scrapy runspider crawler.py")

with open('output.json') as json_file:
    data = json.load(json_file)
names = list(data.keys())
values = list(data.values())
ratio = 1
modifiedByUser = True


def entry_callback(stringVar, second_stringVar):
    global modifiedByUser
    if not modifiedByUser:
        print("entry callback: canceled")
        modifiedByUser = True
        return
    print("entry callback:" + stringVar.get())
    modifiedByUser = False
    try:
        second_stringVar.set(round(float(stringVar.get()) * ratio, 3))
    except:
        second_stringVar.set(0)
    finally:
        print(ratio)


def entry_callback2(stringVar, second_stringVar):
    global modifiedByUser
    if not modifiedByUser:
        print("entry callback: canceled")
        modifiedByUser = True
        return
    print("entry callback:" + stringVar.get())
    modifiedByUser = False
    try:
        second_stringVar.set(round(float(stringVar.get()) / ratio, 3))
    except:
        second_stringVar.set(0)
    finally:
        print(ratio)


def comboBoxCallBack(event, firstBox, secondBox, entry):
    print("comboBox callback:")
    print(firstBox.get() + " " + secondBox.get())
    print(data[firstBox.get()])
    print(data[secondBox.get()])
    global ratio
    ratio = data[firstBox.get()] / data[secondBox.get()]
    print(ratio)
    entry.set(entry.get())


def buttonAction(entry1, entry2):
    entry1.set(entry2.get())


window = tk.Tk()
window.title("Currency Converter")
window.geometry("650x300")
window.resizable(0, 0)
window.iconphoto(False, tk.PhotoImage(file='icon.png'))

######## # # # # # # Left side # # # # # # ########
tk.Label(text="Currency", font=15).place(x=40, y=70)
comboBox1 = ttk.Combobox(window, font=("TkDefaultFont", 15), width=10,
                         values=names)
comboBox1.place(x=130, y=70)
comboBox1.current(0)

tk.Label(text="Amount", font=15).place(x=50, y=150)
stringVar1 = tk.StringVar()
stringVar1.trace('w', lambda name, index, mode, stringVar1=stringVar1: entry_callback(stringVar1, stringVar2))
entry1 = tk.Entry(window, textvariable=stringVar1, font=15, width=15).place(x=130, y=150)

######## # # # # # # Right side # # # # # # ########
tk.Label(text="Currency", font=15).place(x=390, y=70)
comboBox2 = ttk.Combobox(window, font=("TkDefaultFont", 15), width=10,
                         values=names)
comboBox2.place(x=480, y=70)
comboBox2.current(0)

tk.Label(text="Amount", font=15).place(x=400, y=150)
stringVar2 = tk.StringVar()
stringVar2.trace('w', lambda name, index, mode, stringVar2=stringVar2: entry_callback2(stringVar2, stringVar1))
entry2 = tk.Entry(window, textvariable=stringVar2, font=15, width=15).place(x=480, y=150)

######## # # # # # # Central # # # # # # ########
arrow_left = Image.open('arrow_left.png')
arrow_left = arrow_left.resize((50, 50), Image.ANTIALIAS)
my_arrow_left = ImageTk.PhotoImage(arrow_left)
tk.Button(master=window, text='press', command=lambda: buttonAction(stringVar1, stringVar2), image=my_arrow_left).place(
    x=300, y=75)

arrow_right = Image.open('arrow_right.png')
arrow_right = arrow_right.resize((50, 50), Image.ANTIALIAS)
my_arrow_right = ImageTk.PhotoImage(arrow_right)
tk.Button(master=window, text='press', command=lambda: buttonAction(stringVar2, stringVar1),
          image=my_arrow_right).place(x=300, y=125)

####
comboBox1.bind("<<ComboboxSelected>>",
               functools.partial(comboBoxCallBack, firstBox=comboBox1, secondBox=comboBox2, entry=stringVar2))
comboBox2.bind("<<ComboboxSelected>>",
               functools.partial(comboBoxCallBack, firstBox=comboBox1, secondBox=comboBox2, entry=stringVar1))

window.mainloop()
