#tk09.py
#modify to study git/github 2021/2/3
import tkinter as tk
root = tk.Tk()
root.title('.config(()')

root.geometry('350x150+300+800')
lb = tk.Label()
lb['text'] = 'ラベル'

print(lb.config())
root.mainloop()
