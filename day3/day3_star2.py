from more_itertools import chunked

def priority_for_item_type(item_type):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(item_type) + 1


def split_compartments(string):
    first_compartment = string[0:len(string)//2]
    second_compartment = string[len(string)//2:]
    return first_compartment, second_compartment


def common_item_type(rucksack_a, rucksack_b, rucksack_c):
    common_item_type = list(set(rucksack_a) & set(rucksack_b) & set(rucksack_c))[0]
    return common_item_type


accumulator = 0

with open("input", "r") as fh:
    lines = [l.rstrip() for l in fh.readlines()]
    chunks = chunked(lines, 3)

    for c in chunks:
        common = common_item_type(c[0], c[1], c[2])
        accumulator += priority_for_item_type(common)

print(accumulator)
