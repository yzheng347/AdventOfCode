def get_priority(item):
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 38

with open('input.txt') as f:
    lines = f.read().splitlines()
    duplicates = []
    for line in lines:
        left = line[:len(line) // 2]
        right = line[len(line) // 2:]
        left_set, right_set = set(left), set(right)
        dup = left_set.intersection(right_set).pop()
        duplicates.append(dup)
    print("Part 1: ", sum(get_priority(item) for item in duplicates))

    badges = []
    for i in range(0, len(lines), 3):
        elf_1, elf_2, elf_3 = lines[i], lines[i + 1], lines[i + 2]
        badge = set(elf_1).intersection(set(elf_2)).intersection(set(elf_3)).pop()
        badges.append(badge)
    print("Part 2: ", sum(get_priority(item) for item in badges))