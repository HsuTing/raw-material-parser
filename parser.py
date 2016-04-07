import requests
from bs4 import BeautifulSoup

req = requests.get('http://www.stockq.org/market/commodity.php')
req.encoding = 'utf-8'

html = BeautifulSoup(req.text, 'html.parser')
table = html.find("table", {"class": "marketdatatable"})
output = []
for item in table.find_all("tr"):
    if item.get('class') == None:
        continue

    name = ""
    price = ""
    rise_fall = ""
    ratio = ""
    time = ""
    index = 0
    for value in item.find_all("td"):
        if index == 0:
            name = value.text
        elif index == 1:
            price = value.text
        elif index == 2:
            rise_fall = value.text
        elif index == 3:
            ratio = value.text
        elif index == 4:
            time = value.text
        index += 1

    check_ratio = float(ratio.replace('%', ''))
    if check_ratio < 1 and check_ratio > -1:
        continue
    output_item = {
        'name': name,
        'price': price,
        'ratio': ratio,
        'time': time
    }
    output.append(output_item)

print(output)
