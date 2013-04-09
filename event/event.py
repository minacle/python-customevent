#!/usr/bin/python

"""
Copyright (c) 2012-2013 Minacle

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
"""

class event(object):
	
	def __init__(self):
		self.__handlers__ = []
	
	def __iadd__(self, handler):
		self.__handlers__.append(handler)
		return self
		
	def __isub__(self, handler):
		self.__handlers__.remove(handler)
		return self
	
	def __iand__(self, handler):
		self.__handlers__ = [handler] if handler else []
		return self
	
	def __ior__(self, handler):
		if handler in self.__handlers__:
			return self
		return self.__iadd__(handler)
	
	def __ixor__(self, handler):
		if handler in self.__handlers__:
			self.__handlers__.remove(handler)
		return self
	
	def __contains__(self, handler):
		return True if handler in self.__handlers__ else False
	
	def __call__(self, *args, **kwargs):
		for handler in self.__handlers__:
			try:
				handler(*args, **kwargs)
			except:
				continue
	
	def handler(self, func):
		self.__ior__(func)

