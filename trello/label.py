# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class Label(TrelloBase):
    """
    Class representing a Trello Label.
    """
    def __init__(self, client, label_id, name, color=""):
        super(Label, self).__init__()
        self.client = client
        self.id = label_id
        self.name = name
        self.color = color

    @classmethod
    def from_json(cls, board, json_obj):
        """
        Deserialize the label json object to a Label object

        :board: the parent board the label is on
        :json_obj: the label json object
        """
        label = Label(board.client,
                      label_id=json_obj['id'],
                      name=json_obj['name'],
                      color=json_obj['color'])
        return label

    @classmethod
    def from_json_list(cls, board, json_objs):
        return [cls.from_json(board, obj) for obj in json_objs]

    def __repr__(self):
        return force_str(u'<Label %s>' % self.name)

    def fetch(self):
        """Fetch all attributes for this label"""
        json_obj = self.client.fetch_json('/labels/' + self.id)
        self.name = json_obj['name']
        self.color = json_obj['color']
        return self
