import copy


class Instruction:
    def __init__(self, op, value):
        self.op = op
        self.value = int(value)


class VM:
    def __init__(self):
        self.instructions = list()
        self.execution = list()
        self.reset()

    def reset(self):
        self.ip = 0
        self.acc = 0
        for i in range(0, len(self.execution)):
            self.execution[i] = 0

    def addInstrction(self, instraction):
        self.instructions.append(instruction)
        self.execution.append(0)

    def run(self):
        while True:
            if self.ip >= len(self.execution):
                break
            if self.execution[self.ip] != 0:
                return 1
            li = self.instructions[self.ip]
            self.execution[self.ip] = self.ip
            if li.op == "acc":
                self.acc += li.value
            elif li.op == "nop":
                pass
            elif li.op == "jmp":
                self.ip += li.value
                continue
            self.ip += 1
        return 0


def decodeInstruction(line):
    line = line.strip().split(" ")
    return Instruction(line[0], line[1])


if __name__ == "__main__":
    vm = VM()
    with open("input", "r") as f:
        for line in f:
            instruction = decodeInstruction(line)
            vm.addInstrction(instruction)
    vm.run()
    print "Accumulator after stop {}".format(vm.acc)
    execution = copy.copy(vm.execution)

    for i in range(0, len(execution)):
        if execution[i] != 0:
            oldinstr = vm.instructions[i]
            if oldinstr.op == "acc":
                continue
            oiv = oldinstr.op
            if oldinstr.op == "jmp":
                oldinstr.op = "nop"
            elif oldinstr.op == "nop":
                oldinstr.op = "jmp"
            vm.reset()
            if vm.run() == 0:
                break
            oldinstr.op = oiv

    print "Accumulator after finish {}".format(vm.acc)