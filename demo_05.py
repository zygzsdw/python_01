str_01 = 'hj'
print(str_01.join('world'))


str_02 = 'hello world java html css php'
print(str_02.split(' '))


print(str_02.find('j'))
print(str_02.index('j'))
print(len(str_02))
print(str_02.replace('world','python'))


# 12.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数
letter = 0
space = 0
num = 0
other = 0
str_03 = input('输入一个字符串：')
for i in str_03:
    if i.isalpha():
        letter += 1
    elif i.isdigit():
        num += 1
    elif i.isspace():
        space += 1
    else:
        other += 1
print('英文字母有' + str(letter) + '个,空格有' + str(space) + '个,数字有' + str(num) + '个,其它字符有' + str(other) + '个')


