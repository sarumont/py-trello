import exceptions
class ResourceUnavailable(Exception):
	"""Exception representing a failed request to a resource"""

	def __init__(self, msg):
		Exception.__init__(self)
		self._msg = msg

	def __str__(self):
		print "Resource unavailable: %s" % (self._msg, )
		
		
