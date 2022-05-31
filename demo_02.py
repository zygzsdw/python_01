# if语句

a = 10
if a>13:
    print(13)
else:
    print(10)

"""多条件判断
if 条件判断1: 代码1
elif 条件判断2: 代码2
elif 条件判断3: 代码3
else: 代码4
"""
score = 76
if score > 90:
    print('优秀')
elif score > 80:
    print('良')
elif score > 60:
    print('及格')
else:
    print('不及格')
print("==============")
a = 0
if a:
    print('返回的是true')
else:
    print('返回的是false')
print("==============")
a = ''
if a:
    print('返回的是true')
else:
    print('返回的是false')
print("==============")
a = None
if a:
    print('返回的是true')
else:
    print('返回的是false')

print("==============")
# 计算1~100内所有数的和
a = 1
sum = 0
while a <= 100:
    sum += a
    a += 1
print(sum)
print("==============")
# range()方法
sum = 0
for x in range(101):
    sum += x
print(sum)

str = []
for x in range(101):
    str.append(x)
print(str)

