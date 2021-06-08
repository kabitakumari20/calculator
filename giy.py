import tkinter
from tkinter import *
root=tkinter.Tk()
root.resizable(0,0)
root.title("**WELCOME IN CALCULATOR***")


e=Entry(root,width=40,bg="blue")
e.grid(row=0,column=0,columnspan=3,padx=20,pady=20)
e.insert(0," ")


def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))


def check_button():
    e.delete(0,END)


def button_add():
    frist_number=e.get()
    global f_num
    global math
    math="addition"
    f_num=int(frist_number)
    e.delete(0,END)


def button_equal():
    sec_number=e.get()
    e.delete(0,END)
    if math=="addition":
        e.insert(0,f_num+int(sec_number))
    if math=="subtraction":
        e.insert(0,f_num-int(sec_number))
    
    if math=="multiplication":
        e.insert(0,f_num*int(sec_number))


    if math=="division":
        e.insert(0,f_num/int(sec_number))


    if math=="modules":
        e.insert(0,f_num%int(sec_number))


def button_subs():
    frist_number=e.get()
    global f_num
    global math
    math="subtraction"
    f_num=int(frist_number)
    e.delete(0,END)
    


def button_div():
    frist_number=e.get()
    global f_num
    global math
    math="division"
    f_num=int(frist_number)
    e.delete(0,END)
    

def button_modules():
    frist_number=e.get()
    global f_num
    global math
    math="modules"
    f_num=int(frist_number)
    e.delete(0,END)
    

def button_multi():
    frist_number=e.get()
    global f_num
    global math
    math="multiplication"
    f_num=int(frist_number)
    e.delete(0,END)
    



button_1=Button(root,text="1",padx=40,pady=20,command=lambda: button_click(1))
button_2=Button(root,text="2",padx=40,pady=20,command=lambda: button_click(2))
button_3=Button(root,text="3",padx=40,pady=20,command=lambda: button_click(3))
button_4=Button(root,text="4",padx=40,pady=20,command=lambda: button_click(4))

button_5=Button(root,text="5",padx=40,pady=20,command=lambda: button_click(5))
button_6=Button(root,text="6",padx=40,pady=20,command=lambda: button_click(6))
button_7=Button(root,text="7",padx=40,pady=20,command=lambda: button_click(7))
button_8=Button(root,text="8",padx=40,pady=20,command=lambda: button_click(8))

button_9=Button(root,text="9",padx=40,pady=20,command=lambda: button_click(9))
button_0=Button(root,text="0",padx=40,pady=20,command=lambda: button_click(0))


button_add=Button(root,text="+",padx=39,pady=20,command=button_add)
button_equal=Button(root,text="=",padx=40,pady=20,command=button_equal)
button_subs=Button(root,text="-",padx=39,pady=20,command=button_subs)
button_clear=Button(root,text="clear",padx=39,pady=20,command=check_button)


button_div=Button(root,text="/",padx=39,pady=20,command=button_div)
button_modules=Button(root,text="%",padx=39,pady=20,command=button_modules)
button_multi=Button(root,text="*",padx=39,pady=20,command=button_multi)


button_1.grid(row=3 ,column=0)
button_2.grid(row=3 ,column=1)
button_3.grid(row=3 ,column=2)

button_4.grid(row=2 ,column=0)
button_5.grid(row=2 ,column=1)
button_6.grid(row=2 ,column=2)

button_7.grid(row=1 ,column=0)
button_8.grid(row=1 ,column=1)
button_9.grid(row=1 ,column=2)

button_0.grid(row=4 ,column=0)
button_add.grid(row=4 ,column=2)
button_subs.grid(row=5 ,column=1)

button_equal.grid(row=5 ,column=0)
button_clear.grid(row=4 ,column=1)
button_div.grid(row=6 ,column=1)

button_modules.grid(row=6 ,column=0)
button_multi.grid(row=6 ,column=2)

root.mainloop()


