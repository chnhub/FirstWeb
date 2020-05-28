from common.log import logInfo,logError
from selenium import webdriver
from configparser import ConfigParser
import traceback, os

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

        try:
            path_driver = self.get_config('config/config.conf', 'webdriver', 'borwer_webdriverpath')
            if brower_type == '1':
                logInfo('选择谷歌浏览器')
                self.driver = webdriver.Chrome(path_driver)
                #self.driver = webdriver.Chrome('E:/Program/ChromeMaYi/guge/chromedriver')
                self.driver.get('http://www.baidu.com')
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
    
    def get_config(self, confpath, sections, keys):
        '''
            直接获取配置文件中的值。

            parameters：

                path     -> 配置文件路径
                sections -> 配置文件中的节点
                keys     -> 节点下的键

            return：keys对应的value。
        '''
        config = ConfigParser()
        conf_value = None
        if os.path.isfile(confpath):
            config.read(confpath, 'utf-8') # 捕获异常或判断文件是否存在
            value_config = ''
            if config.has_option(sections, keys):
                conf_value = config.get(sections, keys)
            else:
                logError(f'\'{confpath}\'路径配置文件下，找不到键{keys}')
        else:
            logError(f'\'{confpath}\'路径下找不到配置文件')
        return conf_value