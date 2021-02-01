#tk09.py
import tkinter as tk
root = tk.Tk()
root.title('.config(()')

root.geometry('350x150+300+800')
lb = tk.Label()
lb['text'] = 'ラベル'

print(lb.config())
root.mainloop()
