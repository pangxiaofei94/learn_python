# -*- coding: utf-8 -*-
#
import pdb

s = '0'
n = int(s)
pdb.set_trace()
print(10/n)
'''
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)

logging.info('n=%d' % n)
print(10/n)
'''
'''
try:
	print('try...')
	r = 10 / 0
	print('result:', r)
except Exception as e:
	print('except:', e)
finally:
	print('finally...')

print('END')
'''