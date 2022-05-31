# 字符串格式化
my_str = 'my name is %s' % '张三'
print(my_str)
# 格式化整数
my_str1 = '张三今年 %d 岁' % 20
print(my_str1)
# 格式化浮点数
my_str2 = '一斤苹果 %f元' % 500
print(my_str2)

my_str3 = '一斤苹果 %.2f元' % 500000
print(my_str3)

my_str4 = '一斤苹果 %5.2f元' % 5.4
print(my_str4)

my_str6 = '一斤苹果 %-6.2f元' % 5.4
print(my_str6)

my_str5 = '一斤苹果 %+5.2f元' % 5.4
print(my_str5)

# format()
print("今天星期{}，张三买了{}斤苹果".format('二', 3))

print("我是关键字参数:{x}! {y}".format(x='hello', y='python'))
