# 使用try...except
def div(x, y):
    try:
        z = x / y
        return z
    except Exception as e:
        print('不能被0整除')


div(4, 0)
