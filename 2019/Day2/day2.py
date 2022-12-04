def execute_instruction(memory):
    pc = 0
    while pc < len(memory):
        if memory[pc] == 99:
            return memory
        opcode, input_one, input_two, output = memory[pc: pc + 4]
        if opcode == 1:
            memory[output] = memory[input_one] + memory[input_two]
            pc += 4
        elif opcode == 2:
            memory[output] = memory[input_one] * memory[input_two]
            pc += 4
        else:
            print("Noope")
    return memory

if __name__ == "__main__":
    with open('input.txt') as f:
        program = [int(value) for value in f.read().split(',')]

    memory = program.copy()
    memory[1], memory[2] = 12, 2
    execute_instruction(memory)
    print(f"Part 1: {memory[0]}")

    # Part 2
    for x in range(100):
        for y in range(100):
            memory = program.copy()
            memory[1], memory[2] = x, y

            execute_instruction(memory)

            if memory[0] == 19690720:
                result = 100 * x + y
                print(f"Part 2: {result}")
