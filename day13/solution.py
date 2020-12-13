# 7*(11+13*(3+59*(13+31*6)))

# 0,7,13,1
def searchNumber(addnum, divnum, nextnum, pos, llength):
    rpos = nextnum
    while rpos < pos:
        rpos += nextnum
    reml = rpos - pos
    # print reml
    if reml < 0:
        reml = pos
    # print reml
    for i in range(1, nextnum+1):
        ss = addnum + divnum * i
        # print ss%nextnum
        if ss % nextnum == reml:
            return i
    return None


if __name__ == "__main__":

    minutes = 0
    busids = []
    with open("input", "r") as f:
        minutes = int(f.readline().strip())
        bsis = f.readline().strip().split(",")
        for busid in bsis:
            if busid == "x":
                busids.append(busid)
                continue
            busids.append(int(busid))
    # print minutes
    # print busids
    rem = None
    bid = None

    for busid in busids:
        if busid == "x":
            continue
        c = busid - (minutes % busid)
        if rem == None or rem > c:
            bid = busid
            rem = c
    # print bid,rem,bid*rem
    print "Solution part 1", bid * rem

    # busids=[7,13,"x","x",59,"x",31,19]
    add = 0
    pnum = None

    for i in range(0, len(busids)):
        if busids[i] == "x":
            continue
        if pnum == None:
            pnum = busids[i]
            continue
        # print busids[i],i
        resp = searchNumber(add, pnum, busids[i], i, len(busids))
        add += pnum * resp
        pnum = pnum * busids[i]
        # print resp
        # print pnum
    print "Solution part 2", add
