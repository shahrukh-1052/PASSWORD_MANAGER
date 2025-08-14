# gui.py

import tkinter as tk
from tkinter import messagebox
import pyperclip 
from strong import generate_password, check_password_strength

#  UI setup
root = tk.Tk()
root.title("Z+ Password Manager")
root.geometry("450x300")
root.resizable(False, False)

# Password Output Field
password_var = tk.StringVar()

def generate_and_show():
    password = generate_password()
    password_var.set(password)
    status_label.config(text="Password generated successfully.", fg="green")

def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        pyperclip.copy(pwd)
        status_label.config(text="Password copied to clipboard.", fg="blue")
    else:
        status_label.config(text="Nothing to copy!", fg="red")

def check_strength():
    pwd = password_var.get()
    if not pwd:
        status_label.config(text="Enter or generate a password first.", fg="red")
        return

    strong, issues = check_password_strength(pwd)
    if strong:
        messagebox.showinfo("Strength Result", "Your password is strong!")
    else:
        messagebox.showwarning("Weak Password", "\n".join(issues))

# UI Components
tk.Label(root, text="Z+ Password Manager", font=("Helvetica", 16, "bold")).pack(pady=10)

tk.Entry(root, textvariable=password_var, font=("Helvetica", 14), width=35, justify='center').pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_and_show, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Check Strength", command=check_strength).pack(pady=5)

status_label = tk.Label(root, text="", fg="black")
status_label.pack(pady=10)

tk.Label(root, text="Created by Shahrukh", font=("Helvetica", 9)).pack(side="bottom", pady=5)

root.mainloop()
