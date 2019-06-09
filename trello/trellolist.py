# -*- coding: utf-8 -*-
from __future__ import with_statement, print_function, absolute_import

from trello import TrelloBase
from trello.compat import force_str


class List(TrelloBase):
    """
    Class representing a Trello list. List attributes are stored on the object,
    but access to sub-objects (Cards) require an API call
    """

    def __init__(self, board, list_id, name=''):
        """Constructor

        :board: reference to the parent board
        :list_id: ID for this list
        """
        super(List, self).__init__()
        self.board = board
        self.client = board.client
        self.id = list_id
        self.name = name
        self.closed = None
        self.pos = None
        self.subscribed = None

    @classmethod
    def from_json(cls, board, json_obj):
        """
        Deserialize the list json object to a List object

        :board: the board object that the list belongs to
        :json_obj: the json list object
        """
        list = List(board, json_obj['id'], name=json_obj['name'])
        list.closed = json_obj['closed']
        list.pos = json_obj['pos']
	#this method is also called from board.py with a different json object, so we need to make sure 'subscribed' is there
        if 'subscribed' in json_obj:
            list.subscribed = json_obj['subscribed']
        return list

    def __repr__(self):
        return force_str(u'<List %s>' % self.name)

    def fetch(self):
        """Fetch all attributes for this list"""
        json_obj = self.client.fetch_json('/lists/' + self.id)
        self.name = json_obj['name']
        self.closed = json_obj['closed']
        self.pos = json_obj['pos']
        if 'subscribed' in json_obj:
            self.subscribed = json_obj['subscribed']

    def list_cards(self, card_filter="open", actions=None, query={}):
        """Lists all cards in this list"""
        query_params = query
        if card_filter:
            query_params['filter'] = card_filter
        if actions:
            query_params['actions'] = actions
        query_params['customFieldItems'] = 'true'
        json_obj = self.client.fetch_json('/lists/' + self.id + '/cards',
                                          query_params=query_params)
        return [Card.from_json(self, c) for c in json_obj]

    def list_cards_iter(self, card_filter="open", actions=None, query=None, limit=None, batch=300):
        """see https://trello.com/c/8MJOLSCs/10-limit-actions-for-cards-requests"""
        query = {} if query is None else query
        before = None
        total = 0
        while True:
            query['limit'] = batch
            if before:
                query['before'] = before
            cards = self.list_cards(card_filter=card_filter, actions=actions, query=query)
            n = len(cards)
            if n == 0:
                break
            if limit:
                cards = cards[:limit-total]
            for c in cards:
                yield c
            total += n
            before = '%x' % min([int(c.id, 16) for c in cards])
            if limit and limit <= total:
                break

    def add_card(self, name, desc=None, labels=None, due="null", source=None, position=None, assign=None, keep_from_source="all"):
        """Add a card to this list

        :name: name for the card
        :desc: the description of the card
        :labels: a list of label IDs to be added
        :due: due date for the card
        :source: card ID from which to clone from
        :position: position of the card in the list. Must be "top", "bottom" or a positive number.
        :keep_from_source: can be used with source parameter. Can be "attachments", "checklists", "comments", "due", "labels", "members", "stickers" or "all".
        :return: the card
        """
        labels_str = ""
        if labels:
            for label in labels:
                labels_str += label.id + ","

        members_str = ""
        if assign:
            for assignee in assign:
                members_str += assignee.id + ","

        post_args = {
            'name': name,
            'idList': self.id,
            'desc': desc,
            'idLabels': labels_str[:-1],
            'due': due,
            'idMembers': members_str[:-1],
            'idCardSource': source,
            'keepFromSource': keep_from_source if source else None,
        }
        if position is not None:
            post_args["pos"] = position

        json_obj = self.client.fetch_json(
            '/cards',
            http_method='POST',
            post_args=post_args)
        return Card.from_json(self, json_obj)

    def archive_all_cards(self):
        self.client.fetch_json(
            '/lists/' + self.id + '/archiveAllCards',
            http_method='POST')

    def move_all_cards(self, destination_list):
        """
        Move all cards of this list to another list.
        The list can be in the same board (or not).
        """

        self.client.fetch_json(
            '/lists/' + self.id + '/moveAllCards',
            http_method='POST',
            post_args = {
                "idBoard": destination_list.board.id,
                "idList": destination_list.id,
            })

    def fetch_actions(self, action_filter):
        """
        Fetch actions for this list can give more argv to action_filter,
        split for ',' json_obj is list
        """
        json_obj = self.client.fetch_json(
            '/lists/' + self.id + '/actions',
            query_params={'filter': action_filter})
        self.actions = json_obj
        return self.actions

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

    # Move this list
    def move(self, position):
        self.client.fetch_json(
            '/lists/' + self.id + '/pos',
            http_method='PUT',
            post_args={'value': position, }, )
        self.pos = position

    # Subscribe to this list
    def subscribe(self):
        self.client.fetch_json(
        '/lists/' + self.id + '/subscribed',
        http_method='PUT',
            post_args={'value': 'true', }, )
        self.subscribed = True	

    # Unsubscribe from this list
    def unsubscribe(self):
        self.client.fetch_json(
        '/lists/' + self.id + '/subscribed',
        http_method='PUT',
            post_args={'value': 'false', }, )
        self.subscribed = False		
	
    def cardsCnt(self):
        return len(self.list_cards())

    # Change the name of the list
    def set_name(self, name):
        self.client.fetch_json(
            '/lists/{list_id}/name'.format(list_id=self.id),
            http_method='PUT',
            post_args={'value': name})
        self.name = name

    # Change the position of the list
    def set_pos(self, position):
        self.move(position)

from trello.card import Card
