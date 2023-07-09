from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from tkcalendar import *
from PIL import Image,ImageTk
import mysql.connector as sql
from tabulate import tabulate

                    


def add_doctor():
    top4=Toplevel()
    top4.title("Add Doctor")
    top4.geometry("1366x768")
    

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def add_d():
        mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
        curr=mydbb.cursor()
        curr.execute("update last_no2 set last_no=%s"%e)
        mydbb.commit()
        mydbb.close()
        
        DoctorID=f
        Name=e5.get()
        Address=e6.get()
        Contact_No=e7.get()
        Category=mycombo.get()
        Password=e8.get()

        if (Name=="" or Address=="" or Contact_No=="" or Category=="" or Password==""):
            messagebox.showinfo("Insert status","All Fields are mandatory")
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("insert into doctor_registration values('"+ DoctorID +"','"+ Name +"','"+ Address +"','"+ Contact_No +"','"+ Category +"','"+ Password +"')")
            mydb.commit()

            
            

            messagebox.showinfo("Insert Status","Inserted Successfully")
            
            e5.delete(0,'end')
            e6.delete(0,'end')
            e7.delete(0,'end')
            mycombo.delete(0,'end')
            e8.delete(0,'end')
            mydb.close()
            


    l3=Label(top4,text="Add Doctor",font=("arial",40))
    l3.place(x=650,y=0)

   
    mydbb=sql.connect(host="localhost",user="root",password="a507a507",database="doctor_patient")       #Automatic ID
    curr=mydbb.cursor()
    curr.execute("select * from last_no2")
    d=curr.fetchone()
    e=d[0]+1                                        
    
    global f
    f=str(e)

    mydbb.close()                          #Automatic id

    DoctorID=Label(top4,text="Doctor ID",font=("arial",30))
    DoctorID.place(x=600,y=100)
    e4=Label(top4,text=f,width=15,font=("arial",25))
    e4.place(x=900,y=100)

    Name=Label(top4,text="Name",font=("arial",30))
    Name.place(x=600,y=200)
    e5=Entry(top4,font=("arial",25))
    e5.place(x=900,y=200)


    Address=Label(top4,text="Address",font=("arial",30))
    Address.place(x=600,y=300)
    e6=Entry(top4,font=("arial",25))
    e6.place(x=900,y=300)


    Contact_No=Label(top4,text="Contact No.",font=("arial",30))
    Contact_No.place(x=600,y=400)
    e7=Entry(top4,font=("arial",25))
    e7.place(x=900,y=400)


    Category=Label(top4,text="Category",font=("arial",30))
    Category.place(x=600,y=500)

    options=[
        "-Select-",
        "Physician",
        "Orthopedic",
        "Allergist",
        "Cardiologist",
        "Psychiatrist"]
    

    mycombo=ttk.Combobox(top4,font=("arial",20),value=options)
    mycombo.current(0)
    mycombo.place(x=900,y=500)

    Password=Label(top4,text="Password",font=("arial",30))
    Password.place(x=600,y=600)
    e8=Entry(top4,font=("arial",25))
    e8.place(x=900,y=600)

                

    btn=Button(top4,text="Submit",font=("Arial",20),command=add_d)
    btn.place(x=900,y=650)


    

    top4.mainloop()
    

