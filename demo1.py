# -*- coding = utf-8 -*-
# 学习python

def power(x, n):
	s = 1
	while n>0:
		n -= 1
		s = s * x
	return s

print(power(5,2))
# from PIL import Image

# im = Image.open("./images/test.jpg")
# print(im.format, im.size, im.mode)

# im.thumbnail((200,100))
# im.save("./images/test_thumb.jpg", 'JPEG')
'''
with open('test.txt', 'w') as f:
	f.write('hello, xiaofei pang')

try:
	f = open('test.txt', 'r')
	print(f.read())
finally:
	if f:
		f.close()
'''
'''
fangdai = 2230
chedai = 2230
# chedai = 0
xianjiedai = 1800
other = 2500

shouru = 11000
mouth = int(input('请输入多少个月:'))

# if mouth > 12:
# 	xianjiedai = 0
# elif mouth > 15:
# 	xianjiedai = 0
# 	chedai = 0

total = shouru * mouth

totalXf = (fangdai + chedai + xianjiedai + other) * mouth

print(total - totalXf)
'''