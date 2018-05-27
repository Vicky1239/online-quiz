from tkinter import*
from random import randint
import time
global score
global tquestion
global r
global username
import sqlite3
import sys
score=0
r=0
tquestion=0
con=sqlite3.connect('quiz.db')
cur=con.cursor()

def button_countdown(i, label):
    if i > 0:
        i -= 1
        label.set(i)
        root.after(1000, lambda: button_countdown(i, label))
    else:
        close()

def close():
    root.destroy()




def incscore():
    return(score+1)

def inctquestion():
    return(tquestion+1)

def question1(root3):
    root3.destroy()
    root1=Tk()
    question(root1)

def thanku(root3):
    global username
    root3.destroy()
    root4 = Tk()
    root4.geometry("300x300")
    root4.title("THANK YOU")
    root4.configure(background="WHITE")
    topframe = Frame(root4, bg='WHITE')
    topframe.pack(side=TOP)
    l1 = Label(topframe,text="THANK YOU FOR PLAYING", fg='BLACK', bg='WHITE')
    l1.pack()
    b1 = Button(text="EXIT", command=root4.destroy, fg='BLACK', bg='RED')
    b1.pack(side=BOTTOM)
    #cur.execute("SELECT * FROM LOGIN WHERE USER IS 'a'")
    cur.execute("UPDATE LOGIN SET SCORE = "+str(score)+" where user = ?",(str(username),))
    con.commit()


    root4.mainloop()

def correct(root2):
    global score
    score=incscore()
    root2.destroy()
    root3 = Tk()
    root3.geometry("300x300")
    root3.configure(background="WHITE")
    topframe = Frame(root3, bg='WHITE')
    topframe.pack(side=TOP)
    bottomframe = Frame(root3, bg='WHITE')
    bottomframe.pack(side=BOTTOM)
    middleframe = Frame(root3, bg='WHITE')
    middleframe.pack()
    middleframe2 = Frame(root3, bg='WHITE')
    middleframe2.pack()
    leftframe = Frame(root3, bg='WHITE')
    leftframe.pack(side=LEFT)
    rightframe = Frame(root3, bg='WHITE')
    rightframe.pack(side=RIGHT)
    l1 = Label(topframe, text="YOUR SCORE - ", fg='BLACK', bg='WHITE')
    l1.pack(padx=2,side=LEFT)
    l2 = Label(topframe, text=score, fg='BLACK', bg='WHITE')
    l2.pack(padx=3,side=RIGHT)
    l5 = Label(middleframe, text="TOTAL QUESTION ATTEMPTED", fg='WHITE', bg='WHITE')
    l5.pack(side=LEFT,padx=1,pady=1)
    l6 = Label(middleframe, text=tquestion, fg='BLACK', bg='WHITE')
    l6.pack(side=RIGHT,padx=2,pady=1)
    l8 = Label(middleframe2, text="CORRECT ANSWER !!!!", fg='BLACK', bg='WHITE')
    l8.pack()
    b1 = Button(bottomframe, text="EXIT", command=lambda : thanku(root3), fg='BLACK', bg='RED')
    b1.pack(padx=1)
    b2 = Button(bottomframe, text="CONTINUE", command=lambda : question1(root3), fg='BLACK', bg='RED')
    b2.pack(padx=2)

def wrong(root2):
    root2.destroy()
    root3 = Tk()
    root3.geometry("300x300")
    root3.configure(background="WHITE")
    topframe = Frame(root3, bg='WHITE')
    topframe.pack(side=TOP)
    bottomframe = Frame(root3, bg='WHITE')
    bottomframe.pack(side=BOTTOM)
    middleframe = Frame(root3, bg='WHITE')
    middleframe.pack()
    middleframe2 = Frame(root3, bg='WHITE')
    middleframe2.pack()
    leftframe = Frame(root3, bg='WHITE')
    leftframe.pack(side=LEFT)
    rightframe = Frame(root3, bg='WHITE')
    rightframe.pack(side=RIGHT)
    l1 = Label(topframe, text="YOUR SCORE - ", fg='BLACK', bg='WHITE')
    l1.pack(padx=2, side=LEFT)
    l2 = Label(topframe, text=score, fg='BLACK', bg='WHITE')
    l2.pack(padx=3, side=RIGHT)
    l5 = Label(middleframe, text="TOTAL QUESTION ATTEMPTED", fg='WHITE', bg='WHITE')
    l5.pack(side=LEFT, padx=1, pady=1)
    l6 = Label(middleframe, text=tquestion, fg='BLACK', bg='WHITE')
    l6.pack(side=RIGHT, padx=2, pady=1)
    l8 = Label(middleframe2, text="WRONG ANSWER !!!!", fg='BLACK', bg='WHITE')
    l8.pack()
    b1 = Button(bottomframe, text="EXIT", command=lambda: thanku(root3), fg='BLACK', bg='RED')
    b1.pack(padx=1)
    b2 = Button(bottomframe, text="CONTINUE", command=lambda: question1(root3), fg='BLACK', bg='RED')
    b2.pack(padx=2)

