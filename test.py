import subprocess
from PythonUIAutomation.uiautomation.uiautomation import *
import os
import ctypes
import unittest


subprocess.Popen('C:\Program Files (x86)\Lenovo\SmartStorageApp\SmartStorageApp.exe')
window = WindowControl(searchDepth = 1, Name = '想家云(client端)登录')
print(window.NativeWindowHandle)
print(window)
