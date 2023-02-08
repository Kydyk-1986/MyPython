import tkinter as tk
from tkinter import messagebox

def calculate():
    value = window.get()
    if value[-1] in '/+-*':
        value = value[:-1]
    window.delete(0, tk.END)
    try:
        window.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo("Error", 'Нужно вводить только цифры!')
    except ZeroDivisionError:
        messagebox.showinfo('Error', 'На ноль делить нельзя!')


def add_digit(digit):
    window.insert('end', digit)

def add_op(op):
    value = window.get()
    if value[-1] in '/+-*.':
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = window.get()
    window.delete(0, tk.END)
    window.insert(0, value+op)

def make_digit_buttom(digit):
    return tk.Button(text=digit, command=lambda: add_digit(digit))

def make_oper_button(op):
    return tk.Button(text=op, command=lambda: add_op(op))

def make_calc_buttom(op):
    return tk.Button(text=op, command=calculate)

win = tk.Tk()
win.title('Калькулятор')
win['bg'] = 'grey'
#win.geometry('240x280-50-50')
#win.minsize(240, 280)
#win.maxsize(400, 480)
window = tk.Entry(win, justify=tk.RIGHT)
window.grid(row=0, column=0, columnspan=3)

make_digit_buttom('1').grid(row=1, column=0, sticky='wens')
make_digit_buttom('2').grid(row=1, column=1, sticky='wens')
make_digit_buttom('3').grid(row=1, column=2, sticky='wens')
make_digit_buttom('4').grid(row=2, column=0, sticky='wens')
make_digit_buttom('5').grid(row=2, column=1, sticky='wens')
make_digit_buttom('6').grid(row=2, column=2, sticky='wens')
make_digit_buttom('7').grid(row=3, column=0, sticky='wens')
make_digit_buttom('8').grid(row=3, column=1, sticky='wens')
make_digit_buttom('9').grid(row=3, column=2, sticky='wens')
make_digit_buttom('0').grid(row=4, column=1, sticky='wens')

#lab = tk.Label(win, text='SomeText')
#lab.grid(row=0, column=0)

make_oper_button('/').grid(row=1, column=3, sticky='wens')
make_oper_button('+').grid(row=2, column=3, sticky='wens')
make_oper_button('-').grid(row=3, column=3, sticky='wens')
make_oper_button('*').grid(row=4, column=3, sticky='wens')

#make_oper_button('.').grid(row=4, column=2, sticky='wens')
make_calc_buttom('=').grid(row=4, column=0, sticky='wens')
clear = tk.Button(text='c', command=lambda: window.delete(0, tk.END))
clear.grid(row=4, column=2, sticky='wens')
win.mainloop()