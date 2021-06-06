from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
def nextPage():
    import login

class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")

    

        self.bg=ImageTk.PhotoImage(file="C:/Users/ASUS/Documents/files/gitpython/db.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        self.left=ImageTk.PhotoImage(file="C:/Users/ASUS/Documents/files/gitpython/ve.png")
        left=Label(self.root,image=self.left,bg="midnight blue").place(x=80,y=100,width=440,height=480)

        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=480)

        titl=Label(self.root,text="Welcome!!",font=("times new roman",24,"bold"),fg="black").place(x=80,y=10)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",18,"bold"),bg="white",fg="green").place(x=50,y=27)

        f_name=Label(frame1,text="First Name",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=50,y=90)
        txt_fname=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=50,y=125,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=370,y=90)
        txt_lname=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=370,y=125,width=250)

        contact=Label(frame1,text="Contact No",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=50,y=170)
        txt_contact=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=370,y=170)
        txt_email=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=370,y=200,width=250)

        ques=Label(frame1,text="Security Question",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=50,y=240)
        cmb_ques=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        cmb_ques['value']=("Select","Your first pet name","Your first gf names","Your primary school name","Your DOB")
        cmb_ques.place(x=50,y=270,width=250)
        cmb_ques.current(0)

        ans=Label(frame1,text="Answer",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=370,y=240)
        txt_ans=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=370,y=270,width=250)

        pasw=Label(frame1,text="Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=50,y=310)
        txt_pasw=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=50,y=340,width=250)

        cpasw=Label(frame1,text="Confirm Password",font=("times new roman",13,"bold"),bg="white",fg="gray").place(x=370,y=310)
        txt_email=Entry(frame1,font=("times new roman",14),bg="lightgray").place(x=370,y=340,width=250)



        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",onvalue=1,offvalue=0).place(x=50,y=380)



        self.btn_img=ImageTk.PhotoImage(file="C:/Users/ASUS/Documents/files/gitpython/op.jpeg")
        btn=Button(frame1,image=self.btn_img,bd=0,cursor="hand2").place(x=180,y=420,width="270",height="36")

        self.icn=ImageTk.PhotoImage(file="C:/Users/ASUS/Documents/files/gitpython/home.png")
        icn=Label(frame1,image=self.icn,bd=0).place(x=590,y=26,width="70",height="36")
        
        title_r=Label(self.root,text="Already Registered??",font=("times new roman",14),bg="black",fg="lightgray").place(x=200,y=440)
        btn_login=Button(self.root,text="Sign In",font=("times new roman",16),bd=0,cursor="hand2",command=nextPage).place(x=220,y=490,width="130",height="33")

 


root=Tk()
obj=register(root)
root.mainloop()    
