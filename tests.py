from models import AuthenticationError,AuthenticationRequired
from trello import Trello
import unittest
import os

class BoardTestCase(unittest.TestCase):

	def setUp(self):
		self._trello = Trello(os.environ['TRELLO_TEST_USER'], os.environ['TRELLO_TEST_PASS'])

	def test01_list_boards(self):
		print "list boards"
		self.assertEquals(
				len(self._trello.list_boards()),
				int(os.environ['TRELLO_TEST_BOARD_COUNT']))

	def test02_board_attrs(self):
		print "board attrs"
		boards = self._trello.list_boards()
		for b in boards:
			self.assertIsNotNone(b['_id'], msg="_id not provided")
			self.assertIsNotNone(b['name'], msg="name not provided")
			self.assertIsNotNone(b['closed'], msg="closed not provided")

class CardTestCase(unittest.TestCase):
	def setUp(self):
		self._trello = Trello(os.environ['TRELLO_TEST_USER'], os.environ['TRELLO_TEST_PASS'])



if __name__ == "__main__":
	unittest.main()
