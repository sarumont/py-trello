# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class Star(TrelloBase):
    """
    Class representing a Trello board star.
    """
    def __init__(self, star_id, board_id, position):
        super(Star, self).__init__()
        self.id = star_id
        self.board_id = board_id
        self.position = position

    @classmethod
    def from_json(cls, json_obj):
        """
        Deserialize the star json object to a Label object

        :board: the parent board the label is on
        :json_obj: the label json object
        """
        star = Star(star_id = json_obj['id'], board_id = json_obj['idBoard'], position = json_obj['pos'])
        return star

    @classmethod
    def from_json_list(cls, json_objs):
        return [cls.from_json(obj) for obj in json_objs]

    def __repr__(self):
        return force_str(u'<Star %s>' % self.id)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id
