from models import AuthenticationError,AuthenticationRequired
import trello
import unittest
import os

class TestTrello(unittest.TestCase):

	def test_login(self):
		username = os.environ['TRELLO_TEST_USER']
		password = os.environ['TRELLO_TEST_PASS']
		try:
			trello.login(username, password)
		except AuthenticationError:
			self.fail("Could not authenticate")
		except Exception as e:
			self.fail("Unknown error: "+str(e))

if __name__ == "__main__":
	unittest.main()
