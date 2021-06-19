#Module 1
import sqlite3
from tkinter import *
my_conn = sqlite3.connect('my_db.db')
print("Connected to database successfully")

try:
    my_conn.execute('''
    CREATE TABLE IF NOT EXISTS Registered_users(uname text,
    name text,
    email text,
    phone text,
    password text,
    approval text
    );''')
    my_conn.commit()
    print("Table created successfully")
except sqlite3.Error as my_error:
    print("error: ", my_error)

my_conn = sqlite3.connect('my_db.db')

my_w = Tk()
my_w.geometry("600x250")

e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=0)
e.insert(END, "username")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=1)
e.insert(END, "name")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=2)
e.insert(END, "email")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=3)
e.insert(END, "contact")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=4)
e.insert(END, "password")

e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=5)
e.insert(END, "appr. code")

r_set = my_conn.execute('''SELECT * from Registered_users''');
i = 1
for enter in r_set:
    for j in range(len(enter)):
        e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, enter[j])
    i = i + 1

my_w.mainloop()