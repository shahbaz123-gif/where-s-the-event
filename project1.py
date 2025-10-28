import tkinter as tk
from tkinter import messagebox

def convert_inches_to_cm():
    try:
        # Get input from entry widget
        inches = float(entry.get())
        
        # Convert inches to centimeters (1 inch = 2.54 cm)
        centimeters = inches * 2.54
        
        # Update the result label
        result_label.config(text=f"{inches} inches = {centimeters:.2f} centimeters")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Inches to Centimeters Converter")
root.geometry("300x150")

# Create and place widgets
tk.Label(root, text="Enter length in inches:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, font=("Arial", 12), width=15)
entry.pack(pady=5)

convert_btn = tk.Button(root, text="Convert", font=("Arial", 12), 
                       command=convert_inches_to_cm, bg="lightblue")
convert_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Start the main loop
root.mainloop()