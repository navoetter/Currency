exchange_rates = {
    ("EUR", "USD"): 1.08, ("USD", "EUR"): 0.93,
    ("EUR", "YEN"): 160.5, ("YEN", "EUR"): 0.0062,
    ("EUR", "SEK"): 11.2, ("SEK", "EUR"): 0.089,
    ("USD", "YEN"): 148.5, ("YEN", "USD"): 0.0067,
    ("USD", "SEK"): 10.4, ("SEK", "USD"): 0.096,
    ("YEN", "SEK"): 0.070, ("SEK", "YEN"): 14.3,
    ("RUB", "SEK"): 0.011, ("SEK", "RUB"): 0.092, #Russische Rubel exchange rate hinzugefügt
}

amount = float(input("Betrag: "))
from_currency = input("Von (EUR, USD, YEN, SEK, RUB): ").upper()
to_currency = input("Nach (EUR, USD, YEN, SEK, RUB): ").upper()

if from_currency == to_currency:
    print("Die Währungen sind gleich, keine Umrechnung nötig.")
elif (from_currency, to_currency) in exchange_rates:
    rate = exchange_rates[(from_currency, to_currency)]
    print(f"{amount} {from_currency} = {amount * rate:.2f} {to_currency}")
else:
    print("Wechselkurs nicht verfügbar.")
