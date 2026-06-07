import tkinter as tk
from tkinter import messagebox
import math

# သင်္ချာတွက်ချက်မည့် Function
def calculate():
    try:
        expression = entry.get()
        # % သင်္ကေတကို Python အတွက် အစားထိုးခြင်း (ရှိခဲ့လျှင်)
        result = eval(expression)
        
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "သုည (0) ဖြင့် စား၍မရပါ!")
    except Exception:
        messagebox.showerror("Error", "ရိုက်ထည့်ထားသော ပုံသေနည်း မှားယွင်းနေပါသည်။")

# အထူး Function များ (Square Root, Sin, Cos)
def special_calc(operation):
    try:
        val = float(entry.get())
        if operation == "sqrt":
            if val < 0:
                raise ValueError("Minus ကိန်းများကို Square Root ရှာမရပါ!")
            res = math.sqrt(val)
        elif operation == "sin":
            # Degree အဖြစ်တွက်ရန် radians ပြောင်းပေးရသည်
            res = math.sin(math.radians(val))
        elif operation == "cos":
            res = math.cos(math.radians(val))
            
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(res))
    except ValueError as e:
        if "Square Root" in str(e):
            messagebox.showerror("Math Error", str(e))
        else:
            messagebox.showerror("Error", "ကျေးဇူးပြု၍ ဂဏန်းသီးသန့် အရင်ရိုက်ထည့်ပါ။")
    except Exception:
        messagebox.showerror("Error", "မှားယွင်းမှုတစ်ခု ရှိနေပါသည်။")

# ခလုတ်များနှိပ်လျှင် စာသားဝင်စေရန်
def press(num):
    entry.insert(tk.END, str(num))

# မျက်နှာပြင်ရှင်းလင်းရန်
def clear():
    entry.delete(0, tk.END)

# Window အား တည်ဆောက်ခြင်း
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("350x450")
root.configure(bg="#2c3e50")

# ရလဒ်ပြကွက် (Entry Box)
entry = tk.Entry(root, font=("Helvetica", 20), bd=10, insertwidth=4, width=14, borderwidth=5, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=15)

# ခလုတ်များ၏ ပုံစံသတ်မှတ်ချက်
btn_params = {'font': ("Helvetica", 14), 'fg': "#ffffff", 'bg': "#34495e", 'activebackground': "#1abc9c", 'width': 5, 'height': 2}

# Row 1: Advanced Functions & Clear
tk.Button(root, text="√", command=lambda: special_calc("sqrt"), **btn_params).grid(row=1, column=0, pady=5)
tk.Button(root, text="Sin", command=lambda: special_calc("sin"), **btn_params).grid(row=1, column=1, pady=5)
tk.Button(root, text="Cos", command=lambda: special_calc("cos"), **btn_params).grid(row=1, column=2, pady=5)
tk.Button(root, text="C", bg="#e74c3c", command=clear, font=("Helvetica", 14), fg="white", width=5, height=2).grid(row=1, column=3, pady=5)

# Row 2: 7, 8, 9, /
tk.Button(root, text="7", command=lambda: press(7), **btn_params).grid(row=2, column=0, pady=5)
tk.Button(root, text="8", command=lambda: press(8), **btn_params).grid(row=2, column=1, pady=5)
tk.Button(root, text="9", command=lambda: press(9), **btn_params).grid(row=2, column=2, pady=5)
tk.Button(root, text="÷", command=lambda: press("/"), **btn_params, bg="#d35400").grid(row=2, column=3, pady=5)

# Row 3: 4, 5, 6, *
tk.Button(root, text="4", command=lambda: press(4), **btn_params).grid(row=3, column=0, pady=5)
tk.Button(root, text="5", command=lambda: press(5), **btn_params).grid(row=3, column=1, pady=5)
tk.Button(root, text="6", command=lambda: press(6), **btn_params).grid(row=3, column=2, pady=5)
tk.Button(root, text="×", command=lambda: press("*"), **btn_params, bg="#d35400").grid(row=3, column=3, pady=5)

# Row 4: 1, 2, 3, -
tk.Button(root, text="1", command=lambda: press(1), **btn_params).grid(row=4, column=0, pady=5)
tk.Button(root, text="2", command=lambda: press(2), **btn_params).grid(row=4, column=1, pady=5)
tk.Button(root, text="3", command=lambda: press(3), **btn_params).grid(row=4, column=2, pady=5)
tk.Button(root, text="-", command=lambda: press("-"), **btn_params, bg="#d35400").grid(row=4, column=3, pady=5)

# Row 5: 0, ., =, +
tk.Button(root, text="0", command=lambda: press(0), **btn_params).grid(row=5, column=0, pady=5)
tk.Button(root, text=".", command=lambda: press("."), **btn_params).grid(row=5, column=1, pady=5)
tk.Button(root, text="=", command=calculate, bg="#2ecc71", font=("Helvetica", 14), fg="white", width=5, height=2).grid(row=5, column=2, pady=5)
tk.Button(root, text="+", command=lambda: press("+"), **btn_params, bg="#d35400").grid(row=5, column=3, pady=5)

root.mainloop()