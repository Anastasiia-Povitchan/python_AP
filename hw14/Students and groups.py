class Student:

    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def __repr__(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}, Оценка: {self.grades}"


class Group:
    spisok = []

    @staticmethod
    def add(student):
        Group.spisok.append(student)


st1 = Student('Megan', 'Hudson', 4),
st2 = Student('Kelsey', 'Bishop', 3),
st3 = Student('Jessica', 'Miller', 5),
st4 = Student('David', 'Brown', 5),
st5 = Student('Christina', 'Stanley', 2)

Group.add(st1)
Group.add(st2)
Group.add(st3)
Group.add(st4)
Group.add(st5)
print(Group.spisok)
