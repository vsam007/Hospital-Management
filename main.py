from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import *
from PIL import Image,ImageTk
import mysql.connector as sql
from tabulate import tabulate


def func1():                                     #Login window
    top1=Toplevel()
    top1.title("Admin")
    top1.geometry("1366x768")

    def login():
        Name=e1.get()
        Password=e2.get()
        if (Name=="" or Password==""):
            messagebox.showinfo("Login status","All Fields are mandatory",parent=top1)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select * from admin_login where Name=%s and Password=%s",(Name,Password))
            data=cur.fetchone()
            if data==None:
                messagebox.showerror("Login status","username or Password invalid",parent=top1)

            else:
                messagebox.showinfo("Login status","Successfully Logined",parent=top1)
                top1.destroy()
                import admin_window
                admin_window.a_window()

            mydb.close()


                
        

         

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i5.jpg")          #Login page.................
    image=ImageTk.PhotoImage(image)

    label=Label(top1,image=image)
    label.pack(pady=0,padx=0)

  
    Name=Label(top1,text="Username",font=("arial",25))
    Name.place(x=700,y=300)
    e1=Entry(top1,font=("arial",25))
    e1.place(x=900,y=300)
    
    Password=Label(top1,text="Password",font=("arial",25))
    Password.place(x=700 ,y=400)
    e2=Entry(top1,show="*",font=("arial",25))
    e2.place(x=900,y=400)

    b=Button(top1,text="Login",font=("arial",20),command=login)
    b.place(x=950,y=500)


    top1.mainloop()
    
###########################################################################################################################################################################################
def func2():
    top1=Toplevel()
    top1.title("User")
    top1.geometry("1366x768")

    
    def fun():                                                           #Registration window
        top2=Toplevel()
        top2.title("Registration")
        top2.geometry("1366x768")

        image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
        image=ImageTk.PhotoImage(image)

        label=Label(top2,image=image)
        label.pack(pady=0,padx=0)
        def add_p():
            mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
            curr=mydbb.cursor()
            curr.execute("update last_no1 set last_no=%s"%f)
            mydbb.commit()

            mydbb.close()                                      #Automatic id

            
            PatientID=f
            Name=e5.get()
            Address=e6.get()
            Contact_No=e7.get()
            Password=e8.get()

            if (Name=="" or Address=="" or Contact_No=="" or Password==""):
                messagebox.showinfo("Insert status","All Fields are mandatory",parent=top2)
            else:
                mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
                cur=mydb.cursor()
                st="insert into user_registration values('"+ PatientID +"','"+ Name +"','"+ Address +"','"+ Contact_No +"','"+ Password +"',"+ "NULL" +")"
                cur.execute(st)
                mydb.commit()

                messagebox.showinfo("Insert Status","Inserted Successfully",parent=top1)
                
                mydb.close()

        l3=Label(top2,text="Registration!!",font=("arial",40))
        l3.place(x=650,y=0)

        mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
        curr=mydbb.cursor()
        curr.execute("select * from last_no1")
        d=curr.fetchone()
        e=d[0]+1

        global f

        f=str(e)
        
        mydbb.close()


        PatientID=Label(top2,text="Patient ID",font=("arial",30))
        PatientID.place(x=600,y=100)
        e4=Label(top2,text=f,width=15,font=("arial",25))
        e4.place(x=900,y=100)

        Name=Label(top2,text="Name",font=("arial",30))
        Name.place(x=600,y=200)
        e5=Entry(top2,font=("arial",25))
        e5.place(x=900,y=200)


        Address=Label(top2,text="Address",font=("arial",30))
        Address.place(x=600,y=300)
        e6=Entry(top2,font=("arial",25))
        e6.place(x=900,y=300)

        Contact_No=Label(top2,text="Contact No.",font=("arial",30))
        Contact_No.place(x=600,y=400)
        e7=Entry(top2,font=("arial",25))
        e7.place(x=900,y=400)


        Password=Label(top2,text="Password",font=("arial",30))
        Password.place(x=600,y=500)
        e8=Entry(top2,font=("arial",25))
        e8.place(x=900,y=500)

        btn=Button(top2,text="Submit",font=("Arial",25),command=add_p)
        btn.place(x=900,y=550)

        cls=Button(top2,text="Close",font=("arial",25),border=0,fg="blue",command=top2.destroy)
        cls.place(x=900,y=650)

        top2.mainloop()

    def login():
        Name=e1.get()
        Password=e2.get()
        if (Name=="" or Password==""):
            messagebox.showinfo("Login status","All Fields are mandatory",parent=top1)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select * from user_registration where Name=%s and Password=%s",(Name,Password))
            data=cur.fetchone()
            if data==None:
                messagebox.showerror("Login status","username or Password invalid",parent=top1)

            else:
                messagebox.showinfo("Login status","Successfully Logined",parent=top1)
                top1.destroy()
                import patient_window
                patient_window.p_window(Name,Password)
                

            mydb.close()
               
    

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i5.jpg")                #Login page.............
    image=ImageTk.PhotoImage(image)

    label=Label(top1,image=image)
    label.pack(pady=0,padx=0)


    Name=Label(top1,text="Username",font=("arial",25))
    Name.place(x=700,y=300)
    e1=Entry(top1,font=("arial",25))
    e1.place(x=900,y=300)
    
    Password=Label(top1,text="Password",font=("arial",25))
    Password.place(x=700 ,y=400)
    e2=Entry(top1,show="*",font=("arial",25))
    e2.place(x=900,y=400)
   

    b=Button(top1,text="Login",font=("arial",20),command=login)
    b.place(x=950,y=500)

    lb=Label(top1,text="Not registered?",font=("arial",15))   
    lb.place(x=850,y=600)

    bt=Button(top1,text="Register",font=("arial",15),command=fun)      #Registration
    bt.place(x=1000,y=600)

    top1.mainloop()

   
