from tkinter import*
from tkinter import ttk
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime




class LibraryManagementSystem:
    
    def __init__(self,root):
        self.root=root
        self.root.title("Library Mangement System")
        self.root.geometry("1560x800+0+0")


        #variable=================================variable===================================================================

        self.member_var=StringVar()
        self.prn_var =StringVar()
        self.id_var =StringVar()
        self.firstname_var =StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,width=1350,padx=20,bd=15,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,width=44,font=('arial',40,'bold'),text="\tLibrary Management System\t",padx=12,bg="red",fg="green", bd=15)
        self.lblTitle.grid()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        
        DataFrameLEFT =LabelFrame(frame,text="Library Membership Information" , bg="powder blue", fg="green", bd=20,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameLEFT.place(x=0,y=5,width=860,height=365)
        
       #======================LABELS========================
        
        lblMember=Label(DataFrameLEFT,text="Member Type",font=("arial",15,"bold"),padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)


        comMember = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'),textvariable=self.member_var, state='readonly',  width =25)
        comMember['value']=('','Student','Lecturer','Admin staff')
        comMember .grid(row=0, column=1)

        lblref=Label(DataFrameLEFT,text="PRN NO:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.prn_var,width=23)
        txtref.grid(row=1, column=1)

        


        lblTitle=Label(DataFrameLEFT,text="ID NO:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.id_var,width=23)
        txtTitle.grid(row=2, column=1)

        lblFirstname=Label(DataFrameLEFT,text="Firstname:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstname=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.firstname_var,width=23)
        txtFirstname.grid(row=3, column=1)

        lblLastname=Label(DataFrameLEFT,text="Lastname:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.lastname_var,width=23)
        txtLastname.grid(row=4, column=1)

        lblAddress1=Label(DataFrameLEFT,text="Address1:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.address1_var,width=23)
        txtAddress1.grid(row=5, column=1)

        lblAddress2=Label(DataFrameLEFT,text="Address2:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.address2_var,width=23)
        txtAddress2.grid(row=6, column=1)


        lblPostCode=Label(DataFrameLEFT,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.postcode_var,width=23)
        txtPostCode.grid(row=7, column=1)


        lblMobile=Label(DataFrameLEFT,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.mobile_var,width=23)
        txtMobile.grid(row=8, column=1)


        lblBookId=Label(DataFrameLEFT,text="Book Id:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.bookid_var,width=23)
        txtBookId.grid(row=0, column=3)


        lblBookTitle=Label(DataFrameLEFT,text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.booktitle_var,width=23)
        txtBookTitle.grid(row=1, column=3)

        lblAuther=Label(DataFrameLEFT,text="Auther:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.auther_var,width=23)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed=Label(DataFrameLEFT,text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.dateborrowed_var,width=23)
        txtDateBorrowed.grid(row=3, column=3)


        lblDateDue=Label(DataFrameLEFT,text="Date Due:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.datedue_var,width=23)
        txtDateDue.grid(row=4, column=3)



        lblDaysOnBook=Label(DataFrameLEFT,text="DaysOnBook:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.daysonbook_var,width=23)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine=Label(DataFrameLEFT,text="Last Return Fine:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.latereturnfine_var,width=23)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate=Label(DataFrameLEFT,text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.dateoverdue_var,width=23)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice=Label(DataFrameLEFT,text="Actal Price:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.finalprice_var,width=23)
        txtActualPrice.grid(row=8, column=3)

        
       
        #variable=================================variable===================================================================

        self.member_var=StringVar()
        self.prn_var =StringVar()
        self.id_var =StringVar()
        self.firstname_var =StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.latereturnfine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


        MainFrame = Frame(self.root)
        MainFrame.grid()

        TitleFrame = Frame(MainFrame,width=1350,padx=20,bd=15,relief=RIDGE)
        TitleFrame.pack(side=TOP)

        self.lblTitle =Label(TitleFrame,width=44,font=('arial',40,'bold'),text="\tLibrary Management System\t",padx=12,bg="red",fg="green", bd=15)
        self.lblTitle.grid()


        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        frame.place(x=0,y=130,width=1530,height=400)


        
        DataFrameLEFT =LabelFrame(frame,text="Library Membership Information" , bg="powder blue", fg="green", bd=20,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameLEFT.place(x=0,y=5,width=860,height=365)
        
       #======================LABELS========================
        
        lblMember=Label(DataFrameLEFT,text="Member Type",font=("arial",15,"bold"),padx=2,pady=6,bg="powder blue")
        lblMember.grid(row=0,column=0,sticky=W)


        comMember = ttk.Combobox(DataFrameLEFT, font=('arial',12,'bold'),textvariable=self.member_var, state='readonly',  width =25)
        comMember['value']=('','Student','Lecturer','Admin staff')
        comMember .grid(row=0, column=1)

        lblref=Label(DataFrameLEFT,text="PRN NO:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.prn_var,width=23)
        txtref.grid(row=1, column=1)

        


        lblTitle=Label(DataFrameLEFT,text="ID NO:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblTitle.grid(row=2,column=0,sticky=W)
        txtTitle=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.id_var,width=23)
        txtTitle.grid(row=2, column=1)

        lblFirstname=Label(DataFrameLEFT,text="Firstname:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblFirstname.grid(row=3,column=0,sticky=W)
        txtFirstname=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.firstname_var,width=23)
        txtFirstname.grid(row=3, column=1)

        lblLastname=Label(DataFrameLEFT,text="Lastname:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLastname.grid(row=4,column=0,sticky=W)
        txtLastname=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.lastname_var,width=23)
        txtLastname.grid(row=4, column=1)

        lblAddress1=Label(DataFrameLEFT,text="Address1:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress1.grid(row=5,column=0,sticky=W)
        txtAddress1=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.address1_var,width=23)
        txtAddress1.grid(row=5, column=1)

        lblAddress2=Label(DataFrameLEFT,text="Address2:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAddress2.grid(row=6,column=0,sticky=W)
        txtAddress2=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.address2_var,width=23)
        txtAddress2.grid(row=6, column=1)


        lblPostCode=Label(DataFrameLEFT,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblPostCode.grid(row=7,column=0,sticky=W)
        txtPostCode=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.postcode_var,width=23)
        txtPostCode.grid(row=7, column=1)


        lblMobile=Label(DataFrameLEFT,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblMobile.grid(row=8,column=0,sticky=W)
        txtMobile=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.mobile_var,width=23)
        txtMobile.grid(row=8, column=1)


        lblBookId=Label(DataFrameLEFT,text="Book Id:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblBookId.grid(row=0,column=2,sticky=W)
        txtBookId=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.bookid_var,width=23)
        txtBookId.grid(row=0, column=3)


        lblBookTitle=Label(DataFrameLEFT,text="Book Title:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblBookTitle.grid(row=1,column=2,sticky=W)
        txtBookTitle=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.booktitle_var,width=23)
        txtBookTitle.grid(row=1, column=3)

        lblAuther=Label(DataFrameLEFT,text="Auther:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblAuther.grid(row=2,column=2,sticky=W)
        txtAuther=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.auther_var,width=23)
        txtAuther.grid(row=2, column=3)

        lblDateBorrowed=Label(DataFrameLEFT,text="Date Borrowed:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateBorrowed.grid(row=3,column=2,sticky=W)
        txtDateBorrowed=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.dateborrowed_var,width=23)
        txtDateBorrowed.grid(row=3, column=3)


        lblDateDue=Label(DataFrameLEFT,text="Date Due:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateDue.grid(row=4,column=2,sticky=W)
        txtDateDue=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.datedue_var,width=23)
        txtDateDue.grid(row=4, column=3)



        lblDaysOnBook=Label(DataFrameLEFT,text="DaysOnBook:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDaysOnBook.grid(row=5,column=2,sticky=W)
        txtDaysOnBook=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.daysonbook_var,width=23)
        txtDaysOnBook.grid(row=5, column=3)

        lblLateReturnFine=Label(DataFrameLEFT,text="Last Return Fine:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblLateReturnFine.grid(row=6,column=2,sticky=W)
        txtLateReturnFine=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.latereturnfine_var,width=23)
        txtLateReturnFine.grid(row=6, column=3)

        lblDateOverDate=Label(DataFrameLEFT,text="Date Over Due:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblDateOverDate.grid(row=7,column=2,sticky=W)
        txtDateOverDate=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.dateoverdue_var,width=23)
        txtDateOverDate.grid(row=7, column=3)

        lblActualPrice=Label(DataFrameLEFT,text="Actal Price:",font=("arial",12,"bold"),padx=2,pady=6,bg="powder blue")
        lblActualPrice.grid(row=8,column=2,sticky=W)
        txtActualPrice=Entry(DataFrameLEFT,font=("arial",15,"bold"),textvariable=self.finalprice_var,width=23)
        txtActualPrice.grid(row=8, column=3)

        
        #===========DATAFRAME RIGHT==============

        DataFrameRight =LabelFrame(frame,text="Book Details" , bg="powder blue", fg="green", bd=20,relief=RIDGE,font=("arial",15,"bold"))
        DataFrameRight.place(x=910,y=5,width=550,height=370)

        self.txtBox=Text(DataFrameRight,font=("arial",12,"bold"),width=32,height=16,padx=2,pady=6)
        self.txtBox.grid(row=0,column=2)

        listscrollbar = Scrollbar(DataFrameRight)
        listscrollbar.grid(row=0, column=1, sticky='ns')
                                    

        listBooks=['python','Hello India','aptittude Reasoning','MPSC','UPSC','Game Design','London','speech story','english','asp.net','RDBMS','CLOUD COMPUTING','CPP','C LANGUA']

        def SelectBook(event=""):
             value=str(listBox.get(listBox.curselection()))
             x=value
             if (x=="python"):
                 self.bookid_var.set("BkID12345")
                 self.booktitle_var.set("python manual")
                 self.auther_var.set("paul berry")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=15)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(15)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.788")

             elif  (x=="Hello India"):
                 self.bookid_var.set("BkID5565")
                 self.booktitle_var.set("indian")
                 self.auther_var.set("allindians")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=13)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(13)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.100")


             elif  (x=="aptittude Reasoning"):
                 self.bookid_var.set("BkID123")
                 self.booktitle_var.set("math")
                 self.auther_var.set("reasoning")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=14)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(13)
                 self.latereturnfine_var.set("Rs.50")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.500")
            
             elif  (x=="MPSC Design"):
                 self.bookid_var.set("BkID126")
                 self.booktitle_var.set("Gaming")
                 self.auther_var.set("develope")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(13)
                 self.latereturnfine_var.set("Rs.1000")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.800")

             elif  (x=="London"):
                 self.bookid_var.set("BkID127")
                 self.booktitle_var.set("LONDON ")
                 self.auther_var.set("Rk hist")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(13)
                 self.latereturnfine_var.set("Rs.200")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.150")
                 
             elif  (x=="speech story"):
                 self.bookid_var.set("BkID128")
                 self.booktitle_var.set("story")
                 self.auther_var.set("AB story")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(13)
                 self.latereturnfine_var.set("Rs.100")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.100")

             elif  (x=="english"):
                 self.bookid_var.set("BkID129")
                 self.booktitle_var.set("english")
                 self.auther_var.set("pn eng")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(10)
                 self.latereturnfine_var.set("Rs.500")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.450")

             elif  (x=="asp.net"):
                 self.bookid_var.set("BkID129")
                 self.booktitle_var.set("program")
                 self.auther_var.set("rd")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(10)
                 self.latereturnfine_var.set("Rs.500")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.450")

             elif  (x=="RDBMS"):
                 self.bookid_var.set("BkID130")
                 self.booktitle_var.set("COMMAND")
                 self.auther_var.set("AB ")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(10)
                 self.latereturnfine_var.set("Rs.600")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.450")

             elif  (x=="CLOUD COMPUTING"):
                 self.bookid_var.set("BkID131")
                 self.booktitle_var.set("CLOUD")
                 self.auther_var.set("GB ")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(10)
                 self.latereturnfine_var.set("Rs.670")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.700")

             elif  (x=="CPP"):
                 self.bookid_var.set("BkID132")
                 self.booktitle_var.set("PROGRAM")
                 self.auther_var.set("ST ")

                 d1=datetime.datetime.today()
                 d2=datetime.timedelta(days=10)
                 d3=d1+d2
                 self.dateborrowed_var.set(d1)
                 self.datedue_var.set(d3)
                 self.daysonbook_var.set(10)
                 self.latereturnfine_var.set("Rs.900")
                 self.dateoverdue_var.set("NO")
                 self.finalprice_var.set("Rs.1000")


                 

                 
                 
 
        listBox=Listbox(DataFrameRight,font=("arial",12,"bold"),width=20,height=16)
        listBox.bind("<<ListboxSelect>>",SelectBook)         
        listBox.grid(row=0,column=0,padx=4)
        listscrollbar.config(command=listBox.yview)


        for item in listBooks:
            listBox.insert(END,item)

   # ==========BUTTON FRAME==========

        Framebutton=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        Framebutton.place(x=0,y=530,width=1530,height=70)
         
        btnAddData=Button(Framebutton,command=self.adda_data,text="Add Data" ,font=("arial",14,"bold"),width=20,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=0)

        btnAddData=Button(Framebutton,command=self.showData,text="Display Data" ,font=("arial",14,"bold"),width=20,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=1)

        btnAddData=Button(Framebutton,command=self.update,text="Update" ,font=("arial",14,"bold"),width=20,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=2)

        btnAddData=Button(Framebutton,command=self.iexit,text="Exit" ,font=("arial",14,"bold"),width=20,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=3)

        btnAddData=Button(Framebutton,command=self.reset,text="Reset" ,font=("arial",14,"bold"),width=20,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=4)
    
        btnAddData=Button(Framebutton,command=self.delete,text="Delete" ,font=("arial",14,"bold"),width=15,bg="yellow",fg="red")
        btnAddData.grid(row=0,column=5)
    

        


        


      
        #========================INFORMATION FRAME================
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=20,bg="powder blue")
        FrameDetails.place(x=0,y=600,width=1530,height=210)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="powder blue")
        Table_frame.place(x=0,y=2,width=1460,height=190)

        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)
        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","address1","address2","postid","mobile","bookid","booktitle","auther","dateborrowed",
                                                            "datedue","days","latereturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)

        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        
        
        
        

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO.")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last name")
        self.library_table.heading("address1",text="Address1")
        self.library_table.heading("address2",text="Address2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile Number")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther")
        self.library_table.heading("dateborrowed",text="Date Of Borrowed")
        self.library_table.heading("datedue",text="Date Due") 
        self.library_table.heading("days",text="DaysOnBook")
        self.library_table.heading("latereturnfine",text="Late Return Fine")
        self.library_table.heading("dateoverdue",text="Date Over Date")
        self.library_table.heading("finalprice",text="Final Price")

        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype" ,width=100)
        self.library_table.column("prnno" ,width=100)
        self.library_table.column("title" ,width=100)
        self.library_table.column("firstname" ,width=100)
        self.library_table.column("lastname" ,width=100)
        self.library_table.column("address1" ,width=100)
        self.library_table.column("address2" ,width=100)
        self.library_table.column("postid" ,width=100)
        self.library_table.column("mobile" ,width=100)
        self.library_table.column("bookid" ,width=100)
        self.library_table.column("booktitle" ,width=100)
        self.library_table.column("auther" ,width=100)
        self.library_table.column("dateborrowed" ,width=100)
        self.library_table.column("datedue" ,width=100)
        self.library_table.column("days" ,width=100)
        self.library_table.column("latereturnfine" ,width=100)
        self.library_table.column("dateoverdue" ,width=100)
        self.library_table.column("finalprice" ,width=100)

        self.fetch_data()

        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)



    def adda_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ajay@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("insert into library values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                                                                                     self.member_var.get(),
                                                                                                                                                                                     self.prn_var.get(),
                                                                                                                                                                                     self.id_var.get(),
                                                                                                                                                                                     self.firstname_var.get(),
                                                                                                                                                                                     self.lastname_var.get(),
                                                                                                                                                                                     self.address1_var.get(),
                                                                                                                                                                                     self.address2_var.get(),
                                                                                                                                                                                     self.postcode_var.get(),
                                                                                                                                                                                     self.mobile_var.get(),
                                                                                                                                                                                     self.bookid_var.get(),
                                                                                                                                                                                     self.booktitle_var.get(),
                                                                                                                                                                                     self.auther_var.get(),
                                                                                                                                                                                     self.dateborrowed_var.get(),
                                                                                                                                                                                     self.datedue_var.get(),
                                                                                                                                                                                     self.daysonbook_var.get(),
                                                                                                                                                                                     self.latereturnfine_var.get(),
                                                                                                                                                                                     self.dateoverdue_var.get(),
                                                                                                                                                                                     self.finalprice_var.get()
                                                                                                                                                                                    ))

            
                                                                                        
        
        
        
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success","Member has been inserted successfully")
        
    def update(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ajay@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("update library set member=%s,id=%s,firstname=%s,lastname=%s,address1=%s,address2=%s,postcode=%s,mobile=%s,bookid=%s,booktitle=%s,auther=%s,dateborrowed=%s,datedue=%s,daysonbook=%s,latereturnfine=%s,dateoverdue=%s,finalprice=%s where prn=%s",(
                                                                                                                                                                                     self.member_var.get(),
                                                                                                                                                                                     self.id_var.get(),
                                                                                                                                                                                     self.firstname_var.get(),
                                                                                                                                                                                     self.lastname_var.get(),
                                                                                                                                                                                     self.address1_var.get(),
                                                                                                                                                                                     self.address2_var.get(),
                                                                                                                                                                                     self.postcode_var.get(),
                                                                                                                                                                                     self.mobile_var.get(),
                                                                                                                                                                                     self.bookid_var.get(),
                                                                                                                                                                                     self.booktitle_var.get(),
                                                                                                                                                                                     self.auther_var.get(),
                                                                                                                                                                                     self.dateborrowed_var.get(),
                                                                                                                                                                                     self.datedue_var.get(),
                                                                                                                                                                                     self.daysonbook_var.get(),
                                                                                                                                                                                     self.latereturnfine_var.get(),
                                                                                                                                                                                     self.dateoverdue_var.get(),
                                                                                                                                                                                     self.finalprice_var.get(),
                                                                                                                                                                                     self.prn_var.get()
                                                                                                                                                                                     ))
        conn.commit()
        self.fetch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("success","member has been updated")

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Ajay@123",database="mydata")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.latereturnfine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])


    def showData(self):
        self.txtBox.insert(END,"member Type\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN No\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID No\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"FirstName\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"LastName\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Auther\t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateReturnfine\t\t"+self.latereturnfine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice\t\t"+self.finalprice_var.get()+"\n")
                
            
    def reset(self):
        self.member_var.set(""),
        self.prn_var.set(""),
        self.id_var.set(""),
        self.firstname_var.set(""),
        self.lastname_var.set(""),
        self.address1_var.set(""),
        self.address2_var.set(""),
        self.postcode_var.set(""),
        self.mobile_var.set(""),
        self.bookid_var.set(""),
        self.booktitle_var.set(""),
        self.auther_var.set(""),
        self.dateborrowed_var.set(""),
        self.datedue_var.set(""),
        self.daysonbook_var.set(""),
        self.latereturnfine_var.set(""),
        self.dateoverdue_var.set(""),
        self.finalprice_var.set(""),
        self.txtBox.delete("1.0",END)



    def iexit(self):
         iexit=tkinter.messagebox.askyesno("Library management System","Do you want to exit")
         if iexit>0:
             self.root.destroy()
             return
         
            
            
            
            
    def delete(self):
         if self.prn_var.get()=="" or self.id_var.get()=="":
             messagebox.showerror("Error","first select the member")
         else :
             conn=mysql.connector.connect(host="localhost",username="root",password="Ajay@123",database="mydata")
             my_cursor=conn.cursor()
             query= "delete from library where prn=%s"
             value=(self.prn_var.get(),)
             my_cursor.execute(query,value)

             conn.commit()
             self.fetch_data()
             self.reset()
             conn.close()

             messagebox.showinfo("success","member has been deleted")
             
         
        
        

        
        
        
        
                                  
                            
        


        
        
      



        #lbltitle=Label(self.root,text="Library Management System", bg="powder blue", fg="green" ,bd=20,relief=RIDGE,font=("arial",50,"bold"),padx=2,pady=6)
        #lbltitle.pack(side=Top,fill=x)

       







if  __name__  ==  "__main__":
       root=Tk()
       obj=LibraryManagementSystem(root)
       root.mainloop()

    
