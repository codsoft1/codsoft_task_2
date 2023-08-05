import tkinter as tk

def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            label_result.config(text="Cannot divide by zero!")
        else:
            result = num1 / num2
            label_result.config(text=f"Result: {result}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input fields
label_num1 = tk.Label(root, text="Enter number 1:")
label_num1.pack()
entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter number 2:")
label_num2.pack()
entry_num2 = tk.Entry(root)
entry_num2.pack()

# Create buttons for arithmetic operations
btn_add = tk.Button(root, text="Add", command=add)
btn_add.pack()

btn_subtract = tk.Button(root, text="Subtract", command=subtract)
btn_subtract.pack()

btn_multiply = tk.Button(root, text="Multiply", command=multiply)
btn_multiply.pack()

btn_divide = tk.Button(root, text="Divide", command=divide)
btn_divide.pack()

# Create label to display the result
label_result = tk.Label(root, text="Result: ")
label_result.pack()

root.mainloop()
