import requests

url = 'http://dfedorov.spb.ru/python3/src/romeo.txt'

text = requests.get(url).text

text = text.split('\n')

text = f'{text[0]} {text[1]} {text[2]} {text[3]}'

num_dict = {}
clean_text = text.split(' ')
print(clean_text)
for word in clean_text:
    num_dict[word] = text.count(word)
    
print(num_dict)