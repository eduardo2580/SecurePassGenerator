import subprocess
import sys
import importlib
import os
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import random
import string

# Path to the requirements.txt file
requirements_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../requirements.txt'))

# List of required packages from requirements.txt
def get_required_packages():
    with open(requirements_path, 'r') as file:
        packages = [line.strip() for line in file if line.strip()]
    return packages

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def check_and_install_packages():
    packages = get_required_packages()
    for package in packages:
        try:
            importlib.import_module(package.split('==')[0])
        except ImportError:
            print(f"Package '{package}' not found. Installing...")
            install_package(package)
        else:
            print(f"Package '{package}' is already installed.")

# Perform package checks and installations
check_and_install_packages()

# Main application code starts here

# Function to generate password based on selected strength
def generate_password():
    password_length = password_length_var.get()
    if password_strength_var.get() == "Poor":
        password_chars = string.ascii_letters + string.digits
    elif password_strength_var.get() == "Average":
        password_chars = string.ascii_letters + string.digits + string.punctuation
    else:
        password_chars = string.ascii_letters + string.digits + string.punctuation + " "
    password = ''.join(random.choice(password_chars) for _ in range(password_length))
    password_var.set(password)

# Function to copy the generated password to the clipboard
def copy_to_clipboard():
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(password_var.get())  # Append the password to the clipboard
    root.update()  # Update the clipboard

# Create a themed Tkinter root window
root = ThemedTk(theme="arc")  # You can choose other themes like "breeze", "clearlooks", etc.
root.geometry("400x320")
root.title("Password Generator")

# Title label
title_label = ttk.Label(root, text="Select the strength and length of the password", font=("Arial", 12))
title_label.pack(pady=10)

# Frame to hold strength selection
strength_frame = ttk.Frame(root)
strength_frame.pack(pady=15)

password_strength_var = tk.StringVar()
password_strength_var.set("Poor")  # Default value
strength_label = ttk.Label(strength_frame, text="Strength:", font=("Arial", 10))
strength_label.pack(side=tk.LEFT, padx=5)

poor_radio = ttk.Radiobutton(strength_frame, text="Poor", variable=password_strength_var, value="Poor")
poor_radio.pack(side=tk.LEFT, padx=10)
average_radio = ttk.Radiobutton(strength_frame, text="Average", variable=password_strength_var, value="Average")
average_radio.pack(side=tk.LEFT, padx=10)
advanced_radio = ttk.Radiobutton(strength_frame, text="Advanced", variable=password_strength_var, value="Advanced")
advanced_radio.pack(side=tk.LEFT, padx=10)

# Frame to hold length selection
length_frame = ttk.Frame(root)
length_frame.pack(pady=15)

password_length_var = tk.IntVar()
password_length_var.set(8)  # Default value
length_label = ttk.Label(length_frame, text="Length:", font=("Arial", 10))
length_label.pack(side=tk.LEFT, padx=5)

length_spinbox = ttk.Spinbox(length_frame, from_=8, to_=16, textvariable=password_length_var, width=5)
length_spinbox.pack(side=tk.LEFT)

# Generate password button
generate_button = ttk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=15)

# Display generated password
password_var = tk.StringVar()
password_label = ttk.Label(root, textvariable=password_var, font=("Arial", 12), wraplength=300, relief="sunken", padding=10)
password_label.pack(pady=10)

# Copy password button
copy_button = ttk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

root.mainloop()
