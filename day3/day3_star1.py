def priority_for_item_type(item_type):
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".index(item_type) + 1


def split_compartments(string):
    first_compartment = string[0:len(string)//2]
    second_compartment = string[len(string)//2:]
    return first_compartment, second_compartment


def common_item_type(compartment_a, compartment_b):
    common_item_type = list(set(compartment_a).intersection(compartment_b))[0]
    print(common_item_type)
    return common_item_type


accumulator = 0

with open("input", "r") as fh:
    for l in fh.readlines():
        c1, c2 = split_compartments(l)
        common = common_item_type(c1, c2)
        accumulator += priority_for_item_type(common)

print(accumulator)
