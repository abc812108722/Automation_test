import requests,execjs,re


def get_pass():
    with open("q.js","r") as f:
        js=f.read()
    return execjs.compile(js)
js_ob=get_pass()
a=js_ob.call("gb","1")
print(a)