import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import pymysql

win = tk.Tk()
win.geometry("1350x700")
win.title("Information Store Management System")

label=tk.Label(win, text="Information Store Management System",font=("Airal",30,"bold"),border=12,relief=tk.GROOVE,bg="lightgray")
label.pack(side=tk.TOP,fill=tk.X)

#=================== Frame 1 =========================#

detail_frame = tk.LabelFrame(win,text="Enter Details",font=("Airal",25),bd=12,relief=tk.GROOVE,bg="lightgray")
detail_frame.place(x=20,y=90,width=420,height=575)

data_frame = tk.LabelFrame(win,bd=12,bg="lightgray",relief=tk.GROOVE)
data_frame.place(x=475,y=90,width=810,height=575)

#====================Variables=========================#
rollno = tk.StringVar()
name = tk.StringVar()
class_var = tk.StringVar()
division = tk.StringVar()
contact = tk.StringVar()
fathername = tk.StringVar()
address = tk.StringVar()
gender = tk.StringVar()
dob = tk.StringVar()

search_by = tk.StringVar()

#======================================================#
#=========== Entry ============#

rollno_lbl = tk.Label(detail_frame,text="Roll no ",font=("Airal",15),bg="lightgray")
rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=rollno)
rollno_ent.grid(row=0,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

name_lbl = tk.Label(detail_frame,text="Name ",font=("Airal",15),bg="lightgray")
name_lbl.grid(row=1,column=0,padx=2,pady=2)

name_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=name)
name_ent.grid(row=1,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

class_lbl = tk.Label(detail_frame,text="Class ",font=("Airal",15),bg="lightgray")
class_lbl.grid(row=2,column=0,padx=2,pady=2)

class_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=class_var)
class_ent.grid(row=2,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

div_lbl = tk.Label(detail_frame,text="Division ",font=("Airal",15),bg="lightgray")
div_lbl.grid(row=3,column=0,padx=2,pady=2)

div_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=division)
div_ent.grid(row=3,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

contact_lbl = tk.Label(detail_frame,text="Contact ",font=("Airal",15),bg="lightgray")
contact_lbl.grid(row=4,column=0,padx=2,pady=2)

contact_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=contact)
contact_ent.grid(row=4,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

fathername_lbl = tk.Label(detail_frame,text="Father Name ",font=("Airal",15),bg="lightgray")
fathername_lbl.grid(row=5,column=0,padx=2,pady=2)

fathername_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=fathername)
fathername_ent.grid(row=5,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

address_lbl = tk.Label(detail_frame,text="Address ",font=("Airal",15),bg="lightgray")
address_lbl.grid(row=6,column=0,padx=2,pady=2)

address_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=address)
address_ent.grid(row=6,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

gender_lbl = tk.Label(detail_frame,text="Gender ",font=("Airal",15),bg="lightgray")
gender_lbl.grid(row=7,column=0,padx=2,pady=2)

gender_ent = ttk.Combobox(detail_frame,font=("Airal",15),state="readonly",textvariable=gender)
gender_ent['values']=("Male","Female","Other")
gender_ent.grid(row=7,column=1,padx=2,pady=2)

#--------------------------------------------------------------#

dob_lbl = tk.Label(detail_frame,text="DOB ",font=("Airal",15),bg="lightgray")
dob_lbl.grid(row=8,column=0,padx=2,pady=2)

dob_ent = tk.Entry(detail_frame,bd=7,font=("Airal",15),textvariable=dob)
dob_ent.grid(row=8,column=1,padx=2,pady=2)

#=========================================#

#================ Function ===================#

def fetch_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    curr.execute("SELECT * FROM data")
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
        conn.close()

def add_fun():
    if rollno.get()=="" or name.get()=="" or class_var.get()=="" or division.get()=="" or contact.get()=="" or fathername.get()=="" or address.get()=="" or gender.get()=="" or dob.get()=="":
        messagebox.showerror("Error!","Please fill all the fields!")
    else:
        conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
        curr = conn.cursor()
        curr.execute("INSERT INTO data VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(rollno.get(),name.get(),class_var.get(),division.get(),contact.get(),fathername.get(),address.get(),gender.get(),dob.get()))
        conn.commit()
        conn.close()

        fetch_data() #---->This will fetch data after adding (means UPDATE)

def get_cursor(event):
    '''This function fetch the data for selected row'''
    cursor_row = student_table.focus()
    content = student_table.item(cursor_row)
    row = content["values"]
    rollno.set(row[0])
    name.set(row[1])
    class_var.set(row[2])
    division.set(row[3])
    contact.set(row[4])
    fathername.set(row[5])
    address.set(row[6])
    gender.set(row[7])
    dob.set(row[8])

def clear():
    '''This is function will clear the entry boxes'''
    rollno.set("")
    name.set("")
    class_var.set("")
    division.set("")
    contact.set("")
    fathername.set("")
    address.set("")
    gender.set("")
    dob.set("")


def update_fun():
    '''This function update data according to user'''
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    curr.execute("UPDATE data SET name=%s, class=%s, division=%s, contact=%s, fathername=%s, address=%s, gender=%s, dob=%s where rollno =%s",(name.get(),class_var.get(),division.get(),contact.get(),fathername.get(),address.get(),gender.get(),dob.get(),rollno.get()))
    conn.commit()
    conn.close()
    fetch_data()
    clear()

def delete():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    curr.execute("DELETE FROM data WHERE rollno = %s", rollno.get())
    conn.commit()
    conn.close()
    fetch_data() #---->This will fetch data after deleting (means UPDATE)
    clear()

def search_data():
    conn = pymysql.connect(host="localhost",user="root",password="",database="sms1")
    curr = conn.cursor()
    query = ""
    if search_by.get() == "Name":
        query = "SELECT * FROM data WHERE name LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "Roll No":
        query = "SELECT * FROM data WHERE rollno LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "Contact":
        query = "SELECT * FROM data WHERE contact LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "Father's Name":
        query = "SELECT * FROM data WHERE fathername LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "Class":
        query = "SELECT * FROM data WHERE class LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "Division":
        query = "SELECT * FROM data WHERE division LIKE '%{}%'".format(search_ent.get())
    elif search_by.get() == "DOB":
        query = "SELECT * FROM data WHERE dob LIKE '%{}%'".format(search_ent.get())
    curr.execute(query)
    rows = curr.fetchall()
    if len(rows)!=0:
        student_table.delete(*student_table.get_children())
        for row in rows:
            student_table.insert('',tk.END,values=row)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Error!","No data found!")
#================ Frame 2 ================#
#================ Button =================#

btn_frame = tk.LabelFrame(detail_frame,bd=10,relief=tk.GROOVE,bg="lightgray")
btn_frame.place(x=25,y=390,width=342,height=120)

#---------------------------------------------#
add_lbl = tk.Button(btn_frame,text="Add",bd=7,font=("Airal",13),width=15,bg="lightgray",command=add_fun)
add_lbl.grid(row=0,column=0,padx=2,pady=2)

update_lbl = tk.Button(btn_frame,text="Update",bd=7,font=("Airal",13),width=15,bg="lightgray",command=update_fun)
update_lbl.grid(row=0,column=1,padx=2,pady=2)

delete_lbl = tk.Button(btn_frame,text="Delete",bd=7,font=("Airal",13),width=15,bg="lightgray",command=delete)
delete_lbl.grid(row=1,column=0,padx=2,pady=2)

clear_lbl = tk.Button(btn_frame,text="Clear",bd=7,font=("Airal",13),width=15,bg="lightgray",command=clear)
clear_lbl.grid(row=1,column=1,padx=2,pady=2)


#================== Frame 3 =====================#
#================== Search ======================#

search_frame = tk.Frame(data_frame,bd=10,relief=tk.GROOVE,bg="lightgray")
search_frame.pack(side=tk.TOP,fill=tk.X)

#---------------------------------------------#
search_lbl = tk.Label(search_frame,text="Search",font=("Airal",14),bg="lightgray")
search_lbl.grid(row=0,column=0,padx=2,pady=2)

search_in = ttk.Combobox(search_frame,font=("Airal",14),state="readonly",textvariable=search_by)
search_in['values']=("Name","Roll No","Contact","Father's Name","Class","Division","DOB")
search_in.grid(row=0,column=1,padx=2,pady=2)

search_ent = tk.Entry(search_frame,bd=7,font=("Airal",15),textvariable=rollno)
search_ent.grid(row=0,column=2,padx=2,pady=2)

search_btn = tk.Button(search_frame,text="Search",font=("Arial",10),bg="lightgrey",bd=9,width=9,command=search_data)
search_btn.grid(row=0,column=4,padx=2,pady=2)

showall_btn = tk.Button(search_frame,text="Show All",font=("Arial",10),bg="lightgrey",bd=9,width=9,command=fetch_data)
showall_btn.grid(row=0,column=5,padx=2,pady=2)

#===================================================#

#===================== DATABASE Frame==============================#

main_frame = tk.Frame(data_frame,bg="lightgrey",bd=11,relief=tk.GROOVE)
main_frame.pack(fill=tk.BOTH,expand=True)
'''using tree view & tree view comes with ttk'''

y_scroll = tk.Scrollbar(main_frame,orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame,orient=tk.HORIZONTAL)

student_table = ttk.Treeview(main_frame,columns=("Roll No.","Name","Class","Division","Contact","Father's Name","Address","Gender","DOB"),yscrollcommand=y_scroll.set,xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT,fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM,fill=tk.X)

student_table.heading("Roll No.",text="Roll No.")
student_table.heading("Name",text="Name")
student_table.heading("Class",text="Class")
student_table.heading("Division",text="Division")
student_table.heading("Contact",text="Contact")
student_table.heading("Father's Name",text="Father's Name")
student_table.heading("Address",text="Address")
student_table.heading("Gender",text="Gender")
student_table.heading("DOB",text="DOB")

student_table['show']='headings'

student_table.column("Roll No.",width=100)
student_table.column("Name",width=100)
student_table.column("Class",width=100)
student_table.column("Division",width=100)
student_table.column("Contact",width=100)
student_table.column("Father's Name",width=100)
student_table.column("Address",width=150)
student_table.column("Gender",width=100)
student_table.column("DOB",width=100)

student_table.pack(fill=tk.BOTH,expand=True)

fetch_data()

student_table.bind("<ButtonRelease-1>",get_cursor)

#===================================================#
win.mainloop()