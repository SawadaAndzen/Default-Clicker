from tkinter import*
from random import randint

score = 0
n = randint(1, 5)
color = None
rank = 'None'
upg_count = 0
cost = 50
level = 1
y_c = None

code1 = 'qr3410'
code2 = 'clickitnow!'
code3 = 'ezscore'
code4 = 'markovskiy'

def codes(event):
    global y_c, score, code1, code2, code3, code4, no_code
    y_c = code_ent.get()
    if y_c == code1:
        score += 20
        no_code['fg'] = 'light green'
        scr['text'] = 'Score: '+ str(score)
        code1 = None
    elif y_c == code2:
        score += 10
        no_code['fg'] = 'light green'
        scr['text'] = 'Score: '+ str(score)
        code2 = None
    elif y_c == code3:
        score += 30
        no_code['fg'] = 'light green'
        scr['text'] = 'Score: '+ str(score)
        code3 = None
    elif y_c == code4:
        score += 50
        no_code['fg'] = 'light green'
        scr['text'] = 'Score: '+ str(score)
        code4 = None
    elif y_c != code1 or y_c != code2 or y_c != code3 or y_c != code4:
        no_code.pack(side=TOP)
        no_code['fg'] = 'red'

def upgrade(event):
    global upg_count, cost, level, score, upgb
    if score >= cost:
        no_score['fg'] = 'light green'
        score = score - cost
        upg_count += 1
        level += 1
        cost = cost + 100
        upg['text'] = 'Upgrade: '+ str(upg_count)
        dollars['text'] = 'Cost: '+ str(cost) + ' score'
        scr['text'] = 'Score: '+ str(score)
    elif upg_count == 9:
        upg['text'] = 'Upgrade: MAX'
        upgb['bg'] = 'grey'
        upgb['fg'] = 'light grey'
        dollars['fg'] = 'light green'
        upgb['state'] = 'disable'
        
    elif score < cost:
        no_score['fg'] = 'red'
        no_score.pack(side=TOP, pady=1)
    
def set_rank():
    global rank
    rnk['text'] = 'Rank: '+ rank

def rank_system():
    global rank, score
    if score > 48:
        rank = "Newbie"
        set_rank()
    if score > 98:
        rank = "Bronze"
        set_rank()
    if score > 498:
        rank = "Silver"
        set_rank()
    if score > 998:
        rank = "Gold"
        set_rank()
    if score > 1998:
        rank = "MAX"
        set_rank()
def set_color():
    global n, color
    if n == 1:
        color = 'red'
        n = randint(1, 5)
    elif n == 2:
        color = 'cyan'
        n = randint(1, 5)
    elif n == 3:
        color = 'purple'
        n = randint(1, 5)
    elif n == 4:
        color = 'green'
        n = randint(1, 5)
    elif n == 5:
        color = 'yellow'
        n = randint(1, 5)
    
def add_score(event):
    set_color()
    rank_system()
    global score
    score = score + level
    scr['text'] = 'Score: '+ str(score)
    clk['bg'] = color

win = Tk()
win.geometry('500x500+525+150')
win.title('Clicker build 0.250323')
win['bg'] = 'light green'

clk = Button(text='Click!', width=10, bg='light grey', font=('Arial', 14, 'bold'))
upgb = Button(text='Upgrade', width=10, bg='light grey', font=('Arial', 14, 'bold'))
cdb = Button(text='Enter', width=10, bg='light grey', font=('Arial', 10, 'bold'))
rnk = Label(text='Rank: '+ str(rank), font=('Arial', 14), bg='light green')
scr = Label(text='Score: '+ str(score), font=('Arial', 14,), bg='light green')
dollars = Label(text='Cost: '+ str(cost) + ' score', font=('Arial', 14), bg='light green')
upg = Label(text='Upgrade: '+ str(upg_count), font=('Arial', 14), bg='light green')
no_score = Label(text='No enoght points*', font=('Arial', 10), bg='light green', fg='red')
code_ent = Entry(width=15, bd=4, bg='light grey', font=('Arial', 12, 'bold'))
no_code = Label(text='Invalid code or already used*', font=('Arial', 10), bg='light green', fg='red')

code_ent.insert(10, 'Type code here...')

scr.pack(side=TOP, pady=10)
upg.pack(side=TOP, pady=10)
rnk.pack(side=TOP, pady=10)
clk.pack(side=TOP, pady=20)
dollars.pack(side=TOP, pady=20)
upgb.pack(side=TOP, pady=1)
code_ent.pack(side=TOP, pady=20)
cdb.pack(side=TOP)

clk.bind('<1>', add_score)
upgb.bind('<1>', upgrade)
cdb.bind('<1>', codes)

win.mainloop()