import tkinter as tk
import math

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def sqrt():
    global expression
    try:
        result = math.sqrt(float(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")

def power():
    global expression
    expression += "**"
    equation.set(expression)

def log():
    global expression
    try:
        result = math.log10(float(expression))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")

def sin():
    global expression
    try:
        result = math.sin(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")

def cos():
    global expression
    try:
        result = math.cos(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")

def tan():
    global expression
    try:
        result = math.tan(math.radians(float(expression)))
        equation.set(result)
        expression = str(result)
    except:
        equation.set("Error")


# Window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("360x500")
root.configure(bg="#1e1e1e")

equation = tk.StringVar()

# Display
entry = tk.Entry(root, textvariable=equation, font=("Arial",22),
                 bg="#252526", fg="white", bd=10, justify="right")
entry.grid(row=0, column=0, columnspan=5, pady=10)

# Button style
button_style = {
    "font": ("Arial",12),
    "width":6,
    "height":2,
    "bg":"#3c3c3c",
    "fg":"white",
    "bd":0
}

buttons = [
('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3), ('√',1,4),
('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3), ('^',2,4),
('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3), ('log',3,4),
('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3), ('C',4,4),
('sin',5,0), ('cos',5,1), ('tan',5,2)
]

for (text,row,col) in buttons:

    if text == "=":
        tk.Button(root,text=text,command=equal,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "C":
        tk.Button(root,text=text,command=clear,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "√":
        tk.Button(root,text=text,command=sqrt,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "^":
        tk.Button(root,text=text,command=power,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "log":
        tk.Button(root,text=text,command=log,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "sin":
        tk.Button(root,text=text,command=sin,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "cos":
        tk.Button(root,text=text,command=cos,**button_style).grid(row=row,column=col,padx=5,pady=5)

    elif text == "tan":
        tk.Button(root,text=text,command=tan,**button_style).grid(row=row,column=col,padx=5,pady=5)

    else:
        tk.Button(root,text=text,
        command=lambda t=text: press(t),
        **button_style).grid(row=row,column=col,padx=5,pady=5)

root.mainloop()