def view_doctor():
    top4=Toplevel()
    top4.title("View Doctor")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)


    treev=ttk.Treeview(top4,columns=(1,2,3,4,5),show="headings",height="10")
    treev.place(x=400,y=400)

    style=ttk.Style()
    style.configure("Treeview", highlightthickness=0, bd=0, font=('Calibri', 14),rowheight=5)


    treev.column("1", width = 130, anchor ='c') 
    treev.column("2", width = 140, anchor ='c') 
    treev.column("3", width = 200, anchor ='c')
    treev.column("4", width = 140, anchor ='c') 
    treev.column("5", width = 140, anchor ='c') 

    treev.heading("1", text ="Doctor ID") 
    treev.heading("2", text ="Name") 
    treev.heading("3", text ="Address")
    treev.heading("4", text ="Contact_No") 
    treev.heading("5", text ="Category") 
  

    def v_doctor():
        DoctorID=int(e1.get())
        if (DoctorID==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select * from doctor_registration")
            v=cur.fetchall()


            for i in v:
                if i[0]==DoctorID:
                    
                    cur.execute("select DoctorID,Name,Address,Contact_No,Category from doctor_registration where DoctorID={}".format(DoctorID))
                    w=cur.fetchall()
                    
                    for t in w:
                        treev.insert("",'end',values=t)
                        
                    break
            else: 
                messagebox.showinfo("View Status","Doctor Not Found!",parent=top4)
                mydb.commit()
                

            mydb.close()
                    
            
    
            


    l=Label(top4,text="DoctorID",font=("arial",20))
    l.place(x=600,y=150)

    e1=Entry(top4,font=("arial",20))
    e1.place(x=900,y=150)

    b=Button(top4,text="Search",font=("arial",20),command=v_doctor)
    b.place(x=750,y=300)
                        


    top4.mainloop()

def update_doctor():
    top4=Toplevel()
    top4.title("Update Doctor")
    top4.geometry("1366x768")
    
    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)


    def update_d():
        DoctorID=e1.get()
        print(DoctorID)
        Category=mycombo.get()

        if Category=="Address":
            top5=Toplevel()
            top5.title("Update Doctor")
            top5.geometry("1366x768")
            
            image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                
            image=ImageTk.PhotoImage(image)

            label=Label(top5,image=image)
            label.pack(pady=0,padx=0)

            def update_address():
                New_Address=e2.get()
                
                if (New_Address==""):
                    messagebox.showinfo("Insert status","All Fields are mandatory")
                else:
                    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
                    cur=mydb.cursor()
                    st="update doctor_registration set Address='{}' where DoctorID={}".format(New_Address,DoctorID)
                    print(st)
                    cur.execute(st)
                    mydb.commit()

                    messagebox.showinfo("Update status","New Address Updated",parent=top5)

                    mydb.close()
                    

            l2=Label(top5,text="New Address",font=("arial",20))
            l2.place(x=600,y=200)

            e2=Entry(top5,font=("arial",20))
            e2.place(x=900,y=200)

            btn=Button(top5,text="Submit",font=("arial",20),command=update_address)
            btn.place(x=800,y=300)

            top5.mainloop()


        elif Category=="Contact_No":
            top6=Toplevel()
            top6.title("Update Doctor")
            top6.geometry("1366x768")
            
            image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                
            image=ImageTk.PhotoImage(image)

            label=Label(top6,image=image)
            label.pack(pady=0,padx=0)

            def update_contact():
                New_Contact=e3.get()
                
                if (New_Contact==""):
                    messagebox.showinfo("Insert status","All Fields are mandatory")
                else:
                    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
                    cur=mydb.cursor()
                    cur.execute("update doctor_registration set Contact_No={} where DoctorID={}".format(New_Contact,DoctorID))
                    mydb.commit()

                    messagebox.showinfo("Update status","New Contact No Updated",parent=top6)

                    mydb.close()
                    

            l3=Label(top6,text="New Contact No",font=("arial",20))
            l3.place(x=600,y=200)

            e3=Entry(top6,font=("arial",20))
            e3.place(x=900,y=200)

            btn2=Button(top6,text="Submit",font=("arial",20),command=update_contact)
            btn2.place(x=800,y=300)

            top6.mainloop()

    

    l=Label(top4,text="Update!!",font=("arial",40))
    l.place(x=450,y=50)
    DoctorID=Label(top4,text="DoctorID",font=("arial",30))
    DoctorID.place(x=500,y=200)

    e1=IntVar()
    e1=Entry(top4,font=("arial",25))
    e1.place(x=900,y=200)



    l1=Label(top4,text="Change",font=("arial",20))
    l1.place(x=600,y=300)

    options=[
        "-Select-",
        "Address",
        "Contact_No" ]

    mycombo=ttk.Combobox(top4,font=("arial",20),value=options)
    mycombo.current(0)
    mycombo.place(x=900,y=300)

    btn=Button(top4,text="Submit",font=("arial",20),command=update_d)
    btn.place(x=800,y=600)

    
    
    top4.mainloop()

