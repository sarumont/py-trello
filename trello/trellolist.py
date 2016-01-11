# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import


class List(object):
    """
    Class representing a Trello list. List attributes are stored on the object,
    but access to sub-objects (Cards) require an API call
    """

    def __init__(self, board, list_id, name=''):
        """Constructor

        :board: reference to the parent board
        :list_id: ID for this list
        """
        self.board = board
        self.client = board.client
        self.id = list_id
        self.name = name

    @classmethod
    def from_json(cls, board, json_obj):
        """
        Deserialize the list json object to a List object

        :board: the board object that the list belongs to
        :json_obj: the json list object
        """
        list = List(board, json_obj['id'], name=json_obj['name'].encode('utf-8'))
        list.closed = json_obj['closed']
        return list

    def __repr__(self):
        return '<List %s>' % self.name

    def fetch(self):
        """Fetch all attributes for this list"""
        json_obj = self.client.fetch_json('/lists/' + self.id)
        self.name = json_obj['name']
        self.closed = json_obj['closed']

    def list_cards(self, card_filter="open"):
        """Lists all cards in this list"""
        json_obj = self.client.fetch_json('/lists/' + self.id + '/cards/' + card_filter)
        return [Card.from_json(self, c) for c in json_obj]

    def add_card(self, name, desc=None, labels=[], due="null", source=None):
        """Add a card to this list

        :name: name for the card
        :desc: the description of the card
        :labels: a list of label IDs to be added
        :due: due date for the card
        :source: card ID from which to clone from
        :return: the card
        """
        labels_str = ""
        for label in labels:
            labels_str += label.id + ","
        json_obj = self.client.fetch_json(
            '/cards',
            http_method='POST',
            post_args={'name': name, 'idList': self.id, 'desc': desc, 'idLabels': labels_str[:-1], 'due': due, 'idCardSource': source})
        return Card.from_json(self, json_obj)

    def archive_all_cards(self):
        self.client.fetch_json(
            '/lists/' + self.id + '/archiveAllCards',
            http_method='POST')

    def fetch_actions(self, action_filter):
        """
        Fetch actions for this list can give more argv to action_filter,
        split for ',' json_obj is list
        """
        json_obj = self.client.fetch_json(
            '/lists/' + self.id + '/actions',
            query_params={'filter': action_filter})
        self.actions = json_obj

    def _set_remote_attribute(self, attribute, value):
        self.client.fetch_json(
            '/lists/' + self.id + '/' + attribute,
            http_method='PUT',
            post_args={'value': value, }, )

    def close(self):
        self.client.fetch_json(
            '/lists/' + self.id + '/closed',
            http_method='PUT',
            post_args={'value': 'true', }, )
        self.closed = True

    def open(self):
        self.client.fetch_json(
            '/lists/' + self.id + '/closed',
            http_method='PUT',
            post_args={'value': 'false', }, )
        self.closed = False

    def cardsCnt(self):
        return len(self.list_cards())


from trello.card import Card
