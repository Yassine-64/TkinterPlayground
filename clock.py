import tkinter as tk 
from time import strftime

def update_time():
    
    time = strftime('%I:%M:%S %p')

    lbl.config(text=time)

    lbl.after(1000, update_time)



root =tk.Tk()

root.title("Digital clock")

lbl = tk.Label(root,font=('Digital-7',50, 'bold'),background='black',foreground='green')
lbl.pack(anchor='center')
update_time()
root.mainloop()
