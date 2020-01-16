from tkinter import *
import parser

obj = Tk()
obj.title('calculator')
disp = Entry(obj)
disp.grid(row=1, columnspan=6, sticky=W + E)

i = 0

def calcualtion():
    full = disp.get()
    try:
        a = parser.expr(full).compile()
        res = eval(a)
        clearall()
        disp.insert(0,res)

    except Exception as e:
        clearall()
        disp.insert(0,"err")


def fac():
    try:
        a = disp.get()
        if a.isdigit():
            b = int(a)
            res = 1
            for x in range(b, 0, -1):
                res = res*x
            clearall()
            disp.insert(0,res)
        else:
            clearall()
            disp.insert(0, "error")
    except Exception as e:
        clearall()
        disp.insert(0, "error")


def numbers(num):
    global i
    disp.insert(i, num)
    i+=1

def operations(ope):
    global i
    length = len(ope)
    disp.insert(i,ope)
    i+=length

def clearall():

    disp.delete(0,END)

def de():
    st = disp.get()
    newst = st[:-1]
    clearall()
    disp.insert(0,newst)


Button(obj, text="1",command = lambda : numbers(1)).grid(row=2, column=0)
Button(obj, text="2",command = lambda : numbers(2)).grid(row=2, column=1)
Button(obj, text="3",command = lambda : numbers(3)).grid(row=2, column=2)
Button(obj, text="4",command = lambda : numbers(4)).grid(row=3, column=0)
Button(obj, text="5",command = lambda : numbers(5)).grid(row=3, column=1)
Button(obj, text="6",command = lambda : numbers(6)).grid(row=3, column=2)
Button(obj, text="7",command = lambda : numbers(7)).grid(row=4, column=0)
Button(obj, text="8",command = lambda : numbers(8)).grid(row=4, column=1)
Button(obj, text="9",command = lambda : numbers(9)).grid(row=4, column=2)
Button(obj, text="clear",command = clearall).grid(row=5, column=0)
Button(obj, text="0", command = lambda : numbers(0)).grid(row=5, column=1)
Button(obj, text="=", command = calcualtion).grid(row=5, column=2)

Button(obj, text="+", command = lambda : numbers("+")).grid(row=2, column=3)
Button(obj, text="-", command = lambda : numbers("-")).grid(row=3, column=3)
Button(obj, text="*", command = lambda : numbers("*")).grid(row=4, column=3)
Button(obj, text="/", command = lambda : numbers("/")).grid(row=5, column=3)

Button(obj, text="pi", command = lambda : operations("*3.14")).grid(row=2, column=4)
Button(obj, text="%", command = lambda : operations("%")).grid(row=3, column=4)
Button(obj, text="(", command = lambda : operations("*(")).grid(row=4, column=4)
Button(obj, text="pwr", command = lambda : operations("**")).grid(row=5, column=4)

Button(obj, text="del", command =de).grid(row=2, column=5)
Button(obj, text="X!", command = fac).grid(row=3, column=5)
Button(obj, text=")", command = lambda : operations("*)")).grid(row=4, column=5)
Button(obj, text="sq", command = lambda : operations("**2")).grid(row=5, column=5)



obj.mainloop()