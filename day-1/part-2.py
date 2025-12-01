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
                for i in range(value):
                    pointing += 1
                    pointing %= 100

                    if pointing == 0:
                        code += 1
            else:
                for i in range(value):
                    pointing -= 1
                    pointing %= 100

                    if pointing == 0:
                        code += 1
            
            print("%s\n" % pointing)

print(code)