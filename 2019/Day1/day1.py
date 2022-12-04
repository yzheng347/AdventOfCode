def part_1(mass):
    return mass // 3 - 2

def part_2(mass):
    fuel = part_1(mass)
    if fuel <= 0:
        return 0
    else:
        return fuel + part_2(fuel)




if __name__ == "__main__":
    input = []
    with open("input.txt", "r") as inputFile:
        [[input.append(num) for num in line.split()] for line in inputFile]

    result = sum([part_1(int(i)) for i in input])
    print(f"Part 1: {result}")

    more_result = sum([part_2(int(i)) for i in input])
    print(f"Answer to part 1: {more_result}")
