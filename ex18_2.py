import urllib.request

url = ' http://dfedorov.spb.ru/python/files/tutchev.txt'
text = []

with urllib.request.urlopen(url) as webpage:
    for line in webpage:
        line = line.strip()
        line = line.decode('utf-8')
        text.append(line)

text[0] = 'Фёдор Тютчев'

with open('tutchev.html', 'w', encoding='utf-8') as file:
    file.write('<!DOCTYPE>')
    file.write('<html>')
    file.write('<head><meta charset="utf-8"><title>Tutchev</title></head>')
    file.write('<body>')
    for line in text:
        file.write(f'<p>{line}</p>')

    file.write('<p><img src=" http://dfedorov.spb.ru/python/files/tutchev.jpg" alt="Портрет Тютчева"></p>')
    file.write('</body>')
    file.write('</html>')

