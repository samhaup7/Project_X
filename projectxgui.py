
# coding: utf-8



import tkinter as tk
from tkinter import ttk
import PIL.Image, PIL.ImageTk
import pandas as pd
import os.path
from csv import reader
import cv2
import sys
import csv



LARGE_FONT=("Calibri",18)
SMALL_FONT=("Calibri",14)
SMALLER_FONT=("Calibri",10)







def insert(UsernameR,PasswordR,PhoneR,choice):
    #print("Insert Works")
    if(len(UsernameR.get())==0 or len(PasswordR.get())==0 or len(PhoneR.get())==0):
        popupmsg("Fields cannot be Empty","Fill All Fields","OK")
        sys.exit(1)
    else:
        print(choice.get())
        
        fields=[UsernameR.get(), PasswordR.get(), PhoneR.get()]
        if (choice.get() == "Advertiser"):
            if not os.path.exists(r'..\data\advertisers.csv'):
                with open(r'..\data\advertisers.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            else:
                with open(r'..\data\advertisers.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            
        elif (choice.get() == "Operator"):
            if not os.path.exists(r'..\data\operators.csv'):
                with open(r'..\data\operators.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            else:
                with open(r'..\data\operators.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        elif (choice.get() == "Player"):
            if not os.path.exists(r'..\data\players.csv'):
                with open(r'..\data\players.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            else:
                with open(r'..\data\players.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
        else: 
            if not os.path.exists(r'..\data\developers.csv'):
                with open(r'..\data\developers.csv', 'w', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
            else:
                with open(r'..\data\developers.csv', 'a', newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(fields)
               
        #ResetReg(UsernameR.get(),PhoneR.get(),PasswordR.get()) #Clearing Out Fields




def CheckCred(Username,Password, choice):
    #print("CheckCred Works")
    user = Username.get()
    password = Password.get()
    choice = choice.get()
    if(len(Username.get())==0 or len(Password.get())==0):
        popupmsg("Invalid Credentials","Invalid Login","Try Again")
    
    else:
        if (choice == "Advertiser"):
            # open file in read mode
            with open(r'..\data\advertisers.csv', 'r') as read_obj:
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    if row[0] == user:
                        if row[1] == password:
                            r=tk.Tk()
                            r.geometry('300x300')
                            r.wm_title("Successfully Logged In")
                            rlbl=tk.Label(r,text="Welcome to Project X",font=LARGE_FONT)
                            rlbl.pack(pady=20,padx=20)
                            r.mainloop()
                            read_obj.close()
                        else:
                            popupmsg("Invalid Credentials","Invalid Login","Try Again")
                            read_obj.close()
                popupmsg("User does not exist", "Invalid Login", "Try Again")
                       
        elif (choice == "Operator"):
            # open file in read mode
            with open(r'..\data\operators.csv', 'r') as read_obj:
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    if row[0] == user:
                        if row[1] == password:
                            r=tk.Tk()
                            r.geometry('300x300')
                            r.wm_title("Successfully Logged In")
                            rlbl=tk.Label(r,text="Welcome to Project X",font=LARGE_FONT)
                            rlbl.pack(pady=20,padx=20)
                            r.mainloop()
                            read_obj.close()
                        else:
                            popupmsg("Invalid Credentials","Invalid Login","Try Again")
                            read_obj.close()
                popupmsg("User does not exist", "Invalid Login", "Try Again")
        elif (choice == "Player"):
            # open file in read mode
            with open(r'..\data\players.csv', 'r') as read_obj:
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    if row[0] == user:
                        if row[1] == password:
                            r=tk.Tk()
                            r.geometry('300x300')
                            r.wm_title("Successfully Logged In")
                            rlbl=tk.Label(r,text="Welcome to Project X",font=LARGE_FONT)
                            rlbl.pack(pady=20,padx=20)
                            r.mainloop()
                            read_obj.close()
                        else:
                            popupmsg("Invalid Credentials","Invalid Login","Try Again") 
                            read_obj.close()
                    popupmsg("User does not exist", "Invalid Login", "Try Again")
        elif (choice == "Developer"):
            # open file in read mode
            with open(r'..\data\developers.csv', 'r') as read_obj:
                # pass the file object to reader() to get the reader object
                csv_reader = reader(read_obj)
                # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    # row variable is a list that represents a row in csv
                    if row[0] == user:
                        if row[1] == password:
                            r=tk.Tk()
                            r.geometry('300x300')
                            r.wm_title("Successfully Logged In")
                            rlbl=tk.Label(r,text="Welcome to Project X",font=LARGE_FONT)
                            rlbl.pack(pady=20,padx=20)
                            r.mainloop()
                            read_obj.close()
                        else:
                            popupmsg("Invalid Credentials","Invalid Login","Try Again")
                            read_obj.close()
                popupmsg("User does not exist", "Invalid Login", "Try Again")

 


  
        




def popupmsg(msg,heading,buttonText):
    popup=tk.Tk()
    popup.geometry('300x150')
    popup.wm_title(heading)
    label=tk.Label(popup,text=msg,font=SMALLER_FONT)
    label.pack(side="top",fill="x",pady=20,padx=20)
    b1=ttk.Button(popup,text=buttonText,command=popup.destroy)
    b1.pack()
    popup.mainloop()




class GUI(tk.Tk):
    def __init__(self,*args,**kwargs):
        
        tk.Tk.__init__(self,*args,**kwargs)
        
        
        tk.Tk.wm_title(self,"Project X")
        
        
        container=tk.Frame(self) 
        container.pack(side="top",fill="both",expand=False)        
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        
        
     
       
        self.frames={} #Creating an empty dictionary
        
        for F in (StartPage,RegPage,SuccessRegPage):
            frame=F(container,self)
            self.frames[F]= frame 
            frame.grid(row=0,column=0,sticky="nsew") 
        
        self.show_frame(StartPage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()


# In[349]:


class StartPage(tk.Frame): #Inheriting every frame we used
    
    def __init__(self,parent,controller):
        
       

        nameEnterV=tk.StringVar()
        passEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent) #Parent Class is the GUI class
        

        
        
        Wel= tk.Label(self,text="Project X",font=LARGE_FONT)
        Wel.pack(pady=10,padx=10) 
        
        LIFB=tk.Label(self,text="Log In as ",font=SMALL_FONT)
        LIFB.pack(pady=10,padx=10) 
       
        variable = tk.StringVar(self)
        variable.set("Player") # default value    
        w = tk.OptionMenu(self, variable, "Player", "Advertiser", "Operator", "Developer")
        w.pack()
        
        
        Username=tk.Label(self,text="Username",font=("Calibri",11))
        Username.pack(pady=5,padx=5)
        nameEnter=tk.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        Password=tk.Label(self,text="Password",font=("Calibri",11))
        Password.pack(pady=5,padx=5)
        passEnter=tk.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        Loginbutton=ttk.Button(self,text="Log in",command=lambda:CheckCred(nameEnter,passEnter, variable))
                                                                  
        Loginbutton.pack(pady=20,padx=25)
        
        NU=tk.Label(self,text="New User?",font=("Calibri",12))
        NU.pack(pady=25,padx=15)
        
        RH=ttk.Button(self,text="Register Here",
                command=lambda: controller.show_frame(RegPage))
        RH.pack()
        


# In[350]:


class RegPage(tk.Frame):
    def __init__(self,parent,controller):
        nameEnterV=tk.StringVar()
        passEnterV=tk.StringVar()
        tk.Frame.__init__(self,parent)
        
        RHSB=ttk.Label(self,text="Register for Project X",font=LARGE_FONT)
        RHSB.pack(pady=10,padx=10) 
        
        
        variable = tk.StringVar(self)
        variable.set("Player") # default value
        
        w = tk.OptionMenu(self, variable, "Player", "Advertiser", "Operator", "Developer")
        w.pack()
        
        UsernameR=tk.Label(self,text="Username",font=("Calibri",11))
        UsernameR.pack(pady=5,padx=5)
        nameEnter=tk.Entry(self,bd=4,textvariable=nameEnterV)
        nameEnter.pack()
        
        
        Phone=tk.Label(self,text="Phone Number",font=("Verdana",11))
        Phone.pack(pady=5,padx=5)
        phoneEnter=tk.Entry(self,bd=4)
        phoneEnter.pack()
        
        PasswordR=tk.Label(self,text="Password",font=("Verdana",11))
        PasswordR.pack(pady=5,padx=5)
        passEnter=tk.Entry(self,show='*',bd=4,textvariable=passEnterV)
        passEnter.pack()
        
        SU=ttk.Button(self,text="Sign Up ",command=lambda:[insert(nameEnter,passEnter,phoneEnter, variable),controller.show_frame(SuccessRegPage)])
        SU.pack(pady=15,padx=15)
     
        
        AHA=tk.Label(self,text="Already have an account?",font=SMALLER_FONT)
        AHA.pack(pady=30,padx=10)
        
        Loginbutton2=ttk.Button(self,text="Go to Login Page",command=lambda:controller.show_frame(StartPage))                                                         
        Loginbutton2.pack(pady=0,padx=25)
        
def ResetReg(Nentry,Eentry,Pentry,Passentry):
    Nentry.delete(0,'end')
    Pentry.delete(0,'end')
    Passentry.delete(0,'end')  


# In[351]:


class SuccessRegPage(tk.Frame):
        def __init__(self,parent,controller):
            tk.Frame.__init__(self,parent)
            label=ttk.Label(self,text="Succesfully Registered",font=SMALL_FONT)
            label.pack(pady=10,padx=10)

            button4=ttk.Button(self,text="Go To Login Page",
                    command=lambda: controller.show_frame(StartPage))
            button4.pack()


# In[352]:


app=GUI() #Calling the class
app.geometry('1280x720')
app.mainloop() #Tkinter functionality

