from models import AuthenticationError,AuthenticationRequired
from trello import Trello
import unittest
import os

class TrelloTestCase(unittest.TestCase):

	def setUp(self):
		self._trello = Trello(os.environ['TRELLO_TEST_USER'], os.environ['TRELLO_TEST_PASS'])

	def tearDown(self):	
		self._trello.logout()

	def test01_list_boards(self):
		self.assertEquals(
				len(self._trello.list_boards()),
				int(os.environ['TRELLO_TEST_BOARD_COUNT']))

	def test10_board_attrs(self):
		boards = self._trello.list_boards()
		for b in boards:
			self.assertIsNotNone(b['_id'], msg="_id not provided")
			self.assertIsNotNone(b['name'], msg="name not provided")
			self.assertIsNotNone(b['closed'], msg="closed not provided")
	

if __name__ == "__main__":
	unittest.main()
