import requests
from requests.models import encode_multipart_formdata

url = 'http://dfedorov.spb.ru/python3/sport.txt'

text = requests.get(url, encoding = 'cp1251').text

print(text)