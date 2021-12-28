import tkinter as tk

penghitung = 0
ink = 100
kertas = 100

master = tk.Tk()
master.title("Controller")
master.geometry("265x300")

def secondWindow():
      
    inputWindow = tk.Tk()
    inputWindow.title("Monitoring")
    inputWindow.geometry("300x300")
    tk.Label(inputWindow, text="Jenis Kertas     : ").grid(row=0, column=0,sticky=tk.W)
    tk.Label(inputWindow, text="Jumlah Cetak   : ").grid(row=1, column=0, sticky=tk.W)
    tk.Label(inputWindow, text="Sisa Tinta (%)  : ").grid(row=2, column=0, sticky=tk.W)
    tk.Label(inputWindow, text="Jumlah Kertas  : ").grid(row=3, column=0, sticky=tk.W)
    def total_print(): 
            global penghitung
            global ink
            penghitung = penghitung + 1
            label1.configure(text=f'{penghitung} x')
            label2.configure(text=f'{ink} %')
            if penghitung == 25:
                ink = ink - 1
                label2.configure(text=f'{ink} %')
            if penghitung == 50:
                ink = ink - 1
                label2.configure(text=f'{ink} %')
            if penghitung == 75:
                ink = ink - 1
                label2.configure(text=f'{ink} %')
            if penghitung == 100:
                ink = ink - 1
                label2.configure(text=f'{ink} %')
    label1 = tk.Label(inputWindow)
    label1.grid(column=1, row=1,sticky=tk.W)
    label2 = tk.Label(inputWindow)
    label2.grid(column=1, row=2,sticky=tk.W)
    Print = tk.Button(master, text="Print / Count", command=total_print).grid(row=2,column=0, columnspan=2, padx=20, pady=5, sticky=tk.W+tk.E)
    def reset(): 
            global penghitung
            penghitung = 0
            label1.configure(text=f'{penghitung} x')
    label1 = tk.Label(inputWindow)
    label1.grid(column=1, row=1)
    Reset = tk.Button(inputWindow, text="Reset", command=reset)
    Reset.grid(column=0, row=5)
    def saveInput1():
        a4 = inputA4.get()
        viewerA4.config(state='normal')
        viewerA4.delete(0, 'end')
        viewerA4.insert(0, a4)
        viewerA4.config(state='readonly')
        label3.configure(text=f'{a4} ')
    label3 = tk.Label(inputWindow)
    label3.grid(column=1, row=3,sticky=tk.W)
    inputA4 = tk.Entry(master, justify="center")
    viewerA4 = tk.Entry(master, justify="left")
    tk.Label(master, text="Total kertas : ").grid(row=0, column=0, sticky=tk.W)
    inputA4.grid(row=0, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
    tk.Button(master, text="Save Paper Value", command=saveInput1).grid(row=3, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)
    def saveInput2():
        jenis_kertas = inputPAPER.get()
        inputPAPER.config(state='normal')
        inputPAPER.delete(0, 'end')
        inputPAPER.insert(0, jenis_kertas)
        inputPAPER.config(state='readonly')
        label4.configure(text=f'{jenis_kertas} ')
    label4 = tk.Label(inputWindow)
    label4.grid(column=1, row=0,sticky=tk.W)
    jenis_kertas= tk.Entry(master, justify="left")
    inputPAPER= tk.Entry(master, justify="center")
    tk.Label(master, text="Jenis kertas : ").grid(row=1, column=0, sticky=tk.W)
    inputPAPER.grid(row=1, column=1, sticky=tk.N+tk.E+tk.S+tk.W)
    tk.Button(master, text="Save Paper Type", command=saveInput2).grid(row=4, column=0, columnspan=2, padx=20, pady=5, sticky=tk.E+tk.W)

tk.Button(master, text="Setting",command=secondWindow).grid(row=2, column=1, columnspan=1,sticky=tk.E+tk.W)

tk.mainloop()