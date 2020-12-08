import copy


class Instruction:
    def __init__(self, op, value):
        self.op = op
        self.value = int(value)

    def __str__(self):
        return "{0} {1}".format(self.op, self.value)


class VM:
    def __init__(self):
        self.instructions = list()
        self.execution = list()
        self.reset()

    def reset(self, re=False):
        self.ip = 0
        self.acc = 0
        if re == False:
            for i in range(0, len(self.execution)):
                self.execution[i] = 0

    def addInstrction(self, instraction):
        self.instructions.append(instruction)
        self.execution.append(0)

    def run(self, ip=None):
        count = 0
        if ip != None:
            self.ip = ip
        while True:
            if self.ip >= len(self.execution):
                break
            if self.execution[self.ip] != 0:
                return 1
            li = self.instructions[self.ip]
            self.execution[self.ip] = 1
            if li.op == "acc":
                self.acc += li.value
            elif li.op == "nop":
                pass
            elif li.op == "jmp":
                self.ip += li.value
                continue
            self.ip += 1
            count += 1
        return 0

    def __str__(self):
        ret = ""
        for i in self.instructions:
            ret += str(i) + "\n"
        return ret

    def __repr__(self):
        return self.__str__()


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
    instructions_tested = 0
    for i in range(0, len(execution)):
        if execution[i] == 1:

            oldinstr = vm.instructions[i]
            if oldinstr.op == "acc":
                continue
            oiv = oldinstr.op
            if oldinstr.op == "jmp":
                if execution[i + 1] != 0:
                    continue
                oldinstr.op = "nop"
            elif oldinstr.op == "nop":
                if execution[i + oldinstr.value] != 0:
                    continue
                oldinstr.op = "jmp"
            instructions_tested += 1
            vm.reset(True)
            vm.execution[i] = 0
            if vm.run(i) == 0:
                break
            oldinstr.op = oiv
    # print vm.execution
    vm.reset()
    vm.run()
    # print instructions_tested
    print "Accumulator after finish {}".format(vm.acc)
