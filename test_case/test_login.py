import unittest
from pageobjects.login_page import LoginPage
from common.basepage import BasePage
from time import sleep

class TestLogin(unittest.TestCase):

    # 所有的case执行前都会运行
    def setUp(self):
        self.login_page = LoginPage()
        self.login_page.get_url('http://122.225.207.133:20001')
    # 加了修饰器的case才会调用
    @classmethod
    def setUpClass(cls):
       
        # cls.webdriver = BasePage()
        # cls.webdriver.get_url('http://122.225.207.133:20001')
        # sleep(4)
        pass

    def test_login_success(self):
        #self.webdriver.max_window()
        self.login_page.login('Admin', '123456' ,'1234')
        a = 1 - self.login_page.islogin()
        print(f'-----------------{a}')
        self.assertTrue(a)
    def test_login_faild(self):
        #self.webdriver.max_window()
        self.login_page.login('Admin', '123456' ,'2222')
        self.assertTrue(self.login_page.islogin())
    def test_login_faild2(self):
        #self.webdriver.max_window()
        self.login_page.login('Admin', '123456' ,'2222')
        self.assertFalse(self.login_page.islogin())
    