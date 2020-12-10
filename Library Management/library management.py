from tkinter import *
import tkinter

from tkinter import messagebox
import pymysql
def functioninit():
    
    windo=tkinter.Tk()
    windo.title("Check Entry")

    windo.geometry("400x225")

    L3=Label(windo,text="Enter Student Id:",font=('arial',20),fg='blue')
    L3.grid(row=0,column=0)
    E3=Entry(windo,bd=5,width=25)
    E3.grid(row=0,column=1)


    def myButtonEvent(selection):

        id=E3.get()
        if selection in ('Check'):
            con=pymysql.connect("localhost","root","Password","database_name")
            cur=con.cursor()
            query = "SELECT * from record where id="
            while True:     
                loginID=id
                tmp_query=query+loginID
                cur.execute(tmp_query)
                if cur.rowcount==1:

                    print("Success")
                    function1()

                    break

                else:
                    function2()

                    break
                
                    
            con.close() 

    BCheck=tkinter.Button(windo,text='Check',fg='black',bg='orange',font=('arial',18,'bold'),command=lambda:myButtonEvent('Check'))
    BCheck.grid(row=5,column=1)

def function1():
    window=tkinter.Tk()
    window.title("Library Management System")
    window.geometry("800x450")

    L=Label(window,text="Enter Student Id:",font=('arial',30),fg='blue')
    L.grid(row=0,column=0)
    E=Entry(window,bd=5,width=50)
    E.grid(row=0,column=1)

    L1=Label(window,text="Enter Student Name:",font=('arial',30),fg='blue')
    L1.grid(row=1,column=0)
    E1=Entry(window,bd=5,width=50)
    E1.grid(row=1,column=1)

    L2=Label(window,text="Enter Book Id:",font=('arial',30),fg='blue')
    L2.grid(row=2,column=0)
    E2=Entry(window,bd=5,width=50)
    E2.grid(row=2,column=1)


    def myButton(selection):
        print("Student id is : ",E.get())
        print("Student name is : ",E1.get())
        print("Issued book id is : ",E2.get())

        id=E.get()
        name=E1.get()
        bookid=E2.get()

        if selection in ('Issue'):
            con=pymysql.connect("localhost","root","Password","database_name")
            cur=con.cursor()
            #cur.execute("select version()")
            #data=cur.fetchone()
            #print("Mysql Database version",data)

            query="create table if not exists student(id char(20) Not null,name char(20),bookid char(25))"

            try:
                cur.execute(query)
                con.commit()
                print("Table created successfully")

            except Error as e:
                print("Error occured at database table creation",e)
                con.rollback()
                con.close()
            
            insQuery="insert into student(id,name,bookid) values('%s','%s','%s')"%(id,name,bookid)

            try:
                cur.execute(insQuery)
                con.commit()
                print("Book issued successfully",id,", ",name,", ",bookid)
                con.close()
            except Error as e:
                print("Error occured at book issue",e)
                con.rollback()
                con.close()
        elif selection in ('Update'):
            try:
                query="update student set name='%s'"%(name)+", bookid='%s'"%(bookid)+" where id='%s'"%(id)
                con=pymysql.connect("localhost","root","Password","database_name")
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                con.close()
                print("student updated successfully..",id)
            except Error as e:
                print("Error occured at data updation",e)
                con.rollback()
                con.close()

        elif selection in ('Return'):
            try:
                query="delete from student where id='%s'"%(id)
                con=pymysql.connect("localhost","root","Password","database_name")
                cur=con.cursor()
                cur.execute(query)
                con.commit()
                con.close()
                print("Book returned successfully..",id)
            except Error as e:
                print("Error occured at book return",e)
                con.rollback()
                con.close()

        elif selection in ('Show'):
            try:
                query="select * from student where id='%s'"%(id)
                con=pymysql.connect("localhost","root","Password","database_name")
                cur=con.cursor()
                cur.execute(query)
                rows=cur.fetchall()
                bookid1=''
                name1=''
                id1=''
                for row in rows:
                    id1=row[0]
                    name1=row[1]
                    bookid1=row[2]

                E.delete(0,END)
                E1.delete(0,END)
                E2.delete(0,END)

                E.insert(0,id1)
                E1.insert(0,name1)
                E2.insert(0,bookid1)
                con.close()
                print("student fetch successfully..",id)
            except Error as e:
                print("Error occured at data fetch",e)
                con.close()



    BIssue=tkinter.Button(window,text='Issue',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:myButton('Issue'))
    BIssue.grid(row=5,column=0)

    BUpdate=tkinter.Button(window,text='Update',fg='blue',bg='yellow',font=('arial',20,'bold'),command=lambda:myButton('Update'))
    BUpdate.grid(row=5,column=1)

    BReturn=tkinter.Button(window,text='Return',fg='red',bg='white',font=('arial',20,'bold'),command=lambda:myButton('Return'))
    BReturn.grid(row=7,column=0)

    BShow=tkinter.Button(window,text='Show',fg='yellow',bg='white',font=('arial',20,'bold'),command=lambda:myButton('Show'))
    BShow.grid(row=7,column=1)


def function2():

    windowm=tkinter.Tk()
    windowm.title("New Registration")
    windowm.geometry("800x250")

    L=Label(windowm,text="Enter Student Id:",font=('arial',30),fg='blue')
    L.grid(row=0,column=0)
    E=Entry(windowm,bd=5,width=50)
    E.grid(row=0,column=1)

    L1=Label(windowm,text="Enter Student Name:",font=('arial',30),fg='blue')
    L1.grid(row=1,column=0)
    E1=Entry(windowm,bd=5,width=50)
    E1.grid(row=1,column=1)

    L2=Label(windowm,text="Enter Department:",font=('arial',30),fg='blue')
    L2.grid(row=2,column=0)
    E2=Entry(windowm,bd=5,width=50)
    E2.grid(row=2,column=1)

    def myButtonRegistration(selection):
        print("Student id is : ",E.get())
        print("Student name is : ",E1.get())
        print("Issued book id is : ",E2.get())

        id=E.get()
        name=E1.get()
        dept=E2.get()

        if selection in ('Make Entry'):
            con=pymysql.connect("localhost","root","Password","database_name")
            cur=con.cursor()

            query="create table if not exists record(id char(20) Not null,name char(20),dept char(25))"

            try:
                cur.execute(query)
                con.commit()
                #print("Table created successfully")

            except Error as e:
                print("Error occured at database table creation",e)
                con.rollback()
                con.close()
            
            insQuery="insert into record(id,name,dept) values('%s','%s','%s')"%(id,name,dept)

            try:
                cur.execute(insQuery)
                con.commit()
                print("Student Entry Done Successfully : ",id,", ",name,", ",dept)
                con.close()
            except Error as e:
                print("Error occured at Student Registration",e)
                con.rollback()
                con.close()


    BEntry=tkinter.Button(windowm,text='Make Entry',fg='black',bg='orange',font=('arial',20,'bold'),command=lambda:myButtonRegistration('Make Entry'))
    BEntry.grid(row=5,column=1)
    

functioninit()
mainloop()
