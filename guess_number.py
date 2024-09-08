import random,math
from tkinter import Tk,Entry,Frame,Label,Button,StringVar,IntVar,messagebox
class console:
    def __init__(self):
        self.tk=Tk()
        self.tk.title("Gusee the Number Game")
        self.tk.geometry("500x680+450+80")
        self.tk.resizable("false",'false')
        self.tk["bg"]="#452543" 
        self.L1=Label(self.tk,text="Guess The Number Game",font=("times",30,"italic bold"),fg="#3279a8",bg="#452543")
        self.L1.pack()
        self.re=Label(self.tk,text="Report On",fg="#ADD8E6",bg="#452543")
        self.re.place(x=410,y=640)
        self.re2=Label(self.tk,text="Gauravkarbon@gmail.com",fg="#ADD8E6",bg="#452543")
        self.re2.place(x=350,y=660)

        self.Pn=Label(self.tk,text="Player Name",font=("times",20,"italic"),fg="white",bg="#452543")
        self.Pn.place(x=40,y=60)
        self.Pnvar=StringVar()
        self.ePn=Entry(self.tk,width=30,textvariable=self.Pnvar)
        self.ePn.place(x=250,y=70) 

        self.f1=Frame(self.tk,width=350,height=120,bg="#452543")
        self.f1.place(x=44,y=100)       

        self.L2=Label(self.f1,text="Range",font=("times",20,"italic"),fg="white",bg="#452543")
        self.L2.place(x=20,y=10)
        self.a=IntVar()
        self.b=IntVar(value=100)
        self.e1a=Entry(self.f1,width=5,textvariable=self.a)
        self.e1a.place(x=210,y=20)
        self.e1b=Entry(self.f1,width=5,textvariable=self.b)
        self.e1b.place(x=280,y=20)
        
        self.L2=Label(self.f1,text="Attempt         :     10",font=("times",20,"italic"),fg="white",bg="#452543")
        self.L2.place(x=20,y=50)

        self.b1=Button(self.f1,text="Start",background="black",foreground="white",width=10,command=self.start_game)
        self.b1.place(x=150,y=95)
        self.tk.mainloop()
        
    def start_game(self):
        if self.a.get()==self.b.get():
              messagebox.showerror(message="Invalid Range, Restart the Game ")
              quit()
        self.f1.destroy()
        self.ePn.destroy()
        self.Player = Label(self.tk, text=f":   {self.Pnvar.get()}", font=("times", 20, "italic bold"), fg="Green", bg="#452543")
        self.Player.place(x=240, y=58)
        self.Random_number=random.randint(self.a.get(),self.b.get())
        self.intro=f'''   Welcome to the Guess the Number Game!
    I'm thinking of a number between {self.a.get()} and {self.b.get()}.
    You have 10 attempts to guess it.'''
        self.Player = Label(self.tk, text=self.intro,font=("courier new",12,"bold"), fg="yellow", bg="#452543")
        self.Player.place( y=100)

        self.i=180
        self.attempt=0
        self.your_guess_number=StringVar()
        self.guess=Label(self.tk,text="Enter your guess:",fg="white",bg="#452543")
        self.guess.place(x=130,y=170) 
        self.ge=Entry(self.tk,width=int(math.log10(self.b.get())),textvariable=self.your_guess_number)
        self.ge.place(x=250,y=170)
        self.b2=Button(self.tk,text="apply",background="black",foreground="white",width=5,command=self.core_logic)
        self.b2.place(x=300,y=170)          

    def core_logic(self): 
        self.i+=40   
        self.guessp=Label(self.tk,text=f"Your Guess Number   :      {self.your_guess_number.get()}",fg="white",bg="#452543")
        self.guessp.place(x=50,y=self.i)
        
        try:

            self.attempt += 1
            if self.attempt == 10:
             self.guess_result=f"Sorry, you've used all your attempts. The number was {self.Random_number}."
             self.b2.config(state="disabled")
            
           # Check the guess
            if int(self.your_guess_number.get())< self.a.get() or int(self.your_guess_number.get()) > self.b.get():
                    self.guessr.config(text="Please guess a number between 1 and 100.")             
                    
            elif int(self.your_guess_number.get()) < self.Random_number:
                    self.guess_result="Too low! Try again."
                    
            elif int(self.your_guess_number.get()) > self.Random_number:
                    self.guess_result="Too high! Try again."
                    
            else:
                    self.guess_result=f"Congratulations! You've guessed the number {self.Random_number} in {self.attempt} attempts."
                    self.b2.config(state="disabled")

        except ValueError:
             
             messagebox.showerror(message="Invalid input! Please enter a number.")
             self.guess_result="                                ENTER AGAIN"

        self.ge.delete(0,"end")     
        self.guessr=Label(self.tk,text=self.guess_result,fg="white",bg="#452543")
        self.guessr.place(x=50,y=self.i+20)
       
lunch=console()


