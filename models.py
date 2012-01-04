import exceptions

class AuthenticationError(Exception):
	"""Exception representing an authentication error"""

	def __init__(self):
		Exception.__init__(self)
	
	def __str__(self):
		print "Could not log in with given credentials"

class AuthenticationRequired(Exception):
	"""Signify that authentication is required"""

	def __init__(self):
		Exception.__init__(self)

	def __str__(self):
		print "Authentication required. Please call login() with your credentials"
		
		
class MyClass(object):
	"""Docstring for MyClass """

	def __init__(self):
		"""@todo: to be defined """
		
		
