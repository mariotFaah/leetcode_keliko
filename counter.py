import tkinter as tk

def count_occurrences():
    # Get user input from the entry widget
    user_input = entry.get()

    # Count occurrences of each character in the input string 
    char_count = {} # Initialize an empty dictionnary to store the count of occurrences for each character
    # Iterate through each character in the user_input string 
    for char in user_input:
        # Check if the character is already in the dictionary, if not, default to 0
        current_count = char_count.get(char, 0)
        # Increment the count for the current character
        char_count[char] = char_count + 1

        # Display the result in the label
        result_label.config(text=str(char_count))

# Create the main window
root = tk.Tk()
root.title("Character Occurence Counter")

# Create and place widgets
label = tk.Label(root, text='Enter a message.')
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

count_button = tk.Button(root, text='Count Occurences', command=count_occurrences)
count_button.pack(pady=10)

result_label = tk.Label(root, text='')
result_label.pack(pady=10)

root.mainloop()