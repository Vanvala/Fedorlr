
from os import supports_fd, write


with open('plan.txt', 'r') as file:
    planets = file.readlines()
    sort_planets = sorted(planets)
    print(sort_planets)

with open('sort_plan.txt', 'w') as sort_file:
    line = ''
    for planet in sort_planets:
        if planet == 'Neptune':
            planet += '\n'

        line += planet
        print(line)

    sort_file.write(line)
    