from tkinter import *
import tkinter.messagebox as tmsg

equation=''

def show(val):
    global equation
    equation+=val
    resultlabel.config(text=equation)

def showop(val):
    global equation
    if equation=='':
        resultlabel.config(text=equation)
    elif equation[-1]=='*':
        resultlabel.config(text=equation)
    elif equation[-1]=='+':
        resultlabel.config(text=equation)
    elif equation[-1]=='/':
        resultlabel.config(text=equation)
    elif equation[-1]=='%':
        resultlabel.config(text=equation)
    elif equation[-1]=='-':
        resultlabel.config(text=equation)
    else:
        equation+=val
        resultlabel.config(text=equation)

def clear():
    global equation
    equation=''
    resultlabel.config(text=equation)

def calculate():
    global equation
    result=''
    if equation != '':
        try:
            result=eval(equation)
        except:
            result='error'
            equation=''
            tmsg.showinfo('error','ABEY SHI VALUE ENTER KRR')
    resultlabel.config(text=result)



root=Tk()
root.title('calculator GURKEET SINGH una da')
root.geometry("570x600")
root.resizable(False,False)
root.configure(bg='#ADD8E6') #use to change background color 
resultlabel=Label(root,text="Toh chaliye Dosto shuru karte hain",width=30,height=2,fg='#ADD8E6',font='arial 25 bold',relief=GROOVE)
resultlabel.pack(side=TOP,anchor=NW)

mymenu=Menu(root)
mymenu.add_command(label='band etho',command=quit)
root.config(menu=mymenu)

b1=Button(root,text='C',width=5,height=1,font='arial 30 bold',bd=3,fg='#FFA500',bg='#36454F',relief=SUNKEN,command=lambda:clear()).place(x=10,y=100)
b1=Button(root,text='/',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:showop('/')).place(x=150,y=100)
b1=Button(root,text='%',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:showop('%')).place(x=290,y=100)
b1=Button(root,text='*',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:showop('*')).place(x=430,y=100)

b1=Button(root,text='7',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('7')).place(x=10,y=200)
b1=Button(root,text='8',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('8')).place(x=150,y=200)
b1=Button(root,text='9',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('9')).place(x=290,y=200)
b1=Button(root,text='-',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('-')).place(x=430,y=200)

b1=Button(root,text='4',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('4')).place(x=10,y=300)
b1=Button(root,text='5',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('5')).place(x=150,y=300)
b1=Button(root,text='6',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('6')).place(x=290,y=300)
b1=Button(root,text='+',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:showop('+')).place(x=430,y=300)

b1=Button(root,text='1',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('1')).place(x=10,y=400)
b1=Button(root,text='2',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('2')).place(x=150,y=400)
b1=Button(root,text='3',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('3')).place(x=290,y=400)
b1=Button(root,text='0',width=11,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('0')).place(x=10,y=500)

b1=Button(root,text='.',width=5,height=1,font='arial 30 bold',bd=3,fg='#808080',bg='#36454F',relief=SUNKEN,command=lambda:show('.')).place(x=290,y=500)
b1=Button(root,text='=',width=5,height=3,font='arial 30 bold',bd=3,fg='#ffffff',bg='#fe9037',relief=SUNKEN,command=lambda:calculate()).place(x=430,y=400)

root.mainloop()