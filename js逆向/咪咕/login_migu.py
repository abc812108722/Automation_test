import requests
import json

import execjs

class Migu_login(object):
    def __init__(self, account, password):
        modules = '00833c4af965ff7a8409f8b5d5a83d87f2f19d7c1eb40dc59a98d2346cbb145046b2c6facc25b5cc363443f0f7ebd9524b7c1e1917bf7d849212339f6c1d3711b115ecb20f0c89fc2182a985ea28cbb4adf6a321ff7e715ba9b8d7261d1c140485df3b705247a70c28c9068caabbedbf9510dada6d13d99e57642b853a73406817'
        publicExponent = '010001'
        # 获取FingerPrint和FingerPrintDetail参数中JS函数所需的参数c和d
        details_params = '"{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89","language":"zh-CN","color_depth":"24","pixel_ratio":"1.25","hardware_concurrency":"8","resolution":"1536,864","available_resolution":"1536,834","timezone_offset":"-480","session_storage":"1","local_storage":"1","indexed_db":"1","open_database":"1","cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":"Chrome PDF Plugin::Portable Document Format::application/x-google-chrome-pdf~pdf,Chrome PDF Viewer::","webgl_vendor":"Google Inc.~ANGLE (Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0)","adblock":"false","has_lied_languages":"false","has_lied_resolution":"false","has_lied_os":"false","has_lied_browser":"false","touch_support":"0,false,false","js_fonts":"Arial,Arial Black,Arial Narrow,Arial Unicode MS,Book Antiqua,Bookman Old Style,Calibri,Cambria,Cambr"}"'
        result_params = '984eb0bda24963a23008f493d58a84e0'

        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Host": "passport.migu.cn",
            "Origin": "https://passport.migu.cn",
            "Referer": "https://passport.migu.cn/login?sourceid=208003&apptype=0&forceAuthn=false&isPassive=false&authType=MiguPassport&passwordControl=0&display=web&referer=https://www.migu.cn/&logintype=1&qq=null&weibo=null&alipay=null&weixin=null&andPass=null&phoneNumber=&callbackURL=https%3A%2F%2Fwww.migu.cn%2F&relayState=",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
        }

        self.form = {
            # 需要传递的构造出来的参数先写空，后面再使用update即可！
            "sourceID": "208003",
            "appType": "0",
            "relayState": "",
            "loginID":"",             # 加密后的账号
            "enpassword": "",         # 加密后的密码
            "captcha": "",
            "rememberMeBox": "1",
            "fingerPrint": "",         # 指纹
            "fingerPrintDetail":"",    # 指纹detail
            "isAsync": True,
        }

        # 开启会话，保持连接！
        self.session = requests.Session()
        self.session.headers = headers
        self.get_cookie()

        # Python执行JS代码，生成所需参数并更新进表单
        self.js_object = self.compile_js()
        update_form = self.make_rsa_fingerprint(modules, publicExponent, details_params, result_params)
        update_form['loginID'] = self.make_encrypt_account(account, modules, publicExponent)
        update_form['enpassword'] = self.make_encrypt_password(password, modules, publicExponent)
        self.form.update(update_form)


    def compile_js(self):
        """
        python直接执行本地编写的JS代码
        :return:
        """
        with open('en_pwd.js', 'r') as f:
            js = f.read()
        return execjs.compile(js)


    def get_cookie(self):
        """
        为了让会话携带cookie，所以进行如下操作。因为使用的session会话技术，所以即使不return也携带了cookie等一系列参数。
        :return:
        """
        url = 'https://passport.migu.cn/'
        self.session.get(url)

        return self.session.cookies


    def make_encrypt_password(self, password, modulus, publicExponent):
        """生成加密后的密码

        Args:
            password (str): 输入框内输入的原始密码
            modulus (str): rsa加密参数，两个质数的乘积，固定值，前一个请求获得
            publicExponent (str): rsa加密参数，大于1的奇数，固定值，前一个请求获得

        Returns:
            str: 加密后的密码
        """
        return self.js_object.call('getEncryptedPwd', password, modulus, publicExponent)

    def make_encrypt_account(self, account, modulus, publicExponent):
        """生成加密后的账号

        Args:
            account (str): 输入框内输入的账号
            modulus (str): 同上
            publicExponent (str): 同上

        Returns:
            str: 加密后的账号
        """
        return self.js_object.call('getEncryptedAccount', account, modulus, publicExponent)

    def make_rsa_fingerprint(self, modulus, publicExponent, details, result):
        """生成rsa指纹参数

        Args:
            details (str): 请求headers信息
            result (str): headers的加密信息，如果headers不改变这个值也是固定的

        Returns (dict):
            details: 加密后的fingerprint_details信息，fingerPrintDetail表单参数
            result: 加密后的fingerprint_result信息，fingerPrint表单参数
        """
        return self.js_object.call('rsaFingerprint', modulus, publicExponent, details, result)


    def login(self):
        """
        登录函数
        :return:
        """
        url = 'https://passport.migu.cn/authn'
        response = self.session.post(url, data=self.form)

        response_dict = json.loads(response.text)
        token = response_dict.get('result',{}).get('token', '')
        if not token:
            return

        rest_url = [
            'https://passport.migu.cn/portal/sso/authn?callbackURL=&relayState=&token={}'.format(token),
            'https://passport.migu.cn/portal/sso/authn_success?relateToMiguPassport=1&callbackURL=&relayState=',
            'https://passport.migu.cn/portal/home/profile?sourceid=100001',
            'https://passport.migu.cn/portal/home/profile?sourceid=100001',
        ]
        for ru in rest_url:
            response = self.session.get(ru)

        return response
import re
if __name__ == '__main__':

    act = '17323193387'
    pwd = 'lhx473055.*?'
    mg = Migu_login(act,pwd)
    mresponse = mg.login()
    tages = ['1', '2', '3']
    types = ['A', 'B', 'C']
    # firstletters=[chr(i) for i in range(97,123)]
    firstletter = "A"
    page = "1"
    for tag in tages:
        for type in types:
            response = mg.session.get("https://music.migu.cn/v3/music/artist?tagId=%s&type=%s&firstLetter=%s&page=%s" % (tag, type, firstletter, page))
            r = re.findall('class="thumb-link" href="(.*?)"', response.text)
            print(response.text)




