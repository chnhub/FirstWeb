from common.log import logInfo
from selenium import webdriver
import traceback

class BasePage(object):

    def __init__(self):
        logInfo('浏览器构造方法')
    
    def open_brower(self, brower_type = 'chrome'):
        '''
            默认为Chrome浏览器，输错为Chrome浏览器。

            brower_type:

                chrome  -> 谷歌浏览器
                firefox -> 火狐浏览器
                ie      -> ie浏览器
        '''
        logInfo('调用浏览器')
        brower_type = str(brower_type)
        if 'chrome' in brower_type or '谷歌' in brower_type:
            logInfo('使用chrome浏览器')
            brower_type = '1'
            
        elif 'fire' in brower_type or '火狐' in brower_type:
            brower_type = '2'
        elif 'ie' in brower_type:
            brower_type = '3'
        else:
            brower_type = '1'

        path_driver = 'E:/Program/ChromeMaYi/guge/chromedriver'
        try:
            if brower_type == '1':
                logInfo('选择谷歌浏览器')
                driver = webdriver.Chrome(path_driver)
                driver.get('http://www.baidu.com')
                #time.sleep(10)
                logInfo('倒计时结束')
            elif brower_type == '2':
                logInfo('选择火狐浏览器')
            elif brower_type == '3':
                logInfo('选择ie浏览器')
            else:
                logInfo('未选择')
        except Exception as err:
                logInfo(f'初始化浏览器失败，原因：{err}')
                #traceback.print_exc() #直接打印异常 
                logInfo(traceback.format_exc()) #返回字符串 
                
        logInfo('初始化函数结尾')

    
    def open_url(self, url):
        '''
            传入url参数，浏览器打开url链接
        '''
        pass


    def quit(self):
        pass
