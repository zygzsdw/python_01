# a,b,c,d = 'hello world',12,12.1,None
# # type方法
# print(type('hshjh'))
# print(type(111))
#
# # 变量
# print(a,b,c,d)
# print(type(c))
#
# e = a + ' ' + str(b)
# print(e)


a,b = 25,2
# 算数运算符
print(a+b)           #27
print(a-b)           #23
print(a*b)           #50
print(a/b)           #12.5
print(a//b)          #12
print(a%b)           #1
print(a**b)          #625
# 比较运算符
print(a>b)           #true
print(a>=b)          #true
print(a<b)           #false
print(a<=b)          #false
print(a==b)          #false
print(a!=b)          #true
print(a is b)        #false
print(a is not b)    #true
# 赋值运算符
a,b = 25,2
a+=b
print(a)            #27
a-=b
print(a)            #25
a*=b
print(a)            #50
a/=b
print(a)            #25
a%=b
print(a)            #1
a**=b
print(a)            #1
a//=b
print(a)            #0
# 逻辑运算符
# a=0,b=2
a>0,b>1
print(a and b)     # 0
print(a or b)      # 2
print(not a)       #true
