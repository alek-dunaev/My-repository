tickets = int(input("Введите количество билетов "))
price = 0
for i in range(1, tickets + 1):
    age = int(input(f"Возраст {i}го посетителя "))
    if 18 <= age <= 25:
        price += 990
    elif age > 25:
        price += 1390
final_price = price * 0.9 if tickets >= 3 else price
print(f"Итоговая стоимость равна = {final_price} рублей")
