import tkinter as tk
from tkinter import ttk

# intializing the window
window = tk.Tk()
window.title("TABS")
# configuring size of the window
window.geometry('350x200')
#Create Tab Control
TAB_CONTROL = ttk.Notebook(window)
#Tab1
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Tab 1')
#Tab2
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Tab 2')
TAB_CONTROL.pack(expand=1, fill="both")
#Tab Name Labels
ttk.Label(TAB1, text="This is Tab 1").grid(column=0, row=0, padx=10, pady=10)
ttk.Label(TAB2, text="This is Tab 2").grid(column=0, row=0, padx=10, pady=10)
#Calling Main()
window.mainloop()