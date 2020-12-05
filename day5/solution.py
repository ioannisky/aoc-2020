def findSeat(l, h, string):
    for letter in string:
        mid = (h + l) / 2
        if letter in ["F", "L"]:
            h = mid
        elif letter in ["B", "R"]:
            l = mid + 1
    if l == h:
        return l
    else:
        raise Exception("Invalid Input")


def findSeatId(line):
    row = findSeat(0, 127, line[0:7])
    col = findSeat(0, 7, line[7:10])
    return row * 8 + col


if __name__ == "__main__":
    seats = []
    seatNumber=0
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            sid = findSeatId(line)
            seats.append(sid)
    seats = sorted(seats)
    print "Highiest seat: {}".format(seats[-1])
    for i in range(0, len(seats) - 1):
        if seats[i] + 1 != seats[i + 1]:
            seatNumber=seats[i] + 1
            break
    print "Seat Number: {}".format(seatNumber)