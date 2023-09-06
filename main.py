import tkinter as tk
from tkinter import ttk
from currency_converter import CurrencyConverter

converter = CurrencyConverter()

def convert_currency():
    amount = float(entry_amount.get())
    from_currency = combo_from_currency.get()
    to_currency = combo_to_currency.get()

    result = converter.convert(amount, from_currency, to_currency)
    label_result.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")

root = tk.Tk()
root.geometry("500x360")
root.title("Currency Converter")

Heading = tk.Label(root,text="CurrencyConverter", font="Times 25 bold")
label_from_currency = tk.Label(root, text="From Currency:", font="Times 18 bold")
label_to_currency = tk.Label(root, text="To Currency:", font="Times 18 bold")
label_amount = tk.Label(root, text="Amount:", font="Times 18 bold")
label_result = tk.Label(root, text="Result:", font="Times 18 bold")

entry_amount = tk.Entry(root)

available_currencies = converter.currencies
currency_list = list(available_currencies)

combo_from_currency = ttk.Combobox(root, values=currency_list)
combo_to_currency = ttk.Combobox(root, values=currency_list)

convert_button = tk.Button(root, text="Convert", command=convert_currency)

Heading.pack()
label_from_currency.pack()
combo_from_currency.pack()
label_to_currency.pack()
combo_to_currency.pack()
label_amount.pack()
entry_amount.pack()
convert_button.pack()
label_result.pack()

root.mainloop()
