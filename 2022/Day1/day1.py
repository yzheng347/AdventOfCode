with open('input.txt') as f:
    elves = f.read().split("\n\n")
    calories = [sum(int(food) for food in elf.splitlines()) for elf in elves]
    # print(len(calories))
    # print(calories[0])
    print("Part 1: ", max(calories))
    calories.sort()
    print("Part 2: ", sum(calories[-3:]))
    