def question(root1):
    root1.destroy()
    global tquestion
    global flag
    flag=0
    tquestion = inctquestion()
    r=randint(1,20)
    root2 = tkinter.Tk()
    root2.geometry("500x500")
    root2.configure(background="WHITE")
    topframe = Frame(root2, bg='WHITE')
    topframe.pack(side=TOP)
    bottomframe = Frame(root2,bg='WHITE' )
    bottomframe.pack( side=BOTTOM)
    middleframe = Frame(root2, bg='WHITE')
    middleframe.pack(pady=2)
    leftframe = Frame(root2,bg='WHITE')
    leftframe.pack(side=LEFT)
    rightframe = Frame(root2, bg='WHITE')
    rightframe.pack(side=RIGHT)



    counter = 10
    button_label = tkinter.StringVar()
    button_label.set(counter)
    tkinter.Button(root, textvariable=button_label, command=close).pack()
    button_countdown(counter, button_label)




    
    l1 = Label(topframe, text="QUESTION NO. - ", fg='BLACK', bg='WHITE')
    l1.pack(side=LEFT)
    l2= Label(topframe, text=tquestion, fg='BLACK', bg='WHITE')
    l2.pack(side=RIGHT)
    l3 = Label(bottomframe, text="YOUR SCORE", fg='BLACK', bg='WHITE')
    l3.pack(side=LEFT)
    l4 = Label(bottomframe, text=score, fg='BLACK', bg='WHITE')
    l4.pack(side=LEFT,padx=2)
    l6 = Label(bottomframe, text=tquestion-1, fg='BLACK', bg='WHITE')
    l6.pack(side=RIGHT)
    l5 = Label(bottomframe, text="out of", fg='BLACK', bg='WHITE')
    l5.pack(side=RIGHT, padx=2)
    if(r==1):
        l5=Label(middleframe,text="Which of the following is the fastest logic",fg='BLACK', bg='WHITE')
        l5.pack()
        b1l5=Button(middleframe,text="A. TTL",command=lambda : wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe,text="B. LSI",command=lambda : wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe,text="C. CMOS",command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe,text="D. ECL",command=lambda: correct(root2))
        b4l5.pack()

    elif (r == 2):
        l6 = Label(middleframe, text="A bottom up parser generates", fg='BLACK', bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. RMD in reverse", command=lambda: correct(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. RMD", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. LMD", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. LMD in reverse", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 3):
        l6 = Label(middleframe, text="a grammer that produces more than one parse tree for some sentence is called ", fg='BLACK', bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. unambigous", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. ambigous", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. regular", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 4):
        l6 = Label(middleframe, text="An optimizing compiler ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. is optimized to occupy less space", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. uses source code as its input", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. both of mentioned ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above", command=lambda: correct(root2))
        b4l5.pack()

    elif (r == 5):
        l6 = Label(middleframe, text="the linker: ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. is similar to interpreter", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. uuses source code as its input", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. l s is required to create a load module ", command=lambda: correct(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above ", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 6):
        l6 = Label(middleframe, text="Pee Hole optimization: ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. loop optimization", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. local optimization", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. constant folding", command=lambda: correct(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. data flow analysis", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 7):
        l6 = Label(middleframe, text="The optimization which avoids test at every iteration is ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. loop unrolling", command=lambda: correct(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. loop jamming", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. constant folding ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 8):
        l6 = Label(middleframe, text="Shift reduce parsers are  ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. top down parser", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. bottom up parser", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. may be top down or bottom up ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 9):
        l6 = Label(middleframe, text="DAG representation of basic block allows ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. automatic detection of local common subexpressions", command=lambda: correct(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. detection of induction variables", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. automatic detection of loop variant ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 10):
        l6 = Label(middleframe, text="an intermediate code form is  ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. postfix notataion", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. syntax trees", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. three address code ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. all of the above", command=lambda: correct(root2))
        b4l5.pack()

    elif (r == 11):
        l6 = Label(middleframe, text="which of the following action an operator precedence parser may take to recover from error ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. insert symbols onto the stack", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. delete symbols from the stack", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. inserting or deleting symbols from input ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. all of the mntioned", command=lambda: correct(root2))
        b4l5.pack()

    elif (r == 12):
        l6 = Label(middleframe, text="The output of lexical analyser is ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. a set of regular expression", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. syntax trees", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. set of token", command=lambda: correct(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. string of characters", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 13):
        l6 = Label(middleframe, text="which of the following is used for grouping of characters into tokens ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. parser", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. code optimization", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. code generator ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. lexical analyser", command=lambda: correct(root2))
        b4l5.pack()

    elif (r == 14):
        l6 = Label(middleframe, text="a garbage is  ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. unallocated storage", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. allocated storage whose access path are destroyed?", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. allocated storage ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. uninitialized storage", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 15):
        l6 = Label(middleframe, text="input to code generator ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. source code", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. intermediate code", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. target code", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. all of the above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 16):
        l6 = Label(middleframe, text="A synthesized attribute is an attribute whose value at parse tree node depends on ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. attributes at siblings only ", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B.attributes at parent node only ", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. attributes at children node only ", command=lambda: correct(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. none of the above", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 17):
        l6 = Label(middleframe, text="The graph that shows basic blocks and their successor relationship is called ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. DAG", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. flow chart", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. control graph ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. hamilton graph", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 18):
        l6 = Label(middleframe, text="which of the following symbols table implemetation is based on the property of locality of reference ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. hash table", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. search tree", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. self organizing list ", command=lambda: correct(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. linear list", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 19):
        l6 = Label(middleframe, text="which one of the following is a top down parser ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. recursive descent parser", command=lambda: correct(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. operator precedence parser", command=lambda: wrong(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. an LR(k) parser", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. an LALR(k) parser", command=lambda: wrong(root2))
        b4l5.pack()

    elif (r == 20):
        l6 = Label(middleframe, text="An LR-parser can detect a syntatic error as soon as  ", fg='BLACK',bg='WHITE')
        l6.pack()
        b1l5 = Button(middleframe, text="A. The parsing starts", command=lambda: wrong(root2))
        b1l5.pack()
        b2l5 = Button(middleframe, text="B. It is possible to do so a left-to-right scan of the input", command=lambda: correct(root2))
        b2l5.pack()
        b3l5 = Button(middleframe, text="C. It is possible to do so a right-to-left scan of the input ", command=lambda: wrong(root2))
        b3l5.pack()
        b4l5 = Button(middleframe, text="D. parsing ends", command=lambda: wrong(root2))
        b4l5.pack()

    root2.mainloop()



def login():
    global user
    global password
    root1 = Tk()
    root1.geometry("300x300")
    root1.title('Enter your information')
    root1.configure(background="WHITE")
    topframe=Frame(root1,bg='WHITE')
    topframe.pack(side=TOP)
    bottomframe=Frame(root1,)
    bottomframe.pack(pady=40,side=TOP)
    user = make_entry(root1, "User name:", 16)
    password = make_entry(root1, "Password:", 16, show="*")
    #button to attempt to login
    b121 = Button(root1, borderwidth=4, text="Login", width=10, pady=8, command=lambda:check_password(root1))
    b121.pack()
    password.bind('<Return>', enter)
    user.focus_set()
    root1.mainloop()
    con.close()



def make_entry(root1, caption, width=None, **options):
    Label(root1, text=caption).pack(side=TOP)
    entry = Entry(root1, **options)
    if width:
        entry.config(width=width)
    entry.pack(side=TOP, padx=10, fill=BOTH)
    return entry


   
def enter(event):
    check_password(root1)

    
    
def check_password(root1):
    """ Collect 1's for every failure and quit program in case of failure_max failures """
    global username
    passwords =cur.execute("SELECT USER,PASSWORD FROM LOGIN")
    passwords = cur.fetchall()

    if (user.get(), password.get()) in passwords:
        username = user.get()
        question(root1)
        return           
    check_password.failures += 1
    if check_password.failures == failure_max:
        root1.destroy()
        raise SystemExit('Unauthorized login attempt')
    else:
        root1.title('Try again. Attempt %i/%i' % (check_password.failures + 1, failure_max))
check_password.failures = 0



def start():
    root.destroy()
    login()



root=Tk()
failure_max = 3
root.geometry("300x300")
root.configure(background="WHITE")
topframe=Frame(root,bg='WHITE')
topframe.pack(side=TOP)
bottomframe=Frame(root,)
bottomframe.pack(pady=40,side=TOP)
l1=Label(topframe,text="Lets start the QUIZ !!!!",fg='BLACK',bg='WHITE')
l1.pack(pady=30)
l2=Label(topframe,text="-----BEST OF LUCK------",fg='BLACK',bg='WHITE')
l2.pack(pady=30)
b1=Button(bottomframe,text="START",command=start,fg='BLACK',bg='RED')
b1.pack()
root.mainloop()
