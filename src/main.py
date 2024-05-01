from tkinter import *
import random
import string

root = Tk()
root.geometry("400x320")
root.title("Password Generator")

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

# Title label
title_label = Label(root, text="Select the strength and length of the password", font=("Helvetica", 12))
title_label.pack(pady=10)

# Frame to hold strength selection
strength_frame = Frame(root)
strength_frame.pack()

password_strength_var = StringVar()
password_strength_var.set("Poor")  # Default value
strength_label = Label(strength_frame, text="Strength:")
strength_label.pack(side=LEFT, padx=5)

poor_radio = Radiobutton(strength_frame, text="Poor", variable=password_strength_var, value="Poor")
poor_radio.pack(side=LEFT)
average_radio = Radiobutton(strength_frame, text="Average", variable=password_strength_var, value="Average")
average_radio.pack(side=LEFT)
advanced_radio = Radiobutton(strength_frame, text="Advanced", variable=password_strength_var, value="Advanced")
advanced_radio.pack(side=LEFT)

# Frame to hold length selection
length_frame = Frame(root)
length_frame.pack()

password_length_var = IntVar()
password_length_var.set(8)  # Default value
length_label = Label(length_frame, text="Length:")
length_label.pack(side=LEFT, padx=5)

length_spinbox = Spinbox(length_frame, from_=8, to_=16, textvariable=password_length_var, width=5)
length_spinbox.pack(side=LEFT)

# Generate password button
generate_button = Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Display generated password
password_var = StringVar()
password_label = Label(root, textvariable=password_var, font=("Helvetica", 12), wraplength=300)
password_label.pack()

root.mainloop()