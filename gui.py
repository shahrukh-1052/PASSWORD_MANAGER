import tkinter as tk
from tkinter import messagebox
import pyperclip
from strong import generate_password, check_password_strength

# Window setup
root = tk.Tk()
root.title("Z+ Password Manager")
root.geometry("450x300")
root.resizable(False, False)

password_var = tk.StringVar()

# Functions
def update_x(*_):
    if password_var.get():
        x_btn.pack(side="left", padx=2)
    else:
        x_btn.pack_forget()

def generate_and_show():
    password_var.set(generate_password())
    status_label.config(text="Password generated.", fg="green")

def copy_to_clipboard():
    if password_var.get():
        pyperclip.copy(password_var.get())
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

def clear_password():
    password_var.set("")
    status_label.config(text="Password cleared.", fg="red")

# UI Components
tk.Label(root, text="Z+ Password Manager", font=("Helvetica", 16, "bold")).pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=5)

tk.Entry(frame, textvariable=password_var, font=("Helvetica", 14), width=30, justify='center').pack(side="left")

x_btn = tk.Button(frame, text="X", command=clear_password, fg="white", bg="red", width=2)
password_var.trace_add("write", update_x)

tk.Button(root, text="Generate Password", command=generate_and_show, bg="#4CAF50", fg="white").pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)
tk.Button(root, text="Check Strength", command=check_strength).pack(pady=5)

status_label = tk.Label(root, text="", fg="black")
status_label.pack(pady=10)

tk.Label(root, text="Created by Shahrukh", font=("Helvetica", 9)).pack(side="bottom", pady=5)

root.mainloop()
