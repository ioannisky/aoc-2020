class PasswordValidator:
    def __init__(self, password, char, low, high):
        self.password = password
        self.char = char
        self.minimum = low
        self.maximum = high

    def countLettersInPassword(self):
        count = 0
        for pletter in self.password:
            if self.char == pletter:
                count += 1
        return count

    def doesPasswordHaveALetterANumberOfTimes(self):
        occurents = self.countLettersInPassword()
        if (occurents >= self.minimum) and (occurents <= self.maximum):
            return True
        return False

    def doesPasswordHaveALetterInOneOfTheTwoPositions(self):
        count = 0
        if self.password[self.minimum - 1] == self.char:
            count += 1
        if self.password[self.maximum - 1] == self.char:
            count += 1
        if count == 1:
            return True
        else:
            return False


class Parser:
    def __init__(self, opened_file):
        self.opened_file = opened_file

    def readLine(self):
        num1 = self.readUntil("-")
        num2 = self.readUntil(" ")
        char = self.readUntil(":")
        password = self.readUntil("\n")
        data = [num1, num2, char, password]
        if None in data:
            return None
        else:
            password = password.strip()
            return PasswordValidator(password, char, int(num1), int(num2))

    def readUntil(self, stop_char):
        string = ""
        while True:
            char = self.opened_file.read(1)
            if char == "":
                return None
            if char == stop_char:
                return string
            else:
                string += char


class FileReader:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "r")
        return Parser(self.file)

    def __exit__(self, type, value, traceback):
        self.file.close()


if __name__ == "__main__":
    correct_password1 = 0
    correct_password2 = 0

    with FileReader("input") as parser:
        while True:
            p = parser.readLine()
            if p is None:
                break
            if p.doesPasswordHaveALetterANumberOfTimes():
                correct_password1 += 1
            if p.doesPasswordHaveALetterInOneOfTheTwoPositions():
                correct_password2 += 1

    print "Solution 1", correct_password1
    print "Solution 2", correct_password2
