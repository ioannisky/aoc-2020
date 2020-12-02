
def countLettersInPassword(password, letter):
    count = 0
    for pletter in password:
        if(letter == pletter):
            count += 1
    return count


def doesPasswordHaveALetterANumberOfTimes(password, letter,
                                          minimum, maximum):
    occurents = countLettersInPassword(password, letter)
    if((occurents >= minimum) and (occurents <= maximum)):
        return True
    return False


def doesPasswordHaveALetterInOneOfTheTwoPositions(password, letter,
                                                  pos1, pos2):
    count = 0
    if(password[pos1-1] == letter):
        count += 1
    if(password[pos2-1] == letter):
        count += 1
    if(count == 1):
        return True
    else:
        return False


if __name__ == "__main__":
    f = open("input", "r")
    correct_password1 = 0
    correct_password2 = 0
    total_password = 0
    for line in f:
        total_password += 1
        seg = line.strip().split(" ")
        num = seg[0].split("-")
        low = int(num[0])
        heigh = int(num[1])
        letter = seg[1][:-1]
        password = seg[2]

        if(doesPasswordHaveALetterANumberOfTimes(password, letter,
                                                 low, heigh)):
            correct_password1 += 1
        if(doesPasswordHaveALetterInOneOfTheTwoPositions(password, letter,
                                                         low, heigh)):
            correct_password2 += 1

    print "Solution 1", correct_password1
    print "Solution 2", correct_password2
