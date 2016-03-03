# encoding = utf-8
import urllib, urllib2, cookielib, re

class V2ex(object):
    """autosign for V2ex"""

    # site url
    host = 'v2ex.com'
    url_login_page = 'http://v2ex.com/signin'
    url_do_sign = ''
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36', 'Referer': url_login_page, 'Host': host}

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login(self):
        # get once
        self.req = urllib2.Request(self.url_login_page)
        self.response = self.opener.open(self.req)
        reg = r'value="(.*)" name="once"'
        pattern = re.compile(reg)
        once =  pattern.search(self.response.read())

        # do login
        data = {'u': self.username, 'p': self.password, 'once': once, 'next': '/'}
        data = urllib.urlencode(data)
        self.req = urllib2.Request(self.url_login_page, data, self.headers)
        self.response = self.opener.open(self.req)
        return self.response.read()


username = 'username'
password = 'password'

av2ex = V2ex(username, password)
print av2ex.login()