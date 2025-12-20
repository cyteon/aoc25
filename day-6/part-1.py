total = 0

with open("day-6/input.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")

    rows = []

    for i in range(4):
        rows.append([int(x) for x in lines[i].split()])
    
    ops = lines[4].split()

    for i in range(len(rows[0])):
        result = 0

        if ops[i] == "+":
            result = rows[0][i] + rows[1][i] + rows[2][i] + rows[3][i]
        else:
            result = rows[0][i] * rows[1][i] * rows[2][i] * rows[3][i]
        
        total += result

print(total)
