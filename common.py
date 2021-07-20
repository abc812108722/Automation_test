from functools import reduce
from PIL import ImageGrab
import cv2
import os, sys, time
from ctypes import *
from PyQt5.QtWidgets import QApplication
import win32gui, win32api, win32con
import pyautogui


def elementIsExist(webdriver):
    flag = None
    try:
        if webdriver:
            flag = 1
    except Exception:
        flag = 0
    finally:
        return flag


# ORB图片相似度算法
def ORB_img_similarity(img1_path, img2_path):
    """
    :param img1_path: 图片1路径
    :param img2_path: 图片2路径
    :return: 图片相似度
    """
    try:
        # 读取图片
        img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)

        # 初始化ORB检测器
        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        # 提取并计算特征点
        bf = cv2.BFMatcher(cv2.NORM_HAMMING)
        # knn筛选结果
        matches = bf.knnMatch(des1, trainDescriptors=des2, k=2)

        # 查看最大匹配点数目
        good = [m for (m, n) in matches if m.distance < 0.75 * n.distance]
        similary = len(good) / len(matches)
        return int(similary)

    except Exception as e:
        print(e)


from skimage.measure import compare_ssim
import numpy as np


def ssim_compare(imag1, imag2):
    imag1 = cv2.resize(np.asarray(cv2.imdecode(np.fromfile(imag1, dtype=np.uint8), -1)), (256, 256))
    imag2 = cv2.resize(np.asarray(cv2.imdecode(np.fromfile(imag2, dtype=np.uint8), -1)), (256, 256))
    imag1_new = cv2.cvtColor(imag1, cv2.COLOR_BGR2GRAY)
    imag2_new = cv2.cvtColor(imag2, cv2.COLOR_BGR2GRAY)
    S, diff = compare_ssim(imag1_new, imag2_new, full=True)
    print(S)
    return S


def cmp_img(img1, img2):
    a = ssim_compare(img1, img2)
    if (a < 0.8):

        raise Exception('截图匹配度为:' + str(a))
    else:
        print("截图匹配度为" + str(a))


# 删除文件夹下所有图片
def remove_img(dir):
    del_list = os.listdir(dir)
    print(del_list)
    for i in del_list:
        file_path = os.path.join(dir, i)
        print(file_path)
        os.remove(file_path)


def pil_image_similarity(filepath1, filepath2):
    from PIL import Image
    import math
    import operator

    image1 = Image.open(filepath1)
    image2 = Image.open(filepath2)

    #    image1 = get_thumbnail(img1)
    #    image2 = get_thumbnail(img2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    rms = math.sqrt(reduce(operator.add, list(map(lambda a, b: (a - b) ** 2, h1, h2))) / len(h1))
    print(rms)
    return rms


# ssim_compare('C:\\Users\\530s\\PycharmProjects\\untitled\\screenshot_origin\\1.png','E:\\screenshot\\1.png')


def AllScreenShot(name):
    WaitTime(3)
    im = ImageGrab.grab()  # 可以添加一个坐标元组进去
    im.save('C:\\Users\\530s\\PycharmProjects\\untitled\\Screenshot\\{0}.png'.format(name))


def WaitTime(s):
    time.sleep(s)


def GetForegroundWindowHandle():
    user32 = windll.user32
    hwd = user32.GetForegroundWindow()
    return hwd


def WindowScreenShot(name):
    WaitTime(3)
    user32 = windll.user32
    hwnd = user32.GetForegroundWindow()
    app = QApplication(sys.argv)
    print(hwnd)
    screen = QApplication.primaryScreen()

    img = screen.grabWindow(hwnd).toImage()
    img.save('C:\\Users\\530s\\PycharmProjects\\untitled\\Screenshot\\{0}.png'.format(name))


# 获得窗口大小

def getwindowssize(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    return (w, h)


# 获得控件位置
def getcontrollocation(hwnd):
    rect = win32gui.GetWindowRect(hwnd)
    return (rect[0], rect[1])


# 获得屏幕分辨率
def getscreensize():
    return (win32api.GetSystemMetrics(win32con.SM_CXSCREEN), win32api.GetSystemMetrics(win32con.SM_CYSCREEN))

# 获得鼠标的实时位置
def getmouseposition():
    while True:
        x,y=pyautogui.position()
        print(x,y)
        time.sleep(0.2)
