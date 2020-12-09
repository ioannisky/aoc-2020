def findRanage(number, array):
    min_val = 0
    max_val = 0
    n = array[0]
    while n != number:
        if n < number:
            max_val += 1
            n += array[max_val]
        elif n > number:
            n -= array[min_val]
            min_val += 1
    return min_val, max_val


def checkSumOf(number, array):
    for a in range(0, len(array)):
        for b in range(a, len(array)):
            if (array[a] + array[b]) == number:
                return True
    return False


def findNumberwithoutSum(data, length=25):
    for i in range(length, len(data)):
        if not checkSumOf(data[i], data[i - length : i]):
            return data[i]
    return None


if __name__ == "__main__":
    data = []
    with open("input", "r") as f:
        for line in f:
            data.append(int(line.strip()))

    numberWithoutSum = findNumberwithoutSum(data, 25)
    print "Number that has not sum in the previous 25 numbers {}".format(
        numberWithoutSum
    )
    minx, maxx = findRanage(numberWithoutSum, data)
    minn = min(data[minx : maxx + 1])
    maxn = max(data[minx : maxx + 1])
    print "The sum of the min,max of the range of numbers is {}".format(minn + maxn)
