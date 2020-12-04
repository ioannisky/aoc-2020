class Passport:
    def __init__(self):
        self.__dict__ = {}

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def hasAllFields(self):
        c = 0
        for k, v in self.__dict__.items():
            if k in ["ecl", "pid", "eyr", "hcl", "byr", "iyr", "hgt"]:
                c += 1
        if c == 7:
            return True
        return False

    def areFieledsValie(self):
        checks = 0
        if len(self.pid) == 9 and isNumber(self.pid):
            checks += 1
        if self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            checks += 1
        if len(self.hcl) == 7 and (self.hcl[0] == "#") and isAZ09(self.hcl):
            checks += 1
        if validHeight(self.hgt):
            checks += 1
        if isBetween(self.eyr, 2020, 2030):
            checks += 1
        if isBetween(self.iyr, 2010, 2020):
            checks += 1
        if isBetween(self.byr, 1920, 2002):
            checks += 1
        # print checks
        if checks == 7:
            return True
        return False


def readData(file):
    f = open(file, "r")
    data = []
    passport_data = Passport()
    for line in f:
        line = line.strip()
        if line == "":
            data.append(passport_data)
            passport_data = Passport()
            continue
        line = line.split(" ")
        for x in line:
            x = x.split(":")
            passport_data.__setattr__(x[0], x[1])
    data.append(passport_data)

    f.close()
    return data


def isNumber(value):
    for k in value:
        if ord(k) < ord("0") or ord(k) > ord("9"):
            return False
    return True


def isAZ09(value):
    for k in value:
        if ord(k) >= ord("0") or ord(k) <= ord("9"):
            continue
        if ord(k) >= ord("a") or ord(k) <= ord("f"):
            continue
        return False
    return True


def validHeight(hgt):
    u = hgt[-2:]
    try:
        n = int(hgt[:-2])
    except ValueError:
        return False
    if u == "cm" and n >= 150 and n <= 193:
        return True
    if u == "in" and n >= 59 and n <= 76:
        return True

    return False


def isBetween(n, min, max):
    n = int(n)
    if n >= min and n <= max:
        return True
    return False


if __name__ == "__main__":
    data = readData("input")
    count_valid_1 = 0
    count_valid_2 = 0

    for p in data:
        if p.hasAllFields():
            count_valid_1 += 1
            if p.areFieledsValie():
                count_valid_2 += 1

    print "Passports with valid number of fields:", count_valid_1
    print "Passports with valid fields:", count_valid_2
