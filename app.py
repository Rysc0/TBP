from tkinter import *

import psycopg2 as db
from  tkcalendar import * 


# calendar widget
# cal = Calendar(root, selectmode='day', year=2023, month=1, day=1)
# cal.pack(pady=10)

conn = db.connect(database='postgres', user='postgres', password = 'postgres', host='127.0.0.1', port='5432')

print("open succ")

# def window():
#     mainwindow = Toplevel(root)
#     mainwindow.title = "Main"
#     mainwindow.geometry("1280x860")
   
#     return mainwindow



def login():
    # querry to see if these match
    query = """select ime_i_prezime, lozinka from zaposlenik where ime_i_prezime = '{0}' and lozinka = '{1}';""".format(
        username.get(), password.get()
    );
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)


root = Tk()
root.title('Login')
root.geometry("1280x860")
root.configure(background='grey')


loginFrame = Frame(master=root, background='grey')
loginFrame.pack_configure(expand=TRUE)
# loginFrame.grid()



username_label = Label(master=loginFrame, text='Username',font='Arial')
username_label.grid(column=0, row=0, padx=5, pady=5)
password_label = Label(master=loginFrame, text='Password', font='Arial')
password_label.grid(column=0, row=1, padx=5, pady=5)

username = Entry(master=loginFrame)
username.grid(column=3, row=0, padx=5, pady=5)

password = Entry(master=loginFrame)
password.grid(column=3, row=1, padx=5, pady=5)

loginButton = Button(master=loginFrame, text='Login', command=login)
loginButton.grid(column=3, row=3, pady=10)

# uvijek mora bit na kraju
root.mainloop()