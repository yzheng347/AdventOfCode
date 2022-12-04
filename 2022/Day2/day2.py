# X for Rock, Y for Paper, and Z for Scissors
# 1 for Rock, 2 for Paper, and 3 for Scissors
shape = { 'X': 1, 'Y': 2, 'Z': 3 }

# 0 if you lost, 3 if the round was a draw, and 6 if you won
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
outcome = { 'X': 0, 'Y': 3, 'Z': 6 }

# me_shape = { 'X': "Rock", 'Y': "Paper", 'Z': "Scissors" }
# oppo_shape = { 'A': "Rock", 'B': "Paper", 'C': "Scissors" }

def get_outcome(opponent, me):
    me_i = ord(me) - ord('X')
    oppo_i = ord(opponent) - ord('A')
    if oppo_i == me_i:
        return 3
    # print("me:", me_shape[me])
    # print("oppo:", oppo_shape[opponent])
    # print("res: ", "win" if me_i is (oppo_i + 1) % 3 else "loss")
    return 6 if me_i is (oppo_i + 1) % 3 else 0

def get_shape(opponent, outcome):
    oppo_i = ord(opponent) - ord('A')
    if outcome == 'Y':
        return shape[chr(ord('X') + oppo_i)]

    if outcome == 'X':
        return shape[chr(ord('X') + (oppo_i - 1) % 3)]
    
    return shape[chr(ord('X') + (oppo_i + 1) % 3)]

with open('input.txt') as f:
    rounds = [line.strip().split(" ") for line in f.read().splitlines()]

    scores_1 = [ shape[round[1]] + get_outcome(round[0], round[1]) for round in rounds]
    scores_2 = [ outcome[round[1]] + get_shape(round[0], round[1]) for round in rounds]
    
    print("Part 1: ", sum(scores_1))
    print("Part 2: ", sum(scores_2))
    