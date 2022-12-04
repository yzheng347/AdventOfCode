# INPUT = 1
INPUT = 5

def execute_instruction(memory):
    pc = 0
    while pc < len(memory):
        if memory[pc] == 99:
            return memory
        opcode = memory[pc] % 100
        if opcode == 1:
            memory = addr(memory, memory[pc], memory[pc + 1], memory[pc + 2], memory[pc + 3])
            pc += 4
        elif opcode == 2:
            memory = multi(memory, memory[pc], memory[pc + 1], memory[pc + 2], memory[pc + 3])
            pc += 4
        elif opcode == 3:
            memory = input(memory, memory[pc + 1])
            pc += 2
        elif opcode == 4:
            output(memory, memory[pc], memory[pc + 1])
            pc += 2
        elif opcode == 5:
            pc = jmpt(memory, pc, memory[pc], memory[pc + 1], memory[pc + 2])
        elif opcode == 6:
            pc = jmpf(memory, pc, memory[pc], memory[pc + 1], memory[pc + 2])
        elif opcode == 7:
            memory = less(memory, memory[pc], memory[pc + 1], memory[pc + 2], memory[pc + 3])
            pc += 4
        elif opcode == 8:
            memory = eql(memory, memory[pc], memory[pc + 1], memory[pc + 2], memory[pc + 3])
            pc += 4
        else:
            print("Noope")
            print(opcode)
    return memory


def addr(memory, opcode, param_1, param_2, param_3):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    memory[param_3] = value_1 + value_2
    return memory


def multi(memory, opcode, param_1, param_2, param_3):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    memory[param_3] = value_1 * value_2
    return memory

def input(memory, param):
    global INPUT
    memory[param] = INPUT
    return memory

def output(memory, opcode, param):
    outp = get_value(memory, (opcode // 100) % 10, param)
    print(outp)

def jmpt(memory, pc, opcode, param_1, param_2):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    if value_1 != 0:
        return value_2
    return pc + 3

def jmpf(memory, pc, opcode, param_1, param_2):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    if value_1 == 0:
        return value_2
    return pc + 3

def less(memory, opcode, param_1, param_2, param_3):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    memory[param_3] = 1 if value_1 < value_2 else 0
    return memory


def eql(memory, opcode, param_1, param_2, param_3):
    value_1 = get_value(memory, (opcode // 100) % 10, param_1)
    value_2 = get_value(memory, (opcode // 1000) % 10, param_2)
    memory[param_3] = 1 if value_1 == value_2 else 0
    return memory

def get_value(memory, mode, param):
    if mode == 0:
        return memory[param]
    elif mode == 1:
        return param
    else:
        print("Oops, error")


if __name__ == "__main__":

    with open('input.txt') as f:
        program = [int(value) for value in f.read().split(',')]

    memory = program.copy()
    execute_instruction(memory)
