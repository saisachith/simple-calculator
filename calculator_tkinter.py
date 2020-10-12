from tkinter import *

root = Tk()
root.title("simple calculator")
# We use .title function to give a name to the page

e = Entry(root,width = 35,borderwidth = 3)
e.grid(row = 0,column = 0,columnspan = 3, padx = 10, pady = 10)

def button_add(number):
    # e.delete(0,END)
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0,END)

def button_add_num():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = int(first_number)
    e.delete(0,END)
def button_sub_num():
    first_number = e.get()
    global f_num
    global math
    math = 'substraction'
    f_num = int(first_number)
    e.delete(0, END)

def button_mul_num():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = int(first_number)
    e.delete(0, END)

def button_div_num():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = int(first_number)
    e.delete(0, END)

def button_ans():
    second_num = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, f_num + int(second_num))
    if math == 'substraction':
        e.insert(0, f_num - int(second_num))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_num))
    if math == 'division':
        e.insert(0, f_num / int(second_num))
# define buttons


button_1 = Button(root,text = '1',padx = 40,pady = 20,command = lambda : button_add(1))
button_2 = Button(root,text = '2',padx = 40,pady = 20,command = lambda : button_add(2))
button_3 = Button(root,text = '3',padx = 40,pady = 20,command = lambda : button_add(3))
button_4 = Button(root,text = '4',padx = 40,pady = 20,command = lambda : button_add(4))
button_5 = Button(root,text = '5',padx = 40,pady = 20,command = lambda : button_add(5))
button_6 = Button(root,text = '6',padx = 40,pady = 20,command = lambda : button_add(6))
button_7 = Button(root,text = '7',padx = 40,pady = 20,command = lambda : button_add(7))
button_8 = Button(root,text = '8',padx = 40,pady = 20,command = lambda : button_add(8))
button_9 = Button(root,text = '9',padx = 40,pady = 20,command = lambda : button_add(9))
button_0 = Button(root,text = '0',padx = 40,pady = 20,command = lambda : button_add(0))
button_addition = Button(root,text = '+',padx = 40,pady = 20,command = button_add_num)
button_equal = Button(root,text = '=',padx = 91,pady = 20,command = button_ans)
button_clear = Button(root,text = 'clear',padx = 79,pady = 20,command = button_clear)

button_substraction = Button(root,text = '-',padx = 40,pady = 20,command = button_sub_num)
button_multiplication = Button(root,text = '*',padx = 40,pady = 20,command = button_mul_num)
button_division = Button(root,text = '/',padx = 40,pady = 20,command = button_div_num)

# put the button on the screen

button_1.grid(row = 3,column = 0)
button_2.grid(row = 3,column = 1)
button_3.grid(row = 3,column = 2)

button_4.grid(row = 2,column = 0)
button_5.grid(row = 2,column = 1)
button_6.grid(row = 2,column = 2)

button_7.grid(row = 1,column = 0)
button_8.grid(row = 1,column = 1)
button_9.grid(row = 1,column = 2)

button_0.grid(row = 4,column = 0)
button_equal.grid(row = 5,column =1,columnspan = 2 )
button_addition.grid(row = 5,column =0 )
button_clear.grid(row =4 ,column =1 ,columnspan = 2)

button_substraction.grid(row = 6,column =0 )
button_multiplication.grid(row = 6,column =1)
button_division.grid(row = 6,column =2)



root.mainloop()

