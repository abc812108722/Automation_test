import subprocess
import win32con
from PythonUIAutomation.uiautomation.uiautomation import *
import os, sys, win32gui
import ctypes
import unittest
from common import *
from ctypes import *
from TextInfo import *

user32 = windll.user32


class SmartstorageAppAutotest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("想家云client测试***********")

        subprocess.Popen('C:\\Program Files (x86)\\Lenovo\\SmartStorageApp\\SmartStorageApp.exe')
        cls.window = WindowControl(searchDepth=1, Name='想家云(client端)登录')

    def setUp(self) -> None:
        WaitTime(2)

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

    def test_3_LoginTextCheck(self):
        self.assertEqual(self.window.GetChildren()[1].GetChildren()[0].GetChildren()[2].Name, LoginText1)
        self.assertEqual(self.window.GetChildren()[1].GetChildren()[0].GetChildren()[1].Name, LoginText2)

    def test_4_LoginCheckBox(self):
        if self.window.NativeWindowHandle != user32.GetForegroundWindow():
            win32gui.PostMessage(user32.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)
        self.assertEqual(self.window.ButtonControl(Name="登录使用").Element.CurrentIsEnabled, 0)
        self.window.CheckBoxControl(ClassName="QCheckBox").Click()
        self.assertEqual(self.window.ButtonControl(Name="登录使用").Element.CurrentIsEnabled, 1)

    def test_5_Login(self):
        self.window.ButtonControl(Name="登录使用").Click()
        self.window=WindowControl(ClassName="UILoginFrame")
        self.assertEqual(self.window.NativeWindowHandle,user32.GetForegroundWindow())
        ex=True
        while ex:
            # 等待输入账号密码
            if WindowControl(ClassName="AppUpdateWidget").Exists() or WindowControl(Name="想家云(client端)").Exists():
                ex=False

    def test_6_ClientTips(self):
        self.window = WindowControl(Name="想家云(client端)")
        if WindowControl(ClassName="AppUpdateWidget").Exists():
            win32gui.PostMessage(WindowControl(ClassName="AppUpdateWidget").NativeWindowHandle, win32con.WM_CLOSE, 0, 0)
        count=1
        while self.window.ButtonControl(Name="下一个").Exists():

            self.window.ButtonControl(Name="下一个").Click()
            AllScreenShot("Clienttips{0}".format(count))
            count+=1








if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SmartstorageAppAutotest)

    unittest.TextTestRunner(verbosity=2).run(suite)
