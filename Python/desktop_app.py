import tkinter as tk
from tkinter import filedialog, messagebox
import os
from encrypt_html import encrypt_html


def select_input_file():
    file_path = filedialog.askopenfilename(
        title="Select HTML file",
        filetypes=[("HTML files", "*.html"), ("All files", "*.*")]
    )
    if file_path:
        input_file_var.set(file_path)


def select_output_file():
    file_path = filedialog.asksaveasfilename(
        title="Save Encrypted Output",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    if file_path:
        output_file_var.set(file_path)


def perform_encryption():
    input_file = input_file_var.get()
    output_file = output_file_var.get()
    password = password_var.get()

    if not os.path.isfile(input_file):
        messagebox.showerror("Error", "Invalid input file.")
        return
    if not password:
        messagebox.showerror("Error", "Password cannot be empty.")
        return

    try:
        with open(input_file, "r", encoding="utf-8") as f:
            html_content = f.read()

        encrypted = encrypt_html(html_content, password)

        # Save to output file
        if output_file:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(encrypted)
            messagebox.showinfo("Success", "File encrypted successfully!")

        # Optionally display in the text box as well
        encrypted_textbox.delete("1.0", tk.END)
        encrypted_textbox.insert(tk.END, encrypted)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("HTML Encryptor")

# Variables
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()
password_var = tk.StringVar()

# UI Layout
frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

tk.Label(frame, text="Input HTML File:").grid(row=0, column=0, sticky="e")
tk.Entry(frame, textvariable=input_file_var,
         width=50).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Browse", command=select_input_file).grid(
    row=0, column=2, padx=5)

tk.Label(frame, text="Output Encrypted File:").grid(
    row=1, column=0, sticky="e")
tk.Entry(frame, textvariable=output_file_var,
         width=50).grid(row=1, column=1, padx=5)
tk.Button(frame, text="Browse", command=select_output_file).grid(
    row=1, column=2, padx=5)

tk.Label(frame, text="Password:").grid(row=2, column=0, sticky="e")
tk.Entry(frame, textvariable=password_var, width=50,
         show="*").grid(row=2, column=1, padx=5)

tk.Button(frame, text="Encrypt", command=perform_encryption,
          bg="green", fg="white").grid(row=3, column=1, pady=10)

# A text box to display encrypted output
encrypted_textbox = tk.Text(frame, width=60, height=10)
encrypted_textbox.grid(row=4, column=0, columnspan=3, pady=5)

root.mainloop()
