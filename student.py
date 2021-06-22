####============================= Student Management System Using Python and MySql ===================================###

##=============================== Function Used to Add Student =======================================================##

def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            if(id=="" or name=="" or mobile=="" or email=="" or address=="" or gender=="" or dob==""):
                messagebox.showerror("Error","All Fields Are Required")
            else:
                strr = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(strr, (id, name, mobile, email, address, gender, dob, addeddate, addedtime))
                con.commit()
                res = messagebox.askyesnocancel('Notification','Id {} Name {} Added Sucessfully..... and You Want to clean the form'.format(id, name), parent=addroot)
                if (res == True):
                    idval.set('')
                    nameval.set('')
                    mobileval.set('')
                    emailval.set('')
                    addressval.set('')
                    genderval.set('')
                    dobval.set('')
        except:
          messagebox.showerror('Notification','Id Already Exit try another id..',parent=addroot)
        strr = 'select * from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenttable.insert('',END,values=vv)




    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x480+115+180')
    addroot.title('Student Management System')
    addroot.config(bg='deep sky blue')
    addroot.iconbitmap("./res/std_inner.ico")
    addroot.resizable(False,False)

    
    ##============================================= Add student Labels ===============================================##

    idlabel = Label(addroot,text='Enter id : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(addroot,text='Enter Name : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                      borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                        borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(addroot,text='Enter Email : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                       borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(addroot,text='Enter Address : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                         borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                        borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(addroot,text='Enter D.O.B. : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                     borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    
    ##==================================== Variables ================================================================##
    
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()


    ##===================================== Add Student Entry ========================================================##

    identry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = ttk.Combobox(addroot, font=("times new roman", 15, "bold"),textvariable=genderval,
                                state='readonly', width=19)
    genderentry['values'] = ("Male", "Female", "Other")
    genderentry.place(x=250,y=310)

    dobentry = Entry(addroot,font=('times new roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    
    ##========================================== Add Button ==========================================================##

    submitbtn = Button(addroot,text='Submit',font=('timesnew roman',15,'bold'),width=20,bd=5,
                       activebackground='white',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=110,y=420)

    addroot.mainloop()


##=============================== Function Used to Search Student ====================================================##

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        date = dateval.get()
        if(id !=''):
            strr = 'select *from studentdata where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(name !=''):
            strr = 'select *from studentdata where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(mobile !=''):
            strr = 'select *from studentdata where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(email !=''):
            strr = 'select *from studentdata where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(address !=''):
            strr = 'select *from studentdata where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(gender !=''):
            strr = 'select *from studentdata where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(dob !=''):
            strr = 'select *from studentdata where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)
        elif(addeddate !=''):
            strr = 'select *from studentdata where date=%s'
            mycursor.execute(strr,(date))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x540+115+125')
    searchroot.title('Student Management System')
    searchroot.config(bg='deep sky blue')
    searchroot.iconbitmap("./res/std_inner.ico")
    searchroot.resizable(False,False)

    
    ##============================================= Search student Labels ============================================##

    idlabel = Label(searchroot,text='Enter id : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(searchroot,text='Enter Name : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                      borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                        borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                       borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(searchroot,text='Enter Address : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                         borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(searchroot,text='Enter Gender : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                        borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(searchroot,text='Enter D.O.B. : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                     borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(searchroot,text='Enter Date : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                      borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)


    ##==================================== Variables ================================================================##

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()


    ##===================================== Search Student Entry =====================================================##

    identry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = ttk.Combobox(searchroot, font=("times new roman", 15, "bold"),textvariable=genderval,
                                state='readonly', width=19)
    genderentry['values'] = ("Male", "Female", "Other")
    genderentry.place(x=250,y=310)

    dobentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(searchroot,font=('times new roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)


    ##========================================== Search Button =======================================================##

    submitbtn = Button(searchroot,text='Submit',font=('timesnew roman',15,'bold'),width=20,bd=5,
                       activebackground='white',activeforeground='white',bg='red',command=search)
    submitbtn.place(x=110,y=480)

    searchroot.mainloop()

    
##================================= Function Used to Delete Student ==================================================##

def deletestudent():
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id{} Deleted Successfully......'.format(pp))
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


##=============================== Function Used to Update Student ====================================================##

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notification','Id{} Modified successfully......'.format(id),parent=updateroot)

        strr = 'select *from studentdata'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=vv)

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x590+115+100')
    updateroot.title('Student Management System')
    updateroot.config(bg='deep sky blue')
    updateroot.iconbitmap("./res/std_inner.ico")
    updateroot.resizable(False,False)

    
    ##============================================= Update student Labels ============================================##
    
    idlabel = Label(updateroot,text='Enter id : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                    borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel = Label(updateroot,text='Enter Name : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                      borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                        borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                       borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel = Label(updateroot,text='Enter Address : ',bg='gold2',font=('times new roman',20,'bold'),
                         relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)

    genderlabel = Label(updateroot,text='Enter Gender : ',bg='gold2',font=('times new roman',20,'bold'),
                        relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)

    doblabel = Label(updateroot,text='Enter D.O.B. : ',bg='gold2',font=('times new roman',20,'bold'),
                     relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel = Label(updateroot,text='Enter Date : ',bg='gold2',font=('times new roman',20,'bold'),
                      relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel = Label(updateroot,text='Enter Time : ',bg='gold2',font=('times new roman',20,'bold'),
                      relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
    

    ##==================================== Variables ================================================================##

    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()
    

    ##===================================== Update Student Entry =====================================================##

    identry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addressentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)

    genderentry = ttk.Combobox(updateroot, font=("times new roman", 15, "bold"),textvariable=genderval,
                                state='readonly', width=19)
    genderentry['values'] = ("Male", "Female", "Other")
    genderentry.place(x=250,y=310)

    dobentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry = Entry(updateroot,font=('times new roman',15,'bold'),bd=5,textvariable=timeval)
    timeentry.place(x=250,y=490)


    ##========================================== Search Button =======================================================##

    submitbtn = Button(updateroot,text='Submit',font=('timesnew roman',15,'bold'),width=20,bd=3,activebackground='white',activeforeground='white',
                      bg='red',command=update)
    submitbtn.place(x=110,y=540)
    cc = studenttable.focus()
    content = studenttable.item(cc)
    pp = content['values']
    if(len(pp) !=0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()


##=============================== Function Used to Show Student Data =================================================##

def showstudent():
    strr = 'select *from studentdata'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=vv)


##=============================== Function Used to Export Student Data ===============================================##

def exportstudent():
    ff = filedialog.asksaveasfilename()
    gg = studenttable.get_children()
    id,name,mobile,email,address,gender,dob,addeddate,addedtime=[],[],[],[],[],[],[],[],[]
    for i in gg:
        content = studenttable.item(i)
        pp = content['values']
        id.append(pp[0]),name.append(pp[1]),mobile.append(pp[2]),email.append(pp[3]),address.append(pp[4]),
        gender.append(pp[5]),dob.append(pp[6]),addeddate.append(pp[7]),addedtime.append(pp[8])
    dd = ['ID','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']
    df = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=dd)
    paths = r'{}.csv'.format(ff)
    df.to_csv(paths.format(ff,),index=False)
    messagebox.showinfo('Notification', 'Student Data Saved{}......'.format(paths))


##=============================== Function Used to Exit ==============================================================##

def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to Exit')
    if(res == True):
        root.destroy()


##=============================== Function Used to Connect Database ==================================================##

def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = usertval.get()
        password = passwordtval.get()

        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('notifications','Data is incorrect Please try Again',parent=dbroot)
            return
        try:
            strr = 'create database studentsystemsystem'
            mycursor.execute(strr)
            strr = 'use studentsystemsystem'
            mycursor.execute(strr)
            strr = 'create table studentdata(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database is Created And Now Your Connected To The Database......', parent=dbroot)

        except:
            strr = 'use studentsystemsystem'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now You Are Connected To The Database......',parent=dbroot)
        dbroot.destroy()


    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+700+230')
    dbroot.iconbitmap("./res/db.ico")
    dbroot.resizable(False,False)
    dbroot.config(bg='deep sky blue')

    
    ##========================================== Connect Table ======================================================##

    hostlabel = Label(dbroot,text="Enter Host : ",bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                      borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel1 = Label(dbroot,text="Enter User : ",bg='gold2',font=('times new roman',20,'bold'),relief=GROOVE,
                       borderwidth=3,width=13,anchor='w')
    userlabel1.place(x=10,y=70)

    passwordlabel1 = Label(dbroot,text="Enter Password : ",bg='gold2',font=('times new roman',20,'bold'),
                           relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel1.place(x=10,y=130)


    ##==================================== Variables ================================================================##

    hostval = StringVar()
    usertval = StringVar()
    passwordtval = StringVar()


    ##========================================== Connect DB Entry ====================================================##

    hostentry = Entry(dbroot,font=('times new roman',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('times new roman', 15, 'bold'), bd=5, textvariable=usertval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('times new roman', 15, 'bold'), bd=5, textvariable=passwordtval)
    passwordentry.place(x=250, y=130)


    ##========================================== Connect Button ======================================================##

    submitButton = Button(dbroot,text='Submit',font=('times new roman',15,'bold'),bg='red',bd=5,width=20,
                          activebackground='blue',activeforeground='white',command=submitdb)
    submitButton.place(x=120,y=190)

    dbroot.mainloop()


##===================================== Function Used to Set Date and Time ===========================================##

def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)


###====================================== INTRO SLIDER ==============================================================###

colors = ['red','green','blue','pink','red2','gold2']

##==================================== Function Used to Select Automatic Color for a Title ===========================##

def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLable.config(fg=fg)
    SliderLable.after(2,IntroLabelColorTick)

##=================================== Function Used To Move Letters of Title to Look like Sliding ====================##

def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text =''
        SliderLable.config(text=text)
    else:
        text = text+ss[count]
        SliderLable.config(text=text)
        count += 1
    SliderLable.after(200,IntroLabelTick)


##========================================= Creation of Windows and Frames ===========================================##
  
# For importing tkinter and pymysql run this following commands in your cmd (command prompt)
# pip install tkinter 
# pip install pymysql
# pip install pandas
# if any importing error occurs then try to run your cmd in adminstrator then run above commands once again 

from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pandas
import pymysql
import time
import random

root = Tk() 
root.title("Created By Onkar J. Gaikwad") # This gives a title of your window
root.config(bg="red1")                  # This set the background color
root.geometry('1205x700+70+0')          # This is a size of your window
root.iconbitmap("./res/kingmaker.ico")  # This set icon to your window but 1st of all
                                        # you need to give correct location of icon where it is present
root.resizable(False,False)             # This will lock your window size


###================================================== Frames ========================================================###

##================================================== Data Entry FRAME ================================================##

DataEntryFrame = Frame(root,bg="yellow",relief=GROOVE,bd=5)
DataEntryFrame.place(x=30,y=80,width=500,height=600)

frontlabel = Label(DataEntryFrame,text='---------------------Welcome---------------------',width=30,
                   font=('times new roman',20,'italic bold'),bg='gold2',fg='red3')
frontlabel.pack(side=TOP,expand=True)

addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('times new roman',20,'bold'),bd=6,
                bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('times new roman',20,'bold'),bd=6,
                   bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

delbtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('times new roman',20,'bold'),bd=6,
                bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=deletestudent)
delbtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('times new roman',20,'bold'),bd=6,
                   bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('times new roman',20,'bold'),bd=6,
                    bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

exportbtn = Button(DataEntryFrame,text='6. Export Data',width=25,font=('times new roman',20,'bold'),bd=6,
                   bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=exportstudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn = Button(DataEntryFrame,text='7. Exit',width=25,font=('times new roman',20,'bold'),bd=6,
                 bg='cadetblue1',activebackground='blue',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


##================================================ Show data frame ==================================================##

ShowDataFrame = Frame(root,bg="gold2",relief=GROOVE,bd=5)
ShowDataFrame.place(x=560,y=80,width=620,height=600)

style = ttk.Style()
style.configure('Treeview.Heading',font=('times new roman',20,'bold'),foreground='black',background='yellow')
style.configure('Treeview',font=('times new roman',15,'bold'),foreground='black',background='gold2')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date',
                                               'Added Time'),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile No',text='Mobile No')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='Added Date')
studenttable.heading('Added Time',text='Added Time')
studenttable['show'] = 'headings'
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile No',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('Added Date',width=150)
studenttable.column('Added Time',width=150)

studenttable.pack(fill=BOTH,expand=1)


##================================================== Slider =====================================================##

ss = 'Welcome To Student Management System'
count =0
text =''

##============================================== Slider Label ===================================================##

SliderLable =Label(root,text=ss,font =('chiller',28,'italic bold'),relief=RIDGE,bd=4,width=34,bg='yellow')
SliderLable.place(x=185,y=0)

IntroLabelTick()
IntroLabelColorTick()

##=============================================== Clock or Timer =================================================##

clock = Label(root,font=('chiller',12,'italic bold'),relief=RIDGE,borderwidth=4,bg='cadetblue1',bd=4,width=15,
              height=3)
clock.place(x=14,y=0)
tick()


##============================================ It Will Connect to Database =======================================##

connectbutton = Button(root,text='Connect to Database', width=17,font=('times new roman',14,'italic bold'),
                       relief=RIDGE,borderwidth=5,bg='cadetblue1',height=2,
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=989,y=0)

root.mainloop()

##=============================================== End of the Project ==================================================##
