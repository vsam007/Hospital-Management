from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import *
from PIL import Image,ImageTk
import mysql.connector as sql
from datetime import datetime


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
    treev.column("6", width = 150, anchor ='c')

    treev.heading("1", text ="Patient ID") 
    treev.heading("2", text ="Name") 
    treev.heading("3", text ="Address")
    treev.heading("4", text ="Contact_No") 
    treev.heading("5", text ="Password") 
    treev.heading("6", text ="Organ") 

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from user_registration where Name='{}'".format(name))
    v=cur.fetchall()

    
    for i in v:
        treev.insert("",'end',text="L1",values=i)
       

    mydb.close()
    top4.mainloop()

def book_appointment():
    top4=Toplevel()
    top4.title("Book Appointment")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def find_docs():
        Type=mycombo.get()

        mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")
        curr=mydbb.cursor()

        curr.execute("select Name from doctor_registration where Category='{}'".format(Type))
        v=curr.fetchall()
    
        docs.configure(value=v)
        docs.place(x=900,y=600)
        l5.configure(text="Select Doctor")
        l5.place(x=600,y=600)
        b2.config(state="normal")

    def book_a():
        mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
        curr=mydbb.cursor()
        curr.execute("update last_no3 set last_no=%s"%f)
        mydbb.commit()

        mydbb.close()                                      #Automatic id

        AppointmentID=f
        Category=mycombo.get()
        Date=c
        Time=Mycombo.get()
        PatientID=ee.get()
        Doctor=docs.get()

        if (Category=="" or Date=="" or Time==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            st="insert into book_appointment values('"+ AppointmentID +"','"+ Category +"','"+ Date +"','"+ Time +"','"+ PatientID +"','"+ Doctor +"')"
            cur.execute(st)
            mydb.commit()
            

            messagebox.showinfo("Insert Status","Inserted Successfully",parent=top4)
            
            mydb.close()

    mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
    curr=mydbb.cursor()
    curr.execute("select * from last_no3")
    d=curr.fetchone()
    e=d[0]+1

    global f

    f=str(e)
        
    mydbb.close()

    def a_date():                                               #date from calendar
        global c
        a=cal.selection_get()
        c=str(a)


    ll=Label(top4,text="PatientID",font=("arial",20))
    ll.place(x=600,y=50)

    ee=Entry(top4,font=("arial",20))
    ee.place(x=900,y=50)


    l1=Label(top4,text="Appointment ID",font=("arial",20))
    l1.place(x=600,y=100)
    e1=Label(top4,text=f,font=("arial",20))
    e1.place(x=900,y=100)

    l2=Label(top4,text="Category",font=("arial",20))
    l2.place(x=600,y=175)
    
    options=[
        "Choose--",
        "Physician",
        "Orthopedic",
        "Allergist",
        "Cardiologist",
        "Psychiatrist"]
    

    mycombo=ttk.Combobox(top4,font=("arial",20),value=options)
    mycombo.current(0)
    mycombo.place(x=900,y=175)

    l3=Label(top4,text="Date",font=("arial",20))           #Calendar
    l3.place(x=600,y=250)
    

    cal=Calendar(top4,width=12, background='darkblue',foreground='white',borderwidth=2,Calendar =2020) 
    cal.place(x=900,y=250)

    bt=Button(top4,text="select date",command=a_date)
    bt.place(x=900,y=450)


    l4=Label(top4,text="Time",font=("arial",20))
    l4.place(x=600,y=500)
    
    Options=[
        "Choose--",
        "10:00",
        "11:00",
        "12:00",
        "19:00",
        "20:00",
        "21:00 " ]
    Mycombo=ttk.Combobox(top4,font=("arial",20),value=Options)
    Mycombo.current(0)
    Mycombo.place(x=900,y=500)

    

    b1=Button(top4,text="Search",font=("arial",15),command=find_docs)
    b1.place(x=900,y=550)

    docs=ttk.Combobox(top4,font=("arial",20))

    l5=Label(top4,font=("arial",20))
    
    b2=Button(top4,text="Submit",font=("arial",15),command=book_a)
    b2.place(x=900,y=650)

    top4.mainloop()

def view_appointment():
    top4=Toplevel()
    top4.title("View Appiontment")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from book_appointment where PatientID={} order by Date".format(p_id))
    v=cur.fetchall()

    treev=ttk.Treeview(top4,columns=(1,2,3,4,5,6),show="headings",height="20")
    treev.place(x=425,y=150)


    treev.column("1", width = 170, anchor ='c') 
    treev.column("2", width = 160, anchor ='c') 
    treev.column("3", width = 170, anchor ='c')
    treev.column("4", width = 150, anchor ='c') 
    treev.column("5", width = 150, anchor ='c')
    treev.column("6", width = 160, anchor ='c')
   
    treev.heading(1, text ="Appointment ID") 
    treev.heading(2, text ="Category") 
    treev.heading(3, text ="Date")
    treev.heading(4, text ="Time") 
    treev.heading(5, text ="Patient ID")
    treev.heading(6, text ="Doctor")

    
    for i in v:
        treev.insert("",'end',values=i)

        
    mydb.close()


    top4.mainloop()

def cancel_booking():
    top4=Toplevel()
    top4.title("Search doctor")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def c_booking():
        AppointmentID=e2.get()
        
        mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
        cur=mydb.cursor()

        cur.execute("delete from book_appointment where AppointmentID={}".format(AppointmentID))
        mydb.commit()

        messagebox.showinfo("Canceled","Appointment Canceled",parent=top4)

        e2.delete(0,'end')

    l1=Label(top4,text="Cancel Booking!!",font=("arial",35))
    l1.place(x=450,y=50)

    l2=Label(top4,text="AppointmentID",font=("arial",20))
    l2.place(x=600,y=250)

    e2=Entry(top4,font=("arial",20))
    e2.place(x=900,y=250)

    bt=Button(top4,text="Submit",font=("arial",15),command=c_booking)
    bt.place(x=750,y=350)

  
    top4.mainloop()    


def search_doctor():
    top4=Toplevel()
    top4.title("Search doctor")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    treev=ttk.Treeview(top4,columns=(1,2,3),show="headings",height="10")
    treev.place(x=600,y=400)

 
    treev.column("1", width = 170, anchor ='c') 
    treev.column("2", width = 170, anchor ='c') 
    treev.column("3", width = 170, anchor ='c')
  
    
    treev.heading("1", text ="Name") 
    treev.heading("2", text ="Contact_No") 
    treev.heading("3", text ="Category") 
 



    def s_doctor():
        Category=mycombo.get()
        if (Category==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select * from doctor_registration")
            v=cur.fetchall()


            for i in v:
                if i[4]==Category:
                    cur.execute("select Name,Contact_No,Category from doctor_registration where Category='{}'".format(Category))
                    w=cur.fetchall()
                    
                    for t in w:
                        treev.insert("",'end',values=t)  
                    break
            else: 
                messagebox.showinfo("View Status","Doctor Not Found!",parent=top4)
                mydb.commit()
                

            mydb.close()
        
        


    l1=Label(top4,text="Category",font=("arial",20))
    l1.place(x=600,y=200)

    options=[
        "Choose--",
        "Physician",
        "Orthopedic",
        "Allergist",
        "Cardiologist",
        "Psychiatrist"]
    

    mycombo=ttk.Combobox(top4,font=("arial",20),value=options)
    mycombo.current(0)
    mycombo.place(x=900,y=200)


    b=Button(top4,text="Submit",font=("arial",15),command=s_doctor)
    b.place(x=750,y=300)


    top4.mainloop()

def donate_organ():
    top4=Toplevel()
    top4.title("Donate organ")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def d_organ():
        Name=e1.get()
        Organ=mycombo.get()
        if (Name==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("update user_registration set Organ='{}' where Name='{}'".format(Organ,Name))
            mydb.commit()

            e1.delete(0,'end')
            mycombo.delete(0,'end')
            messagebox.showinfo("Insert Status","Inserted Successfully",parent=top4)
            mydb.close()


    l=Label(top4,text="Donate Organ",font=("arial",40))
    l.place(x=650,y=0)

    l1=Label(top4,text="Name",font=("arial",30))
    l1.place(x=550,y=300)
    e1=Entry(top4,font=("arial",30))
    e1.place(x=850,y=300)

    l2=Label(top4,text="Organ",font=("arial",30))
    l2.place(x=550,y=450)
    options=[
        "Eye",
        "Kidney",
        "Heart",
        "Lung",
        "Pancrease"]


    mycombo=ttk.Combobox(top4,font=("arial",30),value=options)
    mycombo.current(0)
    mycombo.place(x=850,y=450)

    b=Button(top4,text="Submit",font=("arial",20),command=d_organ)
    b.place(x=750,y=550)
        

    top4.mainloop()

def search_donor():
    top4=Toplevel()
    top4.title("Search Donor")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def s_donor():
        Name=e1.get()
        Organ=mycombo.get()
        if (Name==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select Organ from user_registration where Organ='{}'".format(Organ))
            v=cur.fetchall()
                                          
            for i in v:
                if i[0]==Organ:
                    messagebox.showinfo("Donor","Congratulations!! Donor Found!",parent=top4)
                    break
            else:
                messagebox.showinfo("Donor","Donor Not Found!Try Again",parent=top4)
                
            e1.delete(0,'end')
            mycombo.delete(0,'end')
            mydb.close()


    l=Label(top4,text="Search Donor",font=("arial",40))
    l.place(x=650,y=0)

    l1=Label(top4,text="Name",font=("arial",30))
    l1.place(x=550,y=300)

    e1=Entry(top4,font=("arial",30))
    e1.place(x=850,y=300)


    l2=Label(top4,text="Organ",font=("arial",30))
    l2.place(x=550,y=450)
    options=[
        "Choose--",
        "Eye",
        "Kidney",
        "Heart",
        "Lung",
        "Pancrease"]


    mycombo=ttk.Combobox(top4,font=("arial",30),value=options)
    mycombo.current(0)
    mycombo.place(x=850,y=450)

    b=Button(top4,text="Submit",font=("arial",20),command=s_donor)
    b.place(x=750,y=550)



    top4.mainloop()

def logout():
    top3.destroy()
    
    return


def p_window(n,p):
    global name
    global password
    global p_id
    name=n
    password=p

    top3=Toplevel()
    top3.title("Patient window")
    top3.geometry("1366x768")


    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  
    image=ImageTk.PhotoImage(image)

    label=Label(top3,image=image)
    label.pack(pady=0,padx=0)

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from user_registration where Name='{}'".format(name))
    v=cur.fetchall()
    
    p_id=v[0][0]

    
    b1=Button(top3,text="My Details",font=("arial",20),border=0,command=my_details)
    b1.place(x=750,y=50)

    b2=Button(top3,text="Book Appointment",font=("arial",20),border=0,command=book_appointment)
    b2.place(x=750,y=125)

    b3=Button(top3,text="View Appointment",font=("arial",20),border=0,command=view_appointment)
    b3.place(x=750,y=200)

    b4=Button(top3,text="Cancel Booking",font=("arial",20),border=0,command=cancel_booking)
    b4.place(x=750,y=275)

    b5=Button(top3,text="Search Doctor",font=("arial",20),border=0,command=search_doctor)
    b5.place(x=750,y=350)

    b6=Button(top3,text="Donate Organ",font=("arial",20),border=0,command=donate_organ)
    b6.place(x=750,y=425)

    b7=Button(top3,text="Search Donor",font=("arial",20),border=0,command=search_donor)
    b7.place(x=750,y=500)


    b9=Button(top3,text="Logout",font=("arial",20),border=0,command=top3.destroy)
    b9.place(x=750,y=575)


    top3.mainloop()                   
