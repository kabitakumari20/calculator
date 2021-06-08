from tkinter import*
def btnclick(number):
    global val
    val=val+str(number)
    data.set(val)


def btnClear():
    global val
    val=""
    data.set("")



def btnEqual():
    global val
    result=str(eval(val))
    data.set(result)



root=Tk()
root.title("my calcualtor")
val=""
data=StringVar()

dispaly=Entry(root,textvariable=data,bd=29,justify="right",bg="blue",font=("ariel",20))

btn7=Button(root,text="7",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(7))

btn8=Button(root,text="8",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(8))

btn9=Button(root,text="9",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(9))

btn4=Button(root,text="4",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(4))

btn5=Button(root,text="5",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(5))

btn6=Button(root,text="6",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(6))

btn1=Button(root,text="1",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(1))

btn2=Button(root,text="2",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(2))

btn3=Button(root,text="3",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(3))

btn0=Button(root,text="0",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(0))


btn_division=Button(root,text="//",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("//"))

btn_Equal=Button(root,text="=",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnEqual)

btn_add=Button(root,text="+",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("+"))

btn_sub=Button(root,text="-",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick("-"))

btn_multi=Button(root,text="",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=lambda:btnclick(""))

btn_Clear=Button(root,text="clear",font=("ariel",20,"italic"),bd=12,height=2,width=7,command=btnClear)




dispaly.grid(row=0,columnspan=4)

btn7.grid(row=1,column=0)

btn8.grid(row=1,column=1)

btn9.grid(row=1,column=2)

btn4.grid(row=2,column=0)

btn5.grid(row=2,column=1)

btn6.grid(row=2,column=2)

btn1.grid(row=3,column=0)

btn2.grid(row=3,column=1)

btn3.grid(row=3,column=2)

btn0.grid(row=4,column=0)

btn_division.grid(row=4,column=1)

btn_Equal.grid(row=4,column=2)

btn_add.grid(row=1,column=3)

btn_sub.grid(row=2,column=3)

btn_multi.grid(row=3,column=3)

btn_Clear.grid(row=4,column=3)


root.mainloop()
