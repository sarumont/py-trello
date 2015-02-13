# -*- coding: utf-8 -*-
from dateutil import parser as dateparser
from datetime import datetime
from checklist import Checklist


class Card(object):
    """
    Class representing a Trello card. Card attributes are stored on
    the object
    """

    @property
    def member_id(self):
        return self.idMembers

    @property
    def short_id(self):
        return self.idShort

    @property
    def list_id(self):
        return self.idList

    @property
    def board_id(self):
        return self.idBoard

    @property
    def description(self):
        return self.desc

    @property
    def date_last_activity(self):
        return self.dateLastActivity

    @description.setter
    def description(self, value):
        self.desc = value

    @property
    def comments(self):
        """
        Lazily loads and returns the comments
        """
        if self._comments is None:
            self._comments = self.fetch_comments()
        return self._comments

    @property
    def checklists(self):
        """
        Lazily loads and returns the checklists
        """
        if self._checklists is None:
            self._checklists = self.fetch_checklists()
        return self._checklists

    def __init__(self, trello_list, card_id, name=''):
        """
        :trello_list: reference to the parent list
        :card_id: ID for this card
        """
        self.trello_list = trello_list
        self.client = trello_list.client
        self.id = card_id
        self.name = name

    @classmethod
    def from_json(cls, trello_list, json_obj):
        """
        Deserialize the card json object to a Card object

        :trello_list: the list object that the card belongs to
        :json_obj: json object
        """
        if 'id' not in json_obj:
            raise Exception("key 'id' is not in json_obj")
        card = cls(trello_list,
                   json_obj['id'],
                   name=json_obj['name'].encode('utf-8'))
        card.desc = json_obj.get('desc', '')
        card.closed = json_obj['closed']
        card.url = json_obj['url']
        card.member_ids = json_obj['idMembers']
        return card

    def __repr__(self):
        return '<Card %s>' % self.name

    def fetch(self, eager=True):
        """
        Fetch all attributes for this card
        :param eager: If eager is true comments and checklists will be fetched immediately, otherwise on demand
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.id,
            query_params={'badges': False})
        self.id = json_obj['id']
        self.name = json_obj['name'].encode('utf-8')
        self.desc = json_obj.get('desc', '')
        self.closed = json_obj['closed']
        self.url = json_obj['url']
        self.idMembers = json_obj['idMembers']
        self.idShort = json_obj['idShort']
        self.idList = json_obj['idList']
        self.idBoard = json_obj['idBoard']
        self.labels = json_obj['labels']
        self.badges = json_obj['badges']
        # For consistency, due date is in YYYY-MM-DD format
        if json_obj.get('due', ''):
            self.due = json_obj.get('due', '')[:10]
        self.checked = json_obj['checkItemStates']
        self.dateLastActivity = dateparser.parse(json_obj['dateLastActivity'])

        self._checklists = self.fetch_checklists() if eager else None
        self._comments = self.fetch_comments() if eager else None

    def fetch_comments(self):
        comments = []

        if self.badges['comments'] > 0:
            comments = self.client.fetch_json(
                '/cards/' + self.id + '/actions',
                query_params={'filter': 'commentCard'})

        return comments

    def get_comments(self):
        comments = []
        comments = self.client.fetch_json(
                '/cards/' + self.id + '/actions',
                query_params={'filter': 'commentCard'})
        return comments

    def fetch_checklists(self):
        checklists = []
        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/checklists', )
        for cl in json_obj:
            checklists.append(Checklist(self.client, self.checked, cl,
                                        trello_card=self.id))
        return checklists

    def fetch_actions(self, action_filter='createCard'):
        """
        Fetch actions for this card can give more argv to action_filter,
        split for ',' json_obj is list
        """
        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/actions',
            query_params={'filter': action_filter})
        self.actions = json_obj

    def attriExp(self, multiple):
        """
            Provides the option to explore what comes from trello
            :multiple is one of the attributes of GET /1/cards/[card id or shortlink]/actions
        """
        self.fetch_actions(multiple)
        return self.actions

    def listCardMove_date(self):
        """
            Will return the history of transitions of a card from one list to another
            The lower the index the more resent the historical item

            It returns a list of lists. The sublists are triplates of
            starting list, ending list and when the transition occured.
        """
        self.fetch_actions('updateCard:idList')
        res = []
        for idx in self.actions:
            date_str = idx['date'][:-5]
            dateDate = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')
            strLst = idx['data']['listBefore']['name']
            endLst = idx['data']['listAfter']['name']
            res.append([strLst, endLst, dateDate])
        return res

    @property
    def latestCardMove_date(self):
        """
            returns the date of the last card transition

        """
        self.fetch_actions('updateCard:idList')
        date_str = self.actions[0]['date'][:-5]
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

    @property
    def create_date(self):
        """
            Will return the creation date of the card.
            WARNING: if the card was create via convertion of a checklist item
                    it fails. attriExp('convertToCardFromCheckItem') allows to
                    test for the condition.
        """
        self.fetch_actions()
        date_str = self.actions[0]['date'][:-5]
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S')

    def set_name(self, new_name):
        """
        Update the name on the card to :new_name:
        """
        self._set_remote_attribute('name', new_name)
        self.name = new_name

    def set_description(self, description):
        self._set_remote_attribute('desc', description)
        self.desc = description

    def set_due(self, due):
        """Set the due time for the card

        :title: due a datetime object
        """
        datestr = due.strftime('%Y-%m-%d')
        self._set_remote_attribute('due', datestr)
        self.due = datestr

    def set_closed(self, closed):
        self._set_remote_attribute('closed', closed)
        self.closed = closed

    def delete(self):
        # Delete this card permanently
        self.client.fetch_json(
            '/cards/' + self.id,
            http_method='DELETE', )

    def assign(self, member_id):
        self.client.fetch_json(
            '/cards/' + self.id + '/members',
            http_method='POST',
            post_args={'value': member_id, })

    def comment(self, comment_text):
        """Add a comment to a card."""
        self.client.fetch_json(
            '/cards/' + self.id + '/actions/comments',
            http_method='POST',
            post_args={'text': comment_text, })

    def attach(self, name=None, mimeType=None, file=None, url=None):
        """
        Add an attachment to the card. The attachment can be either a
        file or a url. Setting the name and/or mime type is optional.
        :param name: The name of the attachment
        :param mimeType: mime type for the attachement
        :param file: a file-like, binary object that supports read()
        :param url: a URL pointing to the resource to be attached
        """
        if (file and url) or (not file and not url):
            raise Exception('Please provide either a file or url, and not both!')

        kwargs = {}
        if file:
            kwargs['files'] = dict(file=(name, file, mimeType))
        else:
            kwargs['name'] = name
            kwargs['mimeType'] = mimeType
            kwargs['url'] = url

        self._post_remote_data(
            'attachments', **kwargs
        )

    def change_list(self, list_id):
        self.client.fetch_json(
            '/cards/' + self.id + '/idList',
            http_method='PUT',
            post_args={'value': list_id, })

    def change_board(self, board_id, list_id=None):
        args = {'value': board_id, }
        if list_id is not None:
            args['idList'] = list_id
        self.client.fetch_json(
            '/cards/' + self.id + '/idBoard',
            http_method='PUT',
            post_args=args)

    def add_checklist(self, title, items, itemstates=None):

        """Add a checklist to this card

        :title: title of the checklist
        :items: a list of the item names
        :itemstates: a list of the state (True/False) of each item
        :return: the checklist
        """
        if itemstates is None:
            itemstates = []

        json_obj = self.client.fetch_json(
            '/cards/' + self.id + '/checklists',
            http_method='POST',
            post_args={'name': title}, )

        cl = Checklist(self.client, [], json_obj, trello_card=self.id)
        for i, name in enumerate(items):
            try:
                checked = itemstates[i]
            except IndexError:
                checked = False
            cl.add_checklist_item(name, checked)

        self.fetch()
        return cl

    def _set_remote_attribute(self, attribute, value):
        self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='PUT',
            post_args={'value': value, }, )

    def _post_remote_data(self, attribute, files=None, **kwargs):
        self.client.fetch_json(
            '/cards/' + self.id + '/' + attribute,
            http_method='POST',
            files=files,
            post_args=kwargs)
