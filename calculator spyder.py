import tkinter as tk

# Global variable to store the text entered into the calculator field
field_text=""

# Function to add characters to the calculator field
def add_to_field(sth):
    global field_text
    field_text = field_text+str(sth)
    field.delete("1.0", "end")
    field.insert("1.0", field_text)

# Function to evaluate the expression in the calculator field and display the result
def calculate():
    global field_text
    result = str(eval(field_text))
    field.delete("1.0", "end")
    field.insert("1.0", result)
    
# Function to clear the calculator field
def clear():
    global field_text
    field_text=""
    field.delete("1.0", "end")

# Create the main window
window=tk.Tk()
window.title("Calculator")
window.geometry("290x500")

# Create the calculator field (Text widget)
field=tk.Text(window, height=2, width=21, font=("Times New Roman",20))
field.place(x=1, y=1, width=285, height=90)

#####################################################
# Number Buttons
#####################################################
btn_1=tk.Button(window, text="1", command=lambda: add_to_field(1), width=5, font=("Times New Roman",14))
btn_1.place(x= 2, y = 260, width = 70, height = 70)

btn_2=tk.Button(window, text="2", command=lambda: add_to_field(2), width=5, font=("Times New Roman",14))
btn_2.place(x= 73, y = 260, width = 70, height = 70)

btn_3=tk.Button(window, text="3", command=lambda: add_to_field(3), width=5, font=("Times New Roman",14))
btn_3.place(x= 145, y = 260, width = 70, height = 70)

btn_4=tk.Button(window, text="4", command=lambda: add_to_field(4), width=5, font=("Times New Roman",14))
btn_4.place(x= 2, y = 180, width = 70, height = 70)

btn_5=tk.Button(window, text="5", command=lambda: add_to_field(5), width=5, font=("Times New Roman",14))
btn_5.place(x= 73, y = 180, width = 70, height = 70)

btn_6=tk.Button(window, text="6", command=lambda: add_to_field(6), width=5, font=("Times New Roman",14))
btn_6.place(x= 145, y = 180, width = 70, height = 70)

btn_7=tk.Button(window, text="7", command=lambda: add_to_field(7), width=5, font=("Times New Roman",14))
btn_7.place(x= 2, y = 100, width = 70, height = 70)

btn_8=tk.Button(window, text="8", command=lambda: add_to_field(8), width=5, font=("Times New Roman",14))
btn_8.place(x= 73, y = 100, width = 70, height = 70)

btn_9=tk.Button(window, text="9", command=lambda: add_to_field(9), width=5, font=("Times New Roman",14))
btn_9.place(x= 145, y = 100, width = 70, height = 70)

btn_0=tk.Button(window, text="0", command=lambda: add_to_field(0), width=5, font=("Times New Roman",14))
btn_0.place(x= 73, y = 340, width = 70, height = 70)

#####################################################
# Operation Buttons
#####################################################
btn_plus=tk.Button(window, text="+", command=lambda: add_to_field("+"), width=5, font=("Times New Roman",14))
btn_plus.place(x= 217, y = 340, width = 70, height = 70)

btn_minus=tk.Button(window, text="-", command=lambda: add_to_field("-"), width=5, font=("Times New Roman",14))
btn_minus.place(x= 217, y = 260, width = 70, height = 70)

btn_times=tk.Button(window, text="x", command=lambda: add_to_field("*"), width=5, font=("Times New Roman",14))
btn_times.place(x= 217, y = 180, width = 70, height = 70)

btn_division=tk.Button(window, text="/", command=lambda: add_to_field("/"), width=5, font=("Times New Roman",14))
btn_division.place(x= 217, y = 100, width = 70, height = 70)

btn_clear=tk.Button(window, text="clear", command=lambda: clear(), width=5, font=("Times New Roman",14))
btn_clear.place(x= 145, y = 340, width = 70, height = 70)

btn_decimal=tk.Button(window, text=".", command=lambda: add_to_field("."), width=5, font=("Times New Roman",14))
btn_decimal.place(x= 2, y = 340, width = 70, height = 70)

btn_equal=tk.Button(window, text="=", command=lambda: calculate(), width=13, font=("Times New Roman",14))
btn_equal.place(x= 2, y = 420, width = 285, height = 70)


# Start the event loop
window.mainloop()
