TAX_RATE = 0.13 

income = float(input("Введите годовой доход: "))

tax = income * TAX_RATE
_income = income - tax

# Форматирование
income_text = f"{income:,.2f}".replace(",", " ")
tax_text = f"{tax:,.2f}".replace(",", " ")
_income_text = f"{_income:,.2f}".replace(",", " ")

print(f"Общая сумма дохода: {income_text} руб.")
print(f"Сумма рассчитанного налога: {tax_text} руб.")
print(f"Сумма на руки после вычета налога: {_income_text} руб.")



