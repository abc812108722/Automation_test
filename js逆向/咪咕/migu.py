import requests,execjs,json



class Migulogin():
    def __init__(self,account,pwd):
        self.mod="00833c4af965ff7a8409f8b5d5a83d87f2f19d7c1eb40dc59a98d2346cbb145046b2c6facc25b5cc363443f0f7ebd9524b7c1e1917bf7d849212339f6c1d3711b115ecb20f0c89fc2182a985ea28cbb4adf6a321ff7e715ba9b8d7261d1c140485df3b705247a70c28c9068caabbedbf9510dada6d13d99e57642b853a73406817"
        self.pub="010001"
        self.detail='{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45","language":"zh-CN","color_depth":"24","pixel_ratio":"1.5","hardware_concurrency":"8","resolution":"1280,720","available_resolution":"1280,720","timezone_offset":"-480","session_storage":"1","local_storage":"1","indexed_db":"1","open_database":"1","cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable D","webgl_vendor":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11-24.20.10","adblock":"false","has_lied_languages":"false","has_lied_resolution":"false","has_lied_os":"false","has_lied_browser":"false","touch_support":"0,false,false","js_fonts":"Arial,Arial Black,Arial Narrow,Book Antiqua,Calibri,Cambria,Cambria Math,Century,Century Gothic,Comi"}'
        self.result="e3fd76fc4d0ffb606ada89a507fe46d9"
        self.account=account
        self.pwd=pwd
        self.headers={
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "max-age=0",
            "Connection": "keep-alive",
            "Cookie": "migu_cn_cookie_id=16b6927c-e274-48a2-bd34-5402e320c8b0; WT_FPC=id=20955bb2d1a28059e0e1637635756486:lv=1637734796501:ss=1637734785660; mgpt_session_id=ADARBKX1K2-GBMVIT40XQVHPDFDK8KU1-TUNC6DWK-0; mgpt_session_create=1637737045445; mgpt_session_last_access=1637737045445; mgnd_session_id=ADARZ2N9L2-GBMVG5T0XOVTF3AVEUHD2-8YNC6DWK-0; mgnd_session_create=1637737045568; mgnd_session_last_access=1637737045568",
            "Host": "passport.migu.cn",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""

        }
        self.form={
            "appType": "0",
            "captcha": "",
            "enpassword": self.get_pass(),
            "fingerPrint": self.get_finger().get("fingerPrint"),
            "fingerPrintDetail": self.get_finger().get("fingerPrintDetail"),
            "imgcodeType": "1",
            "isAsync": "true",
            "loginID": self.get_account(),
            "relayState": "",
            "rememberMeBox": "1",
            "sourceID": "208003"
        }
        self.session=requests.Session()
        self.session.headers=self.headers
        self.session.get("https://passport.migu.cn/")
    def run_js(self):
        with open("migu.js", "r") as f:
            js = f.read()
        return execjs.compile(js)

    def get_pass(self):
        a=self.run_js()
        b=a.call("getencryt",self.pwd,self.mod,self.pub)
        return b
    def get_account(self):
        a = self.run_js()
        b = a.call("getencryt", self.account, self.mod, self.pub)
        return b
    def get_finger(self):
        a = self.run_js()
        b = a.call("finger", self.mod, self.pub,self.detail,self.result)
        return b
    def login(self):
        url="https://passport.migu.cn/authn"
        res=self.session.post(url,data=self.form)
        print(res.text)
        token=json.loads(res.text).get("result").get("token")
        print(token)
        ressponse=self.session.get("https://www.migu.cn/user/tokenValidate?callbackURL=https://www.migu.cn/&relayState=&token=%s" % token)
        print(ressponse.text)
if __name__=="__main__":
    log=Migulogin("17323193387","lhx473055.*?")

    log.login()

