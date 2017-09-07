# -*- coding: utf-8 -*-

import urllib.request

params = {"username":"827464561@qq.com", "password":"pxf15313111209"}
data = urllib.parse.urlencode(params)
print(data)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)
# response = urllib.request.urlopen("http://www.baidu.com")

print(response.read())