from tkinter import *
from .applications import calendar, clock, calculator, translate, tictactoe, dice_roll

def home_page(username):
    window = Toplevel()
    window.resizable(False,False)
    window.state('zoomed')
    image_icon = PhotoImage(file='templates/imgs/application.png')
    window.iconphoto(False, image_icon)
    window.title('Application')
    window.configure(bg='black')
    Body = Frame(window, width=1400, height=800, bg='#d6d6d6')
    Body.pack(padx=0,pady=0)
        
    top_frame = Frame(Body,width=1345, height=200, bg='white', highlightbackground='#adacb1', highlightthickness=1)
    top_frame.place(x=11,y=10)

    text = Label(top_frame, text=f'Welcome {username}, Choose any App ',  font=('Acumin Variable Concept',30), bg='white', fg='#025919')
    text.place(x=400,y=70)

    down_frame = Frame(Body,width=1345, height=520, bg='white', highlightbackground='#adacb1', highlightthickness=1)
    down_frame.place(x=11,y=212)

    apps = Label(down_frame, text='Apps', font=('Acumin Variable Concept',20), bg='white', fg='#025919')
    apps.place(x=620,y=20)

    app1_img = PhotoImage(file='templates/imgs/calendar.png')
    app1 = Button(down_frame, image = app1_img, borderwidth=0, highlightthickness=0, bd=0, command=calendar)
    app1.place(x=130, y=100)

    app2_img = PhotoImage(file='templates/imgs/clock.png')
    app2 = Button(down_frame, image=app2_img,borderwidth=0, highlightthickness=0, bd=0, command=clock)
    app2.place(x=580, y=90)

    app3_img = PhotoImage(file='templates/imgs/calculator.png')
    app3 = Button(down_frame, image=app3_img, borderwidth=0, highlightthickness=0, bd=0, command=calculator)
    app3.place(x=1050, y=90)

    app4_img = PhotoImage(file='templates/imgs/translate.png')
    app4 = Button(down_frame, image=app4_img, borderwidth=0, highlightthickness=0, bd=0, command=translate)
    app4.place(x=130, y=285)

    app5_img = PhotoImage(file='templates/imgs/tictactoe.png')
    app5 = Button(down_frame, image=app5_img, borderwidth=0, highlightthickness=0, bd=0, command=tictactoe)
    app5.place(x=580, y=300)

    app6_img = PhotoImage(file='templates/imgs/dice_roll.png')
    app6 = Button(down_frame, image=app6_img, borderwidth=0, highlightthickness=0, bd=0, command=dice_roll)
    app6.place(x=1050, y=290)

    window.mainloop()
