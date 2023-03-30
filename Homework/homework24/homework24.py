class Student:
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()

    def show(self):
        print(self.name, '=>', self.laptop.name)

    class Laptop:
        def __init__(self):
            self.name = 'HP, i7, 16'


first_student = Student('Roman')
first_student.show()
second_student = Student('Vladimir')
second_student.show()
