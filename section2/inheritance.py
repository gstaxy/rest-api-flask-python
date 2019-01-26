class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, **kwargs):
        return cls(friend_name, origin.school, **kwargs)


class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title


anna = WorkingStudent('Anna', 'Oxford', 20000, 'Data Scientist')
print(anna.salary)

friend = WorkingStudent.friend(anna, 'Greg', salary=10000, job_title='Software Developer')
print(friend.name)
print(friend.school)
print(friend.salary)
