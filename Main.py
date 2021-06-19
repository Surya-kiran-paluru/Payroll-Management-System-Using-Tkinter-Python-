from tkinter import *
import sqlite3
global approval_code 
approval_code = 789456
global basic_pay
basic_pay = 1000


window = Tk()
window.title("Payroll Management System")
window.geometry("1380x720")
from tkinter import messagebox

Status = StringVar()
Status.set("Status:IDLE")


def register():
    my_conn = sqlite3.connect("my_db.db")
    
    top = Toplevel()
    top.minsize(width=400, height=250)
    top.title("Registration")
    
    r_label = Label(top, text="REGISTER NOW", fg="red4", font=("ariel", 20, "bold")).grid(column=1, row=0, columnspan=2)
    space = Label(top, text="").grid(column=0, row=0)

    uname = Label(top, text="Username:", font=("ariel", 15)).grid(column=1, row=1)
    uentry = Entry(top, width=30).grid(column=2, row=1)
    
    name = Label(top, text="Name:", font=("ariel", 15)).grid(column=1, row=2)
    entry = Entry(top, width=30).grid(column=2, row=2)
    
    e_label = Label(top, text="Email:", font=("ariel", 15)).grid(column=1, row=3)
    e_entry = Entry(top, width=30).grid(column=2, row=3)
   
    ph_label = Label(top, text="Ph.Number:", font=("ariel", 15)).grid(column=1, row=4)
    ph_entry = Entry(top, width=30).grid(column=2, row=4)
    
    p_label = Label(top, text="Password:", font=("ariel", 15)).grid(column=1, row=5)
    p_entry = Entry(top, width=30).grid(column=2, row=5)
    
    cp_label = Label(top, text="Confirm Password:", font=("ariel", 15)).grid(column=1, row=6)
    cp_entry = Entry(top, width=30).grid(column=2, row=6)

    ac_label = Label(top, text="Approval code:", font=("ariel", 15)).grid(column=1, row=7)
    ac_entry = Entry(top, width=30).grid(column=2, row=7)



    def reg_add_data():
        global approval_code 
        temp = ac_entry.get()
        flag_validation = True
        f_name = uentry.get()
        l_name = entry.get()
        E_entry = e_entry.get()
        phentry = ph_entry.get()
        pentry = p_entry.get()
        cpentry = cp_entry.get()
        #ac = ac_entry.get()
        
        if ( (flag_validation) and (temp == '789456') and (pentry == cpentry) ):
            try:
                my_data = (f_name, l_name, E_entry, phentry, pentry, temp)
                my_query = "INSERT INTO Registered_users values(?,?,?,?,?,?)"
                my_conn.execute(my_query, my_data)
                my_conn.commit()
                
                uentry.delete(0, END)
                entry.delete(0, END)
                e_entry.delete(0, END)
                ph_entry.delete(0, END)
                p_entry.delete(0, END)
                cp_entry.delete(0,END)
                ac_entry.delete(0, END)

            except sqlite3.Error as my_error:
                print(my_error)
        else:
            print("ERROR")

    signup = Button(top, text="Sign up", command=reg_add_data).grid(column=1, row=8, columnspan=2)

    #Registration database code

    top.mainloop()
    my_conn.close()

