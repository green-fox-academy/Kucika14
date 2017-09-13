# Saturn is missing from the planet_list
# Insert it into the correct position

planet_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Uranus", "Neptune"]
# planet_list.append("Saturn")
# a, b, c = planet_list.index('Uranus'), planet_list.index('Neptune'), planet_list.index('Saturn')
# planet_list[c], planet_list[b], planet_list[a] = planet_list[b], planet_list[a], planet_list[c]

planet_list.insert(5, 'Saturn')

print(planet_list)