#!/usr/bin/python
from __future__ import with_statement, print_function
import os
import unittest
from datetime import datetime
from trello import TrelloClient, Unauthorized, ResourceUnavailable


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
            len(self._trello.list_boards(board_filter="open")),
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

    def test52_list_hooks(self):
        self.assertIsInstance(self._trello.list_hooks(), list)

    def test53_unauthorized(self):
        client = TrelloClient('a')
        self.assertRaises(Unauthorized,
                          client.list_boards)

    def test54_resource_unavailable(self):
        self.assertRaises(ResourceUnavailable,
                          self._trello.get_card, '0')


def suite():
    # tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
    # return unittest.TestSuite(map(TrelloClientTestCase, tests))
    return unittest.TestLoader().loadTestsFromTestCase(TrelloClientTestCase)


if __name__ == "__main__":
    unittest.main()