def view_appointment():
    top4=Toplevel()
    top4.title("View Appointmnet")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
    cur=mydb.cursor()
    cur.execute("select * from book_appointment order by Date")
    v=cur.fetchall()



    treev=ttk.Treeview(top4,columns=(1,2,3,4,5,6),show="headings",height="20")
    treev.place(x=425,y=150)

    treev.column("1", width = 150, anchor ='c') 
    treev.column("2", width = 160, anchor ='c') 
    treev.column("3", width = 180, anchor ='c')
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

def remove_doctor():
    top4=Toplevel()
    top4.title("View Appointmnet")
    top4.geometry("1366x768")

    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Registration background............
    image=ImageTk.PhotoImage(image)

    label=Label(top4,image=image)
    label.pack(pady=0,padx=0)

    def remove_d():
        DoctorID=int(e1.get())
        if (DoctorID==""):
            messagebox.showinfo("Insert status","All Fields are mandatory",parent=top4)
        else:
            mydb=sql.connect(host="localhost",user="root",passwd="a507a507",database="doctor_patient")
            cur=mydb.cursor()
            cur.execute("select DoctorID from doctor_registration")
            v=cur.fetchall()


            for i in v:
                print(i[0])
                if i[0]==DoctorID:
                    cur.execute("delete from doctor_registration where DoctorID={}".format(DoctorID))
                    messagebox.showinfo("Delete Status","Record Deleted Successfully!",parent=top4)
                    mydb.commit()
                   
                    break
            else: 
                messagebox.showinfo("Delete Status","Doctor Not Found!",parent=top4)
                mydb.commit()
                

            e1.delete(0,'end')
            mydb.close()
            

    l1=Label(top4,text="DoctorID",font=("arial",20))
    l1.place(x=600,y=300)

    e1=Entry(top4,font=("arial",20))
    e1.place(x=900,y=300)

    b=Button(top4,text="Delete",font=("arial",20),command=remove_d)
    b.place(x=750,y=400)


    top4.mainloop()

def a_window():
    
    top3=Toplevel()
    top3.title("Admin window")
    top3.geometry("1366x768")
    
    image=Image.open("C:\\Users\\DELL\\Desktop\\Images for project\\i3.jpg")                  #Admin background............
    image=ImageTk.PhotoImage(image)

    label=Label(top3,image=image)
    label.pack(pady=0,padx=0)



    b1=Button(top3,text="Add Doctor",font=("arial",23,"bold"),border=0,command=add_doctor)
    b1.place(x=700,y=250)

    b2=Button(top3,text="View Doctor",font=("arial",23,"bold"),border=0,command=view_doctor)
    b2.place(x=700,y=150)

    b3=Button(top3,text="Update Doctor",font=("arial",23,"bold"),border=0,command=update_doctor)
    b3.place(x=700,y=350)

    b4=Button(top3,text="View Appiontment",font=("arial",23,"bold"),border=0,command=view_appointment)
    b4.place(x=700,y=50)

    b5=Button(top3,text="Remove Doctor",font=("arial",23,"bold"),border=0,command=remove_doctor)
    b5.place(x=700,y=450)

    b6=Button(top3,text="Logout",font=("arial",23,"bold"),border=0,command=top3.destroy)
    b6.place(x=700,y=550)




    top3.mainloop()


