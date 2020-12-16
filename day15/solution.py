def loopForRange(data, last, start, end):
    for i in range(start, end):
        pa = data[last]
        # print data[last]
        ps = pa[-1]
        pf = i - 1
        if len(pa) != 1:
            ps = pa[-2]
            pf = pa[-1]
        new = pf - ps
        if new not in data:
            data[new] = []
        data[new].append(i)
        data[new] = data[new][-2:]
        last = new
    return last


if __name__ == "__main__":
    data = {}
    startTurns = [2, 20, 0, 4, 1, 17]
    # startTurns=[1,3,2]
    # startTurns=[0,3,6]
    last = None
    for i in range(0, len(startTurns)):
        num = startTurns[i]
        if num not in data:
            data[num] = []
        data[num].append(i)
        last = startTurns[i]
    # print last
    last = loopForRange(data, last, len(startTurns), 2020)
    print "Solution 1 {}".format(last)
    last = loopForRange(data, last, 2020, 30000000)
    print "Solution 2 {}".format(last)
