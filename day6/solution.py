def getLetters(cmap, line):
    for char in line:
        if char not in cmap:
            cmap[char] = 1
        else:
            cmap[char] += 1


def getNumberOfItemsEqual(cmap, memberCount):
    count = 0
    for k, v in cmap.items():
        if v == memberCount:
            count += 1
    return count


if __name__ == "__main__":
    totalAnswersOfGroup = 0
    totalCommonAnswersOfGroup = 0
    with open("input", "r") as f:
        cmapGroup = {}
        memberCount = 0
        for line in f:
            line = line.strip()
            if line == "":
                totalCommonAnswersOfGroup += getNumberOfItemsEqual(
                    cmapGroup, memberCount
                )
                totalAnswersOfGroup += len(cmapGroup)
                cmapGroup = {}
                memberCount = 0
                continue
            getLetters(cmapGroup, line)
            memberCount += 1

        totalAnswersOfGroup += len(cmapGroup)
        totalCommonAnswersOfGroup += getNumberOfItemsEqual(
            cmapGroup, memberCount
        )

    print "Total Answers of Group", totalAnswersOfGroup
    print "Total Common Answers of Group", totalCommonAnswersOfGroup
