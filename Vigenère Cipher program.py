#This app is created by Ritesh Naik.
#Support me on Github and mail me for feedback and queries:- itssafe@pm.me

from tkinter import *
import tkinter.messagebox as MessageBox
import pyperclip

m=s=k=""
tk=tm=0    
temp=0

class Frames(object):
    def __init__(self):
        self.m=StringVar()
        self.k=StringVar()

    def p5(self):                              # How to use
        p5=Toplevel(root)
        p5.geometry("450x250")
        p5.config(bg="orange")
        l1=Label(p5,text="Instructions",font=('Times New Roman',25),background='orange').place(x=130,y=20)
        l1=Label(p5,text="1. Enter text message in the default field.",font=('Times New Roman',14),background='orange').place(x=30,y=80)
        l1=Label(p5,text="2. Do not enter any symbols or punctuation marks.",font=('Times New Roman',14),background='orange').place(x=30,y=120)
        l1=Label(p5,text="3. Space will be automatically eliminated and",font=('Times New Roman',14),background='orange').place(x=30,y=160)
        l1=Label(p5,text=" message will be displayed in BLOCK letters.",font=('Times New Roman',14),background='orange').place(x=45,y=180)
        

    def info(self):                            # Info page
        info=Toplevel(root)
        info.geometry("420x300")
        info.config(bg="orange")
        l1=Label(info, text="Contact Me",font=('Arial',18),bg='orange',fg='black').place(x=150,y=10)
        l1=Label(info, text="Thank you so much for using this program.",font=('Arial',15),bg='orange',fg='black').place(x=30,y=50)
        l1=Label(info, text="Created by - Ritesh Naik",font=('Arial',15),bg='orange',fg='black').place(x=30,y=80)
        l1=Label(info, text="1. Github - github.com/naik-98",font=('Arial',15),bg='orange',fg='black').place(x=30,y=140)
        l1=Label(info, text="2. Email -   itssafe@pm.me",font=('Arial',15),bg='orange',fg='black').place(x=30,y=170)
        b1=Button(info,text="Close",font=('Arial',16),background='RoyalBlue2',foreground='yellow',command=info.destroy).place(x=160,y=220)

    def p4(self):                              #  Result
        p4=Toplevel(root)
        p4.title("Vignere Cipher")
        p4.geometry("400x250")
        p4.config(bg='orange')
        global s,m,k,temp
        text=Label(p4,text="Message has been copied!")

        l1=Label(p4,text="Result",font=('bold',18),bg='orange').place(x=150,y=20)

        if(temp==1):
            l1=Label(p4,text="Your encrypted message is :-",font=('bold',18),bg='orange').place(x=30,y=60)
        else:
            l1=Label(p4,text="Your decrypted message is :-",font=('bold',18),bg='orange').place(x=30,y=60)

        l2=Label(p4,text=s,font=('bold',15),bg='orange').place(x=30,y=100)

        b1=Button(p4,text="Copy",font=('bold',15),background='RoyalBlue2',foreground='yellow',command=lambda:[pyperclip.copy(s),MessageBox.showinfo("","Message Copied!!!\nThank You very much.")]).place(x=90,y=180)
        b1=Button(p4,text="Exit",font=('bold',15),background='RoyalBlue2',foreground='yellow',command=root.destroy).place(x=210,y=180)
        temp=0
        s=m=k=""

    def dcalc(self):                        #  decrypting message
        global m, k, s
                
        m=self.m.get()
        k=self.k.get()
        
        m=m.upper().replace(' ','')
        k=((k.upper().replace(' ',''))*10)[0:len(m)]
        e=[0]*len(m)
        
        for i in range(len(m)):
            tm=ord(m[i])-65
            tk=ord(k[i])-65
            e[i]=(((tm-tk)%26)+65)
            
        for i in range(len(e)):
            s=s+str(chr(e[i]))

        self.p4()

    def calc(self):                          #  Encrypting message
        global m, k, s, temp
        
        m=self.m.get()
        k=self.k.get()
        m=m.upper().replace(' ','')
        k=((k.upper().replace(' ',''))*10)[0:len(m)]
        e=[0]*len(m)
        
        for i in range(len(m)):
            tm=ord(m[i])-65
            tk=ord(k[i])-65
            e[i]=((((tm+tk)%26)+65))
            
        for i in range(len(e)):
            s=s+str(chr(e[i]))

        temp=1
        self.p4()
        
    def p1(self):                             #Encryption Page
        p1=Toplevel(root)
        p1.title("Vignere Cipher")
        p1.geometry("300x350")
        p1.config(bg='orange')
        global temp
        if(temp==1):
            l1=Label(p1,text="Encryption ",font=('bold',18),bg='orange').place(x=80,y=25)
            temp=0
            button1=Button(p1, text="OK",font=('bold',15),width=5,background='RoyalBlue2',foreground='yellow',command=self.calc).place(x=120,y=280)
        else:
            l1=Label(p1,text="Decryption ",font=('bold',18),bg='orange').place(x=80,y=25)
            button1=Button(p1, text="OK",font=('bold',15),background='RoyalBlue2',foreground='yellow',width=5,command=self.dcalc).place(x=120,y=280)

        l1=Label(p1,text="Enter message - ",font=('bold',18),bg='orange').place(x=30,y=80)
        e1=Entry(p1,textvariable=self.m,font=('bold',16)).place(x=30,y=130)
        
        l2=Label(p1,text="Enter key - ",font=('bold',18),bg='orange',).place(x=30,y=180)
        e2=Entry(p1,textvariable=self.k,font=('bold',16)).place(x=30,y=220)
        
    def enc(self):
        global temp
        temp=1
        self.p1()

    def mainframe(self,root):                  # Root
        root.title("Vignere Ciphere")
        root.geometry("400x400")
        root.config(bg='orange')

        label1=Label(root, text="Vigenère Ciphere",font=('bold',25),bg='orange').place(x=80,y=40)
        b1=Button(root, text="How to use →",font=('bold',17),width=15,background='RoyalBlue2',foreground='yellow', command=self.p5).place(x=100,y=130)
        b2=Button(root, text="Encrypt",font=('bold',17),width=8,background='RoyalBlue2',foreground='yellow', command=self.enc).place(x=60,y=220)
        b3=Button(root, text="Decrypt",font=('bold',17),width=8,background='RoyalBlue2',foreground='yellow', command=self.p1).place(x=220,y=220)
        b4=Button(root, text="i",font=('Times New Roman',14,'bold'),width=2,background='cyan2',command=self.info).place(x=360,y=10)
        b6=Button(root, text="Exit",font=('Arial',15,'bold'),width=5,background='brown1',foreground='yellow', command=root.destroy).place(x=160,y=300)
        
root=Tk()
app=Frames()
app.mainframe(root)
root.mainloop()
