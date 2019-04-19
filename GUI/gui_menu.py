
import tkinter as tk
from tkinter import *
from tkinter import filedialog


class Window(Frame):

    def __init__(self, master=None):

        Frame.__init__(self, master)

        self.master = master

        self.init_window()

    def init_window(self):
        window.attributes('-zoomed', True)

        window.title("OBJECT DETECTION")
        window.geometry("400x400")

        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)

        file.add_command(label="Exit", command=self.client_exit)

        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)

        edit.add_command(label="Undo")

        menu.add_cascade(label="Edit", menu=edit)

        # ----Function----

        def mfileopen():
            file1 = filedialog.askopenfile()
            file_label = tk.Label(text=file1.name).grid(column=2, row=3)

        # ----LABEL1----
        label1 = tk.Label(text="TensorFlow", font=('Comic Sans MS', 30))
        label1.grid(column=0, row=0, padx=100, pady=100)
        # ----BUTTON1----
        button1 = tk.Button(text="Click me")
        button1.grid(column=0, row=1)

        # ----LABEL2----
        label2 = tk.Label(text="YOLO_RealTime", font=('Comic Sans MS', 30))
        label2.grid(column=1, row=0, padx=100, pady=100)
        # ----BUTTON2----
        button2 = tk.Button(text="Click me")
        button2.grid(column=1, row=1)

        # ----LABEL3----
        label3 = tk.Label(text="YOLO", font=('Comic Sans MS', 30))
        label3.grid(column=2, row=0, padx=100, pady=100)

        # ----BUTTON3----
        file_label = tk.Label(text="Step 1:").grid(column=2, row=1)
        button = tk.Button(text="open file ",
                           command=mfileopen).grid(column=3, row=1)
        label_button3 = tk.Label(text="Step 2 :").grid(column=2, row=2)
        button3 = tk.Button(text="Click me")
        button3.grid(column=3, row=2)

        # ----LABEL4----
        label4 = tk.Label(text="Own Model", font=('Comic Sans MS', 30))
        label4.grid(column=4, row=0, padx=100, pady=100)

        # ----BUTTON4----
        file_label = tk.Label(text="Step 1:").grid(column=4, row=1)
        button = tk.Button(text="open file ",
                           command=mfileopen).grid(column=5, row=1)
        label_button4 = tk.Label(text="Step 2 :").grid(column=4, row=2)
        button4 = tk.Button(text="Click")
        button4.grid(column=5, row=2)

    def client_exit(self):
        exit()


window = tk.Tk()


app = Window(window)


window.mainloop()

