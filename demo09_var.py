# 变量
class Students():

    # def __init__(self,name,grade):
    #     self.name = name
    #     self.grade = grade

    def __init__(self, score):
        self.score = score

    def get_score(self, sex):
        # return self.__score
        print("{},{}".format(self.score, sex))

    def study(self, course):
        print("学生{},目前{}年级,正在学习{}".format(self.name, self.grade, course))


s = Students('张三')
s.get_score('语文课')
