with open("input", "r") as fh:
    input_data = fh.read()

elves_payload = input_data.split("\n\n")

def sum_from_list(a_list):
    int_list = [int(a) for a in a_list]
    total = 0
    for i in int_list:
        total += i
    return total

all_calories = []
for p in elves_payload:
    elf_list = p.splitlines(keepends=False)
    all_calories.append(sum_from_list(elf_list))


all_calories = sorted(all_calories, reverse=True)
print(sum_from_list(all_calories[0:3]))


