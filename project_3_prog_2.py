import tkinter as tk

def on_button_calc_apple():
    label_title.grid_forget()
    label_subtitle_1.grid_forget()
    label_subtitle_2.grid_forget()
    button_app.grid_forget()

    introd_app.grid(row=0, column=0, columnspan=2, pady=5, sticky=tk.W)
    amount_label.grid(row=1, column=0, columnspan=2, pady=5, sticky=tk.W)
    amount_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky=tk.W)
    amount_entry.insert(0,"0.00")
    cost_app_label.grid(row=2, column=0, columnspan=2, pady=5, sticky=tk.W)
    cost_app_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky=tk.W)
    cost_app_entry.insert(0,"25.00")
    total_amount_app_label.grid(row=4, column=0, columnspan=2, pady=5, sticky=tk.W)
    button_calc_apple.grid(row=6, column=1, columnspan=2, pady=5, sticky=tk.W)
    button_exit.grid(row=7, column=1, columnspan=2, pady=5, sticky=tk.W)

def apple_calculation():
    total_amount_value = float(amount_entry.get()) / float(cost_app_entry.get())
    round_total_amount = round(total_amount_value)
    total_amount_app_label.config(text = f"Total Apples: {round_total_amount}")
    total_amount_app_label.grid(row=5, column=1, columnspan=2, pady=5, sticky=tk.W)

def close_window():
    window.destroy()


# Main window
window = tk.Tk()
window.title("VS Browser")

window.geometry("450x250")

# Introductory
label_title = tk.Label(window, text="Thome Yorke's Apple Calculator!")
label_title.grid(row=0, column=0, columnspan=2, pady=10)

label_subtitle_1 = tk.Label(window, text="Do you want to know how many apples fit your budget?")
label_subtitle_1.grid(row=2, column=0, columnspan=2, pady=10)

label_subtitle_2 = tk.Label(window, text="Don't worry, we got you covered!")
label_subtitle_2.grid(row=3, column=0, columnspan=2, pady=10)

button_app = tk.Button(window, text="Apple Calculator", command=on_button_calc_apple) 
button_app.grid(row=4, column=0, columnspan=2, pady=10)

# Apple Calculator
introd_app = tk.Label(window, text="Good day! Just enter your budget below, and we'll do the calculations for you.")
amount_label = tk.Label(window, text="Amount/Budgetc(PHP): ")
amount_entry = tk.Entry(window)
cost_app_label = tk.Label(window, text="Apple cost (PHP): ")
cost_app_entry = tk.Entry(window)
total_amount_app_label = tk.Label(window, text="")
button_calc_apple = tk.Button(window, text="Calculate", command=apple_calculation)
button_exit = tk.Button(window, text="Exit", command=close_window)

window.mainloop()