# encoding = utf-8
import urllib, urllib2, cookielib, json, time

class Zimuzu(object):
    """autosign for Zimuzu"""

    host = 'www.zimuzu.tv'
    url_do_login= 'http://www.zimuzu.tv/User/Login/ajaxLogin'
    url_sign_page = 'http://www.zimuzu.tv/user/sign'
    url_do_sign = 'http://www.zimuzu.tv/user/sign/dosign'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36', 'Referer': url_do_login, 'Host': host}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        data = {'account': self.username, 'password': self.password, 'url_back':self.url_sign_page}
        data = urllib.urlencode(data)
        self.req = urllib2.Request(self.url_do_login, data, self.headers)
        self.response = self.opener.open(self.req)
        res = json.loads(self.response.read())
        return res['status']

    def sign(self):
        self.req = urllib2.Request(self.url_sign_page)
        self.response = self.opener.open(self.req)
        time.sleep(15)

        self.req = urllib2.Request(self.url_do_sign)
        self.response = self.opener.open(self.req)
        res = json.loads(self.response.read())
        return res['status']

    """Main Action to Autosign.
    Returns: 
        0: login fail
        1: sign success
        2: alreadly sign
    """
    def autoSign(self):
        if self.login():
            if self.sign():
                return 1
            else:
                return 2
        else:
            return 0

username = 'username'
password = 'password'

zimu = Zimuzu(username, password)
if zimu.autoSign():
    print 'success'
else:
    print 'fail'