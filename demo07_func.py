# 函数
# 函数的定义
def add(x, y):
    z = x + y
    return z


# 函数的调用
print(add(3, 4))


# 关键字参数
def student_lesson(grade, subject):
    z = "{}年级上{}课".format(grade, subject)
    return z


print(student_lesson(2, '英语'))
print(student_lesson(grade=2, subject='英语'))
print(student_lesson(subject='英语', grade=2))
print(student_lesson(2, subject='英语'))


# 默认参数
def study_language(name, language='python'):
    info = ("{}要学习{}语言".format(name, language))
    return info


print(study_language('一一', 'java'))
print(study_language('小二', 'python'))
print(study_language('小三'))


def add_arg(x, y, *args):
    for i in args:
        z = x + y + i
        return z


print(add_arg(*[1, 3, 4]))


# 面向对象
class Elevator:
    button = "未激活"
    max_people_nums = 15
    floor = 8

    def open(self):
        print("开门")

    def close(self):
        print("关门")

    def run(self):
        print("电梯启动运行")


el = Elevator()
el.open()
el.close()


class Students:
    name = ''
    grade = ''

    def study(self):
        print("{}年纪的学生{}正在学习".format(self.grade, self.name))


s1 = Students()
s1.name = '张三'
s1.grade = '4'
print(s1.study())