def logged():
    my_conn = sqlite3.connect('my_db.db')
    username_trail = user_entry.get()
    password_trail = password_entry.get()
    flag = False
    count = 0
    check_user = my_conn.execute('''SELECT * from Registered_users''');
    for i in check_user:
        if(username_trail == i[0]):
            if(password_trail == i[4]):
                flag = True

    if flag == False:
        Status.set("Status: Incorrect Credentials")
    if(flag == True):
        Status.set("Status: Logged in successfully")
        click = Toplevel()
        click.minsize(width=280, height=80)
        click.title("Employee Details")

        
        ###################################### Module 2
        def show():
            empdispwin = Tk()
            empdispwin.geometry("750x250")
            
            
            
            i_d = emp_entry.get()
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=0)
            e.insert(END, "id")
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=1)
            e.insert(END, "name")
            
            e = Entry(empdispwin, width=25, fg='red')
            e.grid(row=0, column=2)
            e.insert(END, "mail")
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=3)
            e.insert(END, "contact")
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=4)
            e.insert(END, "attendence")

            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=5)
            e.insert(END, "bonus/extra")
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=6)
            e.insert(END, "pay status")
            
            e = Entry(empdispwin, width=10, fg='red')
            e.grid(row=0, column=7)
            e.insert(END, "Designation")
                    
            search_emp = my_conn.execute("SELECT * FROM employee")
            
            for i in search_emp:
                #print(i[0])
                
                if str(i[0]) == i_d :
                    for j in range(len(i)):
                        if j==2 :
                            e = Entry(empdispwin, width=25, fg='blue')
                        else:
                            e = Entry(empdispwin, width=10, fg='blue')
                        e.grid(row=1, column=j)
                        e.insert(END, i[j])
                    break
                
        def updatepay():
            i_d = emp_entry.get()
            search_emp = my_conn.execute("SELECT * FROM employee")
            for i in search_emp:
                #print(i[0])
                if str(i[0]) == i_d :
                    if str(i[6]) == 'yes':
                        my_conn.execute('''UPDATE employee
                                         SET payment = 'no'
                                         ''')
                    if str(i[6]) == 'no':
                        my_conn.execute('''UPDATE employee
                                         SET payment = 'yes'
                                         ''')
                       
               
        ######################################### End Module 2
        
        ######################################### Module 3
        def salary():
            i_d = emp_entry.get()
            search_emp = my_conn.execute("SELECT * FROM employee")
            for i in search_emp:
                
                if str(i[0]) == i_d :
                    global basic_pay
                    bp = basic_pay
                    
                    if(str(i[7]) == "Level 1"):
                        bp = bp*3
                    
                    if(str(i[7]) == "Level 2"):
                        bp = bp*2
                        
                    salary = (i[4] * bp) + i[5]
                
                    window = Tk()
                    window.minsize(width =400,height = 250)
                    
                    p_label = Label(window, text="PAYSLIP", fg="red4", font=("ariel", 20, "bold")).grid(column = 0,row = 1)
                   
                    empname= Label(window,text = f"Employee Name: {i[1]}",font=("ariel", 15)).grid(column = 0,row  = 2)
                    
                    empbon = Label(window,text = f"Designation : {i[7]}",font=("ariel", 15)).grid(column = 0,row = 3)
                   
                    empemail = Label(window,text = f"Employee Email : {i[2]}",font=("ariel", 15)).grid(column = 0,row = 4)
                    
                    empcon = Label(window,text = f"Employee Contact : {i[3]}",font=("ariel", 15)).grid(column = 0,row = 5)
                    
                    empatt = Label(window,text = f"Attendence : {i[4]}",font=("ariel", 15)).grid(column = 0,row = 6)
                    
                    empbon = Label(window,text = f"Bonus : {i[5]}",font=("ariel", 15)).grid(column = 0,row = 7)
                    
                    empsalary = Label(window,text = f"Salary : {salary}",font=("ariel", 15)).grid(column = 0,row = 8)
                    
                    window.mainloop()
                    break;
        ######################################### End Module 3
        
        ######################################### Module 4
        def add_employee():
            
            add = Toplevel()
            add.minsize(width=400, height=250)
            add.title("Add Employee")
            
            id_label = Label(add, text="Enter id: ")
            id_label.grid(column=1, row=0, columnspan=2)
            identry = Entry(add, width=30)
            identry.grid(column=3, row=0)
            
            name_label = Label(add, text="Enter Name: ")
            name_label.grid(column=1, row=1, columnspan=2)
            nameentry = Entry(add, width=30)
            nameentry.grid(column=3, row=1)
            
            mail_label = Label(add, text="Enter Mail: ")
            mail_label.grid(column=1, row=2, columnspan=2)
            mailentry = Entry(add, width=30)
            mailentry.grid(column=3, row=2)
            
            cn_label = Label(add, text="Enter Contact: ")
            cn_label.grid(column=1, row=3, columnspan=2)
            cnentry = Entry(add, width=30)
            cnentry.grid(column=3, row=3)
            
            des_label = Label(add, text="Enter Designation: ")
            des_label.grid(column=1, row=4, columnspan=2)
            desentry = Entry(add, width=30)
            desentry.grid(column=3, row=4)
            
            addStatus = StringVar()
            addStatus.set("Status: Idle")
            addst = Label(add,textvariable = addStatus).grid(column=3,row = 5)
            def add_det():
                #my_conn = sqlite3.connect("my_db.db")
                search_emp = my_conn.execute("SELECT * FROM employee")
        
                for i in search_emp:
                    if str(i[0]) == identry.get():
                        addStatus.set("Status: Id Already Exists")
                        return
                i_d = identry.get()
                name = nameentry.get()
                mail = mailentry.get()
                cn = cnentry.get()
                des = desentry.get()
                
                my_data = (i_d,name,mail,cn,0,0,des,"no")
                my_query = "INSERT INTO employee values(?,?,?,?,?,?,?,?)"
                my_conn.execute(my_query, my_data)
                my_conn.commit()
                addStatus.set('Status: Employee Added')
                        
            
            add_det = Button(add, text="Add Employee", command=add_det)
            add_det.grid(column=1, row=5, columnspan=2)
            
            add.mainloop()
            
        
        def delete():
            dwin = Tk()            
            i_d = int(emp_entry.get())
            search_emp = my_conn.execute("SELECT * FROM employee")
            
            for i in search_emp:
                if i[0] == i_d:
                    mytup = (i[1],i[2],i[3],i[6])
                    Label(dwin, text="Deleted Employee Details", fg="red4", font=("ariel", 20, "bold")).grid(column = 0,row  = 1)
                    empname= Label(dwin,text = f"Employee Name: {mytup[0]}",font=("ariel", 15)).grid(column = 0,row  = 2)
                    empmail= Label(dwin,text = f"Employee Mail: {mytup[1]}",font=("ariel", 15)).grid(column = 0,row  = 3)
                    empphn= Label(dwin,text = f"Employee Phone: {mytup[2]}",font=("ariel", 15)).grid(column = 0,row  = 4)
                    empdes= Label(dwin,text = f"Employee Desg.: {mytup[3]}",font=("ariel", 15)).grid(column = 0,row  = 5)
                    my_conn.execute("DELETE FROM employee WHERE empid = ?",(i_d,))
                    my_conn.commit()
                    dwin.mainloop()
                    return
            delmsg = Label(dwin,text = "No employee found",font=("ariel", 15)).grid(column = 0,row  = 1)
            dwin.mainloop()
        ######################################### End Module 4
        emp_id = Label(click, text="Employee Id:", font=("ariel", 15, "bold"))
        emp_id.grid(column=0, row=0)
        
        emp_entry = Entry(click, width=20)
        emp_entry.grid(column=1, row=0)
        
        emp_button1 = Button(click, text="Show Details",command = show)
        emp_button1.grid(column=0, row=1, columnspan=2)
        
        emp_button2 = Button(click, text="Update Payment Status",command = updatepay)
        emp_button2.grid(column=0, row=2, columnspan=2)
        
        emp_button3 = Button(click, text="Generate Payslip",command = salary)
        emp_button3.grid(column=0, row=3, columnspan=2)
        
        emp_button4 = Button(click, text="Add Employee",command = add_employee)
        emp_button4.grid(column=0, row=4, columnspan=2) 
        
        emp_button5 = Button(click, text="Del Employee",command = delete)
        emp_button5.grid(column=0, row=5, columnspan=2)
        
        emp_button6 = Button(click, text="Save and Quit",command = click.destroy)
        emp_button6.grid(column=0, row=6, columnspan=2)
        
        click.mainloop()
        my_conn.close()
        
            
#App Frontend Code.....
    
canvas = Canvas(height=700, width=1900)
img = PhotoImage(file="pic.png")
canvas.create_image(700, 300, image=img)
canvas.grid(row=0, column=1)

Label(window,textvariable = Status).place(x=720,y=200)

user = Label(text="Username:", bg="black", fg="white")
user.place(x=500, y=100)
user_entry = Entry(width=30)
user_entry.place(x=600, y=100)

password = Label(text="Password:", bg="black", fg="white")
password.place(x=500, y=125)
password_entry = Entry(width=30)
password_entry.place(x=600, y=125)

login = Button(text="Login",width = 10, command=logged)
login.place(x=600, y=150)

p = Label(text="PLEASE", font=("bold", 40), bg="ivory4")
p.place(x=950, y=350)

l = Label(text="LOGIN", font=("bold", 40), bg="ivory4")
l.place(x=1100, y=425)

s_label = Button(text="Register",width = 10, fg="blue", command=register)
s_label.place(x=700, y=150)

#f_label = Button(text="forgot password", fg="blue")
#f_label.place(x=720, y=150)


window.mainloop()