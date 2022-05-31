from project_01.select import login
import unittest
import sys
from package_unittest.HTMLTestRunner import HTMLTestRunner


class TestLogin(unittest.TestCase):

    def test_login_success(self):
        except_value = 0
        actual_value = login('admin', '888888').get('code')
        self.assertEqual(except_value, actual_value)

    def test_user_wrong(self):
        except_value = 1
        actual_value = login('bbb', '888888').get('code')
        self.assertEqual(except_value, actual_value)

    def test_password_is_null(self):
        except_value = 2
        actual_value = login('admin', '').get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':
    suite_a = unittest.TestSuite()
    suite_a.addTest(TestLogin('test_login_success'))
    suite_a.addTest(TestLogin('test_user_wrong'))
    suite_a.addTest(TestLogin('test_password_is_null'))
    print(suite_a)

    test_report = './test_report.html'
    with open(test_report, 'wb') as f:
        # runner = unittest.TextTestRunner()
        runner = HTMLTestRunner(f, title='测试报告', description='测试报告描述')
        runner.run(suite_a)
