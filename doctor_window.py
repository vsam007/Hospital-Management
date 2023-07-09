from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import *
from PIL import Image,ImageTk
import mysql.connector as sql


def my_details():
    top4=Toplevel()
    top4.title("My Details")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    treev=ttk.Treeview(top4)
    treev.place(x=400,y=250)

    style=ttk.Style()
    style.configure("Treeview.Heading",font=("Arial",17))
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14),rowheight=6)

    treev["columns"] = ("1", "2", "3","4","5","6") 
    treev['show'] = 'headings'

    treev.column("1", width = 130, anchor ='c') 
    treev.column("2", width = 160, anchor ='c') 
    treev.column("3", width = 180, anchor ='c')
    treev.column("4", width = 150, anchor ='c') 
    treev.column("5", width = 150, anchor ='c')
    treev.column("6",width= 150,anchor='c')

    treev.heading("1", text ="Doctor ID") 
    treev.heading("2", text ="Name") 
    treev.heading("3", text ="Address")
    treev.heading("4", text ="Contact_No") 
    treev.heading("5", text ="Category") 
    treev.heading("6", text ="Password")

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from doctor_registration where Name='{}'".format(name))
    v=cur.fetchall()
    
  
    for i in v:
        treev.insert("",'end',text="L1",values=i)
       

    mydb.close()

    top4.mainloop()
    
def view_appointment():
    top4=Toplevel()
    top4.title("View Appointment")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from book_appointment where Doctor='{}'".format(name))

    v=cur.fetchall()

    treev=ttk.Treeview(top4,columns=(1,2,3,4,5,6),show="headings",height="5")
    treev.place(x=400,y=300)


    treev.column("1", width = 170, anchor ='c') 
    treev.column("2", width = 160, anchor ='c') 
    treev.column("3", width = 180, anchor ='c')
    treev.column("4", width = 150, anchor ='c') 
    treev.column("5", width = 150, anchor ='c')
    treev.column("6", width = 160, anchor='c')
   
    treev.heading(1, text ="Appointment ID") 
    treev.heading(2, text ="Category") 
    treev.heading(3, text ="Date")
    treev.heading(4, text ="Time") 
    treev.heading(5, text ="Patient ID")
    treev.heading(6, text ="Doctor")

    for i in v:
        treev.insert("",'end',values=i)


    top4.mainloop()

def search_patient():
    top4=Toplevel()
    top4.title("View Appointment")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)



    def s_p():
        PatientID=e1.get()
        
        treevv=ttk.Treeview(top4,columns=(1,2,3,4,5),show="headings",height=3)
        treevv.place(x=400,y=200)



        treevv.column("1", width = 130, anchor ='c') 
        treevv.column("2", width = 160, anchor ='c') 
        treevv.column("3", width = 180, anchor ='c')
        treevv.column("4", width = 150, anchor ='c') 
        treevv.column("5", width = 150, anchor ='c') 
        
        treevv.heading("1", text ="Patient ID") 
        treevv.heading("2", text ="Name") 
        treevv.heading("3", text ="Address")
        treevv.heading("4", text ="Contact_No") 
        treevv.heading("5", text ="Organ")

        mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
        cur1=mydb.cursor()
        cur1.execute("select PatientID,Name,Address,Contact_No,Organ from user_registration where PatientID={}".format(PatientID))
        w=cur1.fetchall()


        for j in w:
            treevv.insert("",'end',values=j)
        
    

        treev=ttk.Treeview(top4,columns=(1,2,3,4,5,6),show="headings",height="5")
        treev.place(x=400,y=300)


        treev.column("1", width = 170, anchor ='c') 
        treev.column("2", width = 160, anchor ='c') 
        treev.column("3", width = 180, anchor ='c')
        treev.column("4", width = 150, anchor ='c') 
        treev.column("5", width = 150, anchor ='c')
        treev.column("6", width = 160, anchor='c')
       
        treev.heading(1, text ="Appointment ID") 
        treev.heading(2, text ="Category") 
        treev.heading(3, text ="Date")
        treev.heading(4, text ="Time") 
        treev.heading(5, text ="Patient ID")
        treev.heading(6, text ="Doctor")

       

        cur2=mydb.cursor()
        cur2.execute("select * from book_appointment where PatientID={} order by Date desc".format(PatientID))     
        v=cur2.fetchall()

        for i in v:
            treev.insert("",'end',values=i)


        
        treev2=ttk.Treeview(top4,columns=(1,2,3,4,5),show="headings",height="5")
        treev2.place(x=400,y=450)


        treev2.column("1", width = 160, anchor ='c') 
        treev2.column("2", width = 160, anchor ='c') 
        treev2.column("3", width = 170, anchor ='c')
        treev2.column("4", width = 170, anchor ='c') 
        treev2.column("5", width = 200, anchor ='c')
       
        treev2.heading(1, text ="Patient ID") 
        treev2.heading(2, text ="Name") 
        treev2.heading(3, text ="Treated For")
        treev2.heading(4, text ="Disease") 
        treev2.heading(5, text ="Note")

        cur3=mydb.cursor()
        cur3.execute("select * from description where PatientID={}".format(PatientID))
        z=cur3.fetchall()


        for y in z:
            treev2.insert("",'end',values=y)


        mydb.close()


    l1=Label(top4,text="PatientID",font=("arial",20))
    l1.place(x=600,y=50)

    e1=Entry(top4,font=("arial",20))
    e1.place(x=900,y=50)

    b=Button(top4,text="Submit",font=("arial",15),command=s_p)
    b.place(x=800,y=150)
    
    top4.mainloop()

