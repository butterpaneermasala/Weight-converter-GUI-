import tkinter as tk

def convert_weight():
    try:
        # Get the values from the entry widget and option menus
        weight = float(entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()

        if weight < 0:
            result_var.set("Please enter a-non negative weight")


        else:
            conversion_factors = {
            "kg_to_lb": 2.20462,
            "lb_to_kg": 0.453592,
            "kg_to_g": 1000,
            "g_to_kg": 0.001,
            "lb_to_g": 453.592,
            "g_to_lb": 0.00220462,
            "oz_to_g": 28.3495,
            "g_to_oz": 0.03527396,
            "kg_to_oz": 35.27396,
            "lb_to_oz": 16,
            "kg_to_kg": 1,
            "lb_to_lb": 1,
            "g_to_g": 1,
            "oz_to_oz": 1
        }

            # Perform conversion
            result = weight * conversion_factors[f"{from_unit}_to_{to_unit}"]

            # Update the result label
            result_var.set(f"{weight} {from_unit} is {result:.2f} {to_unit}")
    except ValueError:
        result_var.set("Please enter a valid number")


window = tk.Tk()
window.title("Weight Converter")
window.config(background='#6497D6')


label = tk.Label(window, text="Enter Weight:", font=("Cambria Math", 16), bg="#6497D6")
label.grid(row=0, column=0, pady=10)

entry = tk.Entry(window)
entry.grid(row=0, column=1, pady=10)

from_unit_var = tk.StringVar()
from_unit_var.set("kg")
from_unit_menu = tk.OptionMenu(window, from_unit_var, "kg", "lb", "g", "oz")
from_unit_menu.config(bg='#6497D6', font=("Cambria", 12), width=5)
from_unit_menu["menu"].config(bg="#B3E7ED")
from_unit_menu.grid(row=0, column=2, pady=10)

to_unit_var = tk.StringVar()
to_unit_var.set("lb")
to_unit_menu = tk.OptionMenu(window, to_unit_var, "kg", "lb", "g", "oz")
to_unit_menu.config(bg='#6497D6', font=("Cambria", 12), width=5)
to_unit_menu["menu"].config(bg="#B3E7ED")
to_unit_menu.grid(row=0, column=3, pady=10)

convert_button = tk.Button(window, text="Convert", bg="#6497D6", command=convert_weight, font=("Cambria", 14))
convert_button.grid(row=1, column=0, columnspan=4, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(window, textvariable=result_var, font=("Cambria Math", 12), background='#6497D6')
result_label.grid(row=2, column=0, columnspan=4, pady=10)

window.mainloop()
