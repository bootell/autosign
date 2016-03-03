import urllib, urllib2, cookielib

class Tieba(object):
    """autosign for Baidu Tieba"""

    url_login = 'http://wappass.baidu.com/passport/login'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.cj = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def login():
        pass