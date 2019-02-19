from Tkinter import*
import time;
import sqlite3;
import tkMessageBox
con=sqlite3.Connection("hrdb")
cur=con.cursor()
cur.execute("create table if not exists senderss(sname varchar(20),saddress varchar(20),scontact number,snationality varchar(10),sstate varchar(10))")
cur.execute("create table if not exists recievers(rname varchar(20),raddress varchar(20),rcontact number,rpostal number  ,rstate varchar(20))")
cur.execute("create table if not exists shipments(cshipment varchar(15),coffice varchar(20),cweight varchar(10), crate number,cno number ,caddress varchar(15))")
z=0
main=Tk()
main.geometry("1920x1080+0+0")
ic=PhotoImage(file="bcd3.gif")
labelz=Label(main,image=ic)
labelz.pack()

def mainfun():
    root=Tk()
    root.title("COURIER SERVICE SYSTEM")
    root.geometry("1600x800+0+0")
    localtime=time.asctime(time.localtime(time.time()))
    #====================top============
    Tops=Frame(root,width=1600,height=150,relief=SUNKEN)
    Tops.pack(side=TOP)

    icon=PhotoImage(file="logo3.gif")
    lab1=Label(root,image=icon)
    lab1.pack()

    tlabel=Label(Tops,text="AGARWAL'S COURIER SERVICE SYSTEM",font=('arial',25,'bold'),bd=20,width=70,fg="black",bg="cornflower blue")
    tlabel.grid(row=0,column=0)
    tlabel=Label(Tops,text=localtime,font=('batang',15,'bold'),bd=5,fg="white",justify="right",width=120,bg="cornflower blue")
    tlabel.grid(row=1,column=0)


    label=Label(root,text="ADMINISTRATOR LOGIN",font=('arial',20,'bold'),bd=20,bg="thistle").place(relx=.5, rely=.3,anchor=CENTER)
    #=====================================1st page====================image===============
    def fun():
        root.destroy()
        r1=Tk()
        icon=PhotoImage(file="policey.gif")
        lab1=Label(r1,image=icon)
        lab1.pack()
        def asf():
            r1.destroy()
            mainfun()
        b1=Button(r1,text="MAIN SCREEN",command=asf,font=('arial',16,'bold'),bg="salmon")
        b1.place(relx=.8,rely=.9,anchor=CENTER)
        r1.mainloop()
        

    button1=Button(root,text="COMPANY POLICEY",font=('arial',14,'bold'),bd=10,command=fun,bg="thistle").place(relx=.5,rely=.2,anchor=CENTER)
    #button1.pack()

    #=====================2ND PAGE CODE================================================================================================
    def newfun():
        if(e7.get() == "161B197" and e8.get() == "sarthak"):
            tkMessageBox.showinfo("CONGRATULATION","YOU ARE SUCCESSFULLY LOGGED IN")
            root.destroy()
            r2=Tk()
            import time;
            localtime=time.asctime(time.localtime(time.time()))
            r2.title("new gui")
            r2.geometry("700x500+0+0")
            Tops=Frame(r2,width=700,height=120,bg="coral",relief=SUNKEN)
            Tops.pack(side=TOP)
            Bottoms=Frame(r2,width=700,height=50,bg="navajo white",relief=SUNKEN)
            Bottoms.pack(side=BOTTOM)
            icon=PhotoImage(file="bcd3.gif")
            lab1=Label(r2,image=icon)
            lab1.pack()
            label1=Label(Tops,text="Welcome To Customer Portal",font=('arial narrow',30,'bold'),bd=18,bg="light goldenrod",width=40)
            label1.pack()
            icons=PhotoImage(file="logo6.gif")
            labz=Label(r2,image=icons)
            labz.place(relx=.16,rely=.54,anchor=CENTER)
            label2=Label(Bottoms,text=localtime,font=('arial ',20,'bold'),bd=18,bg="navajo white").place(relx=.7 , rely=.8 ,anchor=CENTER)
            label3=Label(r2,text="Select Your Choice",font=('arial narrow',25,'bold'),bd=18,bg="navajo white",fg="black",width=40)
            label3.pack()
        else:
            tkMessageBox.showerror("INVALID","WRONG USERNAME OR PASSWORD")
            

    #==============3rd page CODE========================================================================================================    
        def funall():
            #r2.destroy()
            roo=Tk()
            roo.title("3rd GUI")
            roo.geometry("1600x800+0+0")
            Tops=Frame(roo,width=1600,height=120,bg="coral",relief=SUNKEN)
            Tops.pack(side=TOP)
            Bottoms=Frame(roo,width=1600,height=80,bg="coral",relief=SUNKEN)
            Bottoms.pack(side=BOTTOM)
            icon=PhotoImage(file="bcd3.gif")
            lab1=Label(roo,image=icon)
            lab1.pack()
            button1=Button(roo,text="BACK",command=roo.destroy,width=15,font=('times',15,'bold'),bg="tomato",bd=10,fg="white").place(relx=.2 ,rely=.8, anchor=CENTER)
    #=======================4TH page fun...==========================================================================================
            
            def fnnn():
                roo.destroy()
                ra=Tk()
                ra.title("3rd GUI")
                ra.geometry("1600x800+0+0")
                Tops=Frame(ra,width=1600,height=120,bg="medium purple",relief=SUNKEN)
                Tops.pack(side=TOP)
                Bottoms=Frame(ra,width=1600,height=80,bg="light pink",relief=SUNKEN)
                Bottoms.pack(side=BOTTOM)
                label1=Label(Tops,text="AGARWAL'S COURIER SERVICE SYSTEM",bg="light pink",bd=10,font=('times',30,'bold'), fg="black" ,width=60)
                label1.pack()
                label2=Label(Tops,text="Reciever's's Information",bg="light pink",bd=10,font=('times',30,'bold'), fg="white" ,width=60)
                label2.pack()
                icon=PhotoImage(file="bcd3.gif")
                labz=Label(ra,image=icon)
                labz.pack()
    #=====================5TH PAGE CODE=================================================================================================            
                def function5():
                    ra.destroy()
                    roots=Tk()
                    imag=PhotoImage(file="bcd3.gif")
                    label=Label(roots,image=imag)
                    label.pack()
                    label2=Label(roots,text="AGARWAL COURIER SERVICE SYSTEM",bd=10,bg="sandy brown",font=('times',24,'bold'),fg="black").place(relx=.24,rely=.06,anchor=CENTER)
                    label3=Label(roots,text="SHIPMENT DETAILS",bd=10,font=('times',32,'bold'),fg="red").place(relx=.75,rely=.08,anchor=CENTER)
                    

    #=====================6TH PAGE CODE==================================================================================================

                    def function6(cnn1):
                        print cnn1
                        tkMessageBox.showinfo("CONGRATULATION","YOUR INVOICE IS CREATED")
                        roots.destroy()
                        final=Tk()
                        icon=PhotoImage(file="bcd3.gif")
                        lab1=Label(final,image=icon)
                        lab1.pack()
                        tlabel=Label(final,text="AGARWAL'S COURIER SERVICE SYSTEM",font=('batang',25,'bold'),bd=10,fg="black",bg="sandy brown").place(relx=.26,rely=.08,anchor=CENTER)
                        label1=Label(final,text="SALE'S INVOICE",font=('batang',35,'bold'),bd=10,fg="RED").place(relx=.75,rely=.08,anchor=CENTER)
                        
                        label2=Label(final,text="RECIEVER NAME",font=('batang',18,'bold'),bd=10,fg="RED",width=20).place(relx=.08,rely=.18,anchor=CENTER)
                        cur.execute("select rname from recievers")
                        con.commit()
                        b=cur.fetchall()
                        l2=len(b)
                        label2a=Label(final,text=b[l2-1],font=('batang',18,'bold'),bd=10,fg="black").place(relx=.32,rely=.18,anchor=CENTER)
                        
                        label3=Label(final,text="SENDER NAME",font=('batang',18,'bold'),bd=10,fg="RED",width=22).place(relx=.07,rely=.28,anchor=CENTER)
                        cur.execute("select sname from senderss")
                        con.commit()
                        c=cur.fetchall()
                        l3=len(c)
                        label3a=Label(final,text=c[l3-1],font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.28,anchor=CENTER)
                        
                        label4=Label(final,text="SENDERS ID",font=('batang',18,'bold'),bd=10,fg="RED",width=25).place(relx=.06,rely=.38,anchor=CENTER)
                        global z
                        z=z+1
                        label4a=Label(final,text="ACS"+str(z)+str(z+1)+"AD1",font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.38,anchor=CENTER)
                        
                        label5=Label(final,text="DESTINATION OFFICE",font=('batang',18,'bold'),bd=10,fg="RED",width=18).place(relx=.1,rely=.48,anchor=CENTER)
                        cur.execute("select coffice from shipments where cno = ?",[cnn1])
                        e=cur.fetchall()
                        l5=len(e)
                        print e
                        label5a=Label(final,text=e[0][0],font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.48,anchor=CENTER)
                        
                        label6=Label(final,text="PARCEL TYPE",font=('batang',18,'bold'),bd=10,fg="RED",width=24).place(relx=.07,rely=.58,anchor=CENTER)
                        cur.execute("select cshipment from shipments where cno = ?",[cnn1])
                        f=cur.fetchall()
                        label6a=Label(final,text=f[0][0],font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.58,anchor=CENTER)
                        
                        label7=Label(final,text="WEIGHT",font=('batang',18,'bold'),bd=10,fg="RED",width=29).place(relx=.04,rely=.68,anchor=CENTER)
                        cur.execute("select cweight from shipments where cno =?",[cnn1])
                        g=cur.fetchall() 
                        label7a=Label(final,text=g[0][0],font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.68,anchor=CENTER)
                        
                        label8=Label(final,text="RATE",font=('batang',18,'bold'),bd=10,fg="RED",width=26).place(relx=.06,rely=.78,anchor=CENTER)
                        cur.execute("select crate from shipments where cno=?",[cnn1])
                        h=cur.fetchall()
                        label8a=Label(final,text=h[0][0],font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.78,anchor=CENTER)
                        
                        label9=Label(final,text="CONSIGNMENT NO",font=('batang',18,'bold'),bd=10,fg="RED",width=20).place(relx=.09,rely=.88,anchor=CENTER)
                        #con.execute("select cno from shipments where cno=?",[cnn1])
                        #i=cur.fetchall()
                        label9a=Label(final,text=161198,font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.32,rely=.88,anchor=CENTER)
                        
                        label10=Label(final,text="THANK YOU FOR MAKING BUSINESS WITH US ",font=('batang',18,'bold'),bd=10,fg="BLACK",bg="sandy brown").place(relx=.79,rely=.88,anchor=CENTER)
                        iconz=PhotoImage(file="sign.gif")
                        lab2=Label(final,image=iconz).place(relx=.78,rely=.68,anchor=CENTER)
                        label11=Label(final,text="M AGARWAL(SALE'S MANAGER) ",font=('batang',18,'bold'),bd=10,fg="BLACK").place(relx=.80,rely=.78,anchor=CENTER)
                        def fdes():
                            final.destroy()
                        button1=Button(final,text="LOGOUT",command=fdes,font=('arial',15,'bold'),bg="tomato",fg="black")
                        button1.place(relx=.94,rely=.08,anchor=CENTER)
                        final.mainloop()

   #=====================6TH PAGE END============================================================================================================
   #=====================5TH PAGE CONTINUE=======================================================================================================
                    def fun6():
                        if v1.get()==1:
                            u='LOCAL'
                            v=str(e1.get())
                            w=str(e2.get())
                            x=str(e3.get())
                            y=str(e4.get())
                            z=str(e5.get())
                            a=[(u,v,w,x,y,z)]
                            cur.executemany("insert into shipments values(?,?,?,?,?,?)",a)
                            con.commit()
                        elif v1.get()==2:
                            u='NATIONAL'
                            v=str(e1.get())
                            w=str(e2.get())
                            x=str(e3.get())
                            y=str(e4.get())
                            z=str(e5.get())
                            a=[(u,v,w,x,y,z)]
                            cur.executemany("insert into shipments values(?,?,?,?,?,?)",a)
                            con.commit()
                        cnn = e4.get()
                        function6(cnn)




                    v1=IntVar()
                    label4=Label(roots,text="Type OF Shipment=",bd=10,bg="salmon",font=('times',20,'bold'),fg="black").place(relx=.14,rely=.25,anchor=CENTER)
                    r1=Radiobutton(roots,text="INDIVIDUAL",variable=v1,value=1,font=('times',18,'bold'),fg="black",bg="salmon",bd=8,width=14).place(relx=.38,rely=.21,anchor=CENTER)
                    r2=Radiobutton(roots,text="COLLECTIVE",variable=v1,value=2,font=('times',18,'bold'),fg="black",bg="salmon",bd=8,width=14).place(relx=.38,rely=.30,anchor=CENTER)
                    label5=Label(roots,text="Destination Office=",bd=10,bg="salmon",font=('times',20,'bold'),fg="black").place(relx=.14,rely=.39,anchor=CENTER)
                    label6=Label(roots,text="Weight=",bd=10,bg="salmon",font=('times',18,'bold'),fg="black",width=16).place(relx=.14,rely=.50,anchor=CENTER)
                    label7=Label(roots,text="Rate=",bd=10,bg="salmon",font=('times',18,'bold'),fg="black",width=16).place(relx=.14,rely=.59,anchor=CENTER)
                    e1=Entry(roots,font=('times',18,'bold'),bg='salmon',bd=10 , justify="right")
                    e1.place(relx=.38, rely=.39,anchor=CENTER)
                    e2=Entry(roots,font=('times',18,'bold'),bg='salmon',bd=10 , justify="right")
                    e2.place(relx=.38, rely=.50,anchor=CENTER)
                    e3=Entry(roots,font=('times',18,'bold'),bg='salmon',bd=10 , justify="right")
                    e3.place(relx=.38, rely=.59,anchor=CENTER)
                    label8=Label(roots,text="Consignment no=",bd=10,bg="salmon",font=('times',18,'bold'),fg="black",width=16).place(relx=.14,rely=.70,anchor=CENTER)
                    e4=Entry(roots,font=('times',18,'bold'),bg='salmon',bd=10 , justify="right")
                    e4.place(relx=.38, rely=.70,anchor=CENTER)
                    imng=PhotoImage(file="logo.gif")
                    labe9=Label(roots,image=imng).place(relx=.76 ,rely=.45,anchor=CENTER)
                    label10=Label(roots,text="Consignee Address=",bd=10,bg="salmon",font=('times',18,'bold'),fg="black",width=16).place(relx=.14,rely=.82,anchor=CENTER)
                    e5=Entry(roots,font=('times',18,'bold'),bg='salmon',bd=10 , justify="right")
                    e5.place(relx=.38, rely=.82,anchor=CENTER)    
                    buttonz=Button(roots,text="Print Sales Invoice",font=('times',24,'bold'),bg="salmon",bd=10,fg="black",command=fun6).place(relx=.75 ,rely=.82, anchor=CENTER)

                    roots.mainloop()

    #====================5TH PAGE END============================================================================================================
    #====================4TH PAGE CONTINUE=====================================================================================================
                def fun5():
                    if v2.get()==1:
                        u=str(e1.get())
                        v=str(e2.get())
                        w=str(e3.get())
                        x=str(e4.get())
                        y='DELHI'
                        b=[(u,v,w,x,y)]
                        cur.executemany("insert into recievers values(?,?,?,?,?)",b)
                        con.commit()
                    elif v2.get()==2:
                        u=str(e1.get())
                        v=str(e2.get())
                        w=str(e3.get())
                        x=str(e4.get())
                        y='UTTAR PRADESH'
                        b=[(u,v,w,x,z)]
                        cur.executemany("insert into recievers values(?,?,?,?,?)",b)
                        con.commit()
                    elif v2.get()==3:
                        u=str(e1.get())
                        v=str(e2.get())
                        w=str(e3.get())
                        x=str(e4.get())
                        y='HARYANA'
                        b=[(u,v,w,x,y)]
                        cur.executemany("insert into recievers values(?,?,?,?,?)",b)
                        con.commit()
                    function5()
                        
                button1=Button(ra,text="BACK",command=ra.destroy,width=15,font=('times',15,'bold'),bg="light pink",bd=10,fg="black").place(relx=.2 ,rely=.8, anchor=CENTER)
                label3=Label(ra,text="NAME =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.3,anchor=CENTER)
                e1=Entry(ra,font=('times',14,'bold'),bg="light pink",bd=10,fg="black",justify="right",width=25)
                e1.place(relx=.3 ,rely=.3,anchor=CENTER)
                label4=Label(ra,text="ADDRESS =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.4,anchor=CENTER)
                e2=Entry(ra,font=('times',14,'bold'),bg="light pink",bd=10,fg="black",justify="right",width=25)
                e2.place(relx=.3 ,rely=.4,anchor=CENTER)
                label5=Label(ra,text="CONTACT NO =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.5,anchor=CENTER)
                e3=Entry(ra,font=('times',14,'bold'),bg="light pink",bd=10,fg="black",justify="right",width=25)
                e3.place(relx=.3 ,rely=.5,anchor=CENTER)
                label6=Label(ra,text="POSTAL CODE =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.6,anchor=CENTER)
                e4=Entry(ra,font=('times',14,'bold'),bg="light pink",bd=10,fg="black",justify="right",width=25)
                e4.place(relx=.3 ,rely=.6,anchor=CENTER)
                label7=Label(ra,text="State =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.6 ,rely=.3,anchor=CENTER)
                v2=IntVar()
                r3=Radiobutton(ra,text="DELHI",variable=v2,value=1,font=('times' , 14,'bold'),bd=8,bg="light pink",fg="black",width=16).place(relx=.8 ,rely=.3,anchor=CENTER)
                r4=Radiobutton(ra,text="UTTAR  PRADESH",variable=v2,value=2,font=('times' , 14,'bold'),bd=8,bg="light pink",fg="black",width=16).place(relx=.8 ,rely=.4,anchor=CENTER)
                r5=Radiobutton(ra,text="HARYANA",variable=v2,value=3,font=('times' , 14,'bold'),bd=8,bg="light pink",fg="black",width=16).place(relx=.8 ,rely=.5,anchor=CENTER)

                label8=Label(ra,text="CITY =",bg="light pink",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.6 ,rely=.6,anchor=CENTER)
                
                button2=Button(ra,text="NEXT",width=20,font=('times',15,'bold'),bg="light pink",bd=10,fg="black",command=fun5).place(relx=.8 ,rely=.8, anchor=CENTER)
                ra.mainloop()
    #====================4TH PAGE END==========================================================================================================
    #====================3RD PAGE CONTINUE====================================================================================================
            def fun4():
                global z
                z=z+1
                u=str(e1.get())
                v=str(e2.get())
                w=str(e3.get())
                                
                if v1.get()==1:
                    if v2.get()==1:
                        u=str(e1.get())
                        v=str(e2.get())
                        w=str(e3.get())
                        x='INDIAN'
                        y='DELHI'
                        a=[(u,v,w,x,y)]
                        cur.executemany("insert into senderss values(?,?,?,?,?)",a)
                        con.commit() 
                    elif v2.get()==2:
                        cur.execute("insert into senderss values(?,?,?,?,?)",(u,v,w,'INDIAN','UTTAR PRADESH'))
                        con.commit() 
                    elif v2.get()==3:
                         cur.execute("insert into senderss values(?,?,?,?,?.?)",(u,v,w,'INDIAN','UTTAR PRADESH'))
                         con.commit() 
                elif():
                    if v2.get()==1:
                        cur.execute("insert into senderss values(?,?,?,?,?)",(u,v,w,'NRI','DELHI'))
                        con.commit()
                    if v2.get()==2:
                        cur.execut("insert into senderss values(?,?,?,?,?)",(u,v,w,'NRI','UTTAR PRADESH'))
                        con.commit() 
                    elif v2.get()==3:
                        cur.execute("insert into senderss values(?,?,?,?,?)",(u,v,w,'NRI','HARYANA'))
                        con.commit()
                #cur.commit()
                fnnn()
            
            label1=Label(Tops,text="AGARWAL'S COURIER SERVICE SYSTEM",bg="light salmon",bd=10,font=('times',30,'bold'), fg="black" ,width=60)
            label1.pack()
            label2=Label(Tops,text="Sender's Information",bg="light salmon",bd=10,font=('times',30,'bold'), fg="white" ,width=60)
            label2.pack()
            label3=Label(roo,text="NAME =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.3,anchor=CENTER)
            e1=Entry(roo,font=('times',14,'bold'),bg="light salmon",bd=10,fg="black",justify="right",width=25)
            e1.place(relx=.3 ,rely=.3,anchor=CENTER)
            label4=Label(roo,text="ADDRESS =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.4,anchor=CENTER)
            e2=Entry(roo,font=('times',14,'bold'),bg="light salmon",bd=10,fg="black",justify="right",width=25)
            e2.place(relx=.3 ,rely=.4,anchor=CENTER)
            label5=Label(roo,text="CONTACT NO =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.5,anchor=CENTER)
            e3=Entry(roo,font=('times',14,'bold'),bg="light salmon",bd=10,fg="black",justify="right",width=25)
            e3.place(relx=.3 ,rely=.5,anchor=CENTER)
            label6=Label(roo,text="Nationality =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.1 ,rely=.6,anchor=CENTER)

            v1=IntVar()
            r1=Radiobutton(roo,text="INDIAN",variable=v1,value=1,font=('times' , 14,'bold'),bd=8,bg="light salmon",fg="black",width=16).place(relx=.3 ,rely=.6,anchor=CENTER)
            rz=Radiobutton(roo,text="NRI",variable=v1,value=2,font=('times' , 14,'bold'),bd=8,bg="light salmon",fg="black",width=16).place(relx=.3 ,rely=.7,anchor=CENTER)

            label7=Label(roo,text="State =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.6 ,rely=.3,anchor=CENTER)
            v2=IntVar()
            r3=Radiobutton(roo,text="DELHI",variable=v2,value=1,font=('times' , 14,'bold'),bd=8,bg="light salmon",fg="black",width=16).place(relx=.8 ,rely=.3,anchor=CENTER)
            r4=Radiobutton(roo,text="UTTAR  PRADESH",variable=v2,value=2,font=('times' , 14,'bold'),bd=8,bg="light salmon",fg="black",width=16).place(relx=.8 ,rely=.4,anchor=CENTER)
            r5=Radiobutton(roo,text="HARYANA",variable=v2,value=3,font=('times' , 14,'bold'),bd=8,bg="light salmon",fg="black",width=16).place(relx=.8 ,rely=.5,anchor=CENTER)
            #label8=Label(roo,text="SENDERS ID =",bg="light salmon",bd=10,font=('times',16,'bold'), fg="black",width=15).place(relx=.6 ,rely=.6,anchor=CENTER)
            #e4=Entry(roo,font=('times',14,'bold'),bg="light salmon",bd=10,fg="black",justify="right",width=25)
            #e4.place(relx=.8 ,rely=.6,anchor=CENTER)
            
            button2=Button(roo,text="NEXT",width=20,font=('times',15,'bold'),bg="tomato",bd=10,fg="white",command=fun4).place(relx=.8 ,rely=.8, anchor=CENTER)
            
            roo.mainloop()
    #=====================3RD PAGE END===========================================================================================================
    #=====================2ND PAGE CONTINUE======================================================================================================

        def des3():
            r2.destroy()
            funall()
        button1=Button(r2,text="Place  Order",font=('arial narrow',18,'bold'),bd=10,bg="misty rose",fg="black",command=des3).place(relx=.8 , rely=.4 ,anchor=CENTER)
        button2=Button(r2,text="Track  Order",font=('arial narrow',18,'bold'),bd=10,bg="misty rose",fg="black").place(relx=.8 , rely=.6 ,anchor=CENTER)
        r2.mainloop()

    #===================2ND PAGE END=============================================================================================================
    #====================1st page CONTINUE================================================================================================================
    l2=Label(root,text="User Name = ",font=('times',20,'bold'),bd=5,bg="thistle").place(relx=.4, rely=.4,anchor=CENTER)
    l3=Label(root,text="Password = ",font=('times',20,'bold'),bd=5,bg="thistle").place(relx=.4,rely=.5,anchor=CENTER)
    def clear():
        e7.delete(0,END)
        e8.delete(0,END)
    b5=Button(root,text="RESET",width=14,font=('times',20,'bold'),bd=5,bg="thistle",command=clear).place(relx=.5,rely=.7,anchor=CENTER)
    e7=Entry(root,font=('times',15,'bold'),bg='thistle',bd=10 , justify="right")
    e7.place(relx=.6, rely=.4,anchor=CENTER)
    e8=Entry(root,show='*',font=('times',15,'bold'),bg='thistle',bd=10 , justify="right")
    e8.place(relx=.6, rely=.5,anchor=CENTER)
    b4=Button(root,text="OK",width=14,font=('times',20,'bold'),bd=5,bg="thistle",command=newfun).place(relx=.5,rely=.6,anchor=CENTER)
        
    
    

    root.mainloop()


icon=PhotoImage(file="bcd3.gif")
label1=Label(main,image=icon)
def tyu():
    main.destroy()
    mainfun()
label1.after(3000,tyu)
icons=PhotoImage(file="fff.gif")
label9=Label(main,image=icons).place(relx=.75,rely=.55,anchor=CENTER)
label2=Label(main,text=" COURIER MANAGEMENT SYSTEM ",font=('times',27,'bold'),bg="sandy brown",fg="black",bd=10).place(relx=.25,rely=.08 ,anchor=CENTER)
label3=Label(main,text="BY-",font=('arial',18,'bold'),fg="red",bd=10).place(relx=.07,rely=.2 ,anchor=CENTER)
label4=Label(main,text="Sarthak Agarwal",font=('arial',22,'bold'),fg="red").place(relx=.15,rely=.3 ,anchor=CENTER)
label5=Label(main,text="161B197",font=('arial',22,'bold'),fg="red").place(relx=.15,rely=.38 ,anchor=CENTER)
label6=Label(main,text="sarthak.agarwal97@gmail.com",font=('arial',20,'bold'),fg="red").place(relx=.15,rely=.46 ,anchor=CENTER)
label7=Label(main,text="09452307142",font=('arial',22,'bold'),fg="red").place(relx=.15,rely=.54 ,anchor=CENTER)
label8=Label(main,text="B7(BZ) BATCH",font=('arial',22,'bold'),fg="red").place(relx=.15,rely=.62 ,anchor=CENTER)
main.mainloop()
