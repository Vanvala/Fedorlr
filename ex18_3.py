import re
import requests

url = 'http://dfedorov.spb.ru/python/files/mbox-short.txt'

text = requests.get(url).text

# print(text)

mails = re.findall(r'\w+@\w+\.\w+\.\w+\.\w+', text)

print(mails)

with open('mail.txt', 'w', encoding='utf-8') as file:
    for mail in mails: 
        file.write(f'{mail}\n')
