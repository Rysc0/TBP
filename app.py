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

    InOfficeLabel = Label(master=glavniFrame, text='People in office').grid(column=0 ,columnspan=2, row=0, pady=5)
    InOfficeListbox = Listbox(master=glavniFrame, width=40).grid(column=0, columnspan=2, row=1, pady=5, padx=5)

    BolovanjeLabel = Label(master=glavniFrame, text='Sick').grid(column=3, row=0, pady=5, padx=5)
    BolovanjeListbox = Listbox(master=glavniFrame, width=40).grid(column=3, row=1, pady=5, padx=5)

    GodisnjiLabel = Label(master=glavniFrame, text='Vacation').grid(column=4, row=0, pady=5, padx=5)
    GodisnjiListbox = Listbox(master=glavniFrame, width=40).grid(column=4, row=1, pady=5, padx=5)
    

    ukupnoodradeno = Label(master=glavniFrame, text='Ukupno odrađeno sati:').grid(
        column=0, row=2, pady=15, padx=5
    )
    ukupnoodradenosatiLabel = Label(master=glavniFrame, text= 0).grid(column=1, row=2, padx=5, pady=15)
    
    NoviUnosLabel = Label(master=glavniFrame, text="Novi zapis").grid(column=0, row=3)
    DatumLabel = Label(master=glavniFrame, text='Datum').grid(column=0, row=4, pady=5)
    DatumEntry = Entry(master=glavniFrame, state='disabled').grid(column=1, row=4)
    SatiLabel = Label(master=glavniFrame, text="Sati:").grid(column=0, row=5, pady=5)
    SatiEntry = Entry(master=glavniFrame).grid(column=1, row=5)
    UnesiButton = Button(master=glavniFrame, text="Unesi", state='disabled').grid(column=1, row=6, pady=5)

    PlacaLabel = Label(master=glavniFrame, text="Placa:").grid(column=0, row=8, pady=5)
    PlacaEntry = Entry(master=glavniFrame, state='disabled').grid(column=1, row=8)

    # calendar widget
    cal = Calendar(glavniFrame, selectmode='day', year=2023, month=1, day=1)
    cal.grid(column=5, row=1, padx=15)




# uvijek mora bit na kraju
root.mainloop()


