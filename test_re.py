# -*- coding: utf-8 -*-

import re
# s = r'ABC\-001'

s = re.match(r'^\d{3}\-\d{3,8}$', '010 - 12345')
if s:
	print('匹配成功')
else:
	print('匹配失败')