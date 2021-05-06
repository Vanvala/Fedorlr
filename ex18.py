"""file = open('example_text.txt', 'r')
context = file.read()
print(context)
file.close()

try:
    f = open('example_text1.txt' )
except:
    print('Error opening file')
else:
    f.close()
    print('(Очистка: закрытие файла)')
"""

with open('example_text.txt', 'r') as file:
    """context = file.read(10)
    rest = file.read()
    print('10:', context)
    print('Rest:', rest)"""
    lines = file.readlines()
    print(lines)

with open('plan.txt', 'r') as file:
    planets = file.readlines()
    print(planets)

    for planet in reversed(planets):
        print(planet.strip())

with open('top.txt', 'w') as output_file:
    output_file.write('Hello!\n')

with open('top.txt', 'a') as output_file:
    output_file.write('World\n')
