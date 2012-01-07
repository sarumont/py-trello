from trello import Trello
import unittest
import os

class TrelloTestCase(unittest.TestCase):

	"""
	Tests for Trello API. Note these test are in order to preserve dependencies, as an API 
	integration cannot be tested independently.
	"""

	def setUp(self):
		self._trello = Trello(os.environ['TRELLO_API_KEY'], os.environ['TRELLO_TOKEN'])

	def tearDown(self):	
		#self._trello.logout()
		pass

	def test01_list_boards(self):
		self.assertEquals(
				len(self._trello.list_boards()),
				int(os.environ['TRELLO_TEST_BOARD_COUNT']))

	def test10_board_attrs(self):
		boards = self._trello.list_boards()
		for b in boards:
			self.assertIsNotNone(b.id, msg="id not provided")
			self.assertIsNotNone(b.name, msg="name not provided")
			self.assertIsNotNone(b.description, msg="description not provided")
			self.assertIsNotNone(b.closed, msg="closed not provided")
			self.assertIsNotNone(b.url, msg="url not provided")

	def test20_board_lists(self):
		boards = self._trello.list_boards()
		for b in boards:
			try:
				b.lists()
			except Exception as e:
				self.fail("Caught Exception getting lists")

	def test30_list_attrs(self):
		boards = self._trello.list_boards()
		for b in boards:
			for l in b.lists():
				self.assertIsNotNone(l.id, msg="id not provided")
				self.assertIsNotNone(l.name, msg="name not provided")
				self.assertIsNotNone(l.closed, msg="closed not provided")
			break # only need to test one board's lists

	#def test30_add_card(self):
		#pass
		#boards = self._trello.list_boards()
		#board_id = None
		#for b in boards:
			#if b['name'] == os.environ['TRELLO_TEST_BOARD_NAME']:
				#board_id = b['_id']
				#break
		#card_id = self._trello.add_card(board_id, "test card from Python")
		#self.assertIsNotNone(card_id)

def suite():
	tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
	return unittest.TestSuite(map(TrelloTestCase, tests))


if __name__ == "__main__":
	unittest.main()
