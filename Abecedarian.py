import tkinter as tk

def generate_abecedarian_series():
    # Get user input strings from entry widgets
    str1 = entry_str1.get()
    str2 = entry_str2.get()

    # Check if both input strings are non-empty
    if str1 and str2:
        result = ""
        # Iterate through each character in str1
        for char in str1:
            # Concatenate eack character of str1 with str2 and add a space
            result += char + str2 + " "
            # Update the result_label with the current result
            result_label.config(text=result)
    else:
        # Display an error message if eitheir input string is empty
        result_label.config(text= "Both input strings are required. ")

# Create the main window
root = tk.Tk()
root.title("Abecedarian series Generator")
root.geometry("600x500")

# Create an place widgets
# Label to instruct the user to enter a first string
label_str1 = tk.Label(root, text="Enter String 1:")
label_str1.pack(pady=5)

# Entry widget for user to input a first string
entry_str1 = tk.Entry(root)
entry_str1.pack(pady=5)

# Label to instruct the user to enter a second string
label_str2 = tk.Label(root, text="Enter String 2")
label_str2.pack(pady=5)
 
# Entry widget for user to input a first string
entry_str2 = tk.Entry(root)
entry_str2.pack(pady=5)

# Button to generate abecedarian series
generate_button = tk.Button(root, text="Generate abecedarian Series ", command=generate_abecedarian_series)
generate_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the tkinter event loop
root.mainloop()
