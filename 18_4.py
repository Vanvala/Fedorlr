import re
import requests

url = ' http://dfedorov.spb.ru/python/files/p.html'

text = requests.get(url).text

print(text)

html_1 = re.findall(r'<\w+>.*</\w+>', text)
html_2 = re.findall(r'<br>.+', text)


print(html_1, html_2)

# with open('mail.txt', 'w', encoding='utf-8') as file:
#     for mail in mails: 
#         file.write(f'{mail}\n')
