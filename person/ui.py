from tkinter import *
from tkinter import ttk

from person.create import Create
from person.select import Select


def press(click):
    if click == "create":

        name = style['en_name']['textvariable'].get()
        family = style['en_family']['textvariable'].get()
        age = style['en_age']['textvariable'].get()
        phone = style['en_phone']['textvariable'].get()
        Create(name, family, age, phone).create_data()

    elif click == "exit":
        master.destroy()


def select_data():
    print("fhsfj")
    phone=phone_entry.get()
    print(phone)
    s=Select(phone)
    s.select_info()




master = Tk()


style = {
    'lbl_name': {
        'text': 'Name:',
    },
    'lbl_family': {
        'text': 'Family:'
    },
    'lbl_age': {
        'text': 'Age:'
    },
    'lbl_phone': {
        'text': 'Phone:'
    },
    'en_name':{
        'textvariable': StringVar(),
        'width': 40,
        'bg': '#B3E5FC'
    },
    'en_family': {
        'textvariable': StringVar(),
        'width': 40,
        'bg': '#B3E5FC'
    },
    'en_age': {
        'textvariable': StringVar(),
        'width': 40,
        'bg': '#B3E5FC'
    },
    'en_phone': {
        'textvariable': StringVar(),
        'width': 40,
        'bg': '#B3E5FC'
    },
    'btn_create': {
        'text': 'Create',
        'command': lambda : press('create'),
        'width': 20,
        'borderwidth': 3,
        'relief': 'raised',
        'bg': '#4CAF50',
    },
    'btn_exit': {
        'text': 'Exit',
        'command': lambda : press('exit'),
        'width': 20,
        'borderwidth': 3,
        'relief': 'raised',
        'bg': '#f44336',
    }
}

#####create
root_tabs = ttk.Notebook(master)

create_tab = ttk.Frame(root_tabs)
root_tabs.add(create_tab, text='create')

select_tab = ttk.Frame(root_tabs)
root_tabs.add(select_tab, text='select')

update_tab = ttk.Frame(root_tabs)
root_tabs.add(update_tab, text='delete')

delete_tab = ttk.Frame(root_tabs)
root_tabs.add(delete_tab, text='update')

root_tabs.pack()

Label(create_tab, cnf=style['lbl_name']).grid(row=0, column=0, sticky='w')
Entry(create_tab, cnf=style['en_name']).grid(row=1, column=0)

Label(create_tab, cnf=style['lbl_family']).grid(row=2, column=0, sticky='w')
Entry(create_tab, cnf=style['en_family']).grid(row=3, column=0)

Label(create_tab, cnf=style['lbl_age']).grid(row=4, column=0, sticky='w')
Entry(create_tab, cnf=style['en_age']).grid(row=5, column=0)

Label(create_tab, cnf=style['lbl_phone']).grid(row=6, column=0, sticky='w')
Entry(create_tab, cnf=style['en_phone']).grid(row=7, column=0)

Button(create_tab, cnf=style['btn_create']).grid(row=8, column=0)
Button(create_tab, cnf=style['btn_exit']).grid(row=9, column=0)

#####select

phone_label=Label(select_tab,text="Phone")
phone_label.grid(row=0,column=0)

phone_entry=Entry(select_tab)
phone_entry.grid(row=0,column=1)

btn_select=Button(select_tab, text="search", command=select_data)
btn_select.grid(row=0,column=3)

###update

phone_number=Label(select_tab,text="Phone")
phone_number.grid(row=0,column=0)

phone_number_entry=Entry(select_tab)
phone_number_entry.grid(row=0,column=1)

btn_update=Button(select_tab, text="search")
btn_update.grid(row=0,column=3)
master.mainloop()