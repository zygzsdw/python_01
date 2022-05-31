from project_01.select import login
import unittest
import sys


class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    @classmethod
    def tearDownClass(cls) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    def setUp(self) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    def tearDown(self) -> None:
        print('开始运行方法', sys._getframe().f_code.co_name)

    def test_login_success(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 0
        actual_value = login('admin', '888888').get('code')
        self.assertEqual(except_value, actual_value)

    def test_user_wrong(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 1
        actual_value = login('bbb', '888888').get('code')
        self.assertEqual(except_value, actual_value)

    def test_password_is_null(self):
        print('开始运行方法', sys._getframe().f_code.co_name)
        except_value = 2
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    print(suite_a)
    runner = unittest.TextTestRunner()
    runner.run(suite_a)
