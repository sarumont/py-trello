#!/usr/bin/python
from __future__ import with_statement, print_function
from datetime import datetime, timedelta
import unittest
import os
from trello import TrelloClient, ResourceUnavailable


class TrelloCardTestCase(unittest.TestCase):
    """
    Tests for TrelloClient API. Note these test are in order to
    preserve dependencies, as an API integration cannot be tested
    independently.
    """

    @classmethod
    def setUpClass(cls):
        cls._trello = TrelloClient(os.environ['TRELLO_API_KEY'],
                                   token=os.environ['TRELLO_TOKEN'])
        for b in cls._trello.list_boards():
            if b.name == os.environ['TRELLO_TEST_BOARD_NAME']:
                cls._board = b
                break
        if not cls._board:
            cls.fail("Couldn't find test board")
        cls._list = cls._board.add_list(str(datetime.now()))

    def _add_card(self, name, description=None):
        try:
            card = self._list.add_card(name, description)
            self.assertIsNotNone(card, msg="card is None")
            self.assertIsNotNone(card.id, msg="id not provided")
            self.assertEqual(card.name, name)
            return card
        except Exception as e:
            print(str(e))
            self.fail("Caught Exception adding card")

    def test40_add_card(self):
        name = "Testing from Python - no desc"
        card = self._add_card(name)

        self.assertIsNotNone(card.closed, msg="closed not provided")
        self.assertFalse(card.closed, msg="Card should not be closed")

        card2 = self._trello.get_card(card.id)
        self.assertEqual(card.name, card2.name)

    def test41_add_card_desc(self):
        name = "Testing from Python"
        description = "Description goes here"
        card = self._add_card(name, description)

        card.fetch()
        self.assertEqual(description, card.description)
        self.assertIsNotNone(card.url, msg="url not provided")
        self.assertIsNotNone(card.member_id)
        self.assertIsNotNone(card.short_id)
        self.assertIsNotNone(card.list_id)
        self.assertIsNotNone(card.comments)
        self.assertIsNotNone(card.checklists)
        self.assertIsInstance(card.created_date, datetime)

    def test42_add_card_with_comments_fetch(self):
        name = "Card with comments"
        comment = "Hello World!"
        card = self._add_card(name)
        card.comment(comment)
        card.fetch(True)

        self.assertEqual(len(card.comments), 1)
        self.assertEqual(card.comments[0]['data']['text'], comment)

    def test43_get_comments(self):
        name = "Card with comments 2"
        comment = "Hello World!"
        card = self._add_card(name)
        card.comment(comment)
        card._comments = card.get_comments()
        self.assertEqual(len(card.comments), 1)
        self.assertEqual(card.comments[0]['data']['text'], comment)

    def test44_attach_url_to_card(self):
        name = "Testing from Python - url"
        card = self._add_card(name)

        card.attach(name='lwn', url='http://lwn.net/')
        card.fetch()
        self.assertEqual(card.badges['attachments'], 1)
        card.delete()

    def test52_add_card_set_due(self):
        name = "Testing set due"
        card = self._add_card(name)

        # Set the due date to be 3 days from now
        today = datetime.today()
        day_detla = timedelta(3)
        due_date = today + day_detla
        card.set_due(due_date)
        expected_due_date = card.due
        # Refresh the due date from cloud
        card.fetch()
        actual_due_date = card.due
        self.assertEqual(expected_due_date[:8], actual_due_date[:8])

    def test_set_name(self):
        name = "Testing set card name"
        card = self._list.add_card('noname')
        card.set_name(name)
        self.assertEqual(card.name, name)

    def test_set_desc(self):
        card = self._list.add_card("Testing set card desc")
        description = "Description goes here"
        card.set_description(description)
        self.assertEqual(card.description, description)
        card.fetch()
        self.assertEqual(card.description, description)

    def test_set_closed(self):
        name = "Testing set card closed"
        card = self._list.add_card(name)
        self.assertFalse(card.closed)
        card.set_closed(True)
        self.assertTrue(card.closed)
        card.fetch()
        self.assertTrue(card.closed)

    def test81_resource_unavailable(self):
        self.assertRaises(ResourceUnavailable,
                          self._trello.get_card, '0dsfkjhsdf87342ed')


def suite():
    # tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
    # return unittest.TestSuite(map(TrelloBoardTestCase, tests))
    return unittest.TestLoader().loadTestsFromTestCase(TrelloBoardTestCase)


if __name__ == "__main__":
    unittest.main()
