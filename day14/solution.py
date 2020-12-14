def addressGenerator(address):
    xaddress = []
    for c in address:
        xaddress.append(c)
    address = xaddress
    xindex = []
    addresses = []
    for i in range(0, len(address)):
        if address[i] == "X":
            xindex.append([i, 0])

    for v in xindex:
        address[v[0]] = "0"

    # a=int("".join(address),2)
    # addresses.append(a)

    for i in range(0, 2 ** len(xindex)):
        curry = 1
        for v in xindex:
            if v[1] == 0 and curry == 1:
                v[1] = 1
                curry = 0
                address[v[0]] = "1"
                break
            elif v[1] == 1 and curry == 1:
                v[1] = 0
                address[v[0]] = "0"
        addresses.append(int("".join(address), 2))

    return addresses


def createMask(mask):
    andMask = int(mask.replace("X", "1"), 2)
    orMask = int(mask.replace("X", "0"), 2)
    return (andMask, orMask)


def applyMask(mask, num):
    num = num & mask[0]
    num = num | mask[1]
    return num


def applyMask2(mask, num):
    num = "{0:036b}".format(num)
    rnum = ""
    for i in range(0, len(mask)):
        if mask[i] == "0":
            rnum += num[i]
            continue
        rnum += mask[i]
    return rnum


if __name__ == "__main__":
    # a=applyMask2("000000000000000000000000000000X1001X",42)
    # print addressGenerator(a)

    data = dict()
    data2 = dict()
    mask = None
    omask = None
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            if line[0:7] == "mask = ":
                omask = line[7:]
                mask = createMask(omask)
                continue
            n = line.find("]")
            pos = int(line[4:n], 10)
            num = int(line[n + 4 :])
            data[pos] = applyMask(mask, num)
            nmas = applyMask2(omask, pos)
            addresses = addressGenerator(nmas)
            for a in addresses:
                data2[a] = num

    s = 0
    for k, v in data.items():
        s += v
    print "Solution Part 1 {0}".format(s)

    s = 0
    for k, v in data2.items():
        s += v
    print "Solution Part 2 {0}".format(s)

    """
    mask=createMask("XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X")
    num=11
    print applyMask(mask,num)
    print applyMask(mask,101)
    print applyMask(mask,0)
    """