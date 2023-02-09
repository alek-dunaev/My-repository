per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите количество денег"))
deposit = [(per_cent.get("ТКБ")*money/100),
           (per_cent.get("СКБ")*money/100),
           (per_cent.get("ВТБ")*money/100),
           (per_cent.get("СБЕР")*money/100)]
deposit.sort()
print(list(map(int,deposit)))
print("Максимальная сумма, которую вы можете заработать —", int(deposit[-1]))
