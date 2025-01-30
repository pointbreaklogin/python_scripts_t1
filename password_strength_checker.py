import re
import tkinter as tk
from tkinter import ttk, messagebox

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

    #determine feedback
    if strength == 5:
        return "Very Strong", "#4CAF50"  #green
    elif strength >= 3:
        return "Strong", "#8BC34A"  #light Green
    elif strength >= 2:
        return "Moderate", "#FFC107"  #yellow
    else:
        return "Weak", "#F44336"  #red

def on_submit():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    strength, color = check_password_strength(password)
    strength_label.config(text=f"Strength: {strength}", bg=color)
    messagebox.showinfo("Password Strength", f"Your password is: {strength}")

#create the main window
root = tk.Tk()
root.title("Password Strength Checker")

#set the window size (width x height)
root.geometry("500x300")  #larger window
root.configure(bg="#F0F0F0")  #light gray background

#create a custom font
custom_font = ("Helvetica", 14)

#create a label
label = tk.Label(root, text="Enter your password:", font=custom_font, bg="#F0F0F0")
label.pack(pady=20)

#create an entry widget
entry = tk.Entry(root, show="*", font=custom_font, bd=2, relief="flat")
entry.pack(pady=10, ipadx=10, ipady=5)

#create a submit button
submit_button = tk.Button(
    root,
    text="Check Strength",
    command=on_submit,
    font=custom_font,
    bg="#2196F3",  #Blue background
    fg="white",    #White text
    bd=0,
    padx=20,
    pady=10
)
submit_button.pack(pady=20)

#create a label to display strength feedback
strength_label = tk.Label(
    root,
    text="Strength: None",
    font=custom_font,
    bg="#F0F0F0",
    fg="black"
)
strength_label.pack(pady=10)

#run the application
root.mainloop()
