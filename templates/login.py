from tkinter import *
from tkinter import messagebox
from werkzeug.security import check_password_hash
from . import registration, home
import sqlite3

class SignIn:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False,False)
        self.window.state('zoomed')
        self.window.title('Login')
        image_icon = PhotoImage(file='templates/imgs/login.png')
        self.window.iconphoto(False, image_icon)
        self.window.configure(bg='black')

        self.login_txt = Label(self.window, text='Login', font=('Arial',40), fg='#00fff7', bg='black')
        self.login_txt.place(x=600, y=50)

        self.email_txt = Label(self.window, text='Email', font=('Arial', 15), fg='#00fff7', bg='black')
        self.email_txt.place(x=530, y=180)
        self.email = Entry(self.window,  font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.email.place(x=530,y=220, width=300, height=25)

        self.password_txt = Label(self.window, text='Password', font=('Arial',15), fg='#00fff7', bg='black')
        self.password_txt.place(x=530, y=270)
        self.password = Entry(self.window, show='*',font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.password.place(x=530,y=310, width=300, height=25)

        Button(self.window, width=18, pady=4, text='Sign In', font='bold', bg='#00fff7', activebackground='#00fff7', fg='black',bd=0, cursor='hand2', command=self.home).place(x=600,y=400)

        Label(self.window, text='Don\'t have an account?', font=('Quicksand',10), bg='black', fg='#00fff7').place(x=580, y=460)

        Button(self.window, text='sign up', bd=0, fg='#00fff7',bg='black', font=('Quicksand', 10, 'underline'), activebackground='black', cursor='hand2', command=self.registrations).place(x=730, y=458)

    def home(self):
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()
        email = self.email.get()
        password = self.password.get()
        selecting = "select * from users where email=?"
        info = cur.execute(selecting, (email,))
        datarow = info.fetchone()

        try:
            if check_password_hash(datarow[2], password):
                home.home_page(datarow[1])
            else:
                messagebox.showwarning('Warning', 'Invalid Email or Password')
        except Exception as ep:
            messagebox.showwarning('Warning', 'Invalid Email or Password')
        
    def registrations(self):
        win2 = Toplevel()
        registration.Registration(win2)
        self.window.withdraw()
        win2.deiconify()

def login_page():
    window = Tk()
    SignIn(window)
    window.mainloop()