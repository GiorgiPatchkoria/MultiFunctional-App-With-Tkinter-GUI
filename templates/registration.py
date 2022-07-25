from tkinter import *
import re
from tkinter import messagebox
from . import login, home
import sqlite3
from werkzeug.security import generate_password_hash

class Registration:
    def __init__(self, window):
        self.window = window
        self.window.resizable(False,False)
        self.window.state('zoomed')
        image_icon = PhotoImage(file='templates/imgs/registration.png')
        self.window.iconphoto(False, image_icon)
        self.window.title('Registration')
        self.window.configure(bg='black')

        self.login_txt = Label(self.window, text='Registration', font=('Arial',30), fg='#00fff7', bg='black')
        self.login_txt.place(x=580, y=50)

        self.email_txt = Label(self.window, text='Email', font=('Arial',10), fg='#00fff7', bg='black')
        self.email_txt.place(x=530, y=120)
        self.email = Entry(self.window, font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.email.place(x=530,y=160, width=300, height=25)
        
        self.username_txt = Label(self.window, text='Username', font=('Arial',10), fg='#00fff7', bg='black')
        self.username_txt.place(x=530, y=210)
        self.username = Entry(self.window, font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.username.place(x=530, y=250, width=300, height=25)

        self.password1_txt = Label(self.window, text='Password', font=('Arial',10), fg='#00fff7', bg='black')
        self.password1_txt.place(x=530, y=300)
        self.password1 = Entry(self.window, show='*',font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.password1.place(x=530,y=340, width=300, height=25 )

        self.password2_txt = Label(self.window, text='Confirm Password', font=('Arial',10), fg='#00fff7', bg='black')
        self.password2_txt.place(x=530, y=390)
        self.password2 = Entry(self.window, width=30, show='*', font=('Arial', 10), fg='black',bd=0,bg='#00fff7')
        self.password2.place(x=530,y=430, width=300, height=25)

        Button(self.window, width=18, pady=4, text='Sign-Up', font='bold', bg='#00fff7', activebackground='#00fff7', fg='black',bd=0, cursor='hand2', command=self.home).place(x=600,y=500)
        Label(self.window, text='Already have an account?', font=('Quicksand',10), bg='black', fg='#00fff7').place(x=580, y=560)
        Button(self.window, text='sign in', bd=0, fg='#00fff7',bg='black', font=('Quicksand', 10, 'underline'), activebackground='black', cursor='hand2', command=self.login).place(x=740, y=558)

    def home(self):
        con = sqlite3.connect('userdata.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS users(
                    email text,
                    username text,
                    password text)''')
        con.commit()

        email = self.email.get()
        username = self.username.get()
        password1 = self.password1.get()
        password2 = self.password2.get()
        password = generate_password_hash(password1, method='sha256')

        email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
        match = re.fullmatch(email_pattern, email)

        con = sqlite3.connect('userdata.db')
        c = con.cursor()
        c.execute("select email from users")
        email_check = [x for x in c.fetchall() if email in x]
        if len(email) < 7 or match is None:
            messagebox.showwarning('Error', 'This is not a valid email address')
        elif email_check:
            messagebox.showwarning('Error', f'{email_check} is Already Exists')
        elif len(username) < 4:
            messagebox.showwarning('Error', 'Length of Username should be more than 4')
        elif len(password1) < 7:
            messagebox.showwarning('Error', 'Password is too small')
        elif password1 != password2:
            messagebox.showwarning('Error', 'Passwords must be same')
        else:
            con = sqlite3.connect('userdata.db')
            cr = con.cursor()
            cr.execute("INSERT INTO users VALUES (:email, :username, :password)",
                        {'email': email,
                        'username': username,
                        'password': password})
            con.commit()

            con = sqlite3.connect('userdata.db')
            curs = con.cursor()
            selecting = "select * from users where email=?"
            info = curs.execute(selecting, (email,))
            datarow = info.fetchone()
            home.home_page(datarow[1])
       

    def login(self):
        win2 = Toplevel()
        login.SignIn(win2)
        self.window.withdraw()
        win2.deiconify()


def registration_page():
    window = Tk()
    Registration(window)
    window.mainloop()
