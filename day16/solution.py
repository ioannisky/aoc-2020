import copy


class Rule:
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def addRange(self, min, max):
        self.ranges.append({"min": min, "max": max})

    def isInRange(self, number):
        for i in self.ranges:
            if (number >= i["min"]) and (number <= i["max"]):
                return True
        return False

    @staticmethod
    def parseLine(line):
        line = line.split(": ")
        rule = Rule(line[0])
        rules = line[1].split(" or ")
        r1 = rules[0].split("-")
        rule.addRange(int(r1[0]), int(r1[1]))
        r2 = rules[1].split("-")
        rule.addRange(int(r2[0]), int(r2[1]))
        return rule


def evaluate(rules, nums):
    falseNums = []
    for n in nums:
        i = n
        falseRange = 0
        for r in rules:
            if not r.isInRange(i):
                falseRange += 1
        if falseRange == len(rules):
            falseNums.append(i)
    if len(falseNums) != 0:
        return falseNums
    return True


def checkResolved(parray):
    for i in parray:
        if len(i) != 1:
            return False
    return True


if __name__ == "__main__":
    stage = 0
    rules = []
    total = 0
    valid_tickets = []
    own_ticket = None
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            if line == "":
                stage += 1
                continue
            if stage == 0:
                rules.append(Rule.parseLine(line))
            if stage == 1:
                if line[-1] == ":":
                    continue
                own_ticket = [int(i) for i in line.split(",")]
            if stage == 2:
                if line[-1] == ":":
                    continue
                nums = line.split(",")
                nnums = [int(i) for i in nums]
                e = evaluate(rules, nnums)
                if e != True:
                    total += sum(e)
                else:
                    valid_tickets.append(nnums)
    print "Solution for part 1 {}".format(total)

    parray = [copy.copy(rules) for i in range(0, len(rules))]
    for ticket in valid_tickets:
        for i in range(0, len(ticket)):
            num = ticket[i]
            removeRules = []
            for rule in parray[i]:
                if rule.isInRange(num) == False:
                    removeRules.append(rule)
            for rule in removeRules:
                parray[i].remove(rule)

    while not checkResolved(parray):
        for i in range(0, len(parray)):
            rules = parray[i]
            if len(rules) == 1:
                rule = rules[0]
                for h in range(0, len(parray)):
                    if h != i:
                        if rule in parray[h]:
                            parray[h].remove(rule)

    mul = 1
    for i in range(0, len(parray)):
        rule = parray[i][0]
        if "departure" in rule.name:
            mul *= own_ticket[i]
    print "Solution for part 2 {}".format(mul)
