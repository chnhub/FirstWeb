from common.log import logInfo,logError
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from configparser import ConfigParser
import traceback, os
import sys

class BasePage(object):

    def __init__(self, brower_type = 'chrome'):
        '''
            默认为Chrome浏览器，输错为Chrome浏览器。config配置文件可配置浏览器路径，以及浏览器驱动路径。

            brower_type:

                chrome  -> 谷歌浏览器
                firefox -> 火狐浏览器
                ie      -> ie浏览器
        '''
        logInfo('浏览器构造方法')
        #self._webdriver = None
        self._webdriver = webdriver.Chrome.__new__(webdriver.Chrome)
        #(self._webdriver).__class__ = webdriver.Chrome
        # 判断是否初始化为空字符串
        if brower_type.isspace() != True and len(brower_type) !=0 :
            self.open_brower(brower_type)

    def open_brower(self, brower_type):
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
            brower_type = '1'           
        elif 'fire' in brower_type or '火狐' in brower_type:
            brower_type = '2'
        elif 'ie' in brower_type:
            brower_type = '3'
        else:
            brower_type = '1'
        
        #通过配置文件获取浏览器exe的路径
        borwer_path = self.get_config('webdriver', 'borwer_path')
        #通过配置文件获取webdriver的路径
        driver_path = self.get_config('webdriver', 'borwer_webdriverpath')        
        

        if borwer_path :
            options = webdriver.ChromeOptions()
            #options.binary_location = 'E:\\Program\\ChromeMaYi\\guge\\chrome.exe'
            # 设置浏览器路径
            options.binary_location = borwer_path
        try:
            if brower_type == '1':
                logInfo('初始化谷歌浏览器')
                if borwer_path and driver_path:
                    self._webdriver = webdriver.Chrome(executable_path = borwer_path, options = options)
                elif driver_path:
                    self._webdriver = webdriver.Chrome(executable_path = driver_path)
                else:
                    self._webdriver = webdriver.Chrome()
                #self.get_url('http://122.225.207.133:20001')
            elif brower_type == '2':
                logInfo('初始化火狐浏览器')
            elif brower_type == '3':
                logInfo('初始化ie浏览器')
            else:
                logInfo('未初始化浏览器')
        except Exception as err:
                logError(f'初始化浏览器失败，原因：{err}')
                #traceback.print_exc() #直接打印异常 
                logError(traceback.format_exc()) #返回字符串 
                # raise Exception(print('se'))
                raise '浏览器初始化失败，手动抛异常，看上面异常信息。'
        logInfo('初始化函数结尾')
        return self._webdriver       
    def get_webdriver(self):
        return self._webdriver
    def get_url(self, url):
        '''
            传入url参数，浏览器打开url链接
        '''

        
        try:
            self._webdriver.get(url)
        except Exception as err:
            print('进入异常')
            print(err)
    
    def get_element(self, loc, img_doc=''):
        logInfo('查找{}中的元素{}'.format(img_doc,loc))
        try:
            element = self._webdriver.find_element(*loc)
            return element
        except:
            # 日志
            logError('查找元素失败')
            # 截图
            #####

    def click_element(self, loc, img_doc, *args, timeout = 30, firequency = 0.5):
        '''
            点击元素

        '''
        # 1.等待元素

        # 2.找元素
        element = self.get_element(loc, img_doc)
        logInfo(" 点击元素 {}".format(loc))
        # 3.操作
        try:
            element.click()
        except:
            logError('点击元素失败')
            # 截图
            raise
    def input_text(self,loc,img_doc,*args,timeout=30,frequency=0.5):
        '''
            输入文本信息
        '''
        element = self.get_element(loc, img_doc)
        logInfo(" 给元素 {} 输入文本内容:{}".format(loc,args))
        try:
            element.send_keys(*args) 
        except:
            #日志
            #截图
            raise
    def get_element_attribute(self,loc,attr_name,img_doc,timeout=30,frequency=0.5):
        """
        等待元素存在、查找元素、再获取元素的某个属性值。
        :param loc: 元组形式的元素定位表达
        :param attr_name: 要获取的 元素的属性名称
        :param img_doc: 失败截图的文件命名
        :param timeout: 等待元素存在的超时上限。
        :param frequency: 等待元素存在时的，轮询周期。
        :return: 元素的属性值。
        """
        # 等待元素存在
        #self.wait_eleExists(loc,img_doc,timeout,frequency)
        # 查找元素
        ele = self.get_element(loc,img_doc)
        # 获取属性
        try:
            attr_value =  ele.get_attribute(attr_name)
        except:
            # 日志
            logError("获取元素属性失败")
            # 截图
            #self.save_web_screenshot(img_doc)
            raise
        else:
            logInfo("获取元素 {} 的属性 {} 值为:{}".format(loc, attr_name, attr_value))
            return attr_value        
    
    # 查找文本是否存在页面
    def isin_pagesource(self, text):
        '''
            text存在该页面返回Ture，否则返回False。
        '''
        a = text
        b = self._webdriver.page_source 
        #if text.encode("utf-8") in self._webdriver.page_source :
        if a in b :
            return True
        else:
            return False
        
    def max_window(self):
        self._webdriver.maximize_window()
    # 退出浏览器
    def quit(self):
        self._webdriver.quit()
    
    def get_config(self, sections, keys, confpath = 'config/config.conf'):
        '''
            直接获取配置文件中的值。

            parameters：
               
                sections -> 配置文件中的节点
                keys     -> 节点下的键
                path     -> 配置文件路径，不传时默认读取config文件夹下config.conf

            return：keys对应的value。
        '''
        print(os.path.abspath('./'))
        config = ConfigParser()
        conf_value = None
        try:
            if os.path.isfile(confpath):
                config.read(confpath, 'utf-8') # 捕获异常或判断文件是否存在
                if config.has_option(sections, keys):
                    conf_value = config.get(sections, keys)
                else:
                    #logError(f'\'{confpath}\'路径配置文件下，找不到键\'{keys}\'')
                    raise ConfigException(f'找不到\'{confpath}\'路径下的配置文件中的键\'{keys}\'')
            else:
                #logError(f'\'{confpath}\'路径下找不到配置文件')
                raise ConfigException(f'\'{confpath}\'路径下没有该配置文件')
            return conf_value

        # 使用自定义异常
        except ConfigException:
                #logError(err)
                #logError(traceback.format_exc()) #返回字符串 
                #sys.exit()
                return None

        except Exception as identifier:
            logError(f'\'{confpath}\'配置文件异常:\n {identifier}')
            logError(traceback.format_exc()) #返回字符串 
            sys.exit()
            #raise '配置文件的异常，自己看traceback'


    
# 自定义异常处理
class ConfigException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)