from project_01.select import login
import unittest
from parameterized import parameterized
import sys

lst_data = [
    (0, 'admin', '888888'),
    (0, 'dev', '123456'),
    (1, 'aaa', '123456'),
    (1, 'admin', '999999'),
    (1, '', '999999'),
    (1, '111', '')
            ]


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

    @parameterized.expand(lst_data)
    def test_login(self, except_value, username, password):
        actual_value = login(username, password).get('code')
        self.assertEqual(except_value, actual_value)


if __name__ == '__main__':
    unittest.main()
