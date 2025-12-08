map = []
amount_can_take = 0

with open("day-4/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        section = []

        for char in list(line):
            section.append(char)
        
        map.append(section)

last_result = 0

while True:
    for iy, y in enumerate(map):
        for ix, x in enumerate(y):
            if x == "@":
                adjacent = 0

                if iy > 0:
                    if map[iy - 1][ix] == "@":
                        adjacent += 1
                    
                    if ix > 0:
                        if map[iy - 1][ix - 1] == "@":
                            adjacent += 1
                    
                    if ix < len(map[iy - 1]) - 1:
                        if map[iy - 1][ix + 1] == "@":
                            adjacent += 1
                
                if ix > 0:
                    if map[iy][ix - 1] == "@":
                        adjacent += 1
                
                if ix < len(map[iy]) - 1:
                    if map[iy][ix + 1] == "@":
                        adjacent += 1
                
                if iy < len(map) - 1:
                    if map[iy + 1][ix] == "@":
                        adjacent += 1
                    
                    if ix > 0:
                        if map[iy + 1][ix - 1] == "@":
                            adjacent += 1
                    
                    if ix < len(map[iy + 1]) - 1:
                        if map[iy + 1][ix + 1] == "@":
                            adjacent += 1
                
                if adjacent < 4:
                    amount_can_take += 1
                    map[iy][ix] = "."
    
    if amount_can_take == last_result:
        break
    else:
        last_result = amount_can_take

print(amount_can_take)