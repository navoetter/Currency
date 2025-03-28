import tkinter as tk
from tkinter import messagebox

exchange_rates = {
    ("EUR", "USD"): 1.08, ("USD", "EUR"): 0.93,
    ("EUR", "YEN"): 160.5, ("YEN", "EUR"): 0.0062,
    ("EUR", "SEK"): 11.2, ("SEK", "EUR"): 0.089,
    ("USD", "YEN"): 148.5, ("YEN", "USD"): 0.0067,
    ("USD", "SEK"): 10.4, ("SEK", "USD"): 0.096,
    ("YEN", "SEK"): 0.070, ("SEK", "YEN"): 14.3
}

def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            messagebox.showinfo("Info", "Die Währungen sind gleich.")
            return

        if (from_currency, to_currency) in exchange_rates:
            rate = exchange_rates[(from_currency, to_currency)]
            result = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            messagebox.showerror("Fehler", "Wechselkurs nicht verfügbar.")
    except ValueError:
        messagebox.showerror("Fehler", "Ungültiger Betrag.")

root = tk.Tk()
root.title("Währungsumrechner")

amount_label = tk.Label(root, text="Betrag:")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(root, text="Von:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_var = tk.StringVar(root)
from_currency_var.set("EUR")
from_currency_menu = tk.OptionMenu(root, from_currency_var, "EUR", "USD", "YEN", "SEK")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(root, text="Nach:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_var = tk.StringVar(root)
to_currency_var.set("USD")
to_currency_menu = tk.OptionMenu(root, to_currency_var, "EUR", "USD", "YEN", "SEK")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Umrechnen", command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root, text="Ergebnis")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
