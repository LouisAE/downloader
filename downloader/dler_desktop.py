#python desktop
import dler
import tkinter as tk
from tkinter import ttk
from time import sleep

#savformat = "text"

def stop():
    print("ERROR:User Interrupt")
    raise
    

def start():
    dler.get_info(e1.get())
    dler.addr = e2.get()#没用？
    dler.withdraw_address()
    
    #e1.config(state=tk.NORMAL)
    #e2.config(state=tk.NORMAL)
    #b0.config(state=tk.NORMAL)
    #b2.config(state=tk.NORMAL)

"""
def SelectFormat(*args):
    savformat = c0.get()
    print(c0.get())
    #print(type(savtype))
"""

root = tk.Tk()
tk.Label(root,text="URL:").grid(row=0,column=0)
tk.Label(root,text="Save:").grid(row=1,column=0)
#tk.Label(root,text="Format:").grid(row=2,column=0)

tv1 = tk.StringVar()
tv2 = tk.StringVar()

e1 = tk.Entry(root,textvariable=tv1)
e1.grid(row=0,column=1,padx=10,pady=10)

e2 = tk.Entry(root,textvariable=tv2)
e2.grid(row=1,column=1,padx=10,pady=10)
"""
cv = tk.StringVar()
c0 = ttk.Combobox(root,textvariable=cv)
c0.grid(row=2,column=1,padx=10,pady=10)
c0["values"] = ("text","picture")
c0.bind("<<ComboboxSelected>>",SelectFormat)
c0.current(0)
"""

b0 = tk.Button(root,text="Start",command=start)
b0.grid(row=3,column=0,sticky="w",padx=10,pady=5)
b1 = tk.Button(root,text="Stop",command=stop)
b1.grid(row=3,column=1,padx=10,pady=5)
b2 = tk.Button(root,text="Exit",command=root.quit)
b2.grid(row=3,column=2,sticky="e",padx=10,pady=5)


root.mainloop()


