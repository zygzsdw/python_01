# 序列
for x in range(11):
    print(x)
for x in range(1,11,1):
    if x % 2 == 0:
        print(x)
print('=====================')
str = ['red','blue','green']
str.append('yellow')
str.append('black')
print(str)
str.clear()
print(str)
print('=====================')

array1 =  {
    'name': 'xiaoyi',
    'age': '20',
    'sex':'女'
     }
for i in array1.items():
    print(i)