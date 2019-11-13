import hashlib

from requests_html import HTMLSession
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__mta=218019497.1565764895582.1566373645392.1566373925144.14; _lxsdk_cuid=16c8edc21825f-0d2831709596ea-36664c08-1fa400-16c8edc2183c8; _hc.v=830a45c4-443f-e2e9-c4d1-ed8fcb171aa5.1565769197; iuuid=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _lxsdk=F2C3AE1137C6F8D72DEF05B520CA10A372AF9057871F50EEC01AC1BDB31C2ACC; _ga=GA1.2.1348654524.1565938623; mtcdn=K; cityname=%E6%B7%B1%E5%9C%B3; webp=1; __utmz=74597006.1566210835.3.3.utmcsr=meishi.meituan.com|utmccn=(referral)|utmcmd=referral|utmcct=/i/; isid=52FD344F5848EC3D3150CCF9FC21EC7D; logintype=normal; ci=30; rvct=30%2C118%2C280%2C277%2C113%2C91%2C281%2C92%2C686%2C20%2C108; client-id=0a40bbc7-1433-4fe8-aac3-21c3339e0517; __utma=74597006.1348654524.1565938623.1566210835.1566368904.4; a2h=4; IJSESSIONID=78jhqc02kupgoa4pnvsui3f0; oops=WCEN-yeleLVOqemGHAzNNiikyNIAAAAA5QgAAKgzJktpa4MpobcC4KwY02edRR1ZVfOqmcmsXl8Eiy-0PZCckDd1_W7T3bnhjmnREw; u=56727782; __utmc=74597006; ci3=1; latlng=22.527887,113.934118,1566370142419; i_extend=Gimthomepagecategory122H__a100265__b4; uuid=6d32a37a57944cf49334.1566370783.1.0.0; _lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; __mta=218019497.1565764895582.1566369259828.1566370784636.9; _lxsdk_s=16cb2b17226-482-632-310%7C%7C79',
    'Host': 'sz.meituan.com',
    'Referer': 'https://sz.meituan.com/jiankangliren/c76/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
}

def html_from_uri(uri):
    print('html_from_uri uri: {}'.format(uri))
    try:
        if uri is None:
            return
        session = HTMLSession()
        # r = session.get(uri, headers=headers)
        r = session.get(uri)
        return r.html.html
    except Exception as e:
        print('html_from_uri Exception: {}'.format(e))
        return html_from_uri(uri)


# 把浏览器的cookies字符串转成字典
def cookies2dict(cookies):
    items = cookies.split(';')
    d = {}
    for item in items:
        kv = item.split('=', 1)
        k = kv[0]
        v = kv[1]
        d[k] = v
    return d


# 对评论内容（或tag）进行摘要算法，作为主键
def calc_md5(content):
    md5 = hashlib.md5()
    str_dd = str(content)
    md5.update(str_dd.encode('utf-8'))
    return md5.hexdigest()
