from common.basepage import BasePage
from configparser import ConfigParser
from pageobjects.login_page import LoginPage
from time import sleep
from PIL import Image, ImageEnhance

def test1():
    page = BasePage()
    #page.get_url('http://192.168.191.80')
    page.get_url('http://www.baidu.com')

def test2():
    confpath = 'config/config.conf'
    config = ConfigParser()
    config.read(confpath, 'utf-8') # 捕获异常或判断文件是否存在
    test = config.has_option('webdriver', 'borwer_webdriverpath')
    print(test)

    brower_type = ''
    if not brower_type:
        print('不为空')
    else:
        print('为空')

def test3():
    
    LoginPage().login('Admin', '123456', '0241')
    sleep(100)
  


def get_pictures():
    
    img = Image.open('logs/img2.png')
    img = img.convert("RGB")
    enhancer = ImageEnhance.Color(img)
    enhancer = enhancer.enhance(0)
    enhancer = ImageEnhance.Brightness(enhancer)
    enhancer = enhancer.enhance(2)
    enhancer = ImageEnhance.Contrast(enhancer)
    enhancer = enhancer.enhance(8)
    enhancer = ImageEnhance.Sharpness(enhancer)
    img = enhancer.enhance(20)
    img.show()






if __name__ == "__main__":
    print('hello world')
    test3()
    #get_pictures()
# pip freeze --all > requirements.txt
# pip install -r requirements.txt
