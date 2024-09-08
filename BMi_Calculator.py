from decimal import DivisionByZero
from tkinter import Button, Entry,Frame,Label,Tk,messagebox,StringVar,DoubleVar
class interface:
    def __init__(self,root):
        root.title("BMI CALCULATOR")
        root.geometry("350x500+550+130")
        root.resizable(False, False)
        
        self.heading=Label(root,text="BMI CALCULATOR",font=("fixedsys",30,"bold"),fg="#299DF6")
        self.heading.pack(pady=40)
        self.mainfreme=Frame(root)
        self.mainfreme.pack()

        self.name=Label(self.mainfreme,text="Name :",font=("tkdefaultfont",12,"italic bold"))
        self.name.grid(row=0,column=0,pady=10)
        self.namevar=StringVar()
        self.nameentry=Entry(self.mainfreme,width=20,relief="solid",justify="center",textvariable=self.namevar)
        self.nameentry.grid(row=0,column=1,pady=10)

        self.weight=Label(self.mainfreme,text="Weight (kg) :",font=("tkdefaultfont",12,"italic bold"))
        self.weight.grid(row=1,column=0,pady=10)
        self.weightvar=StringVar()
        self.weightentry=Entry(self.mainfreme,width=20,relief="solid",textvariable=self.weightvar)
        self.weightentry.grid(row=1,column=1,pady=10)

        self.height=Label(self.mainfreme,text="Heigh (m) :",font=("tkdefaultfont",12,"italic bold"))
        self.height.grid(row=2,column=0,pady=10)
        self.heightvar=StringVar()
        
        self.heightentry=Entry(self.mainfreme,width=20,relief="solid",textvariable=self.heightvar)
        self.heightentry.grid(row=2,column=1,pady=10)

        self.button=Button(self.mainfreme,text="CALCULATE",background="#299DF6",width=30,height=2,command=self.calculation)
        self.button.grid(row=3,column=0,columnspan=2,pady=10)
        self.result=Label(self.mainfreme,font=("tkdefaultfont",12,"italic bold"))
        self.result.grid(row=4,column=0,pady=10)

        

    def calculation(self):
         self.result.config(text=f" Hii :  {self.namevar.get()}")
         
         try: 
          self.weight=float(self.weightvar.get())
          self.height=float(self.heightvar.get())
          if self.height<=0 or self.weight<=0:
            messagebox.showwarning(message="Values can't be Less then 0. For bugs report on Gauravkarbon@gmail.com")
            quit()
          else:
           self.bmi=self.weight/(self.height**2)
           self.result=Label(self.mainfreme,text=f"Your BMI is :   {round(self.bmi,1)}",font=("tkdefaultfont",12,"italic bold"))
           self.result.grid(row=5,column=0,pady=10,columnspan=1)
           self.classification=Label(self.mainfreme,font=("tkdefaultfont",12,"italic bold"))
           if self.bmi < 18.5:
            self.clsfy="Underweight"
            self.classification.config(fg="blue",text=f"Your are calssified as : {self.clsfy}")
           elif 18.5 <=self.bmi < 24.9:
            self.clsfy="Normal weight"
            self.classification.config(fg="#148404",text=f"Your are calssified as : {self.clsfy}")
           elif 25 <=self.bmi < 29.9:
            self.clsfy="Overweight"
            self.classification.config(fg="#D49605",text=f"Your are calssified as : {self.clsfy}")
           else:
            self.clsfy="Obesity"
            self.classification.config(fg="#C4171E",text=f"Your are calssified as : {self.clsfy}")
          self.classification.grid(row=6,column=0,pady=10,padx=10,columnspan=2) 
         except ValueError:
          messagebox.showerror(message="Invalid input! Please enter numerical values for weight and height.For bugs report on Gauravkarbon@gmail.com")
          quit()
        
win=Tk()
client=interface(win)
win.mainloop()

