import math


class ShipState2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = 1
        self.ang = 90

    def addAngle(self, ang):
        na = self.ang + ang
        diff = self.ang - na
        if diff == 90:
            z = self.wx
            self.wx = -1 * self.wy
            self.wy = z
        elif abs(diff) == 180:
            self.wx = -1 * self.wx
            self.wy = -1 * self.wy
        elif diff == 270:
            z = self.wx
            self.wx = self.wy
            self.wy = -1 * z
        elif diff == -90:
            z = self.wx
            self.wx = self.wy
            self.wy = -1 * z
        elif diff == -270:
            z = self.wx
            self.wx = -1 * self.wy
            self.wy = z
        else:
            raise Exception("Invalid diff angle " + str(diff))
        self.ang = na

    def processState(self, inst, num):
        if inst == "N":
            self.wy += num
        elif inst == "S":
            self.wy -= num
        elif inst == "E":
            self.wx += num
        elif inst == "W":
            self.wx -= num
        elif inst == "L":
            self.addAngle(-num)
            # self.ang-=num
        elif inst == "R":
            self.addAngle(num)
            # self.ang+=num
        elif inst == "F":
            self.x += num * (self.wx)
            self.y += num * (self.wy)
        else:
            raise Exception("Invalid instruction " + inst)

    def getManhattanDistance(self):
        return abs(self.x) + abs(self.y)

    def __repr__(self):
        return "X: {} Y: {} WX: {} WY: {} ANG: {}".format(
            self.x, self.y, self.wx, self.wy, self.ang
        )


class ShipState:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.ang = 90

    def translateAngle(self):

        if self.ang >= 360:
            self.ang = self.ang % 360
        if self.ang < 0:
            self.ang = 360 + self.ang

        if self.ang == 0:
            return "N"
        if self.ang == 90:
            return "E"
        if self.ang == 180:
            return "S"
        if self.ang == 270:
            return "W"
        raise Exception("Not valid angle " + str(self.ang))

    def __repr__(self):
        return "X: {} Y: {} ANG: {}".format(self.x, self.y, self.ang)

    def processState(self, inst, num):
        if inst == "N":
            self.y += num
        elif inst == "S":
            self.y -= num
        elif inst == "E":
            self.x += num
        elif inst == "W":
            self.x -= num
        elif inst == "L":
            self.ang -= num
        elif inst == "R":
            self.ang += num
        elif inst == "F":
            self.processState(self.translateAngle(), num)
        else:
            raise Exception("Invalid instruction " + inst)

    def getManhattanDistance(self):
        return abs(self.x) + abs(self.y)


if __name__ == "__main__":
    ss = ShipState()
    ss2 = ShipState2()
    with open("input", "r") as f:
        for inst in f:
            inst = inst.strip()
            ss.processState(inst[0], int(inst[1:]))
            ss2.processState(inst[0], int(inst[1:]))

    print "Solution for distance 1: {}".format(ss.getManhattanDistance())
    print "Solution for distance 2: {}".format(ss2.getManhattanDistance())
