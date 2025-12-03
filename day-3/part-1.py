voltage = 0

with open("day-3/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        chars = list(line)

        biggest_combo = 0
        for i, c in enumerate(chars):
            temp = chars[i + 1:]

            biggest_num = 0
            for c2 in temp:
                if int(c2) > biggest_num:
                    biggest_num = int(c2)
                        
            if int(c + str(biggest_num)) > biggest_combo and biggest_num != 0:
                biggest_combo = int(c + str(biggest_num))
        
        voltage += biggest_combo

print(voltage)
