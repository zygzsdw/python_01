class Students:
    name = ''
    grade = ''

    def __init__(self, grade, name):
        self.name = name
        self.grade = grade

    def study(self):
        print("{}年纪的学生{}正在学习".format(self.grade, self.name))


s1 = Students("张三", 4)
s1.study()
