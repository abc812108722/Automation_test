import requests,os
headers={
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
response = requests.get("https://freetyst.nf.migu.cn/public/product8th/product39/2020/04/0815/2013%E5%B9%B404%E6%9C%8818%E6%97%A5%E6%BB%9A%E7%9F%B3%E5%94%B1%E7%89%87%E5%86%85%E5%AE%B9%E5%87%86%E5%85%A5972%E9%A6%96/%E6%AD%8C%E6%9B%B2%E4%B8%8B%E8%BD%BD/MP3_40_16_Stero/63480205377155001.mp3",headers=headers)
pwd=os.getcwd()
path=os.path.join(pwd,"ff.mp3")
print(response.content)

with open(path,"wb") as f:
    f.write(response.content)