#***************************************************************************************************************************************************************
    
def func3():
    top1=Toplevel()
    top1.title("Doctor Window")
    top1.geometry("1366x768")

    def login():
        Name=e1.get()
        Password=e2.get()
        if (Name=="" or Password==""):
            messagebox.showinfo("Login status","All Fields are mandatory",parent=top1)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select * from doctor_registration where Name=%s and Password=%s",(Name,Password))
            data=cur.fetchone()
            if data==None:
                messagebox.showerror("Login status","username or Password invalid",parent=top1)

            else:
                messagebox.showinfo("Login status","Successfully Logined",parent=top1)
                top1.destroy()
                import doctor_window
                doctor_window.d_window(Name)

            mydb.close()

         



    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i5.jpg")          #Login Page...............
    image=ImageTk.PhotoImage(image)

    label=Label(top1,image=image)
    label.pack(pady=0,padx=0)


    l1=Label(top1,text="Username",font=("arial",25))
    l1.place(x=700,y=300)
    e1=Entry(top1,font=("arial",25))
    e1.place(x=900,y=300)
    
    l2=Label(top1,text="Password",font=("arial",25))
    l2.place(x=700 ,y=400)
    e2=Entry(top1,show="*",font=("arial",25))
    e2.place(x=900,y=400)
   

    b=Button(top1,text="Login",font=("arial",20),command=login)
    b.place(x=950,y=500)
    
    top1.mainloop()
    



    
root1=Tk()
root1.title("Doctor-Pateint Portal")
root1.geometry("1300x600")
root1.resizable(0,0)

image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\main 1.jpg")
image=ImageTk.PhotoImage(image)

l=Label(root1,image=image)
l.pack(pady=0,padx=0)


b1=Button(root1,text="Admin",font=("arial",40),command=func1)
b1.place(x=100,y=100)

b2=Button(root1,text="Patient",font=("arial",40),command=func2)
b2.place(x=100,y=250)

b3=Button(root1,text="Doctor",font=("arial",40),command=func3)
b3.place(x=100,y=400)



root1.mainloop()