def add_descp():
    top4=Toplevel()
    top4.title("View Appointment")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def a_d():
        PatientID=e1.get()
        Name=e2.get()
        Treated_For=e3.get()
        Treatment=e4.get()
        Note=e5.get()

        if (PatientID=="" or Name=="" or Treated_For=="" or Treatment=="" or Note==""):
            messagebox.showinfo("Insert Status","All Fields are mandetory",parent=top4)

        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("insert into description values('"+ PatientID +"','"+ Name +"','"+ Treated_For +"','"+ Treatment +"','"+ Note +"')")
            mydb.commit()

            e1.delete(0,'end')
            e2.delete(0,'end')
            e3.delete(0,'end')
            e4.delete(0,'end')
            e5.delete(0,'end')

            messagebox.showinfo("Insert Status","Inserted Successfully",parent=top4)

            mydb.close()

    l=Label(top4,text="Add Description",font=("arial",35))
    l.place(x=650,y=50)
                
    l1=Label(top4,text="PatientID",font=("arial",20))
    l1.place(x=600,y=150)

    e1=Entry(top4,font=("arial",20))
    e1.place(x=900,y=150)

    l2=Label(top4,text="Name",font=("arial",20))
    l2.place(x=600,y=250)

    e2=Entry(top4,font=("arial",20))
    e2.place(x=900,y=250)

    l3=Label(top4,text="Treated For",font=("arial",20))
    l3.place(x=600,y=350)

    e3=Entry(top4,font=("arial",20))
    e3.place(x=900,y=350)

    l4=Label(top4,text="Treatment",font=("arial",20))
    l4.place(x=600,y=450)

    e4=Entry(top4,font=("arial",20))
    e4.place(x=900,y=450)

    l5=Label(top4,text="Note",font=("arial",20))
    l5.place(x=600,y=550)

    e5=Entry(top4,font=("arial",20))
    e5.place(x=900,y=550)

    bt=Button(top4,text="Submit",font=("arial",20),command=a_d)
    bt.place(x=750,y=600)

    top4.mainloop()


def d_window(n):
    global name
    name=n

    top3=Toplevel()
    top3.title("Doctor window")
    top3.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")
    image=ImageTk.PhotoImage(image)

    label=Label(top3,image=image)
    label.pack(pady=0,padx=0)

    l=Label(top3,text="Welcome!!",font=("arial",35))
    l.place(x=650,y=50)
    
    b1=Button(top3,text="My Details",font=("arial",20),command=my_details)
    b1.place(x=700,y=150)

    b2=Button(top3,text="My Appointments",font=("arial",20),command=view_appointment)
    b2.place(x=700,y=250)

    b3=Button(top3,text="Search Patient",font=("arial",20),command=search_patient)
    b3.place(x=700,y=350)

    b4=Button(top3,text="Add Description",font=("arial",20),command=add_descp)
    b4.place(x=700,y=450)

    b5=Button(top3,text="Logout",font=("arial",20),command=top3.destroy)
    b5.place(x=700,y=550)


    top3.mainloop()
