# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import Board as TrelloBoard
from trello.trellolist import List
import urllib.parse


class Board:
    """
    Class representing a Trello board. Board attributes are stored as normal
    Python attributes; access to all sub-objects, however, is always
    an API call (Lists, Cards).
    """
    class GetLists:
        def __init__(self, board_id, fields=None, cards=None, card_fields=None):
            self.board_id = board_id
            self.fields = fields if fields is not None else []
            self.cards = cards
            self.card_fields = card_fields if card_fields is not None else []

        def path(self):
            path = f"/boards/{self.board_id}/lists"
            params = {}
            if self.fields:
                fields = ','.join(field for field in self.fields)
                params['fields'] = fields
            if self.cards:
                params['cards'] = self.cards
            if self.card_fields:
                params['card_fields'] = ','.join(field for field in self.card_fields)
            path += "?" + urllib.parse.urlencode(params) if params else ""
            return path

        def parse(self, json):
            board = TrelloBoard(self.board_id)
            lists = []
            for list_ in json:
                lists.append(List.from_json(board, list_))
            return lists

    class GetBoard:
        def __init__(self, board_id, fields=None):
            self.board_id = board_id
            self.fields = fields if fields is not None else []

        def path(self):
            path = f"/boards/{self.board_id}"
            params = {}
            if self.fields:
                fields = ','.join(field for field in self.fields)
                params['fields'] = fields
            path += "?" + urllib.parse.urlencode(params) if params else ""
            return path

        def parse(self, json):
            return TrelloBoard.from_json(json_obj=json)
