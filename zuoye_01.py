# 1. 输入a,b,c,d4个整数，计算a+b-c*d的结果
# a = int()
# b = int()
# c = int()
# d = int()
#
#
# def func(a, b, c, d):
#     print('计算a+b-c*d的结果:', a + b - c * d)
#
#
# func(6, 4, 5, 3)

a = int(input('输入整数：'))
b = int(input('输入整数：'))
c = int(input('输入整数：'))
d = int(input('输入整数：'))
print('计算a+b-c*d的结果:', a + b - c * d)
# 2.打印1~100内被3整除的所有数的和
sum1 = 0
for i in range(1, 101, 1):
    if i % 3 == 0:
        sum1 += i
print('被3整除的所有数的和:', sum1)

sum2 = 0
x = 1
# 方法2
while x <= 100:
    if x % 3 == 0:
        sum2 += x
    x += 1
print(sum2)
# 3.使用range()输出1~10内的所有奇数
for i in range(1, 11, 1):
    if i % 2 == 1:
        print('奇数:', i)
# 方法2
for i in range(1, 11, 2):
    print('奇数:', i)
# 4.打印1~100所有偶数的和 减去 所有奇数的和 的值
even_sum, odd_sum = 0, 0
for i in range(1, 101, 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print('所有偶数的和减去所有奇数的和的值:', even_sum - odd_sum)
# 5.求1+2+3+...+100的和
sum3 = 0
for i in range(1, 101, 1):
    sum3 += i
print('求1+2+3+...+100的和:', sum3)


# 6.判断一个数n能同时被3和5整除
x = int(input('输入整数：'))
if x % 3 == 0 and x % 5 == 0:
    print('能同时被3和5整除')
else:
    print('不能能同时被3和5整除')
# 7.定义一个整数变量，判断该变量值是否是1-100内的某个数，如果是打印出来
n = int(input('输入一个数：'))
if 1 <= n <= 100:
    print(n, '在1-100内')
else:
    print(n, '不在在1-100内')
# 8.输入三个整数x,y,z，请把这三个数由小到大输出。备注：输入方法：input()
arr = []
x = int(input('输入x: '))
y = int(input('输入y: '))
z = int(input('输入z: '))
arr.append(x)
arr.append(y)
arr.append(z)
arr.sort()
print(arr)
# 9. 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。备注：需要使用input()方法
score = int(input('输入分数：'))
if score >= 90:
    print('学习成绩:A')
elif 60 <= score <= 89:
    print('学习成绩:B')
else:
    print('学习成绩:C')
# 10. 将一个列表的数据复制到另一个列表中。
list1 = ['red', 1, 89.9, None]
list2 = ['hello', 33, 'world']
list2.extend(list1)
print(list2)
# 11.输出 9*9 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(str(j) + str("*") + str(i) + "=" + str(i * j), end="\t")
    print()
# 12.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
s = input('输入一个字符串:')
num = 0
letter = 0
spc = 0
other = 0
for i in s:
    if i.isdigit():
        num += 1
    elif i.isalpha():
        letter += 1
    elif i.isspace():
        spc += 1
    else:
        other += 1
print('英文字母有' + str(letter) + '个', '空格有' + str(spc) + '个', '数字有' + str(num) + '个', '其它有' + str(other) + '个')
# 13. 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
num = input("输入要相加的数字：")
count = int(input("输入要想加的个数："))
a = []
s = 0
for i in range(1, count + 1):
    a.append(num * i)
    s += int(num * i)
print(f"{s} = {'+'.join(a)}")
# 打印出如下图案（菱形）:
s = '*'
for i in range(1, 8, 2):
    print((s * i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s * i).center(7))
