import os
import tkinter as tk

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'gray90', relief = 'raised')
canvas1.pack()

def myCmd ():
    os.system('cmd /k "color a & ping google.com -t"')
     
button1 = tk.Button(text='      Run Command      ', command=myCmd, bg='green', fg='white', font=('helvetica', 12, 'bold'))
canvas1.create_window(150, 100, window=button1)

root.mainloop()
