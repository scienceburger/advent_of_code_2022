with open("input", "r") as fh:
    strategy_guide = fh.readlines()

#rock = A, X
#scissors = B, Y
#paper = C, Z

hand_points = {"rock": 1, "paper": 2, "scissors": 3}
match_points = {"win": 6, "draw": 3, "loss": 0}

hand_map = {
    "rock win": "paper",
    "rock draw": "rock",
    "rock loss": "scissors",
    "paper win": "scissors",
    "paper draw": "paper",
    "paper loss": "rock",
    "scissors win": "rock",
    "scissors draw": "scissors",
    "scissors loss": "paper"
}

tr = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "loss",
    "Y": "draw",
    "Z": "win"
}


def resolve_hand(opponent, you):
    played = hand_map[f"{tr[opponent]} {tr[you]}"]
    score = hand_points[played] + match_points[tr[you]]
    print(f"Resolving {tr[opponent]} - {tr[you]} : {played} (score: {score})")
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
    total_score += resolve_line(l)

print(total_score)
