red_squares = []

with open("day-9/input.txt", "r") as file:
    content = file.read()
    lines = content.split("\n")

    for line in lines:
        red_squares.append((
            int(line.split(",")[0]), int(line.split(",")[1])
        ))

largest_square = 0

for s1 in red_squares:
    for s2 in red_squares:
        dist_x = abs(s1[0] - s2[0]) + 1
        dist_y = abs(s1[1] - s2[1]) + 1

        if dist_x * dist_y > largest_square:
            largest_square = dist_x * dist_y

print(largest_square)