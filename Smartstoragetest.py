import subprocess

import win32con

from PythonUIAutomation.uiautomation.uiautomation import *
import os, sys,win32gui
import ctypes
import unittest
from common import *
from ctypes import *

user32 = windll.user32


class SmartstorageAppAutotest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("想家云client测试***********")

        subprocess.Popen('C:\Program Files (x86)\Lenovo\SmartStorageApp\SmartStorageApp.exe')
        cls.window = WindowControl(searchDepth=1, Name='想家云(client端)登录')

    def setUp(self) -> None:
        WaitTime(2)

    def tearDown(self) -> None:
        AllScreenShot(self._testMethodName)

    def test_1_LoginLinkClick_1(self):
        self.window.TextControl(Name="联想许可和服务协议").Click()

    def test_2_LoginLinkClick_2(self):
        if self.window.NativeWindowHandle != user32.GetForegroundWindow():
            win32gui.PostMessage(user32.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)
        self.window.TextControl(Name="隐私政策").Click()

    def test_3_LoginCheckBox(self):
        if self.window.NativeWindowHandle != user32.GetForegroundWindow():
            win32gui.PostMessage(user32.GetForegroundWindow(), win32con.WM_CLOSE, 0, 0)
        self.window.CheckBoxControl(ClassName="QCheckBox").Click()


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(SmartstorageAppAutotest)

    unittest.TextTestRunner(verbosity=2).run(suite)
