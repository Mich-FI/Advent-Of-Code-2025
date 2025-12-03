class DayTwo:

    def fetchfromtext(self):
        with open('ranges.txt', 'r', encoding="utf-8") as f:
            a = f.read().split(',')
        return a
    
    def check_invalid_id(self, list):
        total_invalid_id_sum = 0
        for index, i in enumerate(list):
            first_range, last_range = list[index].split('-', 1)
            total_invalid_id_sum += self.twice_checker(first_range, last_range)
        return total_invalid_id_sum

    def twice_checker(self, first_range, last_range):
        invalid_id_sum = 0
        current_id = int(first_range)
        while current_id <= int(last_range):
            current_id_str = str(current_id)
            if (current_id_str[:(len(current_id_str)//2)]) == (current_id_str[(len(current_id_str)//2):]):
                invalid_id_sum += current_id
            current_id += 1
        return invalid_id_sum

    def main(self):
        print(self.check_invalid_id(self.fetchfromtext()))

if __name__ == "__main__":
    DayTwo().main()
