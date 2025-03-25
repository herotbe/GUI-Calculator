import customtkinter as cstk
from tkinter import END
from tkinter import messagebox

#FUNCTIONALITY 

def clear():
    entry.delete(0,END)


def click(number):
    entry.insert(END,number)

def equal():
    value=entry.get()
    try:
        result=eval(value)
        ans=round(result,3)
        entry.delete(0,END)
        entry.insert(0,ans)
    except SyntaxError:
        messagebox.showerror('Error','Invalid Expression')
    except ZeroDivisionError:
        messagebox.showerror('Error','Number Cant Be Divided By Zero')

    

    



#GUI BUILDING

window=cstk.CTk()
window.title('BEAST MODE CALCULATOR')
window.geometry('500x450')
window.config(bg='black')

entry=cstk.CTkEntry(window,font=('arial',35,'bold'),placeholder_text_color='white',fg_color='black',border_color='white',width=480,height=50,bg_color='black')
entry.grid(row=0,column=0,padx=10,pady=10,columnspan=4)

buttons7=cstk.CTkButton(window,text='7',text_color='white',font=('arial',20,'bold'),width=100,height=50,bg_color='black',command=lambda : click('7'))
buttons7.grid(row=1,column=0,pady=10)

buttons8=cstk.CTkButton(window,text='8',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('8'))
buttons8.grid(row=1,column=1)

buttons9=cstk.CTkButton(window,text='9',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('9'))
buttons9.grid(row=1,column=2)

buttonsmultiply=cstk.CTkButton(window,text='x',text_color='white',font=('arial',20,'bold'),text_color_disabled='red',width=50,height=50,bg_color='black',fg_color='orange',command=lambda : click('*'))
buttonsmultiply.grid(row=1,column=3)

buttonsplus=cstk.CTkButton(window,text='+',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=50,height=50,bg_color='black',fg_color='orange',command=lambda : click('+'))
buttonsplus.grid(row=2,column=3)

buttons4=cstk.CTkButton(window,text='4',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('4'))
buttons4.grid(row=2,column=0,pady=10)

buttons5=cstk.CTkButton(window,text='5',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('5'))
buttons5.grid(row=2,column=1)

buttons6=cstk.CTkButton(window,text='6',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('6'))
buttons6.grid(row=2,column=2)

buttonsminus=cstk.CTkButton(window,text='-',text_color='white',font=('arial',20,'bold'),text_color_disabled='orange',width=50,height=50,bg_color='black',fg_color='orange',command=lambda : click('-'))
buttonsminus.grid(row=5,column=3,pady=10)

buttons1=cstk.CTkButton(window,text='1',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('1'))
buttons1.grid(row=5,column=0)

buttons2=cstk.CTkButton(window,text='2',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('2'))
buttons2.grid(row=5,column=1)

buttons3=cstk.CTkButton(window,text='3',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('3'))
buttons3.grid(row=5,column=2)

buttons0=cstk.CTkButton(window,text='0',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('0'))
buttons0.grid(row=6,column=0,pady=10)

buttonsdot=cstk.CTkButton(window,text='.',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',command=lambda : click('.'))
buttonsdot.grid(row=6,column=1)

buttonsc=cstk.CTkButton(window,text='C',text_color='white',font=('arial',20,'bold'),text_color_disabled='black',width=100,height=50,bg_color='black',fg_color='red',command=clear)
buttonsc.grid(row=6,column=2)

buttonsdivide=cstk.CTkButton(window,text='/',text_color='white',font=('arial',20,'bold'),text_color_disabled='orange',width=50,height=50,bg_color='black',fg_color='orange',command=lambda : click('/'))
buttonsdivide.grid(row=6,column=3,pady=10)


buttonsequal=cstk.CTkButton(window,text='=',text_color='white',font=('arial',20,'bold'),text_color_disabled='orange',width=450,height=50,bg_color='black',fg_color='green',command=lambda: equal())
buttonsequal.grid(row=7,column=0,columnspan=4,pady=10)


window.mainloop()


