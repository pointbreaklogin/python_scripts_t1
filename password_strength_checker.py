import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    #deefine criteria
    length_criteria = len(password) >= 8
    digit_criteria = bool(re.search(r'\d', password))
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    #calculate strength
    strength = 0
    if length_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    # feedback
    if strength == 5:
        return "Very Strong"
    elif strength >= 3:
        return "Strong"
    elif strength >= 2:
        return "Moderate"
    else:
        return "Weak"

def on_submit():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength = check_password_strength(password)
    messagebox.showinfo("Password Strength", f"Your password is: {strength}")

#create the main window
root = tk.Tk()
root.title("Password Strength Checker")

#set the window size (width x height)
root.geometry("400x200")  # Adjust the size as needed

#create a label
label = tk.Label(root, text="Enter your password:", font=("Arial", 14))
label.pack(pady=20)

#create an entry widget
entry = tk.Entry(root, show="*", font=("Arial", 12))
entry.pack(pady=10)

#create a submit button
submit_button = tk.Button(root, text="Check Strength", command=on_submit, font=("Arial", 12))
submit_button.pack(pady=20)

#run the application
root.mainloop()
