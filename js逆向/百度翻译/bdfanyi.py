import execjs, requests, re

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1"
}
session = requests.Session()
session.headers = headers


def run_js():
    with open("baidu.js", "r") as f:
        js = f.read()
    return execjs.compile(js)
a = run_js()

def get_token_gtk():
    url='https://fanyi.baidu.com/'
    for i in range(2):
        response = session.get(url)
        token = re.findall("token: '(.*?)'",response.text)[0]
        gtk = re.findall("window.gtk = '(.*?)'", response.text)[0]
        print('[%s] token: '%i , token)
        print('[%s] gtk: '%i,  gtk)

    return token, gtk





def trans(query):
    url = "https://fanyi.baidu.com/v2transapi?from=zh&to=en"
    token,gtk = get_token_gtk()

    sign = a.call("e", query, gtk)
    print("sign:%s" % sign)
    form = {
        "from": "zh",
        "to": "en",
        "query": "%s" % query,
        "transtype": "realtime",
        "simple_means_flag": "3",
        "sign": "%s" % sign,
        "token": token,

        "domain": "common",
    }
    res = session.post(url, data=form)

    res = re.findall('"dst":"(.*?)"', res.text)[0]
    return res



if __name__ == "__main__":
    input=input("输入中文:")
    t = trans(input)
    print("翻译结果:%s" % t)
