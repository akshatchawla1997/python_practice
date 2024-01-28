class Teacher:
    def teachers_action(self):
        print("I can teach")

class Engineer:
    def Engineers_action(self):
        print("I can code")

class Youtuber:
    def youtubers_action(self):
        print("I can teach as well as code")

class Person(Teacher, Engineer, Youtuber):
    pass

coder = Person()
coder.teachers_action()
coder.Engineers_action()
coder.youtubers_action()