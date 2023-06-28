"""Сравнение файлов. Несколько строк кода и вы сравнили файлы, причем визуально."""

import difflib as dl
import os


output = os.popen('wmic process get description, processid').read()
output_file = open('compare_before.txt', 'w+')
output_file.write(output)
output_file.close()

print(output)

show_pre = open('compare_before.txt', encoding='utf-8').read().replace('\n\n', '\n').splitlines()
show_aft = open('compare_after.txt', encoding='utf-8').read().replace('\n\n', '\n').splitlines()

print(show_pre)

dl.SequenceMatcher(a=show_pre, b=show_aft).ratio()

difference = dl.HtmlDiff().make_file(fromlines=show_pre, tolines=show_aft, charset='utf-8')
difference_report = open('show_comp.html', 'w+', encoding='utf-8')
difference_report.write(difference)
difference_report.close()
print(difference)
