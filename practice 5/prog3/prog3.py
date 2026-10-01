USD_TO_RUB = 95.50  # курс доллара к рублю

def convert_usd_to_rub(amount_usd):
    """Конвертирует сумму из долларов в рубли по заданному курсу.

    Args:
        amount_usd(float) : доллары
    Return:
        amount_usd*USD_TO_RUB : доллары в рубли
    """
    return amount_usd * USD_TO_RUB

amount = float(input("Введите сумму в долларах: "))
rub = convert_usd_to_rub(amount)

print(f"{amount:.2f} USD = {rub:.2f} RUB")