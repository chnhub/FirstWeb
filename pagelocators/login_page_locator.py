# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By
class LoginPageLocator:
    # 用户名输入框
    user_loc = (By.XPATH,'//*[@id="usrid"]')
    # 密码输入框
    passwd_loc = (By.XPATH,'//*[@id="pwd"]')
    # 验证码
    vercode_loc = (By.XPATH,'//*[@id="vercode"]')
    # 验证码图片
    verimg_loc = (By.XPATH,'//*[@id="imagecode"]')

    # 登录按钮
    login_button_loc = (By.XPATH,'//*[@id="button1"]')
    # 提示框 - 登陆表单区域
    #error_notify_from_loginForm = (By.XPATH, '//div[@class="form-error-info"]')
    # 提示框 - 页面中间区域
    #error_notify_from_pageCenter = (By.XPATH,'//div[@class="layui-layer-content"]')
