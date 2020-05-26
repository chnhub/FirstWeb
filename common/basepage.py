from common.logging import *

class BasePage(object):

    def __init__(self):
        print('初始化')
        __self__ = self
    
    def open_brower(self, brower_type = 'chrome'):
        '''
            默认为Chrome浏览器，输错为Chrome浏览器。

            brower_type:

                chrome  -> 谷歌浏览器
                firefox -> 火狐浏览器
                ie      -> ie浏览器
        '''
        debug('调用浏览器')
        brower_type = str(brower_type)
        if 'chrome' in brower_type or '谷歌' in brower_type:
            debug('使用chrome浏览器')
            brower_type = '1'
            
        elif 'fire' in brower_type or '火狐' in brower_type:
            brower_type = '2'
        elif 'ie' in brower_type:
            brower_type = '3'
        else:
            brower_type = '1'
        

    
    def open_url(self, url):
        '''
            传入url参数，浏览器打开url链接
        '''
        pass


    def quit(self):
        pass
