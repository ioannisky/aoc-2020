import sys


class Cube:
    def __init__(self):
        self.z_min = 0
        self.z_max = 0
        self.y_min = 0
        self.y_max = 0
        self.x_min = 0
        self.x_max = 0
        self.active = {}

    def setActive(self, z, y, x):
        self.z_min = min(self.z_min, z)
        self.z_max = max(self.z_max, z)
        self.y_min = min(self.y_min, y)
        self.y_max = max(self.y_max, y)
        self.x_min = min(self.x_min, x)
        self.x_max = max(self.x_max, x)
        key = "{}_{}_{}".format(z, y, x)
        self.active[key] = "#"

    def isActive(self, z, y, x):
        key = "{}_{}_{}".format(z, y, x)
        if key in self.active:
            return True
        return False

    def setInactive(self, z, y, x):
        key = "{}_{}_{}".format(z, y, x)
        if key in self.active:
            del self.active[key]

    def round(self):
        active = []
        inactive = []
        for q in range(self.z_min - 1, self.z_max + 2):
            for i in range(self.y_min - 1, self.y_max + 2):
                for h in range(self.x_min - 1, self.x_max + 2):
                    n = self.getNeighbors(q, i, h)
                    if self.isActive(q, i, h):
                        if n in [2, 3]:
                            continue
                        else:
                            inactive.append([q, i, h])

                    else:
                        if n == 3:
                            active.append([q, i, h])

        for a in active:
            self.setActive(a[0], a[1], a[2])
        for i in inactive:
            self.setInactive(i[0], i[1], i[2])

    def getNeighbors(self, z, y, x):
        count = 0
        for q in range(z - 1, z + 2):
            for i in range(y - 1, y + 2):
                for h in range(x - 1, x + 2):
                    if q == z and i == y and h == x:
                        continue
                    key = "{}_{}_{}".format(q, i, h)
                    if key in self.active:
                        count += 1
        return count

    def printCube(self):
        for q in range(self.z_min, self.z_max + 1):
            sys.stdout.write("{}---\n".format(q))
            for i in range(self.y_min, self.y_max + 1):
                for h in range(self.x_min, self.x_max + 1):
                    key = "{}_{}_{}".format(q, i, h)
                    if key in self.active:
                        sys.stdout.write("#")
                    else:
                        sys.stdout.write(".")
                sys.stdout.write("\n")


class Cube2:
    def __init__(self):
        self.w_min = 0
        self.w_max = 0
        self.z_min = 0
        self.z_max = 0
        self.y_min = 0
        self.y_max = 0
        self.x_min = 0
        self.x_max = 0
        self.active = {}

    def setActive(self, w, z, y, x):
        self.w_min = min(self.w_min, w)
        self.w_max = max(self.w_max, w)
        self.z_min = min(self.z_min, z)
        self.z_max = max(self.z_max, z)
        self.y_min = min(self.y_min, y)
        self.y_max = max(self.y_max, y)
        self.x_min = min(self.x_min, x)
        self.x_max = max(self.x_max, x)
        key = "{}_{}_{}_{}".format(w, z, y, x)
        self.active[key] = "#"

    def isActive(self, w, z, y, x):
        key = "{}_{}_{}_{}".format(w, z, y, x)
        if key in self.active:
            return True
        return False

    def setInactive(self, w, z, y, x):
        key = "{}_{}_{}_{}".format(w, z, y, x)
        if key in self.active:
            del self.active[key]

    def round(self):
        active = []
        inactive = []
        for f in range(self.w_min - 1, self.w_max + 2):
            for q in range(self.z_min - 1, self.z_max + 2):
                for i in range(self.y_min - 1, self.y_max + 2):
                    for h in range(self.x_min - 1, self.x_max + 2):
                        n = self.getNeighbors(f, q, i, h)
                        # print f,q,i,h,"->",n
                        if self.isActive(f, q, i, h):
                            if n in [2, 3]:
                                continue
                            else:
                                inactive.append([f, q, i, h])
                        else:
                            if n == 3:
                                active.append([f, q, i, h])

        for a in active:
            self.setActive(a[0], a[1], a[2], a[3])
        for i in inactive:
            self.setInactive(i[0], i[1], i[2], i[3])

    def getNeighbors(self, w, z, y, x):
        count = 0
        rcount = 0
        for f in range(w - 1, w + 2):
            for q in range(z - 1, z + 2):
                for i in range(y - 1, y + 2):
                    for h in range(x - 1, x + 2):
                        if f == w and q == z and i == y and h == x:
                            continue
                        rcount += 1
                        key = "{}_{}_{}_{}".format(f, q, i, h)
                        if key in self.active:
                            count += 1
        return count

    def printCube(self):
        for f in range(self.w_min, self.w_min + 1):
            for q in range(self.z_min, self.z_max + 1):
                sys.stdout.write("{} {}---\n".format(f, q))
                for i in range(self.y_min, self.y_max + 1):
                    for h in range(self.x_min, self.x_max + 1):
                        key = "{}_{}_{}_{}".format(f, q, i, h)
                        if key in self.active:
                            sys.stdout.write("#")
                        else:
                            sys.stdout.write(".")
                    sys.stdout.write("\n")


"""
def getNeibours(data,z,y,x):
    startz=z-1
    endz=z+2
    starty=y-1 
    endy=y+2
    startx=x-1 
    endx=x+2
    count=0
    for q in range(startz,endz):
        for i in range(starty,endy):
            for h in range(startx,endx):
                if(i==y and h==x):
                    continue
                if(data[i][h]=="#"):
                    count+=1
    return count    



def playRound(data):
    switch=[]
    for i in range(0,len(data)):
        for h in range(0,len(data[i])):
            n=getNeibours(data,i,h)
            if(data[i][h]=="#"):
                if(n in [2,3]):
                    continue
                else:
                    switch.append([i,h])
            elif(data[i][h]=="." and n==3):
                switch.append([i,h])
    for a in switch:
        y=a[0]
        x=a[1]
        if(data[y][x]=="."):
            data[y][x]="#"
        elif(data[y][x]=="#"):
            data[y][x]="."
        else:
            raise Exception("Invalid datat "+data[y][x])




def printData(data):
    for l in data:
        print "".join(l)

def countActive(data):
    count=0
    for i in data:
        for x in i:
            if(x=="#"):
                count+=1
    return count
"""


def readData(fileName, cube):
    z = 0
    y = 0
    with open(fileName, "r") as f:
        for line in f:
            x = 0
            for letter in line.strip():
                if letter == "#":
                    cube.setActive(z, y, x)
                x += 1
            y += 1


def readData2(fileName, cube):
    w = 0
    z = 0
    y = 0
    with open(fileName, "r") as f:
        for line in f:
            x = 0
            for letter in line.strip():
                if letter == "#":
                    cube.setActive(w, z, y, x)
                x += 1
            y += 1


if __name__ == "__main__":

    c = Cube()
    readData("input", c)
    for i in range(0, 6):
        c.round()
    print "Solution Part 1 {}".format(len(c.active))

    c = Cube2()
    readData2("input", c)
    for i in range(0, 6):
        c.round()
    print "Solution Part 2 {}".format(len(c.active))
