
import tkinter as tk

def on_button_click(value):#اين تابع براي وقتي استفاده ميشود که يک دکمه عدد يا عملگر فشرده ميشود مقدار دکمه به عنوان ورودي گرفته شده و به انتهاي متن فعلي ورودي افزوده ميشود.
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + str(value))

def clear_entry():#اين تابع براي پاک کردن محتواي ورودي متني است.
    entry.delete(0, tk.END)

def calculate_result():#اين تابع براي محاسبه نتيجه عبارت موجود در ورودي متن استفاده ميشود 
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

#  دراين بخش يک پنجره اصلي براي نمايش ماشين حساب ايجاد ميشودایجاد یک پنجره
window = tk.Tk()
window.title("Calculator")

# ایجاد یک ورودی متنی برای نمایش و وارد کردن اعداد
entry = tk.Entry(window, width=20, font=('Arial', 16), justify="right")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# يک ليست ازدکمه هاي ماشين حساب تعريف شده:تعریف اعداد و عملگرها
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+', 'C'
]

# ایجاد دکمه‌ها و قرار دادن آنها در شبکه
row_val = 1
col_val = 0

for button in buttons:
    # باشد'c'اگر دکمه مربوطه
    if button == 'C':
        tk.Button(window, text=button, width=5, height=2, command=clear_entry).grid(row=row_val, column=col_val)
    else:
        #اگر دکمه معمولي باشد   دکمه با اندازه و تابع مرتبط خود ايجاد ميشود 
        tk.Button(window, text=button, width=5, height=2,
                  command=lambda b=button: on_button_click(b) if b != '=' else calculate_result() if b == '=' else clear_entry()).grid(row=row_val, column=col_val)
    
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

#  پنحره را باز ميدارد تا رويداد ها انجام شوند:شروع حلقه رویدادها
window.mainloop()
