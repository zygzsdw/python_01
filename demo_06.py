# 列表索引
lst = ['1', '1.1', 'red']
print(lst.index('1'))
print(lst[0])

# 切片   seq[start,end,step]
lst5 = ['red', 'green', 'blue', 'black', 'gold', 'orange']
print(lst5[0:4:1])  # 获取第一个到第4个元素
print(lst5[1:6:2])  # 获取偶数的元素

print(lst5[:2])
print(lst5[::2])

print(lst5[2:])

print(lst5[::-1])

lst6 = ['red', 'green', 'blue', 'black', 'gold', 'orange', '1', '2', '3', '4']
print(lst6[::2])
# lst6 = ('red', 'green', 'blue', 'black', 'gold', 'orange')
# print(lst6[0:4:1])
# print(lst6[1:6:2])
#
# lst7 = 'redgreen'
# print(lst7[0:4:1])
# print(lst7[1:6:2])
print('=' * 30)
lst7 = ['1', '2', '3', '4', '5']
str2 = ''
for i in str(lst7):
    # if i.isdigit():
    #     str2 += i
    if i not in ["[", "]", ",", "'", " "]:
        str2 += i
print(str2)
print(''.join(lst7))


lst7 = ['1', '2', '3', '4', '5']
print(str(lst7).split(','))
print(type(str(lst7).split(',')))
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(str(j) + str("*") + str(i) + "=" + str(i * j), end="\t")
#     print()

