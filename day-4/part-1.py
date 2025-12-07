map = []
amount_can_take = 0

with open("day-4/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        section = []

        for char in list(line):
            section.append(char)
        
        map.append(section)

for y in map:
    for x in y:
        pass

print(map)

# havent finished day 4 yet