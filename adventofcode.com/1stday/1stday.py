class DayOne:

    def __init__(self):
        self.saved_number = 50

    def fetchfromtext(self):
        zero_counter = 0
        start = self.saved_number
        with open('commands.txt', 'r', encoding="utf-8") as file:
            a = [line.strip() for line in file]
        for i in a:
            s = int(i[1:])
            if i[0] == 'R':
                start += s
                while start > 99:
                    start = start - 100
                if start == 0:
                    zero_counter += 1
            else:
                start -= s
                while start < 0:
                    start = start + 100
                if start == 0:
                    zero_counter += 1
        print(zero_counter)
        return zero_counter

    def main(self):
        self.fetchfromtext()

if __name__ == "__main__":
    DayOne().main()
