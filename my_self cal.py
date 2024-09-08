from tkinter import*
from tkinter import colorchooser
from datetime import datetime



class r(): #add functionality class
    
    def __init__(self,m):
     self.e=Entry(m,justify="center",width=2,font=('Georgia 20'))
     self.e.grid(pady=10,padx=7,ipady=10)
     #self.name=10
     
    def no(self):
       c=self.e.get()
       c=len(c)-1
       self.e.delete(c,"end")
       
    def r(self):
       #self.e.delete(0,"end")
       a=self.e.get()
       
       tup=("+","-","*","/")
       for j in tup:
         
         if j in a:
          i=a.find(j)
          b=a[:i] 
          c=a[i+1:]
          if j=="+":
           result=float(b)+float(c)
          elif j=="-":
           result=float(b)-float(c)
          elif j=="*":
           result=float(b)*float(c)
          elif j=="/":
           if c=="0":
            self.e.delete(0,"end")
            self.e.insert(0,"error")
            break
           else:
            result=float(b)/float(c) 
          self.e.delete(0,"end")
          self.e.insert(0,str(result))
          
       



class b(r):
    def __init__(self,m):
     super().__init__(m)
   
     self.f1=Frame(m,width=5,background="white")
     self.f1.grid(row=3,column=0,padx=10)
     bwc= Button(self.f1,text="change theme",width=10,height=4,command=self.fcol)
     bwc.grid(row=2,column=4,padx=5,pady=5)
     bw= Button(self.f1,text="0",width=10,height=4,command=lambda:self.e.insert("end","0"))
     bw.grid(row=3,column=3,padx=5,pady=5)
     bw= Button(self.f1,text="=",width=10,height=4,command=self.r)
     bw.grid(row=3,column=2,padx=5,pady=5)
     

     self.count=1
     for i in range(3):
        for j in range(3):
          bw= Button(self.f1,text=self.count,width=10,height=4,command=lambda x=self.count:self.e.insert("end",x))
          bw.grid(row=i,column=j,padx=5,pady=5)
          self.count+=1
     self.ari()
    def ari(self):
       self.count1=0
       t=("+","-","*")
       for i in t:
          if self.count1==3:
             break
          bw= Button(self.f1,text=i,width=10,height=4,command=lambda x=i:self.e.insert("end",x))
          bw.grid(row=self.count1,column=3,padx=5,pady=5)
          self.count1+=1
       del(self.count1)
      
       bw= Button(self.f1,text="/",width=10,height=4,command=lambda:self.e.insert("end","/"))
       bw.grid(row=3,column=0,padx=5,pady=5)
       #The line of code you provided is not working because the command parameter of the Button widget in Tkinter expects a function or method to be passed as an argument, not the result of a function call.
      #In your code, you are trying to call the self.e.insert("end","/") function and pass its result as the command. This is not the correct way to use the command parameter.

       bw= Button(self.f1,text="C",width=10,height=4,command=lambda:self.e.delete(0,"end"))
       bw.grid(row=3,column=1,padx=5,pady=5)
       b3=Button(self.f1,text="Quit this app",height=4,command=m.quit)
       b3.grid(row=3,column=4)
       b3=Button(self.f1,text=".",width=10,height=4,command=lambda:self.e.insert("end","."))
       b3.grid(row=1,column=4)
       b3=Button(self.f1,text="back",width=10,height=4,command=self.no)
       b3.grid(row=0,column=4)
    def fcol(self):
      
      self.rv=StringVar(m)
      
      self.rd=Radiobutton(m,text="Entry",value="E",variable=self.rv,command=self.ract)
      self.rd.place(x=453,y=150)
      self.rd1=Radiobutton(m,text="Frame",value="F",variable=self.rv,command=self.ract)
      self.rd1.place(x=453,y=200)
      print(self.rv.get())
      #value=color: This specifies the value that the control variable will take when the radiobutton is selected. In this case, the value is a color.
    def ract(self):

      self.color = colorchooser.askcolor() #The function returns a tuple containing the RGB value of the selected color and a string representing the color name.
      if self.rv.get()=="E":
        self.e.configure(background=self.color[1])
        self.rd.destroy()
        self.rd1.destroy()
      else:
       self.f1.config(background=self.color[1]) #configure or config use to upadate wedget proprty from anywhere 
       #The colorchooser.askcolor() function returns a tuple containing two values:The RGB value of the selected color as a tuple (e.g., (255, 0, 0) for red) The color name as a string (e.g., "red") so we use [1]  By using self.color[1], you are accessing the second element of the tuple, which is the color name as a string
       self.rd.destroy()
       self.rd1.destroy()
      
       
    
     

class basic (Tk,r):
    def __init__(self):
     super().__init__()
     self.title("gaurav")
     self.geometry("510x400+500+200")
     dt=datetime.now()
     dt12=dt.strftime("%I:%M") #"%I:%M %p" for am pm mode
     l1=Label(self,text=str(dt12),font=500).place(x=455,y=30)
     
     
     
     
     
     
 
m= basic()


b1=b(m)
m.mainloop()
