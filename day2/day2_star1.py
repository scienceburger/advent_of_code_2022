with open("input", "r") as fh:
    strategy_guide = fh.readlines()

#rock = A, X
#scissors = B, Y
#paper = C, Z

hand_points = {"rock": 1, "paper": 2, "scissors": 3}
match_points = {"win": 6, "draw": 3, "loss": 0}

hand_map = {
    "rock rock": "draw",
    "rock paper": "win",
    "rock scissors": "loss",
    "paper rock": "loss",
    "paper paper": "draw",
    "paper scissors": "win",
    "scissors rock": "win",
    "scissors paper": "loss",
    "scissors scissors": "draw"
}

tr = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors"
}

def resolve_hand(opponent, you):
    result = hand_map[f"{tr[opponent]} {tr[you]}"]
    score = hand_points[tr[you]] + match_points[result]
    print(f"Resolving {tr[opponent]} - {tr[you]} : {result} - {score}")
    return score


def split_game(a_string):
    return a_string.split()


def resolve_line(line):
    o = split_game(line)[0]
    y = split_game(line)[1]
    s = resolve_hand(o, y)
    return s

total_score = 0

for l in strategy_guide:
    print(l)
    total_score += resolve_line(l)

print(total_score)
