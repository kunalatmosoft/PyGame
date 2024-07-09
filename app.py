import tkinter as tk
from tkinter import messagebox
import math

def calculate():
    try:
        expression = entry.get()
        # Replace function names with math module equivalents
        expression = expression.replace("sin", "math.sin")
        expression = expression.replace("cos", "math.cos")
        expression = expression.replace("tan", "math.tan")
        expression = expression.replace("sqrt", "math.sqrt")
        expression = expression.replace("log", "math.log")
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input")

app = tk.Tk()
app.title("Scientific Calculator")

# Set window icon
""" app.iconbitmap("assets/icon.ico") """

entry = tk.Entry(app, width=40, borderwidth=5)
entry.grid(row=0, column=0, columnspan=5)

button_1 = tk.Button(app, text="1", padx=20, pady=20, command=lambda: entry.insert(tk.END, "1"))
button_2 = tk.Button(app, text="2", padx=20, pady=20, command=lambda: entry.insert(tk.END, "2"))
button_3 = tk.Button(app, text="3", padx=20, pady=20, command=lambda: entry.insert(tk.END, "3"))
button_4 = tk.Button(app, text="4", padx=20, pady=20, command=lambda: entry.insert(tk.END, "4"))
button_5 = tk.Button(app, text="5", padx=20, pady=20, command=lambda: entry.insert(tk.END, "5"))
button_6 = tk.Button(app, text="6", padx=20, pady=20, command=lambda: entry.insert(tk.END, "6"))
button_7 = tk.Button(app, text="7", padx=20, pady=20, command=lambda: entry.insert(tk.END, "7"))
button_8 = tk.Button(app, text="8", padx=20, pady=20, command=lambda: entry.insert(tk.END, "8"))
button_9 = tk.Button(app, text="9", padx=20, pady=20, command=lambda: entry.insert(tk.END, "9"))
button_0 = tk.Button(app, text="0", padx=20, pady=20, command=lambda: entry.insert(tk.END, "0"))

button_add = tk.Button(app, text="+", padx=20, pady=20, command=lambda: entry.insert(tk.END, "+"))
button_subtract = tk.Button(app, text="-", padx=20, pady=20, command=lambda: entry.insert(tk.END, "-"))
button_multiply = tk.Button(app, text="*", padx=20, pady=20, command=lambda: entry.insert(tk.END, "*"))
button_divide = tk.Button(app, text="/", padx=20, pady=20, command=lambda: entry.insert(tk.END, "/"))
button_equal = tk.Button(app, text="=", padx=20, pady=20, command=calculate)
button_clear = tk.Button(app, text="C", padx=20, pady=20, command=lambda: entry.delete(0, tk.END))

button_sin = tk.Button(app, text="sin", padx=20, pady=20, command=lambda: entry.insert(tk.END, "sin("))
button_cos = tk.Button(app, text="cos", padx=20, pady=20, command=lambda: entry.insert(tk.END, "cos("))
button_tan = tk.Button(app, text="tan", padx=20, pady=20, command=lambda: entry.insert(tk.END, "tan("))
button_sqrt = tk.Button(app, text="sqrt", padx=20, pady=20, command=lambda: entry.insert(tk.END, "sqrt("))
button_log = tk.Button(app, text="log", padx=20, pady=20, command=lambda: entry.insert(tk.END, "log("))

button_left_paren = tk.Button(app, text="(", padx=20, pady=20, command=lambda: entry.insert(tk.END, "("))
button_right_paren = tk.Button(app, text=")", padx=20, pady=20, command=lambda: entry.insert(tk.END, ")"))

# Arrange buttons in a grid
button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_add.grid(row=1, column=3)
button_sin.grid(row=1, column=4)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)
button_cos.grid(row=2, column=4)

button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button_tan.grid(row=3, column=4)

button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
button_equal.grid(row=4, column=2)
button_divide.grid(row=4, column=3)
button_sqrt.grid(row=4, column=4)

button_log.grid(row=5, column=0)
button_left_paren.grid(row=5, column=1)
button_right_paren.grid(row=5, column=2)

app.mainloop()
