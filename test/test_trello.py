from datetime import datetime, timedelta
from trello import TrelloClient
import unittest
import os


class TrelloClientTestCase(unittest.TestCase):
    """

    Tests for TrelloClient API. Note these test are in order to
    preserve dependencies, as an API integration cannot be tested
    independently.

    """

    def setUp(self):
        self._trello = TrelloClient(os.environ['TRELLO_API_KEY'],
                                    token=os.environ['TRELLO_TOKEN'])

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

    def test20_board_all_lists(self):
        boards = self._trello.list_boards()
        for b in boards:
            try:
                b.all_lists()
            except Exception:
                self.fail("Caught Exception getting lists")

    def test21_board_open_lists(self):
        boards = self._trello.list_boards()
        for b in boards:
            try:
                b.open_lists()
            except Exception:
                self.fail("Caught Exception getting open lists")

    def test22_board_closed_lists(self):
        boards = self._trello.list_boards()
        for b in boards:
            try:
                b.closed_lists()
            except Exception:
                self.fail("Caught Exception getting closed lists")

    def test30_list_attrs(self):
        boards = self._trello.list_boards()
        for b in boards:
            for l in b.all_lists():
                self.assertIsNotNone(l.id, msg="id not provided")
                self.assertIsNotNone(l.name, msg="name not provided")
                self.assertIsNotNone(l.closed, msg="closed not provided")
            break  # only need to test one board's lists

    def test50_list_cards(self):
        boards = self._trello.list_boards()
        for b in boards:
            for l in b.all_lists():
                for c in l.list_cards():
                    self.assertIsNotNone(c.id, msg="id not provided")
                    self.assertIsNotNone(c.name, msg="name not provided")
                    self.assertIsNotNone(c.description,
                                         msg="description not provided")
                    self.assertIsNotNone(c.closed, msg="closed not provided")
                    self.assertIsNotNone(c.url, msg="url not provided")
                break
            break
        pass

    def test51_fetch_cards(self):
        """
        Tests fetching all attributes for all cards
        """
        boards = self._trello.list_boards()
        for b in boards:
            for l in b.all_lists():
                for c in l.list_cards():
                    c.fetch()

                    self.assertIsInstance(c.date_last_activity, datetime,
                                          msg='date not provided')
                    self.assertTrue(len(c.board_id) > 0,
                                    msg='board id not provided')
                break
            break
        pass


class TrelloBoardTestCase(unittest.TestCase):
    """
    Tests for TrelloClient API. Note these test are in order to
    preserve dependencies, as an API integration cannot be tested
    independently.
    """

    def setUp(self):
        self._trello = TrelloClient(os.environ['TRELLO_API_KEY'],
                                    token=os.environ['TRELLO_TOKEN'])
        for b in self._trello.list_boards():
            if b.name == os.environ['TRELLO_TEST_BOARD_NAME']:
                self._board = b
                break
        try:
            self._list = self._board.open_lists()[0]
        except IndexError:
            self._list = self._board.add_list('List')

    def _add_card(self, name, description=None):
        try:
            card = self._list.add_card(name, description)
            self.assertIsNotNone(card, msg="card is None")
            self.assertIsNotNone(card.id, msg="id not provided")
            self.assertEquals(card.name, name)
            return card
        except Exception as e:
            print(str(e))
            self.fail("Caught Exception adding card")

    def test40_add_card(self):
        name = "Testing from Python - no desc"
        card = self._add_card(name)

        self.assertIsNotNone(card.closed, msg="closed not provided")
        self.assertIsNotNone(card.url, msg="url not provided")

    def test41_add_card(self):
        name = "Testing from Python"
        description = "Description goes here"
        card = self._add_card(name, description)

        self.assertEquals(card.description, description)
        self.assertIsNotNone(card.closed, msg="closed not provided")
        self.assertIsNotNone(card.url, msg="url not provided")

    def test42_add_card_with_comments(self):
        name = "Card with comments"
        comment = "Hello World!"
        card = self._add_card(name)
        card.comment(comment)
        card.fetch(True)

        self.assertEquals(card.description, '')
        self.assertIsNotNone(card.closed, msg="closed not provided")
        self.assertIsNotNone(card.url, msg="url not provided")
        self.assertEquals(len(card.comments), 1)
        self.assertEquals(card.comments[0]['data']['text'], comment)

    def test43_delete_checklist(self):
        name = "Card with comments"
        card = self._list.add_card(name)
        card.fetch(True)

        name = 'Checklists'
        checklist = card.add_checklist(name,
                                       ['item1', 'item2'])
        self.assertIsNotNone(checklist, msg="checklist is None")
        self.assertIsNotNone(checklist.id, msg="id not provided")
        self.assertEquals(checklist.name, name)
        checklist.delete()
        card.delete()

    def test52_get_cards(self):
        cards = self._board.get_cards()
        self.assertEqual(len(cards), 4)

        for card in cards:
            if card.name == 'Testing from Python':
                self.assertEqual(card.description, 'Description goes here')
            elif card.name == 'Testing from Python - no desc':
                self.assertEqual(card.description, '')
            elif card.name == 'Card with comments':
                self.assertEqual(card.description, '')
            else:
                self.fail(msg='Unexpected card found')

    def test52_add_card_set_due(self):
        name = "Testing from Python"
        description = "Description goes here"
        card = self._list.add_card(name, description)

        # Set the due date to be 3 days from now
        today = datetime.today()
        day_detla = timedelta(3)
        due_date = today + day_detla
        card.set_due(due_date)
        expected_due_date = card.due
        # Refresh the due date from cloud
        card.fetch()
        actual_due_date = card.due[:10]
        self.assertEquals(expected_due_date, actual_due_date)

    def test53_checklist(self):
        name = "Testing from Python"
        description = "Description goes here"
        card = self._list.add_card(name, description)

        name = 'Checklists'
        checklist = card.add_checklist(name,
                                       ['item1', 'item2'])
        self.assertIsNotNone(checklist, msg="checklist is None")
        self.assertIsNotNone(checklist.id, msg="id not provided")
        self.assertEquals(checklist.name, name)
        checklist.rename('Renamed')
        self.assertEquals(checklist.name, 'Renamed')

    def test60_delete_cards(self):
        cards = self._board.get_cards()
        for card in cards:
            card.delete()


def suite():
    tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
    return unittest.TestSuite(map(TrelloClientTestCase, tests))


if __name__ == "__main__":
    unittest.main()
