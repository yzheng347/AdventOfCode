import re

with open('input.txt') as f:
    lines = f.read().splitlines()
    contained = 0
    overlapped = 0
    for line in lines:
        sections = re.split(',|-', line)
        start_1, end_1, start_2, end_2 = [int(sec) for sec in sections]
        if start_1 <= start_2 and end_2 <= end_1 or start_2 <= start_1 and end_1 <= end_2:
            contained += 1

        if start_2 <= end_1 and start_1 <= end_2:
            overlapped += 1
    print("Part 1: ", contained)
    print("Part 2: ", overlapped)
    