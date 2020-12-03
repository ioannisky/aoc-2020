def checkTreesOnSlope(mapdata, x_slope, y_slope):
    height = len(mapdata)
    width = len(mapdata[0])
    pos_x = 0
    pos_y = 0
    trees = 0
    # print height,width
    while pos_y < height:
        if mapdata[pos_y][pos_x] == "#":
            trees += 1
        pos_x = (pos_x + x_slope) % width
        pos_y = pos_y + y_slope
    return trees


if __name__ == "__main__":
    mapdata = []
    f = open("input", "r")
    for l in f:
        l = l.strip()
        mapdata.append(l)

    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    total = 1
    for s in slopes:
        trees = checkTreesOnSlope(mapdata, s[0], s[1])
        print "Trees on slope {}, {} = {}".format(s[0], s[1], trees)
        total *= trees

    print "Total * ", total
