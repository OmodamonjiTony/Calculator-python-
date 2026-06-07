import tkinter as tk
from tkinter import messagebox
import math

# သင်္ချာတွက်ချက်မည့် Function
def calculate():
    try:
        expression = entry.get()
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

# ခလုတ်များအတွက် ပုံသေစတိုင်လ်များ
FONT = ("Helvetica", 14)
W, H = 5, 2
BG_NUM = "#34495e"    # ဂဏန်းခလုတ်အရောင်
BG_OP = "#d35400"     # ပေါင်း/နှုတ်/မြှောက်/စား ခလုတ်အရောင်
BG_C = "#e74c3c"      # Clear ခလုတ်အရောင်
BG_EQUAL = "#2ecc71"  # ညီမျှခြင်းခလုတ်အရောင်
FG_COLOR = "#ffffff"  # စာလုံးအရောင်

# Row 1: Advanced Functions & Clear
tk.Button(root, text="√", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: special_calc("sqrt")).grid(row=1, column=0, pady=5)
tk.Button(root, text="Sin", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: special_calc("sin")).grid(row=1, column=1, pady=5)
tk.Button(root, text="Cos", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: special_calc("cos")).grid(row=1, column=2, pady=5)
tk.Button(root, text="C", font=FONT, fg=FG_COLOR, bg=BG_C, width=W, height=H, command=clear).grid(row=1, column=3, pady=5)

# Row 2: 7, 8, 9, /
tk.Button(root, text="7", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(7)).grid(row=2, column=0, pady=5)
tk.Button(root, text="8", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(8)).grid(row=2, column=1, pady=5)
tk.Button(root, text="9", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(9)).grid(row=2, column=2, pady=5)
tk.Button(root, text="÷", font=FONT, fg=FG_COLOR, bg=BG_OP, width=W, height=H, command=lambda: press("/")).grid(row=2, column=3, pady=5)

# Row 3: 4, 5, 6, *
tk.Button(root, text="4", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(4)).grid(row=3, column=0, pady=5)
tk.Button(root, text="5", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(5)).grid(row=3, column=1, pady=5)
tk.Button(root, text="6", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(6)).grid(row=3, column=2, pady=5)
tk.Button(root, text="×", font=FONT, fg=FG_COLOR, bg=BG_OP, width=W, height=H, command=lambda: press("*")).grid(row=3, column=3, pady=5)

# Row 4: 1, 2, 3, -
tk.Button(root, text="1", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(1)).grid(row=4, column=0, pady=5)
tk.Button(root, text="2", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(2)).grid(row=4, column=1, pady=5)
tk.Button(root, text="3", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(3)).grid(row=4, column=2, pady=5)
tk.Button(root, text="-", font=FONT, fg=FG_COLOR, bg=BG_OP, width=W, height=H, command=lambda: press("-")).grid(row=4, column=3, pady=5)

# Row 5: 0, ., =, +
tk.Button(root, text="0", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(0)).grid(row=5, column=0, pady=5)
tk.Button(root, text=".", font=FONT, fg=FG_COLOR, bg=BG_NUM, width=W, height=H, command=lambda: press(".")).grid(row=5, column=1, pady=5)
tk.Button(root, text="=", font=FONT, fg=FG_COLOR, bg=BG_EQUAL, width=W, height=H, command=calculate).grid(row=5, column=2, pady=5)
tk.Button(root, text="+", font=FONT, fg=FG_COLOR, bg=BG_OP, width=W, height=H, command=lambda: press("+")).grid(row=5, column=3, pady=5)

root.mainloop()