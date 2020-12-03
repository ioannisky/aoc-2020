"""
Solution 2
==========
Using python generator

"""


class Generator:
    def __init__(self, width, height, slope_x, slope_y):
        self.width = width
        self.height = height
        self.slope_x = slope_x
        self.slope_y = slope_y
        self.top = 0
        self.left = 0

    def __iter__(self):
        return self

    def next(self):
        if self.top >= self.height:
            raise StopIteration
        x = self.left
        y = self.top
        self.top += self.slope_y
        self.left = (self.left + self.slope_x) % self.width
        return x, y


if __name__ == "__main__":
    mapdata = []
    f = open("input", "r")
    for line in f:
        line = line.strip()
        mapdata.append(line)

    height = len(mapdata)
    width = len(mapdata[0])
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    total = 1
    for s in slopes:
        generator = Generator(width, height, s[0], s[1])
        trees = sum([mapdata[y][x] == "#" for x, y in generator])
        print "Trees on slope {}, {} = {}".format(s[0], s[1], trees)
        total *= trees
    print "Total * ", total
