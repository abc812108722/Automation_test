import subprocess
from PythonUIAutomation.uiautomation.uiautomation import *
import os, sys, win32gui, win32api, win32con
import unittest
from common import *
from ctypes import *
from TextInfo import *
import pyautogui

user32 = windll.user32


class SmartstorageAppAutotest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("想家云client测试***********")

        subprocess.Popen('C:\\Program Files (x86)\\Lenovo\\SmartStorageApp\\SmartStorageApp.exe')
        # cls.window = WindowControl(searchDepth=1, Name='想家云(client端)登录')

    def setUp(self) -> None:
        WaitTime(1)

    def tearDown(self) -> None:
        AllScreenShot(self._testMethodName)

    # def test_1_LoginLinkClick_1(self):
    #     self.window.TextControl(Name="联想许可和服务协议").Click()
    #     WaitTime(2)
    #     self.assertNotEqual(self.window.NativeWindowHandle, user32.GetForegroundWindow())
    #
    # def test_2_LoginLinkClick_2(self):
    #     if self.window.NativeWindowHandle != user32.GetForegroundWindow():
    #         win32gui.PostMessage(user32.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)
    #     self.window.TextControl(Name="隐私政策").Click()
    #     WaitTime(2)
    #     self.assertNotEqual(self.window.NativeWindowHandle, user32.GetForegroundWindow())

    # def test_3_LoginTextCheck(self):
    #     self.assertEqual(self.window.GetChildren()[1].GetChildren()[0].GetChildren()[2].Name, LoginText1)
    #     self.assertEqual(self.window.GetChildren()[1].GetChildren()[0].GetChildren()[1].Name, LoginText2)
    #
    # def test_4_LoginCheckBox(self):
    #     关闭更新弹窗
    #     if self.window.NativeWindowHandle != user32.GetForegroundWindow():
    #         win32gui.PostMessage(user32.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)
    #     self.assertEqual(self.window.ButtonControl(Name="登录使用").Element.CurrentIsEnabled, 0)
    #     self.window.CheckBoxControl(ClassName="QCheckBox").Click()
    #     self.assertEqual(self.window.ButtonControl(Name="登录使用").Element.CurrentIsEnabled, 1)
    #
    # def test_5_Login(self):
    #     self.window.ButtonControl(Name="登录使用").Click()
    #     self.window = WindowControl(ClassName="UILoginFrame")
    #     self.assertEqual(self.window.NativeWindowHandle, user32.GetForegroundWindow())
    #     ex = True
    #     while ex:
    #         # 等待输入账号密码
    #         if WindowControl(ClassName="AppUpdateWidget").Exists() or WindowControl(Name="想家云(client端)").Exists():
    #             ex = False

    # def test_6_ClientTips(self):
    #     self.window = WindowControl(Name="想家云(client端)")
    #     if WindowControl(ClassName="AppUpdateWidget").Exists():
    #         win32gui.PostMessage(WindowControl(ClassName="AppUpdateWidget").NativeWindowHandle, win32con.WM_CLOSE, 0, 0)
    #     count = 1
    #     while self.window.ButtonControl(Name="下一个").Exists():
    #         self.window.ButtonControl(Name="下一个").Click()
    #         AllScreenShot("Clienttips{0}".format(count))
    #         count += 1
    #     self.window.ButtonControl(Name="我知道了").Click()

    # def test_7_getwindowsize_and_styleoflistbutton(self):
    #     self.window = WindowControl(Name="想家云(client端)")
    #     print(getwindowssize(self.window.NativeWindowHandle))
    #     AllScreenShot("test_7_getwindowsize_and_styleoflistbutton{0}".format("三横列表"))
    #     self.window.ButtonControl(Name="显示模式").Click()
    #     self.window.CheckBoxControl(Name="电脑端备份").Click()
    #     if  self.window.GetChildren()[2].GetChildren()[2].GetChildren()[1].GetChildren()[0].Name !="文件名":
    #         self.window.ButtonControl(Name="显示模式").Click()
    #     self.assertEqual(
    #         self.window.GetChildren()[2].GetChildren()[2].GetChildren()[1].GetChildren()[0].Name,"文件名")
    #     self.assertEqual(
    #         self.window.GetChildren()[2].GetChildren()[2].GetChildren()[1].GetChildren()[1].Name, "时间")
    #     self.assertEqual(
    #         self.window.GetChildren()[2].GetChildren()[2].GetChildren()[1].GetChildren()[2].Name, "大小")
    # def test_8_maximizeandminimize(self):
    #     self.window = WindowControl(Name="想家云(client端)")
    #     self.window.ButtonControl(Name="最大化").Click()
    #     AllScreenShot("MaximizeWindow")
    #     self.window.ButtonControl(Name="最大化").Click()
    #    鼠标拖拽行为未完成
    # def test_9_dragdropchangewindowsize(self):
    #     self.window = WindowControl(Name="想家云(client端)")
    #
    #     qlabel = self.window.ImageControl(ClassName="QLabel").MoveCursorToInnerPos()
    #     pyautogui.dragTo(x=124, y=40, duration=3,button='left')
    #     AllScreenShot("拖动1")
        # pyautogui.dragTo(x=1421, y=50, duration=3, button='left')
        # pyautogui.dragTo(x=86, y=649, duration=3, button='left')
        # pyautogui.dragTo(x=328, y=62, duration=3, button='left')
        # a=self.window.ThumbControl(ClassName="QSizeGrip").MoveCursorToInnerPos()
        # pyautogui.dragTo(x=1700, y=1000, duration=3,button='left')
        # AllScreenShot("拉伸窗口1")
        # pyautogui.dragTo(x=20, y=20, duration=3, button='left')

    def test_10_hidetotaskbar(self):
        self.window=WindowControl(Name="想家云(client端)")
        self.window.ButtonControl(Name="最小化").Click()
        self.window2=WindowControl(Name="Desktop")
        self.window2.ButtonControl(Name="Notification Chevron").Click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SmartstorageAppAutotest)

    unittest.TextTestRunner(verbosity=2).run(suite)
