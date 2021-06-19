#Module 2
import sqlite3
from tkinter import *
  
conn = sqlite3.connect('my_db.db')
c = conn.cursor()
#c.execute('''DROP TABLE employee''')
try:
    conn.execute('''
    CREATE TABLE IF NOT EXISTS employee(
    empid int,
    name text,
    email text,
    phone text,
    attendence int,
    bonus int,
    payment text,
    designation text
    );''')
    conn.commit()
    print("Table created successfully")
except sqlite3.Error as my_error:
    print("error: ", my_error)

comm = "INSERT INTO employee (empid,name,email,phone,attendence,bonus,payment,designation) VALUES (?,?,?,?,?,?,?,?)"


my_w = Tk()
my_w.geometry("600x250")
conn = sqlite3.connect('my_db.db')

e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=0)
e.insert(END, "Id")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=1)
e.insert(END, "Name")
            
e = Entry(my_w, width=25, fg='red')
e.grid(row=0, column=2)
e.insert(END, "Mail")
            
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=3)
e.insert(END, "Contact")
           
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=4)
e.insert(END, "Attendence")

e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=5)
e.insert(END, "PA+TA")
    
e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=6)
e.insert(END, "Designation")

e = Entry(my_w, width=10, fg='red')
e.grid(row=0, column=7)
e.insert(END, "Pay Status")

r_set = conn.execute('''SELECT * from employee''');
i = 1
for enter in r_set:
    for j in range(len(enter)):
        if j==2 :
            e = Entry(my_w, width=25, fg='blue')
        else:
            e = Entry(my_w, width=10, fg='blue')
        e.grid(row=i, column=j)
        e.insert(END, enter[j])
    i = i + 1

my_w.mainloop()