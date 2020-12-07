class Bag:
    def __init__(self, name):
        self.name = name
        self.contains = list()

    def addContains(self, bag, count):
        self.contains.append({"bag": bag, "count": count})

    def doesContain(self, bagName):
        for k in self.contains:
            if k["bag"].name == bagName:
                return True
            if k["bag"].doesContain(bagName):
                return True
        return False

    def countBags(self):
        ret = 0
        for k in self.contains:
            ret += k["count"] + k["count"] * k["bag"].countBags()
        return ret


if __name__ == "__main__":
    rindex = {}
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            line = line.split(" bags contain ")
            bagName = line[0]
            contains = line[1]
            content = contains.split(", ")
            if bagName not in rindex:
                rindex[bagName] = Bag(bagName)
            for bag in content:
                bag = bag.split(" ")
                containsBagName = " ".join(bag[1:3])
                if containsBagName not in rindex:
                    rindex[containsBagName] = Bag(containsBagName)
                bagNumber = 0
                try:
                    #if bag[0]=="no"
                    bagNumber = int(bag[0])
                except ValueError:
                    continue
                rindex[bagName].addContains(rindex[containsBagName], bagNumber)

    count = 0
    for k, v in rindex.items():
        if v.doesContain("shiny gold"):
            count += 1
    print "shiny gold is contained in {0}".format(count)

    print "shiny gold contains {0} bags".format(
        rindex["shiny gold"].countBags()
        )
