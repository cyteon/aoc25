area = []

with open("day-7/input.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")

    for line in lines:
        area.append([ char for char in list(line) ])

rows = len(area)
cols = len(area[0])

start_row = None
start_col = None

for y in range(rows):
    for x in range(len(area[y])):
        if area[y][x] == "S":
            start_row, start_col = y, x
            break
    
    if start_row is not None:
        break

splits = 0
active = {start_col}

for y in range(start_row + 1, rows):
    new_active = set()

    for x in active:
        if x < 0 or x >= len(area[y]):
            continue

        cell = area[y][x]

        if cell == '^':
            splits += 1

            if x - 1 >= 0:
                new_active.add(x - 1)
            
            if x + 1 < len(area[y]):
                new_active.add(x + 1)
        else:
            new_active.add(x)
    active = new_active

print(splits)