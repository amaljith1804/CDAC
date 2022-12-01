from tkinter import *
root = Tk()
root.title("Sample calculator")

Ent1 = Entry(root,width=35)
Ent1.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def buttonck(n):
    a = Ent1.get()
    Ent1.delete(0,END)
    Ent1.insert(0,str(a)+str(n))

def buttoncl():
	Ent1.delete(0, END)

def add_button():
	first_number = Ent1.get()
	global f_num
	global math
	math = "addition"
	f_num = int(first_number)
	Ent1.delete(0, END)
def button_equal():
	second_number = Ent1.get()
	Ent1.delete(0, END)
	
	if math == "addition":
		Ent1.insert(0, f_num + int(second_number))

	if math == "subtraction":
		Ent1.insert(0, f_num - int(second_number))

	if math == "multiplication":
		Ent1.insert(0, f_num * int(second_number))

	if math == "division":
		Ent1.insert(0, f_num / int(second_number))
def sin():
    global f_num
    f_num = float(f_num)
    f_num = round(math.sin(math.radians(f_num)), 5)
    Ent1.set(float(f_num))
    f_num = str(f_num)
def button_subtract():
	first_number = Ent1.get()
	global f_num
	global math
	math = "subtraction"
	f_num = int(first_number)
	Ent1.delete(0, END)

def button_multiply():
	first_number = Ent1.get()
	global f_num
	global math
	math = "multiplication"
	f_num = int(first_number)
	Ent1.delete(0, END)

def button_divide():
	first_number = Ent1.get()
	global f_num
	global math
	math = "division"
	f_num = int(first_number)
	Ent1.delete(0, END)

button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: buttonck(1))
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: buttonck(2))
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: buttonck(3))
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: buttonck(4))
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: buttonck(5))
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: buttonck(6))
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: buttonck(7))
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: buttonck(8))
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: buttonck(9))
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: buttonck(0))
button_10 =Button(root,text="sine",padx=20, pady=20, command=lambda: sin)
button_add = Button(root, text="+", padx=20, pady=20, command=add_button)
button_equal = Button(root, text="=", padx=70, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=50, pady=20, command=buttoncl)

button_subtract = Button(root, text="-", padx=41, pady=20, command=button_subtract)
button_multiply = Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(root, text="/", padx=41, pady=20, command=button_divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_10.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=5, column=1, columnspan=2)
button_add.grid(row=5, column=0)
button_equal.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()