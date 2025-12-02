total_of_invalid_ids = 0

def is_repeated_sequence(s: str) -> bool:
    if len(s) < 2:
        return False
    
    return (s + s).find(s, 1) < len(s)

with open("day-2/input.txt", "r") as file:
    content = file.read()

    for id_range in content.split(","):
        start_s, end_s = [p for p in id_range.split("-")]
        start, end = int(start_s), int(end_s)

        for i in range(start, end):
            if is_repeated_sequence(str(i)):
                total_of_invalid_ids += i

print(total_of_invalid_ids)