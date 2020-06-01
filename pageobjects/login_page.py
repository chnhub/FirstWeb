from pagelocators.login_page_locator import LoginPageLocator as loc
from common.basepage import BasePage
import pytesseract
import re
from PIL import Image  # 用于打开图片和对图片处理

# 一个用例，一次浏览器的打开和结束。
class LoginPage(BasePage):


    # 登陆功能
    def login(self,user,passwd,vercode):
        self.input_text(loc.user_loc,"登陆页面_输入用户名",user)
        self.input_text(loc.passwd_loc,"登陆页面_输入密码",passwd)
        self.input_text(loc.vercode_loc,"登陆页面_输入密码",vercode)
        #self.click_element(loc.login_button_loc,"登陆页面_点击登陆按钮")
        #print (self.get_element_attribute(loc.verimg_loc, 'src' , '登录页面验证码'))
        #self.request_download(self.get_element_attribute(loc.verimg_loc, 'src' , '登录页面验证码'))
        self.image_str()
    '''
    # //div[@class="form-error-info"]
    # 获取表单区域的错误信息
    def get_error_msg_from_loginForm(self):
        return self.get_element_text(loc.error_notify_from_loginForm,"登陆页面_表单区域错误信息")

    # 获取页面中间的错误信息
    def get_error_msg_from_pageCenter(self):
        return self.get_element_text(loc.error_notify_from_pageCenter,"登陆页面_页面中间错误信息")

    '''
    # 传入url保存图片(此方法不行 需要截图
    def request_download(self, IMAGE_URL):
        import requests
        r = requests.get(IMAGE_URL)
        with open('logs/img2.png', 'wb') as f:
            f.write(r.content)       

       
    def get_pictures(self):
        self._driver.save_screenshot('logs/pictures.png')
        page_snap_obj = Image.open('logs/pictures.png')

        element = self.get_element(loc.verimg_loc, '验证码图片')
        location = element.location
        left = location['x']
        top = location['y']
        size = element.size
        right = left + size['width']
        bottom = top + size['height']
        image_obj = page_snap_obj.crop((left, top, right, bottom))  # 按照验证码的长宽，切割验证码
        # image_obj.show() 
        return image_obj

    def processing_image(self):
        image_obj = self.get_pictures()  # 获取验证码
        img = image_obj.convert("L")  # 转灰度

        pixdata = img.load()
        w, h = img.size
        threshold = 160
        # 遍历所有像素，大于阈值的为黑色
        for y in range(h):
            for x in range(w):
                if pixdata[x, y] < threshold:
                    pixdata[x, y] = 0
                else:
                    pixdata[x, y] = 255
        #img.show()
        return img

    def delete_spot(self):
        images = self.processing_image()
        data = images.getdata()
        w, h = images.size
        black_point = 0
        for x in range(1, w - 1):
            for y in range(1, h - 1):
                mid_pixel = data[w * y + x]  # 中央像素点像素值
                if mid_pixel < 50:  # 找出上下左右四个方向像素点像素值
                    top_pixel = data[w * (y - 1) + x]
                    left_pixel = data[w * y + (x - 1)]
                    down_pixel = data[w * (y + 1) + x]
                    right_pixel = data[w * y + (x + 1)]
                    # 判断上下左右的黑色像素点总个数
                    if top_pixel < 10:
                        black_point += 1
                    if left_pixel < 10:
                        black_point += 1
                    if down_pixel < 10:
                        black_point += 1
                    if right_pixel < 10:
                        black_point += 1
                    if black_point < 1:
                        images.putpixel((x, y), 255)
                    black_point = 0
        # images.show()
        return images

    def image_str(self):
        image = self.delete_spot()
        #pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # 设置pyteseract路径
        result = pytesseract.image_to_string(image)  # 图片转文字
        resultj = re.sub(u"([^\u4e00-\u9fa5\u0030-\u0039\u0041-\u005a\u0061-\u007a])", "", result)  # 去除识别出来的特殊字符
        result_four = resultj[0:4]  # 只获取前4个字符
        # print(resultj)  # 打印识别的验证码
        return result_four

 
