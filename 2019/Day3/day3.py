deltaX = {"R": 1, "L": -1, "U": 0, "D": 0}
deltaY = {"R": 0, "L": 0, "U": 1, "D": -1}

def process(input):
    wires = []
    x = 0
    y = 0
    step = 0
    for inp in input:
        dir = inp[0]
        len = int(inp[1:])
        for i in range(len):
            step = step + 1
            x = x + deltaX[dir]
            y = y + deltaY[dir]
            wires.append((x,y))
    return wires

def calc_intersect_step(wire_1, wire_2, intersection):
    steps = []
    for inter in intersection:
        step_1 = 1 + wire_1.index(inter)
        step_2 = 1 + wire_2.index(inter)
        steps.append(step_1 + step_2)
    return steps

def manhattan(pos_1, pos_2):
    x_1, y_1 = pos_1
    x_2, y_2 = pos_2
    return abs(x_1 - x_2) + abs(y_1 - y_2)

if __name__ == "__main__":
    input = []
    for line in open('input.txt').readlines():
        input.append(line)
    # input = ["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]
    wire_1 = process(input[0].split(","))
    wire_2 = process(input[1].split(","))
    intersection = set(wire_1) & set(wire_2)
    dist = [manhattan(inter, (0, 0)) for inter in intersection]
    print(f"Part 1: {min(dist)}")

    steps = calc_intersect_step(wire_1, wire_2, intersection)
    print(f"Part 2: {min(steps)}")
