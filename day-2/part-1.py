total_of_invalid_ids = 0

with open("day-2/input.txt", "r") as file:
    content = file.read()

    for id_range in content.split(","):
        start = id_range.split("-")[0]
        end = id_range.split("-")[1]

        for i in range(int(start), int(end)):
            s = str(i)
            sl = len(s) // 2

            if s[:sl] == s[sl:]:
                total_of_invalid_ids += i

print(total_of_invalid_ids)