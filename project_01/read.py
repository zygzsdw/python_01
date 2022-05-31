user_list = []


class Read:

    def read(self):
        f = None
        try:
            f = open("/Users/zhaoyali/PycharmProjects/pythonProject/python_01/project_01/data.txt", 'r')
            contents = f.readlines()
            for x in contents:
                # print(x, end="")
                user_list.append(eval(x.strip("\n")))
        except Exception as e:
            print(e)
        finally:
            if f:
                f.close()


el = Read()
el.read()
