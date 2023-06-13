"""Загрузка всех паролей от wi_fi на русской Windows"""

import subprocess
import re


command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True).stdout.decode('cp866')
# print(command_output)
profile_names = (re.findall("Все профили пользователей     : (.*)\r", command_output))
print(profile_names)
wifi_list = []

if len(profile_names) != 0:
    for name in profile_names:
        wifi_profile = {}
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output=True).stdout.decode('cp866')
        if re.search("Ключ безопасности:       Отсутствует", profile_info):
            continue
        else:
            wifi_profile["ssid"] = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output=True).stdout.decode('cp866')
            password = re.search("Содержимое ключа            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

for x in range(len(wifi_list)):
    print(wifi_list[x])
    
