from tkinter import *

 
root = Tk()
root.title("Simple Calculator")

screan= Entry(root, width=40, borderwidth=5 )
screan.grid(column=0, columnspan=4, row=0, )


# functions

def buttons_click(number):
    current=screan.get()
    screan.delete(0, END)
    screan.insert(0, str(current)+ str(number))


def buttons_neg_bos():
    current=(float(screan.get())*-1)
    screan.delete(0, END)
    screan.insert(0, str(current))


def button_clear():
    screan.delete(0,END)


def button_equal():

	second_number = screan.get()
	screan.delete(0, END)

	if math == "addition":
		screan.insert(0, first_num + float(second_number))

	if math == "subtraction":
		screan.insert(0, first_num - float(second_number))

	if math == "multiplication":
		screan.insert(0, first_num * float(second_number))

	if math == "division":
		screan.insert(0, first_num / float(second_number))
		
	if math == "Remainder":
		screan.insert(0, first_num % float(second_number))

		
		

def button_add():
	first_number = screan.get()
	global first_num
	global math
	math = "addition"
	first_num = float(first_number)
	screan.delete(0, END)

def button_subtract():
	first_number = screan.get()
	global first_num
	global math
	math = "subtraction"
	first_num = float(first_number)
	screan.delete(0, END)

def button_multipli():
	first_number = screan.get()
	global first_num
	global math
	math = "multiplication"
	first_num = float(first_number)
	screan.delete(0, END)

def button_div():
	first_number = screan.get()
	global first_num
	global math
	math = "division"
	first_num = float(first_number)
	screan.delete(0, END)

def button_rem():
	first_number = screan.get()
	global first_num
	global math
	math = "Remainder"
	first_num = float(first_number)
	screan.delete(0, END)
	

# buttons defind

# numbers
button_1= Button(root, text = '1', command = lambda: buttons_click(1),width=6,height=3, fg= 'white', bg= 'black', font=40)    
button_2= Button(root, text = '2', command = lambda: buttons_click(2),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_3= Button(root, text = '3', command = lambda: buttons_click(3),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_4= Button(root, text = '4', command = lambda: buttons_click(4),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_5= Button(root, text = '5', command = lambda: buttons_click(5),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_6= Button(root, text = '6', command = lambda: buttons_click(6),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_7= Button(root, text = '7', command = lambda: buttons_click(7),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_8= Button(root, text = '8', command = lambda: buttons_click(8),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_9= Button(root, text = '9', command = lambda: buttons_click(9),width=6,height=3, fg= 'white', bg= 'black', font=40)  
button_0= Button(root, text = '0', command = lambda: buttons_click(0),width=13,height=3, fg= 'white', bg= 'black', font=40) 
button_poin= Button(root, text = '.', command = lambda: buttons_click('.'),width=6,height=3, fg= 'white', bg= 'black', font=40 ) 

# condetions
button_bls= Button(root, text = '+', command = button_add ,width=6,height=3, fg= 'white', bg= 'orange', font=45) 
button_myn= Button(root, text = '-', command = button_subtract ,width=6,height=3,fg= 'white', bg= 'orange', font=45) 
button_div= Button(root, text = '/', command = button_div ,width=6,height=3, fg= 'white', bg= 'orange', font=45) 
button_ast= Button(root, text = '*', command = button_multipli ,width=6,height=3, fg= 'white', bg= 'orange', font=45) 
button_eq= Button(root, text = '=', command = button_equal ,width=6,height=3, fg= 'white', bg= 'orange', font=45) 
button_clear= Button(root, text = 'clear', command = button_clear, width=6,height=3, fg= 'black', bg= 'gray', font=40) 
button_mod= Button(root, text = '%', command = button_rem ,width=6,height=3, fg= 'black', bg= 'gray', font=40) 
button_neg= Button(root, text = '+/-', command = buttons_neg_bos ,width=6,height=3, fg= 'black', bg= 'gray', font=40) 


# buttons griding

button_clear.grid(column=0,row=1)
button_neg.grid(column=1,row=1)
button_mod.grid(column=2,row=1)
button_div.grid(column=3,row=1)
button_7.grid(column=0,row=2)
button_8.grid(column=1,row=2)
button_9.grid(column=2,row=2)
button_ast.grid(column=3,row=2)
button_4.grid(column=0,row=3)
button_5.grid(column=1,row=3)
button_6.grid(column=2,row=3)
button_myn.grid(column=3,row=3)
button_1.grid(column=0,row=4)
button_2.grid(column=1,row=4)
button_3.grid(column=2,row=4)
button_bls.grid(column=3,row=4)
button_0.grid(column=0,row=5,columnspan=2)
button_poin.grid(column=2,row=5)
button_eq.grid(column=3,row=5)


root.mainloop()