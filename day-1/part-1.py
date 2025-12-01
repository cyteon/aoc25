code = 0
pointing = 50

with open("day-1/input.txt", "r") as file:
    content = file.read()

    for line in content.split("\n"):
        chars = list(line)

        if len(chars) > 0:
            direction = chars.pop(0)
            value = int("".join(chars))

            print("\n%s, %s%s" % (pointing, direction, value))

            if direction == "L":
                pointing += value
                pointing %= 100
            else:
                pointing -= value
                pointing %= 100
            
            print("%s\n" % pointing)

            if pointing == 0:
                code += 1

print(code)