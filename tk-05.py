import tkinter as tk
root = tk.Tk()
root.title ('Position and size setting')
root.geometry('450x150')
lb = tk.Label(text='Label-1')
bt = tk.Button(text='BUTTON-1')
lb.pack()
bt.pack()
root.mainloop()
