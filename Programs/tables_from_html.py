"""Парсируем веб страницу, ищем табличные данные и сохраняем в Excel. Pandas."""
import pandas as pd
# from urllib import parse # Для русских URl


# pip install openpyxl
# pip install pandas

url = 'https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0_%D0%B8_%D1%80%D0%B5%D0%BA%D0%BE%D1%80%D0%B4%D1%8B_%D0%A4%D0%9A_%C2%AB%D0%A0%D0%B5%D0%B0%D0%BB_%D0%9C%D0%B0%D0%B4%D1%80%D0%B8%D0%B4%C2%BB'
# url = 'https://ru.wikipedia.org/wiki/Статистика_и_рекорды_ФК_«Реал_Мадрид»'
data = pd.read_html(url, encoding='utf-8')

print(data[1])
print(data.__len__())

# url = parse.quote(url, safe=':/')# если ссылки русские. Safe = ':/' что точно не переделывать оставить в ASCII

with pd.ExcelWriter('outreal_madrid.xlsx') as writer:
    for idx, df in enumerate(data, start=1): #enumerate добавляет индекс(idx)
        df.to_excel(writer, sheet_name=f'Таблица {idx}')
