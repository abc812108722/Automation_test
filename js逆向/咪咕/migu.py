import requests
import execjs,json
import re



class Migulogin():
    def __init__(self,account,pwd):
        self.mod="00833c4af965ff7a8409f8b5d5a83d87f2f19d7c1eb40dc59a98d2346cbb145046b2c6facc25b5cc363443f0f7ebd9524b7c1e1917bf7d849212339f6c1d3711b115ecb20f0c89fc2182a985ea28cbb4adf6a321ff7e715ba9b8d7261d1c140485df3b705247a70c28c9068caabbedbf9510dada6d13d99e57642b853a73406817"
        self.pub="010001"
        #self.detail='{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45","language":"zh-CN","color_depth":"24","pixel_ratio":"1.5","hardware_concurrency":"8","resolution":"1280,720","available_resolution":"1280,720","timezone_offset":"-480","session_storage":"1","local_storage":"1","indexed_db":"1","open_database":"1","cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":"PDF Viewer::Portable Document Format::application/pdf~pdf,text/pdf~pdf,Chrome PDF Viewer::Portable D","webgl_vendor":"Google Inc. (Intel)~ANGLE (Intel, Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0, D3D11-24.20.10","adblock":"false","has_lied_languages":"false","has_lied_resolution":"false","has_lied_os":"false","has_lied_browser":"false","touch_support":"0,false,false","js_fonts":"Arial,Arial Black,Arial Narrow,Book Antiqua,Calibri,Cambria,Cambria Math,Century,Century Gothic,Comi"}'
        self.detail = '"{"user_agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89","language":"zh-CN","color_depth":"24","pixel_ratio":"1.25","hardware_concurrency":"8","resolution":"1536,864","available_resolution":"1536,834","timezone_offset":"-480","session_storage":"1","local_storage":"1","indexed_db":"1","open_database":"1","cpu_class":"unknown","navigator_platform":"Win32","do_not_track":"unknown","regular_plugins":"Chrome PDF Plugin::Portable Document Format::application/x-google-chrome-pdf~pdf,Chrome PDF Viewer::","webgl_vendor":"Google Inc.~ANGLE (Intel(R) UHD Graphics 620 Direct3D11 vs_5_0 ps_5_0)","adblock":"false","has_lied_languages":"false","has_lied_resolution":"false","has_lied_os":"false","has_lied_browser":"false","touch_support":"0,false,false","js_fonts":"Arial,Arial Black,Arial Narrow,Arial Unicode MS,Book Antiqua,Bookman Old Style,Calibri,Cambria,Cambr"}"'

        self.result="984eb0bda24963a23008f493d58a84e0"
        self.account=account
        self.pwd=pwd
        self.headers={
            # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # "Accept-Encoding": "gzip, deflate, br",
            # "Accept-Language": "zh-CN,zh;q=0.9",
            # "Cache-Control": "max-age=0",
            # "Connection": "keep-alive",
            # "Cookie": "migu_cn_cookie_id=16b6927c-e274-48a2-bd34-5402e320c8b0; WT_FPC=id=20955bb2d1a28059e0e1637635756486:lv=1637734796501:ss=1637734785660; mgpt_session_id=ADARBKX1K2-GBMVIT40XQVHPDFDK8KU1-TUNC6DWK-0; mgpt_session_create=1637737045445; mgpt_session_last_access=1637737045445; mgnd_session_id=ADARZ2N9L2-GBMVG5T0XOVTF3AVEUHD2-8YNC6DWK-0; mgnd_session_create=1637737045568; mgnd_session_last_access=1637737045568",
            # "Host": "passport.migu.cn",
            # "Sec-Fetch-Dest": "document",
            # "Sec-Fetch-Mode": "navigate",
            # "Sec-Fetch-Site": "none",
            # "Sec-Fetch-User": "?1",
            # "Upgrade-Insecure-Requests": "1",
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            # "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            # "sec-ch-ua-mobile": "?0",
            # "sec-ch-ua-platform": "\"Windows\""
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
        # ressponse1=self.session.get("https://passport.migu.cn/portal/sso/authn?callbackURL=&relayState=&token=%s" % token)
        # response2=self.session.get('https://passport.migu.cn/portal/home/profile?sourceid=100001')
        rest_url = [
            'https://passport.migu.cn/portal/sso/authn?callbackURL=&relayState=&token={}'.format(token),
            'https://passport.migu.cn/portal/sso/authn_success?relateToMiguPassport=1&callbackURL=&relayState=',
            'https://passport.migu.cn/portal/home/profile?sourceid=100001',
            'https://passport.migu.cn/portal/home/profile?sourceid=100001',
        ]
        for ru in rest_url:
            response = self.session.get(ru)

    def get_artist_urls(self):
        urls=[]
        headers = {
            "authority": "music.migu.cn",
            "method": "GET",
            "path": "/v3/music/artist?tagId=1&type=A&firstLetter=A&page=1",
            "scheme": "https",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "age": "1596",
            "cache-control": "no-cache",
            "content-encoding": "gzip",
            "content-type": "text/html; charset=utf-8",
            "cookie": "migu_cn_cookie_id=16b6927c-e274-48a2-bd34-5402e320c8b0; Hm_lvt_ec5a5474d9d871cb3d82b846d861979d=1637744256; idmpauth=true@passport.migu.cn; Hm_lpvt_ec5a5474d9d871cb3d82b846d861979d=1637806352; migu_cookie_id=78f07636-236f-4dfc-a74c-e4e55f3d00a0-n41637806371602; mg_uem_user_id_9fbe6599400e43a4a58700a822fd57f8=84e684f8-271a-4969-b0cf-0381e7911acb; cookieId=hAJH51FvTDnkH2yZaJtQ8-J_LLsBpWl1637806891978; playlist_adding=1; player_stop_open=0; addplaylist_has=1; audioplayer_new=1; add_play_now=1; WT_FPC=id=20955bb2d1a28059e0e1637635756486:lv=1637808496282:ss=1637803979651; migu_music_status=true; migu_music_uid=91493564140; migu_music_avatar=%252F%252Fcdnmusic.migu.cn%252Fv3%252Fstatic%252Fimg%252Fcommon%252Fheader%252Fdefault-avatar.png; migu_music_nickname=%E5%92%AA%E5%92%95%E9%9F%B3%E4%B9%90%E7%94%A8%E6%88%B7; migu_music_level=0; migu_music_credit_level=1; migu_music_platinum=0; migu_music_msisdn=oScRbqf%2BjgoRE9WTL1PYbQ%3D%3D; migu_music_email=; migu_music_sid=s%3Ax1Ildmc7xO1ryg32znCpq6a4Zw6ldXL7.qgfJjSBmbfIS2OsuNlbuaQ0ByFE2eQtQuEZM5W%2FhNeo; audioplayer_exist=1; playlist_change=0; audioplayer_open=0; WT_FPC=id=20955bb2d1a28059e0e1637635756486:lv=1637826863917:ss=1637826863917",
            "date": "Thu, 25 Nov 2021 08:16:38 GMT",
            "etag": "W/\"42a3-UxxmFwdKDVyzqZZrm+Gz9WoCrAs\"",
            "pragma": "no-cache",
            "referer": "https://music.migu.cn/v3/music/artist?tagId=1&type=A&firstLetter=D&page=1",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"96\", \"Google Chrome\";v=\"96\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "server": "nginx",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "via": "1.1 ID-0001544136660615 uproxy-2",
            "x-powered-by": "Express"
        }
        self.session.headers=headers
        tages=['1','2','3']
        types=['A','B','C']
        #firstletters=[chr(i) for i in range(97,123)]
        firstletter="A"
        page="1"
        for tag in tages:
            for type in types:
                response=self.session.get("https://music.migu.cn/v3/music/artist?tagId=%s&type=%s&firstLetter=%s&page=%s" % (tag,type,firstletter,page))
                r=re.findall('class="thumb-link" href="/v3/music/artist/(.*?)"',response.text)

                urls=urls+r
        print(urls)


if __name__=="__main__":
    log=Migulogin("17323193387","lhx473055.*?")
    log.login()
    log.get_artist_urls()



