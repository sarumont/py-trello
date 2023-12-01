#!/usr/bin/python
from __future__ import with_statement, print_function
import os
import unittest
from datetime import datetime
from trello import TrelloClient, Unauthorized, ResourceUnavailable, Board, List
from trello.batch.board import Board as BatchBoard
from trello.batch.batcherror import BatchError


class TrelloClientTestCase(unittest.TestCase):
    """

    Tests for TrelloClient API. Note these test are in order to
    preserve dependencies, as an API integration cannot be tested
    independently.

    """

    def setUp(self):
        self._trello = TrelloClient(os.environ['TRELLO_API_KEY'],
                                    token=os.environ['TRELLO_TOKEN'])

    def test_fetch_batch(self):
        board = self._trello.add_board("TEST BOARD")

        batch_responses = self._trello.fetch_batch([
            BatchBoard.GetLists(board.id, ['id', 'name'], 'open', ['idCard']),
            BatchBoard.GetBoard(board.id, ['id', 'name']),
            BatchBoard.GetLists('123', ['name'])
        ])
        board_lists = batch_responses[0]
        boards = batch_responses[1]
        batch_error = batch_responses[2]

        self.assertTrue(board_lists.success)
        self.assertIsInstance(board_lists.payload[0], List)
        self.assertEqual(len(board_lists.payload), 3)

        self.assertTrue(boards.success)
        self.assertIsInstance(boards.payload, Board)
        self.assertEqual(boards.payload.name, "TEST BOARD")

        self.assertFalse(batch_error.success)
        self.assertIsInstance(batch_error.payload, BatchError)
        self.assertEqual(batch_error.payload.message, "invalid id")

        board.delete()

    def test01_list_boards(self):
        board = self._trello.add_board("TEST BOARD")
        boards = self._trello.list_boards(board_filter="open")
        self.assertGreater(len(boards), 0)
        self.assertIn(board, boards)
        board.delete()

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

    def test_add_delete_star(self):
        """
        Test add and delete star to/from test board
        """
        board = self._trello.add_board("TEST BOARD")
        new_star = self._trello.add_star(board.id)
        star_list = self._trello.list_stars()
        self.assertTrue(new_star in star_list, "Star id was not added in list of starred boards")
        deleted_star = self._trello.delete_star(new_star)
        star_list = self._trello.list_stars()
        self.assertFalse(deleted_star in star_list, "Star id was not deleted from list of starred boards")
        board.delete()

class TrelloClientTestCaseWithoutOAuth(unittest.TestCase):
    """

    Tests for TrelloClient API when OAuth not activated.

    """

    def setUp(self):
        self._trello = TrelloClient(os.environ['TRELLO_API_KEY'],
                                    api_secret=os.environ['TRELLO_TOKEN'])

    def test01_oauth_not_activated(self):
        self.assertIsNone(self._trello.oauth)


def suite():
    test_classes_to_run = [TrelloClientTestCase,
                           TrelloClientTestCaseWithoutOAuth]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    return unittest.TestSuite(suites_list)


if __name__ == "__main__":
    unittest.main()
