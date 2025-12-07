fresh = 0

id_ranges = []
ids = []

with open("day-5/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        if "-" in line:
            id_ranges.append(
                (
                    int(line.split("-")[0]), 
                    int(line.split("-")[1])
                )
            )
        elif len(line) > 0:
            ids.append(int(line))

for id in ids:
    for range in id_ranges:
        if id >= range[0] and id <= range[1]:
            fresh += 1
            break

print(fresh)
