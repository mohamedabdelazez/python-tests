import pandas as pd
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox
from openpyxl import load_workbook


file_name = 'mony.xlsx'


def create_excel_file():
    try:
        df = pd.read_excel(file_name)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['Date', 'Time', 'Value', 'Notes', 'Transaction Type', 'Remaining Balance'])
        df.to_excel(file_name, index=False)


def adjust_excel_column_width():
    wb = load_workbook(file_name)
    ws = wb.active

    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    wb.save(file_name)


def add_transaction():
    try:
        value = float(entry_value.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the value.")
        return

    transaction_type = combo_type.get()
    notes = entry_notes.get()
    date = datetime.now().strftime('%Y-%m-%d')
    time = datetime.now().strftime('%I:%M:%S %p')

    try:
        df = pd.read_excel(file_name)
        remaining_balance = float(df['Remaining Balance'].iloc[-1].split()[0]) if not df.empty else 0
    except FileNotFoundError:
        remaining_balance = 0

    if transaction_type == 'Deposit':
        remaining_balance += value
    elif transaction_type == 'Withdrawal':
        remaining_balance -= value

    value_with_currency = f"{value} EGP"
    new_data = pd.DataFrame({
        'Date': [date], 
        'Time': [time], 
        'Value': [value_with_currency], 
        'Notes': [notes],
        'Transaction Type': [transaction_type], 
        'Remaining Balance': [f"{remaining_balance} EGP"]
    })
    df = pd.concat([df, new_data], ignore_index=True)
    df.to_excel(file_name, index=False)

    adjust_excel_column_width()

    messagebox.showinfo("Success", "Transaction added successfully")
    entry_value.delete(0, tk.END)
    entry_notes.delete(0, tk.END)


root = tk.Tk()
root.title("Financial Savings Tracker")


label_value = tk.Label(root, text="Value:")
label_value.grid(row=0, column=0, padx=10, pady=10)

entry_value = tk.Entry(root)
entry_value.grid(row=0, column=1, padx=10, pady=10)

label_notes = tk.Label(root, text="Notes:")
label_notes.grid(row=1, column=0, padx=10, pady=10)

entry_notes = tk.Entry(root)
entry_notes.grid(row=1, column=1, padx=10, pady=10)

label_type = tk.Label(root, text="Transaction Type:")
label_type.grid(row=2, column=0, padx=10, pady=10)

combo_type = ttk.Combobox(root, values=["Deposit", "Withdrawal"])
combo_type.grid(row=2, column=1, padx=10, pady=10)

button_add = tk.Button(root, text="Add Transaction", command=add_transaction)
button_add.grid(row=3, column=0, columnspan=2, padx=10, pady=10)


create_excel_file()


root.mainloop()
