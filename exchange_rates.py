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

translations = {
    "en": {
        "amount_label": "Amount:",
        "from_currency_label": "From:",
        "to_currency_label": "To:",
        "convert_button": "Convert",
        "result_label": "Result",
        "error_message": "Invalid amount.",
        "no_conversion_message": "The currencies are the same.",
        "no_rate_message": "Exchange rate not available."
    },
    "de": {
        "amount_label": "Betrag:",
        "from_currency_label": "Von:",
        "to_currency_label": "Nach:",
        "convert_button": "Umrechnen",
        "result_label": "Ergebnis",
        "error_message": "Ungültiger Betrag.",
        "no_conversion_message": "Die Währungen sind gleich.",
        "no_rate_message": "Wechselkurs nicht verfügbar."
    }
}

current_language = "en"

def change_language(language):
    global current_language
    current_language = language
    update_labels()

def update_labels():
    amount_label.config(text=translations[current_language]["amount_label"])
    from_currency_label.config(text=translations[current_language]["from_currency_label"])
    to_currency_label.config(text=translations[current_language]["to_currency_label"])
    convert_button.config(text=translations[current_language]["convert_button"])
    result_label.config(text=translations[current_language]["result_label"])

def convert():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        if from_currency == to_currency:
            messagebox.showinfo("Info", translations[current_language]["no_conversion_message"])
            return

        if (from_currency, to_currency) in exchange_rates:
            rate = exchange_rates[(from_currency, to_currency)]
            result = amount * rate
            result_label.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}")
        else:
            messagebox.showerror("Fehler", translations[current_language]["no_rate_message"])
    except ValueError:
        messagebox.showerror("Fehler", translations[current_language]["error_message"])

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root)
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = tk.Label(root)
from_currency_label.grid(row=1, column=0, padx=10, pady=10)

from_currency_var = tk.StringVar(root)
from_currency_var.set("EUR")
from_currency_menu = tk.OptionMenu(root, from_currency_var, "EUR", "USD", "YEN", "SEK")
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = tk.Label(root)
to_currency_label.grid(row=2, column=0, padx=10, pady=10)

to_currency_var = tk.StringVar(root)
to_currency_var.set("USD")
to_currency_menu = tk.OptionMenu(root, to_currency_var, "EUR", "USD", "YEN", "SEK")
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, command=convert)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

result_label = tk.Label(root)
result_label.grid(row=4, column=0, columnspan=2, pady=10)

language_button = tk.Button(root, text="Switch to Deutsch", command=lambda: change_language("de"))
language_button.grid(row=5, column=0, columnspan=2, pady=10)

update_labels()

root.mainloop()
