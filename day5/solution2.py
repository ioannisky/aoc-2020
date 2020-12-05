def findSeat(string):
    string = string.replace("F", "0")
    string = string.replace("L", "0")
    string = string.replace("B", "1")
    string = string.replace("R", "1")
    return int(string, 2)


def findSeatId(line):
    row = findSeat(line[0:7])
    col = findSeat(line[7:10])
    return row * 8 + col


if __name__ == "__main__":
    seats = []
    seatNumber = None
    with open("input", "r") as f:
        for line in f:
            line = line.strip()
            sid = findSeatId(line)
            seats.append(sid)
    seats = sorted(seats)
    print "Highiest seat: {}".format(seats[-1])
    for i in range(0, len(seats) - 1):
        if seats[i] + 1 != seats[i + 1]:
            seatNumber = seats[i] + 1
            break
    print "Seat Number: {}".format(seatNumber)