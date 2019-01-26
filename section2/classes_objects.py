lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (1, 2, 3, 4, 5, 6)
}


class LotteryPlayer:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf', (1, 2, 3))
player_two = LotteryPlayer('John', (2, 3, 4))

# print(player_one.name == player_two.name)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        print("I'm going to school")
        #print("I'm a {}".format(cls))


anna = Student('Anna', 'MIT')
rolf = Student('Rolf', 'Havard')

anna.marks.append(56)
anna.marks.append(52)
Student.go_to_school()
