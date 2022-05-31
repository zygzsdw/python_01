user_list = [
    {'role': 'root', 'account': 'dev', 'password': '123456', 'department': 'dev'},
    {'role': 'admin', 'account': 'admin', 'password': '888888', 'department': 'tester'}
]
result = {'message': '登录成功', 'code': 0}


def login(user_name, user_pwd):
    user_lst = []
    if user_name is None or user_name == '':
        result.update({'code': 1, 'message': '用户名不能为空！'})
        return result
    elif user_pwd is None or user_pwd == '':
        result.update({'code': 1, 'message': '密码不能为空！'})
        return result
    else:
        for i in user_list:
            if i['account'] == user_name and i['password'] == user_pwd:
                result['code'] = 0
                if result['code'] == 0:
                    user_lst.append(i)
                    result.update({'code': 0, 'message': '登录成功！', 'user_list': user_lst})
                else:
                    result.update({'code': 1, 'message': '登录失败！'})
                break
            else:
                result.update({'code': 1, 'message': '请检查您的用户名或密码是否填写正确！'})
        return result


if __name__ == '__main__':
    user_name = input('输入用户名：')
    user_pwd = input('输入密码:')
    print(login(user_name, user_pwd))
