temperature = float(input("Укажите Вашу температуру °C: "))
pressure = float(input("Укажите Ваше давление(верхнее): "))
pulse = float(input("Укажите Ваш пульс (уд/мин): "))

if 36<=temperature<=37 and 110<=pressure<=130 and 60<=pulse<=100:
    print("С Вами все в порядке.")

elif (35<temperature<36 or 37<temperature<38) and (105<pressure<110 or 130<pressure<140) and (55<pulse<60 or 100<pulse<110):
    print("У Вас недомогание, отдыхайте и пейте воду.")

else:
    print("Вызывайте врача!")
