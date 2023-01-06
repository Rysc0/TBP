from tkinter import *
import psycopg2 as db
from  tkcalendar import * 







conn = db.connect(database='postgres', user='postgres', password = 'postgres', host='127.0.0.1', port='5432')

print("open succ")

def login():
    # querry to see if these match
    query = """select ime_i_prezime, lozinka from zaposlenik where ime_i_prezime = '{0}' and lozinka = '{1}';""".format(
        username.get(), password.get()
    );
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    if result is not None and result[0] == username.get() and result[1] == password.get():
        loginFrame.destroy()
        mainFrame()

    else:
        username.delete(0, 'end')
        password.delete(0, 'end')
    




root = Tk()
root.title('Login')
root.geometry("300x300")
root.configure(background='grey')

loginFrame = Frame(master=root, background='black')
loginFrame.pack_configure(expand=TRUE)

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




def mainFrame():
    root.title("Tracker")
    root.geometry("1280x860")
    glavniFrame = Frame(master=root, background='grey')
    glavniFrame.grid()

    Label(master=glavniFrame, text='Ukupno odrađeno sati:').grid(
        column=0, row=0, pady=15, padx=5
    )
    Label(master=glavniFrame, text= 0).grid(column=1, row=0, padx=5, pady=15)
    # calendar widget
    cal = Calendar(glavniFrame, selectmode='day', year=2023, month=1, day=1)
    cal.grid(column=5, row=0)


# uvijek mora bit na kraju

root.mainloop()


