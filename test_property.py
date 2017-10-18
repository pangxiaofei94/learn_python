# -*- coding: utf-8 -*-


class Chain(object):

	def __init__(self, path=''):
		self._path = path

	def __getattr__(self, path):
		if path == 'users':
			return lambda user: Chain('%s/%s/%s' % (self._path, path, user))
		else:
			return Chain('%s/%s' % (self._path, path))
	# def users(self, username):
	# 	return Chain('%s/%s/%s' % (self._path, 'user', username))

	def __str__(self):
		return self._path

	__repr__ = __str__

# Chain().status.user.timeline.list
# print(Chain().status.user)
print(Chain().status.users('pangxiaofei').list)
'''
class Screen(object):
	# __slots__ = ('width', 'height')
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, value):
		self._width = value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768

print(s.resolution)
assert s.resolution == 786432, '1024 * 786 = %d ?' % s.resolution

'''

