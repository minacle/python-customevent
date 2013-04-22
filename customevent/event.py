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

import threading
import traceback
import sys

class event(object):
	
	def __init__(self, threaded=False):
		"""Initialise new event object.
			connected = event(threaded=True)
		"""
		self.threaded = threaded
		self.__handlers__ = []
	
	def __iadd__(self, handler):
		"""Add event handler to event object.
			connected += on_connected
		"""
		self.__handlers__.append(handler)
		return self
	
	def __isub__(self, handler):
		"""Remove event handler from event object.
			connected -= on_connected
		"""
		self.__handlers__.remove(handler)
		return self
	
	def __iand__(self, handler):
		"""
			connected &= on_connected
		"""
		self.__handlers__ = [handler] if handler else []
		return self
	
	def __ior__(self, handler):
		"""
			connected |= on_connected
		"""
		if handler in self.__handlers__:
			return self
		return self.__iadd__(handler)
	
	def __ixor__(self, handler):
		"""
			connected ^= on_connected
		"""
		if handler in self.__handlers__:
			self.__handlers__.remove(handler)
		return self
	
	def __contains__(self, handler):
		"""
			on_connected in connected
		"""
		return True if handler in self.__handlers__ else False
	
	def __call__(self, *args, **kwargs):
		"""
			connected()
		"""
		def __event__(*args, **kwargs):
			for handler in self.__handlers__:
				try:
					handler(*args, **kwargs)
				except Exception as err:
					traceback.print_exc(file=sys.stderr)
					continue
		if self.threaded:
			threading.Thread(target=__event__, args=args, kwargs=kwargs).start()
		else:
			__event__(*args, **kwargs)
	
	def handler(self, func):
		"""
			@connected.handler
			def on_connected(): pass
		"""
		self.__ior__(func)

