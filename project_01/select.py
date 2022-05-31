from datetime import datetime

result = {'message': '登录失败', 'code': 1}
flag = True


# 读取文件
def from_file_get_data(file_name):
    f = None
    try:
        f = open(file_name, 'r')
        contents = f.readlines()
        for x in contents:
            user_list.append(eval(x))
        return user_list
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()


# 方法 ：向文件中写入内容，用户添加的信息是在原来的基础上添加的。
def save_data(file_name, file_content):
    f = None
    try:
        f = open(file_name, "a")
        f.write('\n' + str(file_content))
    except Exception as e:
        print(e)
    finally:
        if not f:
            f.close()


user_list = []
user_list = user_list if user_list else from_file_get_data(
    f'/Users/zhaoyali/PycharmProjects/pythonProject/python_01/project_01/data.txt')
print(user_list, '000000000')


# 用户登录
def login(user_name, user_pwd):
    user_lst = []
    if user_name is None or user_name == '':
        result.update({'code': 1, 'message': '用户名不能为空！'})
    elif user_pwd is None or user_pwd == '':
        result.update({'code': 1, 'message': '密码不能为空！'})
    else:
        for i in user_list:
            if i.get('account') == user_name and i.get('password') == user_pwd:
                user_lst.append(i)
                result.update({'code': 0, 'message': '登录成功！', 'user_list': user_lst})
                break
            else:
                result.update({'code': 1, 'message': '请检查您的用户名或密码是否填写正确！'})
    print(result)
    return result


class User:

    # 查询用户
    def select(self, username):
        print(result.get('code'))
        if result.get('code') != 1:
            result.update({'user_list': []})
            result_list = []  # 查询到的结果的list
            for i in user_list:
                if username in i['account']:  # 模糊查询
                    i.pop('password')
                    result_list.append(i)
            if result_list:
                result.update({'code': 0, 'message': '查询成功！', 'user_list': result_list})
            else:
                result.update({'code': 12, 'message': '未查到用户，请重新输入！'})
        else:
            result.update({'code': 11, 'message': '用户未登录，没有权限！'})
        print(result)
        return result

    # 添加用户
    def add(self, username, password=123456, **kwargs):
        user_dict = {'account': username, 'password': password}
        user_dict.update(**kwargs)
        # 将组装的数据添加到用户列表中
        user_list.append(user_dict)
        save_data('project_01/data.txt', user_dict)
        result.update({"message": "用户添加成功", "code": 12, "add_time": datetime.now(), "user_list": user_list})


if __name__ == '__main__':

    el = User()
    # 进入循环，方便用户进行各种操作
    while flag:
        vls = input("输入对应编号进行操作："
                    "\n 1:) 进行登录"
                    "\n 2:) 进行查询用户，请输入用户名"
                    "\n 3:) 进行新增用户"
                    "\n q:) 退出操作"
                    "\n 其它字符:) 位置操作，请重新输入:"
                    )
        if vls not in ("1", "2", "3", "q", "quit"):
            print("=" * 30)
            continue
        if vls == "1":
            user_name = input('输入用户名：')
            user_pwd = input('输入密码:')
            login(user_name, user_pwd)
            print("=" * 30)
            continue
        if vls == "2":
            username = input('请输入查询的关键字:')
            el.select(username)
            print("=" * 30)
            continue
        if vls == "3":
            name = input("请输入添加的用户名:")
            get_result = el.select(name)
            if 12 == get_result.get('code'):
                password = input("请输入用户密码:")
                role = input("请输入用户角色:")
                dept = input("请输入用户部门:")
                el.add(name, password, role=role, department=dept)
            if 0 == get_result.get('code'):
                result.update({"code": 13, "message": "用户已存在，无法添加"})
            print(get_result)
            print("=" * 30)
        if vls == "q":
            flag = False
            print('退出成功！')
