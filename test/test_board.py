#!/usr/bin/python
from __future__ import with_statement, print_function
from datetime import datetime
import unittest
import os
from trello import TrelloClient, Board


class TrelloBoardTestCase(unittest.TestCase):
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
            if b.name == os.environ['TRELLO_TEST_BOARD_NAME'].encode('utf-8'):
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
            self.assertEquals(card.name, name)
            return card
        except Exception as e:
            print(str(e))
            self.fail("Caught Exception adding card")

    def test_get_cards(self):
        # Let's ensure we have no cards in board
        for card in self._board.get_cards():
            card.delete()

        nb_cards = 3
        names = ["Card #" + str(i) for i in range(nb_cards)]
        for i in range(nb_cards):
            self._add_card(names[i])
        cards = self._board.get_cards()
        self.assertEquals(len(cards), nb_cards)
        self.assertEquals(len(cards), len(self._board.open_cards()))

        for card in cards:
            self.assertTrue(card.name in names, 'Unexpected card found')

        self.assertIsInstance(self._board.all_cards(), list)
        self.assertIsInstance(self._board.open_cards(), list)
        self.assertIsInstance(self._board.closed_cards(), list)

    def test_delete_cards(self):
        nb_deleted_cards = len(self._board.closed_cards())
        cards = self._board.open_cards()
        nb_open_cards = len(cards)
        if nb_open_cards == 0:
            self._add_card("card to be deleted")
            nb_open_cards = 1
        for card in cards:
            card.delete()
        self.assertEquals(len(self._board.closed_cards()), nb_deleted_cards + nb_open_cards)

    def test_all_cards_reachable(self):
        if not len(self._board.open_cards()):
            self._add_card("an open card")
        if not len(self._board.closed_cards()):
            card = self._add_card("card to be closed")
            card.set_closed(True)
        self.assertEquals(len(self._board.all_cards()),
                          len(self._board.open_cards()) + len(self._board.closed_cards()))

    def test70_all_members(self):
        self.assertTrue(len(self._board.all_members()) > 0)

    def test71_normal_members(self):
        self.assertTrue(len(self._board.normal_members()) >= 0)

    def test72_admin_members(self):
        self.assertTrue(len(self._board.admin_members()) > 0)

    def test73_owner_members(self):
        members = self._board.owner_members()
        self.assertTrue(len(members) > 0)
        member = members[0].fetch()
        self.assertNotEqual(member.status, None)
        self.assertNotEqual(member.id, None)
        self.assertNotEqual(member.bio, None)
        self.assertNotEqual(member.url, None)
        self.assertNotEqual(member.username, None)
        self.assertNotEqual(member.full_name, None)
        self.assertNotEqual(member.initials, None)
        member2 = self._trello.get_member(member.id)
        self.assertEqual(member.username, member2.username)

    def test90_get_board(self):
        board = self._trello.get_board(self._board.id)
        self.assertEqual(self._board.name, board.name)

    def test100_add_board(self):
        test_board = self._trello.add_board("test_create_board")
        test_list = test_board.add_list("test_list")
        test_list.add_card("test_card")
        open_boards = self._trello.list_boards(board_filter="open")
        self.assertEqual(len([x for x in open_boards if x.name == "test_create_board"]), 1)

    def test110_copy_board(self):
        boards = self._trello.list_boards(board_filter="open")
        source_board = next( x for x in boards if x.name == "test_create_board")
        self._trello.add_board("copied_board", source_board=source_board)
        listed_boards = self._trello.list_boards(board_filter="open")
        copied_board = next(iter([x for x in listed_boards if x.name == "copied_board"]), None)
        self.assertIsNotNone(copied_board)
        open_lists = copied_board.open_lists()
        self.assertEqual(len(open_lists), 4) # default lists plus mine
        test_list = open_lists[0]
        self.assertEqual(len(test_list.list_cards()), 1)
        test_card = next ( iter([ x for x in test_list.list_cards() if x.name == "test_card"]), None )
        self.assertIsNotNone(test_card)

    def test120_close_board(self):
        boards = self._trello.list_boards(board_filter="open")
        open_count = len(boards)
        test_create_board = next( x for x in boards if x.name == "test_create_board") # type: Board
        copied_board = next( x for x in boards if x.name == "copied_board") # type: Board
        test_create_board.close()
        copied_board.close()
        still_open_boards = self._trello.list_boards(board_filter="open")
        still_open_count = len(still_open_boards)
        self.assertEqual(still_open_count, open_count - 2)


def suite():
    # tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
    # return unittest.TestSuite(map(TrelloBoardTestCase, tests))
    return unittest.TestLoader().loadTestsFromTestCase(TrelloBoardTestCase)

if __name__ == "__main__":
    unittest.main()
