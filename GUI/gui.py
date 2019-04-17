import tkinter as tk
from tkinter import filedialog
import tkinter as tk
import os
import inspect
import pathlib

window = tk.Tk()

window.title("OBJECT DETECTION")
window.geometry("400x400")

# ----Function----


def mfileopen():
    file1 = filedialog.askopenfile()
    global p
    p = file1.name



def callYOLORealTime():
    os.system(' python3 yolo-real-time.py --yolo yolo-coco')


def callYOLO():
    os.system(' python yolo.py --image '+ p + ' --yolo yolo-coco ')

def callTensor():
    os.system('python3 test.py')



#----LABEL1----
label1 = tk.Label(text="TensorFlow", font=('Comic Sans MS', 30))
label1.grid(column=0, row=0, padx=100, pady=100)
# ----BUTTON1----
button1 = tk.Button(text="Click me",command = callTensor)
button1.grid(column=0, row=1)

# ----LABEL2----
label1 = tk.Label(text="YOLO_RealTime", font=('Comic Sans MS', 30))
label1.grid(column=1, row=0, padx=100, pady=100)
# ----BUTTON2----
button1 = tk.Button(text="Click me",command = callYOLORealTime)
button1.grid(column=1, row=1)

# ----LABEL3----
label3 = tk.Label(text="YOLO", font=('Comic Sans MS', 30))
label3.grid(column=2, row=0, padx=100, pady=100)


# ----BUTTON3----
file_label = tk.Label(text="Step 1:").grid(column=2, row=1)
button = tk.Button(text="open file ", command=mfileopen).grid(column=3, row=1)
label_button3 = tk.Label(text="Step 2 :").grid(column=2, row=2)
button3 = tk.Button(text="Click me", command=callYOLO)
button3.grid(column=3, row=2)

# ----LABEL4----
label4 = tk.Label(text="Own Model", font=('Comic Sans MS', 30))
label4.grid(column=4, row=0, padx=100, pady=100)

# ----BUTTON4----
file_label = tk.Label(text="Step 1:").grid(column=4, row=1)
button = tk.Button(text="open file ", command=mfileopen).grid(column=5, row=1)
label_button4 = tk.Label(text="Step 2 :").grid(column=4, row=2)
button4 = tk.Button(text="Click")
button4.grid(column=5, row=2)


window.mainloop()
