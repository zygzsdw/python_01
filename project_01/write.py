# 打开文件


data = [
    "{'role': 'test', 'account': 'test', 'password': '123456', 'department': 'tester'}"
]
try:
    f = open("data.txt", "a")
    for line in data:
        f.write(line  + '\n')
except (ValueError, NameError, FileNotFoundError) as result:
    print("存在异常，正在处理...", result)
finally:
    if f:
        f.close()
