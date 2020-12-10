if __name__ == "__main__":
    data = [0]
    with open("input", "r") as f:
        for line in f:
            data.append(int(line))
    data = sorted(data)
    data.append(data[-1] + 3)
    diffIndex = [0, 0, 0, 0]
    diffArray = []
    for i in range(1, len(data)):
        diff = data[i] - data[i - 1]
        diffArray.append(diff)
        diffIndex[diff] += 1

    counter = 0
    onesInSequence = []
    for i in range(0, len(diffArray)):
        if diffArray[i] == 1:
            counter += 1
        else:
            if counter != 0:
                onesInSequence.append(counter)
            counter = 0

    counter = 1
    for ois in onesInSequence:
        if ois - 1 == 0:
            continue
        ois - 1
        res = (ois - 1) * (ois) / 2
        counter *= res + 1

    print diffIndex[1] * diffIndex[3]
    print counter