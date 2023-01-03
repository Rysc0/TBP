import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

masterFrame = tk.Frame(master=root, width=800, height=600, background='grey')
masterFrame.pack(padx=20, pady=20, fill='both', expand='True')


label = tk.Label(master=masterFrame, text='Login', font='Arial')
label.pack(pady=14)


username = tk.Entry(master=masterFrame)
username.pack(pady=5)

password = tk.Entry(master=masterFrame)
password.pack(pady=5)


loginButton = tk.Button(master=masterFrame, text='Login')
loginButton.pack()
# uvijek mora bit na kraju
root.mainloop()