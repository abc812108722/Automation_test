from appium import webdriver
import unittest
import time, os
from common import *
from TextInfo import *

count = 1


class Testandroid(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        de = {}
        de['platformName'] = 'Android'
        de['platformVersion'] = '10'
        de['deviceName'] = '822ccaaa'
        de['appPackage'] = 'com.lenovo.homeedgeserver'
        de['appActivity'] = 'com.lenovo.homeedgeserver.ui.start.LauncherActivity'
        de['newCommandTimeout'] = 10000
        de['unicodeKeyboard'] = True
        de['resetKeyboard'] = True

        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', de)
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        # remove_img(screenshot_path)
        pass


    def setUp(self):
        global count
        print("*****************Starting Excute TestCase %s *******************" % count)

        count = count + 1

    # 第一次打开软件软件许可和服务协议提示
    def test_1firstlogin_protocol_info(self):
        # a=self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_link_title")
        if elementIsExist(
                self.driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button')):
            self.driver.find_element_by_id("com.lbe.security.miui:id/permission_allow_foreground_only_button").click()
        text1 = self.driver.find_elements_by_class_name("android.widget.TextView")[0].text
        self.assertEqual(text1, "软件许可和服务协议及隐私政策", msg="标题文本信息不一致")
        # self.assertEqual(self.driver.find_elements_by_class_name("android.widget.TextView")[1].text,second,msg="内容文本信息不一致")
        self.assertEqual(self.driver.find_elements_by_class_name("android.widget.TextView")[2].text.strip(),
                         "您可以通过阅读完整版《联想许可和服务协议》和《隐私政策》了解详细信息。", msg="结尾文本信息不一致")
        self.assertEqual(elementIsExist(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_agree")), 1,
                         msg="同意按钮不存在")
        self.assertEqual(elementIsExist(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_disagree")), 1,
                         msg="不同意按钮不存在")
        self.driver.get_screenshot_as_file(screenshot_path + '1.png')
        cmp_img(os.path.join(screenshot_path, '1.png'), os.path.join(screenshot_origin_path, '1.png'))

    # 跳转到登录界面，检查登录界面元素
    def test_2click_agree(self):
        self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_agree").click()
        self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_start_use").click()
        time.sleep(3)
        self.driver.get_screenshot_as_file('E:\\screenshot\\2.png')
        cmp_img('E:\\screenshot\\2.png','C:\\Users\\530s\\PycharmProjects\\untitled\\screenshot_origin\\2.png')
        self.assertEqual(
            elementIsExist(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_login_register")), 1,
            msg="立即注册按钮不存在")
        self.assertEqual(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_login_register").text, "立即注册",
                         msg="立即注册文本信息不一致")
        self.assertEqual(elementIsExist(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_login_email")),
                         1, msg="邮箱登录按钮不存在")
        self.assertEqual(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_login_email").text, "邮箱登录",
                         msg="邮箱登录文本信息不一致")
        self.assertEqual(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_provicy").text,
                         "登录表示您已阅读并同意使用条款和隐私条款", msg="使用条款和隐私条款文本信息不一致")

    # 手机账号登录
    def test_3input_account_password(self):
        self.driver.find_element_by_id('com.lenovo.homeedgeserver:id/et_login_or_psw_edit').send_keys(account[1])
        self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/bt_login_next_or_login").click()
        # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/et_password").send_keys(password).clear()
        self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/et_password").send_keys(password)
        self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/b_login").click()
        time.sleep(5)

    # 设备列表页面元素检查
    def test_4device_page_check(self):
        try:
            if elementIsExist(self.driver.find_element_by_xpath('//*[@text="抱歉，暂无设备"]')):
                self.driver.get_screenshot_as_file(screenshot_path + '4.png')
                cmp_img(os.path.join(screenshot_path, '4.png'), os.path.join(screenshot_origin_path, '4.png'))
                print("没有添加设备，程序退出")
                os._exit(0)
            # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/ibtn_back").click()
            # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_dialog_left").click()
        except Exception as e:
            # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/layout_add_device").click()
            # if elementIsExist(
                    # self.driver.find_element_by_id('com.lbe.security.miui:id/permission_allow_foreground_only_button')):
                # self.driver.find_element_by_id(
                    # "com.lbe.security.miui:id/permission_allow_foreground_only_button").click()
            # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/tv_title_right").click()
            # self.driver.find_element_by_id("com.android.gallery3d:id/icon_left").click()
            # self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/ibtn_back").click()
            print("登录设备")
        finally:
            self.driver.find_elements_by_id('com.lenovo.homeedgeserver:id/btn_login_device')[0].click()
            time.sleep(5)

    # 引导页面
    def test_5introduce(self):
        self.driver.get_screenshot_as_file(screenshot_path + '5_1.png')
        # cmp_img(os.path.join(screenshot_path,'5_1.png'), os.path.join(screenshot_origin_path,'5_1.png'))
        self.driver.find_element_by_id('com.lenovo.homeedgeserver:id/tv_item_name').click()
        self.driver.find_element_by_xpath('//*[@text="我知道啦"]').click()
        self.driver.get_screenshot_as_file(screenshot_path+'5_2.png')
        # cmp_img(os.path.join(screenshot_path, '5_2.png'), os.path.join(screenshot_origin_path, '5_2.png'))
        self.driver.find_element_by_xpath('//*[@text="我知道啦"]').click()
        self.driver.get_screenshot_as_file(screenshot_path+'5_3.png')
        # cmp_img(os.path.join(screenshot_path, '5_3.png'), os.path.join(screenshot_origin_path, '5_3.png'))
        self.driver.find_element_by_xpath('//*[@text="我知道啦"]').click()
        self.driver.get_screenshot_as_file(screenshot_path + '5_4.png')
        # cmp_img(os.path.join(screenshot_path, '5_4.png'), os.path.join(screenshot_origin_path, '5_4.png'))
        self.driver.find_element_by_id('com.lenovo.homeedgeserver:id/btn_dialog_right').click()
        self.driver.get_screenshot_as_file(screenshot_path + '5_5.png')
        # cmp_img(os.path.join(screenshot_path, '5_5.png'), os.path.join(screenshot_origin_path, '5_5.png'))
        self.driver.find_element_by_xpath('//*[@text="我知道啦"]').click()
        self.driver.find_element_by_id('com.lenovo.homeedgeserver:id/ibtn_back').click()

    def test_6upload_page(self):
        time.sleep(5)
        try:

            if elementIsExist(self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_dialog_left")):
                self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/btn_dialog_left").click()
        except Exception as e:
            print("无升级提示")
        finally:
            self.driver.find_element_by_id("com.lenovo.homeedgeserver:id/img_add_guide").click()
            self.driver.get_screenshot_as_file(os.path.join(screenshot_path,'6.png'))
            # cmp_img(os.path.join(screenshot_path,'6.png'),os.path.join(screenshot_origin_path,'6.png'))
            self.driver.find_element_by_id('com.lenovo.homeedgeserver:id/tv_space_disk').click()

if __name__ == "_main_":
    unittest.main()
