#!/usr/bin/python
from __future__ import with_statement, print_function
from datetime import datetime
import unittest
import os
from trello import TrelloClient


class TrelloChecklistTestCase(unittest.TestCase):
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

    def _add_checklist(self, card, name, items=[]):
        checklist = card.add_checklist(name, items)
        self.assertIsNotNone(checklist, msg="checklist is None")
        self.assertIsNotNone(checklist.id, msg="id not provided")
        self.assertEqual(checklist.name, name)
        return checklist

    def test_delete_checklist(self):
        name = "Card with checklist, test deletion"
        card = self._list.add_card(name)
        card.fetch(eager=True)
        checklist = self._add_checklist(card, 'ChecklistsToDelete', ['item1', 'item2'])
        checklist.delete()
        card._checklists = card.fetch_checklists()
        self.assertEqual(len(card.checklists), 0)

    def test_delete_checklist_remaining(self):
        name = "Card with checklist, test deletion"
        card = self._list.add_card(name)
        card.fetch(eager=True)

        name = 'ChecklistsToDelete'
        checklist_delete = self._add_checklist(card, name, ['item1', 'item2'])

        name_keep = 'ChecklistsToKeep'
        self._add_checklist(card, name_keep, [])
        checklist_delete.delete()
        card._checklists = card.fetch_checklists()
        self.assertEqual(len(card.checklists), 1)
        self.assertEqual(card.checklists[0].name, name_keep)

    def test_checklist_rename(self):
        name = "Testing checklist rename"
        description = "Description goes here"
        card = self._list.add_card(name, description)

        name = 'ToBeRenamed'
        new_name = "Renamed"
        checklist = self._add_checklist(card, name, ['item1', 'item2'])
        checklist.rename(new_name)
        self.assertEqual(checklist.name, new_name)
        card._checklists = card.fetch_checklists()
        self.assertEqual(len(card.checklists), 1)
        self.assertEqual(card.checklists[0].name, new_name)

    def test_delete_checklist_item(self):
        name = "Testing checklist item delete"
        card = self._list.add_card(name, "Description goes here")

        name = 'Checklist'
        checklist = self._add_checklist(card, name, ['item1', 'item2'])
        checklist.delete_checklist_item('item2')

        checklists = card.fetch_checklists()
        self.assertEqual(len(checklists[0].items), 1)
        self.assertEqual(checklists[0].items[0]['name'], 'item1')

    def test_clear_checklist(self):
        name = "Testing checklist clear"
        card = self._list.add_card(name, "Description goes here")

        name = 'Checklist'
        checklist = self._add_checklist(card, name, ['item1', 'item2', 'item3'])
        checklist.clear()

        checklists = card.fetch_checklists()
        self.assertEqual(len(checklists[0].items), 0)


def suite():
    # tests = ['test01_list_boards', 'test10_board_attrs', 'test20_add_card']
    # return unittest.TestSuite(map(TrelloBoardTestCase, tests))
    return unittest.TestLoader().loadTestsFromTestCase(TrelloChecklistTestCase)

if __name__ == "__main__":
    unittest.main()
