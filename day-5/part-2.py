# TODO: make this work, shouldve worked in theory but dosent

fresh = set()

with open("day-5/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        if "-" in line:
            range_set = set(range(int(line.split("-")[0]), int(line.split("-")[1])))
            fresh = fresh.union(range_set)

print(len(fresh))
