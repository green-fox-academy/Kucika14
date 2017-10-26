# - Create a two dimensional list
#   which can contain the different shades of specified colors
# - In `colors[0]` store the shades of green:
#   `"lime", "forest green", "olive", "pale green", "spring green"`
# - In `colors[1]` store the shades of red:
#   `"orange red", "red", "tomato"`
# - In `colors[2]` store the shades of pink:
#   `"orchid", "violet", "pink", "hot pink"`
all_colors = []

for i in range(3):
    if i == 0:
        all_colors.append(["lime", "forest green", "olive", "pale green", "spring green"])
    elif i == 1:
        all_colors.append(["orange red", "red", "tomato"])
    else:
        all_colors.append(["orchid", "violet", "pink", "hot pink"])

print(all_colors[0])