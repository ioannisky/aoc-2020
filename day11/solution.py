def countSeatsInAllDirections(data, y, x):
    occubied = 0
    # countSeatsUp
    i = y - 1
    while i >= 0:
        c = data[i][x]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i -= 1
    # countSeatsDown
    i = y + 1
    while i < len(data):
        c = data[i][x]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i += 1
    # countSeatsLeft
    i = x - 1
    while i >= 0:
        c = data[y][i]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i -= 1
    # countSeatsRight
    i = x + 1
    while i < len(data[y]):
        c = data[y][i]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i += 1
    # countUpLeft
    i = y - 1
    h = x - 1
    while (i >= 0) and (h >= 0):
        c = data[i][h]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i -= 1
        h -= 1
    # countUpRight
    i = y - 1
    h = x + 1
    while (i >= 0) and (h < len(data[y])):
        c = data[i][h]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i -= 1
        h += 1
    # countDownLeft
    i = y + 1
    h = x - 1
    while (i < len(data)) and (h >= 0):
        c = data[i][h]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i += 1
        h -= 1
    # countDownRight
    i = y + 1
    h = x + 1
    while (i < len(data)) and (h < len(data[y])):
        c = data[i][h]
        if c == "L":
            break
        if c == "#":
            occubied += 1
            break
        i += 1
        h += 1
    # print "DR",occubied
    return occubied


def countSeats(data):
    occubied = 0
    empty = 0
    for l in data:
        for c in l:
            if c == "#":
                occubied += 1
            elif c == "L":
                empty += 1
    return occubied, empty


def countAdjacent(data, y, x):
    count = 0
    for i in range(y - 1, y + 2):
        for h in range(x - 1, x + 2):
            if (
                (i < 0)
                or (i > len(data) - 1)
                or (h < 0)
                or (h > len(data[i]) - 1)
                or (i == y and h == x)
            ):
                continue

            if data[i][h] == "#":
                count += 1
    return count


def moveRound(data):
    switchSeats = []
    for i in range(0, len(data)):
        for h in range(0, len(data[i])):
            n = countAdjacent(data, i, h)
            # print n
            if data[i][h] == "L" and n == 0:
                switchSeats.append([i, h])
            elif (data[i][h] == "#") and n >= 4:
                switchSeats.append([i, h])

    for p in switchSeats:
        if data[p[0]][p[1]] == "L":
            data[p[0]][p[1]] = "#"
        elif data[p[0]][p[1]] == "#":
            data[p[0]][p[1]] = "L"

    return len(switchSeats)


def moveRound2(data):
    switchSeats = []
    for i in range(0, len(data)):
        for h in range(0, len(data[i])):
            n = countSeatsInAllDirections(data, i, h)
            if data[i][h] == "L" and n == 0:
                switchSeats.append([i, h])
            elif (data[i][h] == "#") and n >= 5:
                switchSeats.append([i, h])

    for p in switchSeats:
        if data[p[0]][p[1]] == "L":
            data[p[0]][p[1]] = "#"
        elif data[p[0]][p[1]] == "#":
            data[p[0]][p[1]] = "L"

    return len(switchSeats)


def printData(data):
    for a in data:
        print "".join(a)


def loadData(fileName):
    data = []
    with open(fileName, "r") as f:
        for line in f:
            line = line.strip()
            linea = []
            for c in line:
                linea.append(c)
            data.append(linea)
    return data


if __name__ == "__main__":
    data = loadData("input")

    while True:
        if moveRound(data) == 0:
            break

    print "Solution to part 1 {}".format(countSeats(data)[0])
    data = loadData("input")
    while True:
        if moveRound2(data) == 0:
            break

    print "Solution to part 2 {}".format(countSeats(data)[0])
