# Изучить список открытых API (https://www.programmableweb.com/category/all/apis)
# Найти среди них любое, требующее авторизацию (любого типа)
# Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл

from pprint import pprint
import requests
import json

main_link = 'https://api.vk.com/method/groups.get'
params = {
    'v': '5.52',
    'access_token': 'aed9b20687d7f62d5b2f4f522d42722b651679378d6465fe9a68a4a168814de032bce8047d7a93ed8c88e'
}
response = requests.get(main_link, params=params)
j_data = response.json()
pprint(j_data['response']['items'])
with open('groups.json', 'w') as outfile:
    json.dump(j_data, outfile)