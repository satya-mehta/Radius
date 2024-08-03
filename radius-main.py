import tkinter as tk
from tkinter import messagebox
import json


def save_student():
    # Gather student information from entries
    student = {
        'Name': name_entry.get(),
        'Father\'s Name': father_name_entry.get(),
        'Roll Number': roll_number_entry.get(),
        'Mobile Number': mobile_number_entry.get(),
        'Parent\'s Number': parent_number_entry.get(),
        'Payment Date': payment_date_entry.get(),
        'Registration Date': registration_date_entry.get(),
        'RFID Serial Number': rfid_entry.get()
    }
    try:
        with open('students.json', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    data.append(student)
    with open('students.json', 'w') as file:
        json.dump(data, file, indent=4)
    messagebox.showinfo("Success", "Student information saved successfully!")
    clear_entries()


def clear_entries():
    # Clear all entries
    for entry in entries.values():
        entry.delete(0, tk.END)
        entry.insert(0, placeholders[entry])


def validate_number_input(event, entry):
    value = entry.get()
    if not value.isdigit() and value != "":
        entry.delete(len(value) - 1, tk.END)
    return None


def on_entry_click(event, entry):
    if entry.get() == placeholders[entry]:
        entry.delete(0, tk.END)
        entry.config(fg='black')


def on_focus_out(event, entry):
    if entry.get() == '':
        entry.insert(0, placeholders[entry])
        entry.config(fg='grey')


# Create the main window
root = tk.Tk()
root.title("Student Registration")
root.geometry("600x300")  # Increase the width of the interface window

# Initialize entries dictionary and placeholders
entries = {}
placeholders = {}

# Create and place labels and entries in two columns
labels_col1 = ['Name', 'Father\'s Name', 'Mobile Number', 'Parent\'s Number']
labels_col2 = ['Roll Number', 'Payment Date', 'Registration Date', 'RFID Serial Number']

placeholder_texts = {
    'Name': 'Enter Name',
    'Father\'s Name': 'Enter Father\'s Name',
    'Roll Number': 'Enter Roll Number',
    'Mobile Number': 'Enter Mobile Number',
    'Parent\'s Number': 'Enter Parent\'s Number',
    'Payment Date': '(DD/MM/YY)',
    'Registration Date': '(DD/MM/YY)',
    'RFID Serial Number': 'RFID Serial Number'
}

# Place labels and entries for column 1
for i, label in enumerate(labels_col1):
    tk.Label(root, text=label).grid(row=i, column=0, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root, fg='grey')
    entry.insert(0, placeholder_texts[label])
    entry.bind("<FocusIn>", lambda e, entry=entry: on_entry_click(e, entry))
    entry.bind("<FocusOut>", lambda e, entry=entry: on_focus_out(e, entry))
    entry.grid(row=i, column=1, padx=10, pady=5, sticky='w')
    entries[label] = entry
    placeholders[entry] = placeholder_texts[label]

# Place labels and entries for column 2
for i, label in enumerate(labels_col2):
    tk.Label(root, text=label).grid(row=i, column=2, padx=10, pady=5, sticky='e')
    entry = tk.Entry(root, fg='grey')
    entry.insert(0, placeholder_texts[label])
    entry.bind("<FocusIn>", lambda e, entry=entry: on_entry_click(e, entry))
    entry.bind("<FocusOut>", lambda e, entry=entry: on_focus_out(e, entry))
    entry.grid(row=i, column=3, padx=10, pady=5, sticky='w')
    entries[label] = entry
    placeholders[entry] = placeholder_texts[label]

# Assign entries to variables
name_entry = entries['Name']
father_name_entry = entries['Father\'s Name']
mobile_number_entry = entries['Mobile Number']
parent_number_entry = entries['Parent\'s Number']
roll_number_entry = entries['Roll Number']
payment_date_entry = entries['Payment Date']
registration_date_entry = entries['Registration Date']
rfid_entry = entries['RFID Serial Number']

# Add validation for number input fields
mobile_number_entry.bind("<KeyRelease>", lambda e: validate_number_input(e, mobile_number_entry))
parent_number_entry.bind("<KeyRelease>", lambda e: validate_number_input(e, parent_number_entry))

# Save and Clear Buttons
button_frame = tk.Frame(root)
button_frame.grid(row=max(len(labels_col1), len(labels_col2)), column=0, columnspan=4, pady=10)

save_button = tk.Button(button_frame, text="Save", command=save_student, width=20)
save_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear_entries, width=20)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
