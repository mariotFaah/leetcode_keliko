import tkinter as tk
from tkinter import messagebox

def calculate():
        try:
            # Attempt to retrieve the values entered in the entry fields and convert them to integers
            num1 = int(entry_num1.get())
            num2 = int(entry_num2.get())

            # Calculate the GCD using the previously defined gcd function 
            result = gcd(num1, num2)

            # Calculate the LCM using the formula : LCM = (num * num2)/ GCD
            lcm = (num1 * num2) / result

            # Display the result in a message box, including both the GCD and LCM
            messagebox.showinfo("Result", f"The GCD of{num1} and {num2} is {result} \n "f"The LCM of {num1} and {num2} is {lcm}")
        except ValueError:
            # If the user entered invalid input (e.g , non-integer values), display an error message
            messagebox.showerror("Error", "Please enter a valid integers for both numbers. ")
def gcd(a,b):
    # Continuously loop until b becomes zero
    while b != 0:
        # Store the current value of b in a temporary variable c
        c = b
        # Update the value of b to be the remainder of a divided by the current value of b
        b = a % b
        # Assign the original value of b (stored in c) to a, effectively swapping the values
        a = c
        # When b becomes zero , return the current value of a, which is th GCD
        return a
    
    

root = tk.Tk()
root.title("GCD and LCM Calculator")
bold_font = ("Arial", 20, "bold")
title_label = tk.Label(root, text='GCD & LCM Calculator', bg='white', fg='Green', font=bold_font)
title_label.pack()

# Creating labels and entry fields
label_num1 = tk.Label(root, text='Enter firs number: ')
label_num1.pack(padx=5, pady=5)

entry_num1 =tk.Entry(root)
entry_num1.pack(padx=5, pady=5)

label_num2 = tk.Label(root, text='Enter firs number: ')
label_num1.pack(padx=5, pady=5)

entry_num2 =tk.Entry(root)
entry_num2.pack(padx=5, pady=5)

# Creating a button to a trigger calculation
calculate_button = tk.Button(root, text='Calculate GCD and LCM', command=calculate)
calculate_button.pack(padx=5, pady=5)

root.mainloop()
