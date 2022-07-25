from tkinter import *
from tkinter import ttk
from tkinter import ttk, Tk, Entry, Button, StringVar
from time import strftime
import time
import math
from tkcalendar import *
import random
import googletrans
from googletrans import Translator 
from googletrans import LANGUAGES


# Calendar App

def calendar():
    calendar_app = Toplevel()
    calendar_app.state('zoomed')
    calendar_app.title('Calendar')
    calendar_app.resizable(False,False)
    image_icon = PhotoImage(file='templates/imgs/calendar.png')
    calendar_app.iconphoto(False, image_icon)

    calendar = Calendar(calendar_app, setmode='day', date_pattern='d/m/yy')
    calendar.pack(fill='both', expand=True)

    calendar_app.mainloop()

# Clock App

def clock():
    clock_app = Toplevel()
    clock_app.state('zoomed')
    clock_app.resizable(False,False)
    clock_app.title('Clock')
    clock_app.config(bg='black')
    image_icon = PhotoImage(file='templates/imgs/clock.png')
    clock_app.iconphoto(False, image_icon)

    def digital_clock():
        label = Label(clock_app, fg='black',bg='black')
        label.place(x=500, y=300, width=400, height=300)
        def update_clock():
            text = strftime('%H:%M:%S')
            label.configure(text=text)
            label.after(1000,update_clock)
        label = Label(clock_app, font=('digital-7', 70, 'bold'),width=25, bg='#000000', fg='#00fff7')
        label.place(x=1, y=350)
        update_clock()

    
    def analog_clock(): 
        label = Label(clock_app, font=('digital-7', 70, 'bold'),width=25, bg='#000000')      
        label.place(x=1,y=350) 
        def update_clock():
            hours = int(time.strftime("%I"))
            minutes = int(time.strftime("%M"))
            seconds = int(time.strftime("%S"))

            # updating seconds hand
            seconds_x = seconds_hand_len * math.sin(math.radians(seconds * 6)) + center_x
            seconds_y = -1 * seconds_hand_len * math.cos(math.radians(seconds * 6)) + center_y
            canvas.coords(seconds_hand, center_x, center_y, seconds_x, seconds_y)

            # updating minutes hand
            minutes_x = minutes_hand_len * math.sin(math.radians(minutes * 6)) + center_x
            minutes_y = -1 * minutes_hand_len * math.cos(math.radians(minutes * 6)) + center_y
            canvas.coords(minutes_hand, center_x, center_y, minutes_x, minutes_y)

            # updating hours hand
            hours_x = hours_hand_len * math.sin(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_x
            hours_y = -1 * hours_hand_len * math.cos(math.radians(hours * 30 + 0.5 * minutes + 0.008 * seconds)) + center_y
            canvas.coords(hours_hand, center_x, center_y, hours_x, hours_y)

            clock_app.after(1000, update_clock)


        canvas = Canvas(clock_app, width=400, height=400, bd=0, highlightthickness=0, bg="black")
        canvas.place(x=480, y=250)

        # create background
        bg = PhotoImage(file='templates/imgs/analog_clock.png')
        bg.image = bg
        canvas.create_image(200, 200, image=bg)


        # create clock hands
        # seconds hand
        center_x = 200
        center_y = 200

        seconds_hand_len = 95
        minutes_hand_len = 80
        hours_hand_len = 60

        seconds_hand = canvas.create_line(200, 200, 200 + seconds_hand_len, 200 + seconds_hand_len, width=1.5, fill='cyan')
        # minutes hand
        minutes_hand = canvas.create_line(200, 200, 200 + minutes_hand_len, 200 + minutes_hand_len, width=2.5, fill='#234714')
        # hours hand
        hours_hand = canvas.create_line(200, 200, 200 + hours_hand_len, 200 + hours_hand_len, width=4, fill='#253b5e')

        update_clock()

    
    digital_btn = Button(clock_app, text='Digital Clock', font=('bold',15), bg='cyan', fg='black', activebackground='cyan', command=digital_clock)
    digital_btn.place(x=450, y=100)

    digital_btn = Button(clock_app, text='Analog Clock', font=('bold',15), bg='cyan', fg='black', activebackground='cyan', command=analog_clock)
    digital_btn.place(x=850, y=100)

    clock_app.mainloop()


# Calculator App

def calculator():
    class Calculator:
        def __init__(self, window): 
            window.state('zoomed')
            window.title('Calculator')
            window.config(bg='#ffffff')
            window.resizable(False,False)
            image_icon = PhotoImage(file='templates/imgs/calculator.png')
            window.iconphoto(False, image_icon)
            self.equation=StringVar()
            self.entry_value=''
            Entry(calculator_app, width=15, font=('Arial Bold', 121), bg='#00fff7',textvariable=self.equation).place(x=5,y=5)

            Button(calculator_app, width=94, height=6, text='C', relief='flat',bg='#000000',fg='#00fff7',activebackground='#000000',command=self.clear).place(x=5, y=197)
            Button(calculator_app, width=47, height=6, text='%', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('%')).place(x=677, y=197)
            Button(calculator_app, width=47, height=6, text='/', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('/')).place(x=1020, y=197)
            Button(calculator_app, width=46, height=6, text='7', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('7')).place(x=5, y=302)
            Button(calculator_app, width=46, height=6, text='8', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('8')).place(x=341, y=302)
            Button(calculator_app, width=47, height=6, text='9', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('9')).place(x=677, y=302)
            Button(calculator_app, width=47, height=6, text='*', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('*')).place(x=1020, y=302)
            Button(calculator_app, width=46, height=6, text='4', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('4')).place(x=5, y=407)
            Button(calculator_app, width=46, height=6, text='5', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('5')).place(x=341, y=407)
            Button(calculator_app, width=47, height=6, text='6', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('6')).place(x=677, y=407)
            Button(calculator_app, width=47, height=6, text='-', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('-')).place(x=1020, y=407)
            Button(calculator_app, width=46, height=6, text='1', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('1')).place(x=5, y=512)
            Button(calculator_app, width=46, height=6, text='2', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('2')).place(x=341, y=512)
            Button(calculator_app, width=47, height=6, text='3', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('3')).place(x=677, y=512)
            Button(calculator_app, width=47, height=6, text='+', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('+')).place(x=1020, y=512)
            Button(calculator_app, width=46, height=7, text='.', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('.')).place(x=5, y=617)
            Button(calculator_app, width=46, height=7, text='0', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=lambda:self.show('0')).place(x=341, y=617)
            Button(calculator_app, width=96, height=7, text='=', relief='flat',bg='#000000', fg='#00fff7',activebackground='#000000',command=self.solve).place(x=677, y=617)
        
        def show(self,value):
            self.entry_value += str(value)
            self.equation.set(self.entry_value)
            
        def clear(self):
            self.entry_value = ''
            self.equation.set(self.entry_value)

        def solve(self):
            result=eval(self.entry_value)
            self.equation.set(result)

    calculator_app = Toplevel()
    Calculator(calculator_app)
    calculator_app.mainloop()

# Translate App    

def translate():
    translate_app = Toplevel()
    translate_app.state('zoomed')
    translate_app.resizable(False,False)
    translate_app.title('Translate')
    translate_app.configure(bg='#85817b')
    image_icon = PhotoImage(file='templates/imgs/translate.png')
    translate_app.iconphoto(False, image_icon)

        
    def change(text='type', src='', dest=''):
        text1 = text
        src1= src
        dest1 = dest
        trans = Translator()
        trans1 = trans.translate(text, src=src1, dest=dest1)
        return trans1.text

    def data():
        s = first_language.get()
        d = second_language.get()
        masg = first_txt.get(1.0,END)
        textget = change(text=masg, src=s, dest=d)
        second_txt.delete(1.0,END)
        second_txt.insert(END,textget)


    language = googletrans.LANGUAGES
    list_text = list(language.values())

    first_language = ttk.Combobox(translate_app, values=list_text) 
    first_language.place(x=100, y=160, width=200, height=30)
    first_language.set('english')
    second_language = ttk.Combobox(translate_app, values=list_text) 
    second_language.place(x=900, y=160, width=200, height=30)
    second_language.set('english')

    f1 = Frame(translate_app, bg='#00fff7', bd=2)
    f1.place(x=100, y=200, width=400, height=300)
    first_txt = Text(f1, font=('Time New Roman', 20, 'bold'), bg="#00fff7", bd=0, wrap=WORD)
    first_txt.place(x=1, y=1, width=397, height=297)

    f2 = Frame(translate_app, bg='#00fff7', bd=2)
    f2.place(x=900, y=200, width=400, height=300)
    second_txt = Text(f2, font=('Time New Roman', 20, 'bold'), bg="#00fff7", bd=0, wrap=WORD)
    second_txt.place(x=1, y=1, width=397, height=297)
        
    trans_button = Button(translate_app, text='Translate', font=20, bg='black', fg='#00fff7', activebackground='black', relief=RAISED, command=data)
    trans_button.place(x=650, y=320, width=100, height=50)

    translate_app.mainloop()

# Tic-Tac-Toe App

def tictactoe():
    tictactoe_app = Toplevel()
    tictactoe_app.state('zoomed')
    tictactoe_app.title('Tic-Tac-Toe')
    tictactoe_app.configure(bg='#000000')
    tictactoe_app.resizable(False,False)
    image_icon = PhotoImage(file='templates/imgs/tictactoe.png')
    tictactoe_app.iconphoto(False, image_icon)

    def next_turn(row, column):

        global player

        if buttons[row][column]['text'] == "" and check_winner() is False:

            if player == players[0]:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[1]
                    text.config(text=(players[1]+" turn"))

                elif check_winner() is True:
                    text.config(text=(players[0]+" wins"))

                elif check_winner() == "Tie":
                    text.config(text="Tie!")

            else:

                buttons[row][column]['text'] = player

                if check_winner() is False:
                    player = players[0]
                    text.config(text=(players[0]+" turn"))

                elif check_winner() is True:
                    text.config(text=(players[1]+" wins"))

                elif check_winner() == "Tie":
                    text.config(text="Tie!")

    def check_winner():

        for row in range(3):
            if buttons[0][0]['text'] == buttons[0][1]['text'] == buttons[0][2]['text'] != "":
                buttons[0][0].config(bg="white")
                buttons[0][1].config(bg="white")
                buttons[0][2].config(bg="white")
                return True

        for row in range(3):
            if buttons[1][0]['text'] == buttons[1][1]['text'] == buttons[1][2]['text'] != "":
                buttons[1][0].config(bg="white")
                buttons[1][1].config(bg="white")
                buttons[1][2].config(bg="white")
                return True

        for row in range(3):
            if buttons[2][0]['text'] == buttons[2][1]['text'] == buttons[2][2]['text'] != "":
                buttons[2][0].config(bg="white")
                buttons[2][1].config(bg="white")
                buttons[2][2].config(bg="white")
                return True

        for column in range(3):
            if buttons[0][0]['text'] == buttons[1][0]['text'] == buttons[2][0]['text'] != "":
                buttons[0][0].config(bg="white")
                buttons[1][0].config(bg="white")
                buttons[2][0].config(bg="white")
                return True

        for column in range(3):
            if buttons[0][1]['text'] == buttons[1][1]['text'] == buttons[2][1]['text'] != "":
                buttons[0][1].config(bg="white")
                buttons[1][1].config(bg="white")
                buttons[2][1].config(bg="white")
                return True

        for column in range(3):
            if buttons[0][2]['text'] == buttons[1][2]['text'] == buttons[2][2]['text'] != "":
                buttons[0][2].config(bg="white")
                buttons[1][2].config(bg="white")
                buttons[2][2].config(bg="white")
                return True

        if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
            buttons[0][0].config(bg="white")
            buttons[1][1].config(bg="white")
            buttons[2][2].config(bg="white")
            return True

        elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
            buttons[0][2].config(bg="white")
            buttons[1][1].config(bg="white")
            buttons[2][0].config(bg="white")
            return True

        elif empty_spaces() is False:

            for row in range(3):
                for column in range(3):
                    buttons[row][column].config(bg="yellow")
            return "Tie"

        else:
            return False


    def empty_spaces():

        spaces = 9

        for row in range(3):
            for column in range(3):
                if buttons[row][column]['text'] != "":
                    spaces -= 1

        if spaces == 0:
            return False
        else:
            return True

    def new_game():

        global player

        player = random.choice(players)

        text.config(text=player+" turn")

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(text="", bg='#00fff7')


    players = ["x", "o"]
    global player
    player = random.choice(players)
    buttons = [[0,0,0],
            [0,0,0],
            [0,0,0]]

    text = Label(tictactoe_app, text=player + " turn", font=('consolas',35), bg='black', fg='#00fff7')
    text.place(x=600, y=20)

    reset_button = Button(tictactoe_app, text="restart", font=('consolas',20),  bg='black', fg='#00fff7', bd=3, activebackground='black',command=new_game)
    reset_button.place(x=600, y=100)

    frame = Frame(tictactoe_app)
    frame.place(x=435, y=180, width=462, height=528)
        

    for row in range(3):
        for column in range(3):
            buttons[row][column] = Button(frame, text="",font=('consolas',24), bg='#00fff7', activebackground='#00fff7', fg='black', width=8, height=4,
                                                command= lambda row=row, column=column: next_turn(row,column))
            buttons[row][column].grid(row=row,column=column)

    tictactoe_app.mainloop()
        
# Dice roll App

def dice_roll():
    dice_roll_app = Toplevel()
    dice_roll_app.state('zoomed')
    dice_roll_app.title('Dice Roll')
    dice_roll_app.configure(bg='#000000')
    dice_roll_app.resizable(False,False)
    image_icon = PhotoImage(file='templates/imgs/dice_roll.png')
    dice_roll_app.iconphoto(False, image_icon)

    label = Label(dice_roll_app, text='', font=('times', 300), bg='#000000', fg='#00fff7')

    def roll():
        dices = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
        label.configure(text=f'{random.choice(dices)}{random.choice(dices)}')
        label.place(x=375, y=150)
    btn = Button(dice_roll_app, width=20, height=3, text='Click to roll', bg='#c20000', fg='#000000', activebackground='#c20000', bd=0, command=roll)
    btn.place(x=600, y=50)

    dice_roll_app.mainloop()