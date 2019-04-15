import tkinter as tk

window = tk.Tk()

window.title("OBJECT DETECTION")
window.geometry("400x400")


# ----LABEL1----
label1 = tk.Label(text="TensorFlow", font=('Comic Sans MS', 30))
label1.grid(column=0, row=0, padx=100, pady=100)
# ----BUTTON1----
button1 = tk.Button(text="Click me")
button1.grid(column=0, row=1)

# ----LABEL2----
label1 = tk.Label(text="YOLO_RealTime", font=('Comic Sans MS', 30))
label1.grid(column=1, row=0, padx=100, pady=100)
# ----BUTTON2----
button1 = tk.Button(text="Click me")
button1.grid(column=1, row=1)

# ----LABEL3----
label1 = tk.Label(text="YOLO", font=('Comic Sans MS', 30))
label1.grid(column=2, row=0, padx=100, pady=100)
# ----BUTTON3----
button1 = tk.Button(text="Click me")
button1.grid(column=2, row=1)


window.mainloop()
